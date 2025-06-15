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
                model=self.config.model or 'claude-sonnet-4',
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
                generation_config=genai.types.GenerationConfig(
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
        root_path = Path(project_root)
        
        # Read from the AI cursor init package's rules first
        package_cursor_path = root_path / '.cursor' / 'rules' / 'cursor-init'
        if package_cursor_path.exists():
            for rule_file in package_cursor_path.rglob('*.md'):
                try:
                    content = rule_file.read_text(encoding='utf-8')
                    cursor_rules.append(f'## Package Rule: {rule_file.name}\n{content}')
                except Exception as e:
                    print(f'Warning: Could not read package rule {rule_file}: {e}')
        
        # Read from project-specific cursor rules
        project_cursor_path = root_path / '.cursor' / 'rules'
        if project_cursor_path.exists():
            for rule_file in project_cursor_path.rglob('*.md'):
                # Skip the cursor-init package rules to avoid duplication
                if 'cursor-init' not in str(rule_file):
                    try:
                        content = rule_file.read_text(encoding='utf-8')
                        cursor_rules.append(f'## Project Rule: {rule_file.name}\n{content}')
                    except Exception as e:
                        print(f'Warning: Could not read project rule {rule_file}: {e}')
        
        # Also check for .cursorrules file
        cursorrules_file = root_path / '.cursorrules'
        if cursorrules_file.exists():
            try:
                content = cursorrules_file.read_text(encoding='utf-8')
                cursor_rules.append(f'## Project .cursorrules\n{content}')
            except Exception as e:
                print(f'Warning: Could not read .cursorrules: {e}')
                    
        return '\n\n'.join(cursor_rules) if cursor_rules else 'No cursor rules found.'
    
    def _analyze_project_structure(self, project_root: str = '.') -> Dict[str, Any]:
        structure = {}
        root_path = Path(project_root)
        
        # Analyze key files and directories with more detail
        key_files = []
        source_files = []
        config_files = []
        
        # Scan for important file patterns
        file_patterns = {
            'source': ['*.py', '*.js', '*.ts', '*.tsx', '*.jsx', '*.go', '*.rs', '*.java', '*.cpp', '*.c'],
            'config': ['requirements.txt', 'package.json', 'pyproject.toml', 'Cargo.toml', 'pom.xml', 'build.gradle', '*.yaml', '*.yml', '*.toml', '*.json'],
            'docs': ['README.md', '*.md', '*.rst', '*.txt'],
            'scripts': ['*.sh', '*.bat', '*.ps1', 'Makefile', 'docker-compose.yml', 'Dockerfile']
        }
        
        for category, patterns in file_patterns.items():
            for pattern in patterns:
                files_found = list(root_path.glob(pattern))
                # Also search one level deep
                files_found.extend(list(root_path.glob(f'*/{pattern}')))
                
                for file_path in files_found[:10]:  # Limit to prevent overwhelming
                    if file_path.is_file():
                        relative_path = str(file_path.relative_to(root_path))
                        if category == 'source':
                            source_files.append(relative_path)
                        elif category == 'config':
                            config_files.append(relative_path)
                        key_files.append(relative_path)
                    
        # Read important config files with more content
        config_contents = {}
        important_configs = ['pyproject.toml', 'package.json', 'requirements.txt', 'Cargo.toml', 'composer.json']
        
        for config_file in important_configs:
            config_path = root_path / config_file
            if config_path.exists():
                try:
                    content = config_path.read_text(encoding='utf-8')
                    config_contents[config_file] = content[:3000]  # Increased limit
                except Exception:
                    pass
        
        # Analyze directory structure with more depth
        dirs = []
        important_dirs = []
        for item in root_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                dirs.append(item.name)
                # Identify important directories
                if item.name in ['src', 'lib', 'app', 'components', 'pages', 'api', 'models', 'services', 'utils', 'cli']:
                    important_dirs.append(item.name)
        
        # Detect frameworks and technologies
        technologies = self._detect_technologies(config_contents, source_files)
        
        # Analyze imports and dependencies
        imports_analysis = self._analyze_imports(root_path, source_files[:5])  # Limit to prevent slowdown
                
        structure = {
            'key_files': key_files[:30],  # Increased limit
            'source_files': source_files[:20],
            'config_files': config_files,
            'directories': dirs,
            'important_directories': important_dirs,
            'config_contents': config_contents,
            'technologies': technologies,
            'imports_analysis': imports_analysis,
            'project_name': self._infer_project_name(root_path, config_contents)
        }
        
        return structure
    
    def _detect_technologies(self, config_contents: Dict[str, str], source_files: List[str]) -> Dict[str, Any]:
        """Detect technologies used in the project."""
        technologies = {
            'languages': set(),
            'frameworks': set(),
            'databases': set(),
            'tools': set()
        }
        
        # Detect languages from file extensions
        for file_path in source_files:
            ext = Path(file_path).suffix.lower()
            lang_map = {
                '.py': 'Python',
                '.js': 'JavaScript', 
                '.ts': 'TypeScript',
                '.tsx': 'TypeScript/React',
                '.jsx': 'JavaScript/React',
                '.go': 'Go',
                '.rs': 'Rust',
                '.java': 'Java',
                '.cpp': 'C++',
                '.c': 'C'
            }
            if ext in lang_map:
                technologies['languages'].add(lang_map[ext])
        
        # Detect frameworks from config files
        for filename, content in config_contents.items():
            content_lower = content.lower()
            
            # Python frameworks
            if 'fastapi' in content_lower:
                technologies['frameworks'].add('FastAPI')
            if 'django' in content_lower:
                technologies['frameworks'].add('Django')
            if 'flask' in content_lower:
                technologies['frameworks'].add('Flask')
            if 'sqlalchemy' in content_lower:
                technologies['frameworks'].add('SQLAlchemy')
                technologies['databases'].add('SQL Database')
            
            # JavaScript/TypeScript frameworks
            if 'react' in content_lower:
                technologies['frameworks'].add('React')
            if 'next' in content_lower:
                technologies['frameworks'].add('Next.js')
            if 'vue' in content_lower:
                technologies['frameworks'].add('Vue.js')
            if 'express' in content_lower:
                technologies['frameworks'].add('Express.js')
            
            # Databases
            if 'postgresql' in content_lower or 'psycopg' in content_lower:
                technologies['databases'].add('PostgreSQL')
            if 'mysql' in content_lower:
                technologies['databases'].add('MySQL')
            if 'mongodb' in content_lower:
                technologies['databases'].add('MongoDB')
            if 'redis' in content_lower:
                technologies['databases'].add('Redis')
        
        # Convert sets to lists for JSON serialization
        return {k: list(v) for k, v in technologies.items()}
    
    def _analyze_imports(self, root_path: Path, source_files: List[str]) -> Dict[str, List[str]]:
        """Analyze imports in source files to understand dependencies."""
        imports = {
            'python': [],
            'javascript': [],
            'typescript': []
        }
        
        for file_path in source_files:
            try:
                full_path = root_path / file_path
                if not full_path.exists():
                    continue
                    
                content = full_path.read_text(encoding='utf-8')[:1000]  # First 1000 chars
                
                if file_path.endswith('.py'):
                    # Extract Python imports
                    import re
                    py_imports = re.findall(r'(?:from\s+(\S+)\s+import|import\s+(\S+))', content)
                    for imp_tuple in py_imports:
                        imp = imp_tuple[0] or imp_tuple[1]
                        if imp and not imp.startswith('.'):  # Skip relative imports
                            imports['python'].append(imp.split('.')[0])
                
                elif file_path.endswith(('.js', '.jsx')):
                    # Extract JavaScript imports
                    js_imports = re.findall(r'(?:import.*?from\s+[\'"]([^\'"]+)|require\([\'"]([^\'"]+))', content)
                    for imp_tuple in js_imports:
                        imp = imp_tuple[0] or imp_tuple[1]
                        if imp and not imp.startswith('.'):
                            imports['javascript'].append(imp.split('/')[0])
                
                elif file_path.endswith(('.ts', '.tsx')):
                    # Extract TypeScript imports
                    ts_imports = re.findall(r'(?:import.*?from\s+[\'"]([^\'"]+)|require\([\'"]([^\'"]+))', content)
                    for imp_tuple in ts_imports:
                        imp = imp_tuple[0] or imp_tuple[1]
                        if imp and not imp.startswith('.'):
                            imports['typescript'].append(imp.split('/')[0])
                            
            except Exception:
                continue
        
        # Remove duplicates and limit size
        return {k: list(set(v))[:10] for k, v in imports.items()}
    
    def _infer_project_name(self, root_path: Path, config_contents: Dict[str, str]) -> str:
        """Infer project name from various sources."""
        # Try to get from package.json
        if 'package.json' in config_contents:
            try:
                import json
                package_data = json.loads(config_contents['package.json'])
                if 'name' in package_data:
                    return package_data['name']
            except:
                pass
        
        # Try to get from pyproject.toml
        if 'pyproject.toml' in config_contents:
            content = config_contents['pyproject.toml']
            import re
            name_match = re.search(r'name\s*=\s*[\'"]([^\'"]+)', content)
            if name_match:
                return name_match.group(1)
        
        # Fall back to directory name
        return root_path.name
    
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

    def generate_data_model_docs(self, project_root: str = '.') -> str:
        cursor_rules = self._read_cursor_rules(project_root)
        project_structure = self._analyze_project_structure(project_root)
        
        # Analyze code files for database models
        model_analysis = self._analyze_database_models(project_root)
        
        system_prompt = '''You are an expert technical documentation writer specializing in database design and data modeling. Generate comprehensive data model documentation.

Your output should be in markdown format and include:
1. Data Model Overview
2. Entity Relationship Diagram (using Mermaid syntax)
3. Entity Descriptions
4. Key Relationships
5. Data Flow Patterns

Focus on extracting actual database schema information from the codebase when available.'''

        user_prompt = f'''Based on the following project information, generate data model documentation:

## Cursor Rules Context:
{cursor_rules}

## Project Structure:
{json.dumps(project_structure, indent=2)}

## Database Models Analysis:
{model_analysis}

Generate comprehensive data model documentation. If no database models are found, create a template structure that explains how to add data models to the project.'''

        return self.ai_service.generate_completion(user_prompt, system_prompt)

    def _analyze_database_models(self, project_root: str = '.') -> str:
        """Analyze the project for database models and schema information."""
        root_path = Path(project_root)
        model_info = []
        
        # Look for common database model patterns
        model_patterns = [
            '**/*model*.py',  # Python models
            '**/*schema*.py',  # Schema files
            '**/*entity*.py',  # Entity files
            '**/*models*.ts',  # TypeScript models
            '**/*schema*.ts',  # TypeScript schema
        ]
        
        for pattern in model_patterns:
            for file_path in root_path.glob(pattern):
                if file_path.is_file():
                    try:
                        content = file_path.read_text(encoding='utf-8')
                        # Look for SQLAlchemy, Django, or other ORM patterns
                        if any(keyword in content.lower() for keyword in ['sqlalchemy', 'django.db', 'model', 'table', 'column']):
                            model_info.append(f'## {file_path.name}\n```python\n{content[:1500]}\n```')  # Limit size
                    except Exception:
                        continue
        
        if model_info:
            return '\n\n'.join(model_info)
        else:
            return 'No database models found in the project. This appears to be a project without explicit database schema definitions.'


def get_default_ai_service(provider_override: Optional[str] = None) -> AIService:
    from .ai_config import CursorInitAIConfig
    
    config_manager = CursorInitAIConfig()
    ai_config = config_manager.get_ai_config(provider_override)
    
    return AIService(ai_config) 