import os
import json
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import dotenv

try:
    import openai
except ImportError:
    openai = None

try:
    import anthropic
except ImportError:
    anthropic = None

try:
    import google.generativeai as genai
except ImportError:
    genai = None


class AIProvider(Enum):
    OPENAI = 'openai'
    ANTHROPIC = 'anthropic'
    GEMINI = 'gemini'


@dataclass
class AIConfig:
    provider: AIProvider
    api_key: Optional[str] = None
    model: Optional[str] = None
    base_url: Optional[str] = None
    temperature: float = 0.3
    max_tokens: int = 4000


class AIService:
    def __init__(self, config: AIConfig):
        self.config = config
        self._client = None
        dotenv.load_dotenv()
        
    def _get_client(self):
        if self._client:
            return self._client
            
        if self.config.provider == AIProvider.OPENAI:
            if not openai:
                raise ImportError('OpenAI library not installed. Install with: pip install openai')
            api_key = self.config.api_key or os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise ValueError('OpenAI API key not found. Set OPENAI_API_KEY environment variable.')
            self._client = openai.OpenAI(api_key=api_key)
            
        elif self.config.provider == AIProvider.ANTHROPIC:
            if not anthropic:
                raise ImportError('Anthropic library not installed. Install with: pip install anthropic')
            api_key = self.config.api_key or os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                raise ValueError('Anthropic API key not found. Set ANTHROPIC_API_KEY environment variable.')
            self._client = anthropic.Anthropic(api_key=api_key)
            
        elif self.config.provider == AIProvider.GEMINI:
            if not genai:
                raise ImportError('Google Generative AI library not installed. Install with: pip install google-generativeai')
            api_key = self.config.api_key or os.getenv('GEMINI_API_KEY')
            if not api_key:
                raise ValueError('Gemini API key not found. Set GEMINI_API_KEY environment variable.')
            genai.configure(api_key=api_key)
            self._client = genai
            
        return self._client

    def generate_completion(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        client = self._get_client()
        
        if self.config.provider == AIProvider.ANTHROPIC:
            response = client.messages.create(
                model=self.config.model or 'claude-4-sonnet',
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                system=system_prompt or '',
                messages=[{'role': 'user', 'content': prompt}]
            )
            return response.content[0].text
            
        elif self.config.provider == AIProvider.GEMINI:
            model_name = self.config.model or 'gemini-2.5-pro'
            model = client.GenerativeModel(model_name)
            
            # Combine system prompt and user prompt for Gemini
            full_prompt = prompt
            if system_prompt:
                full_prompt = f"{system_prompt}\n\n{prompt}"
            
            response = model.generate_content(
                full_prompt,
                generation_config=client.types.GenerationConfig(
                    temperature=self.config.temperature,
                    max_output_tokens=self.config.max_tokens
                )
            )
            return response.text
            
        else:  # OpenAI
            messages = []
            if system_prompt:
                messages.append({'role': 'system', 'content': system_prompt})
            messages.append({'role': 'user', 'content': prompt})
            
            response = client.chat.completions.create(
                model=self.config.model or 'o3',
                messages=messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            return response.choices[0].message.content


class DocumentationGenerator:
    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service
        
    def _read_cursor_rules(self, project_root: str = '.') -> str:
        cursor_rules = []
        cursor_path = Path(project_root) / '.cursor' / 'rules'
        
        if cursor_path.exists():
            for rule_file in cursor_path.rglob('*.md'):
                try:
                    content = rule_file.read_text(encoding='utf-8')
                    cursor_rules.append(f'## {rule_file.name}\n{content}')
                except Exception as e:
                    print(f'Warning: Could not read {rule_file}: {e}')
                    
        return '\n\n'.join(cursor_rules) if cursor_rules else 'No cursor rules found.'
    
    def _analyze_project_structure(self, project_root: str = '.') -> Dict[str, Any]:
        structure = {}
        root_path = Path(project_root)
        
        # Analyze key files and directories
        key_files = []
        for pattern in ['*.py', '*.js', '*.ts', '*.tsx', '*.jsx', 'requirements.txt', 'package.json', 'pyproject.toml']:
            key_files.extend(list(root_path.glob(pattern)))
            
        # Read important config files
        config_contents = {}
        for config_file in ['pyproject.toml', 'package.json', 'requirements.txt']:
            config_path = root_path / config_file
            if config_path.exists():
                try:
                    config_contents[config_file] = config_path.read_text(encoding='utf-8')[:2000]  # Limit size
                except Exception:
                    pass
                    
        # Get directory structure (limited depth)
        dirs = []
        for item in root_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                dirs.append(item.name)
                
        structure = {
            'key_files': [f.name for f in key_files[:20]],  # Limit to 20 files
            'directories': dirs,
            'config_contents': config_contents
        }
        
        return structure
    
    def generate_architecture_docs(self, project_root: str = '.') -> str:
        cursor_rules = self._read_cursor_rules(project_root)
        project_structure = self._analyze_project_structure(project_root)
        
        system_prompt = '''You are an expert technical documentation writer. Generate comprehensive architecture documentation based on the provided project context and cursor rules.

Your output should be in markdown format and include:
1. Project Overview
2. System Architecture
3. Technology Stack
4. Component Relationships
5. Key Design Decisions

Focus on being accurate and extracting insights from the actual project structure and configuration files.'''

        user_prompt = f'''Based on the following project information, generate architecture documentation:

## Cursor Rules Context:
{cursor_rules}

## Project Structure:
{json.dumps(project_structure, indent=2)}

Generate comprehensive architecture documentation that reflects the actual project structure and follows the patterns indicated in the cursor rules.'''

        return self.ai_service.generate_completion(user_prompt, system_prompt)
    
    def generate_onboarding_docs(self, project_root: str = '.') -> str:
        cursor_rules = self._read_cursor_rules(project_root)
        project_structure = self._analyze_project_structure(project_root)
        
        system_prompt = '''You are an expert technical documentation writer. Generate comprehensive onboarding documentation for new developers joining this project.

Your output should be in markdown format and include:
1. Getting Started
2. Prerequisites
3. Installation Steps
4. Development Setup
5. Running the Project
6. Key Commands
7. Project Structure Overview

Make it practical and actionable for new team members.'''

        user_prompt = f'''Based on the following project information, generate onboarding documentation:

## Cursor Rules Context:
{cursor_rules}

## Project Structure:
{json.dumps(project_structure, indent=2)}

Generate practical onboarding documentation that helps new developers get up and running quickly.'''

        return self.ai_service.generate_completion(user_prompt, system_prompt)
    
    def generate_adr(self, title: str, context: str = '', project_root: str = '.') -> str:
        cursor_rules = self._read_cursor_rules(project_root)
        project_structure = self._analyze_project_structure(project_root)
        
        system_prompt = '''You are an expert in documenting architecture decisions. Generate an Architecture Decision Record (ADR) following the standard format.

Your output should be in markdown format with:
1. Title
2. Status (Proposed)
3. Context (the forces at play)
4. Decision (what was decided)
5. Consequences (positive and negative outcomes)

Base your analysis on the project context and any additional context provided.'''

        user_prompt = f'''Generate an ADR for: {title}

## Additional Context:
{context}

## Cursor Rules Context:
{cursor_rules}

## Project Structure:
{json.dumps(project_structure, indent=2)}

Create a comprehensive ADR that captures the decision context and rationale.'''

        return self.ai_service.generate_completion(user_prompt, system_prompt)


def get_default_ai_service(provider_override: Optional[str] = None) -> AIService:
    from .ai_config import CursorInitAIConfig
    
    config_manager = CursorInitAIConfig()
    ai_config = config_manager.get_ai_config(provider_override)
    
    return AIService(ai_config) 