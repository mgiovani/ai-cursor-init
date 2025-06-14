import os
import yaml
from pathlib import Path
from typing import Dict, Optional, Any
from .ai_service import AIProvider, AIConfig
import dotenv

class CursorInitAIConfig:
    def __init__(self, config_file: str = '.cursor-init.yaml'):
        self.config_file = config_file
        self.config = self._load_config()
        dotenv.load_dotenv()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return yaml.safe_load(f) or {}
            except Exception as e:
                print(f'Warning: Could not load config file {self.config_file}: {e}')
        return {}
    
    def _save_config(self):
        """Save configuration to YAML file."""
        try:
            with open(self.config_file, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False)
        except Exception as e:
            print(f'Warning: Could not save config file {self.config_file}: {e}')
    
    def get_ai_config(self, provider_override: Optional[str] = None) -> AIConfig:
        """Get AI configuration based on settings and environment."""
        
        # Determine provider
        if provider_override:
            provider = AIProvider(provider_override)
        else:
            provider = self._detect_best_provider()
        
        # Get provider-specific settings
        ai_settings = self.config.get('ai', {})
        provider_settings = ai_settings.get(provider.value, {})
        
        return AIConfig(
            provider=provider,
            api_key=provider_settings.get('api_key'),
            model=provider_settings.get('model'),
            base_url=provider_settings.get('base_url'),
            temperature=provider_settings.get('temperature', 0.3),
            max_tokens=provider_settings.get('max_tokens', 4000)
        )
    
    def _detect_best_provider(self) -> AIProvider:
        """Auto-detect the best available AI provider based on API keys."""
        
        # Check configuration preferences first
        ai_config = self.config.get('ai', {})
        preferred_provider = ai_config.get('preferred_provider')
        
        if preferred_provider:
            try:
                return AIProvider(preferred_provider)
            except ValueError:
                print(f'Warning: Invalid preferred provider: {preferred_provider}')
        
        # Check environment variables
        if os.getenv('ANTHROPIC_API_KEY'):
            return AIProvider.ANTHROPIC
        elif os.getenv('OPENAI_API_KEY'):
            return AIProvider.OPENAI
        elif os.getenv('AZURE_OPENAI_API_KEY') and os.getenv('AZURE_OPENAI_ENDPOINT'):
            return AIProvider.AZURE_OPENAI
        else:
            # Default to OpenAI (will show helpful error if no key)
            return AIProvider.OPENAI
    
    def configure_provider(self, provider: str, **kwargs):
        """Configure a specific AI provider."""
        if 'ai' not in self.config:
            self.config['ai'] = {}
        
        if provider not in self.config['ai']:
            self.config['ai'][provider] = {}
        
        self.config['ai'][provider].update(kwargs)
        self._save_config()
    
    def set_preferred_provider(self, provider: str):
        """Set the preferred AI provider."""
        if 'ai' not in self.config:
            self.config['ai'] = {}
        
        self.config['ai']['preferred_provider'] = provider
        self._save_config()
    
    def list_configured_providers(self) -> Dict[str, Dict]:
        """List all configured AI providers."""
        return self.config.get('ai', {})
    
    def get_example_config(self) -> str:
        """Return an example configuration."""
        return '''ai:
  preferred_provider: "anthropic"  # or "openai", "azure_openai"
  
  anthropic:
    model: "claude-3-5-sonnet-20241022"
    temperature: 0.3
    max_tokens: 4000
  
  openai:
    model: "gpt-4o"
    temperature: 0.3
    max_tokens: 4000
  
  azure_openai:
    model: "gpt-4"
    base_url: "https://your-resource.openai.azure.com/"
    temperature: 0.3
    max_tokens: 4000

# Environment variables (recommended for API keys):
# ANTHROPIC_API_KEY=your_anthropic_key
# OPENAI_API_KEY=your_openai_key
# AZURE_OPENAI_API_KEY=your_azure_key
# AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
'''

def init_ai_config() -> str:
    """Initialize AI configuration interactively."""
    config = CursorInitAIConfig()
    
    print('AI Configuration Setup')
    print('=====================')
    print()
    print('Available providers:')
    print('1. OpenAI (GPT-4)')
    print('2. Anthropic (Claude)')
    print('3. Azure OpenAI')
    print()
    
    choice = input('Select provider (1-3): ').strip()
    
    if choice == '1':
        provider = 'openai'
        print('\nSet your OpenAI API key:')
        print('export OPENAI_API_KEY=your_key_here')
        model = input('Model (default: gpt-4o): ').strip() or 'gpt-4o'
        config.configure_provider(provider, model=model)
        
    elif choice == '2':
        provider = 'anthropic'
        print('\nSet your Anthropic API key:')
        print('export ANTHROPIC_API_KEY=your_key_here')
        model = input('Model (default: claude-3-5-sonnet-20241022): ').strip() or 'claude-3-5-sonnet-20241022'
        config.configure_provider(provider, model=model)
        
    elif choice == '3':
        provider = 'azure_openai'
        print('\nSet your Azure OpenAI credentials:')
        print('export AZURE_OPENAI_API_KEY=your_key_here')
        print('export AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/')
        endpoint = input('Azure OpenAI Endpoint: ').strip()
        model = input('Model (default: gpt-4): ').strip() or 'gpt-4'
        config.configure_provider(provider, base_url=endpoint, model=model)
        
    else:
        print('Invalid choice. Configuration cancelled.')
        return 'Configuration cancelled.'
    
    config.set_preferred_provider(provider)
    
    print(f'\nConfiguration saved! Provider "{provider}" is now configured.')
    print(f'Configuration file: {config.config_file}')
    
    return f'AI provider "{provider}" configured successfully.' 