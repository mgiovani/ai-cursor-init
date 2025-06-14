# AI-Powered Documentation Generation

The `ai-cursor-init` CLI tool has been completely refactored to use AI for intelligent documentation generation, replacing the previous template-based approach with context-aware AI analysis.

## 🚀 What's New

### AI-Powered Generation

- **Context-Aware**: Analyzes your `.cursor` rules and project structure
- **Intelligent Content**: Generates documentation that reflects your actual codebase
- **Multiple Providers**: Support for OpenAI, Anthropic Claude, and Google Gemini
- **Fallback Support**: Graceful degradation to basic templates if AI fails

### Enhanced Features

- **Smart Analysis**: AI reviews existing documentation for freshness and accuracy
- **Progressive Enhancement**: Updates existing docs while preserving important content
- **Rich CLI Output**: Beautiful terminal UI with progress indicators
- **Flexible Configuration**: YAML-based configuration with environment variable support

## 🔧 Installation & Setup

### 1. Install Dependencies

```bash
pip install openai anthropic python-dotenv rich tiktoken PyYAML
```

### 2. Configure AI Provider

```bash
# Quick interactive setup
python -m cursor_init configure

# Or set environment variables directly
export OPENAI_API_KEY=your_openai_key
# OR
export ANTHROPIC_API_KEY=your_anthropic_key
# OR
export GEMINI_API_KEY=your_gemini_key
```

### 3. Optional: Create Configuration File

Create `.cursor-init.yaml` in your project root:

```yaml
ai:
  preferred_provider: "anthropic"  # or "openai", "gemini"
  
  anthropic:
    model: "claude-4-sonnet-20250514"
    temperature: 0.3
    max_tokens: 4000
  
  openai:
    model: "gpt-4o-2024-11-20"
    temperature: 0.3
    max_tokens: 4000
  
  gemini:
    model: "gemini-2.5-pro-preview-06-05"
    temperature: 0.3
    max_tokens: 4000
```

## 📖 Usage

### Initialize Documentation

Generate comprehensive documentation based on your project:

```bash
python -m cursor_init init
```

**What it does:**

- Analyzes your `.cursor` rules for context
- Examines project structure and dependencies
- Generates `docs/architecture.md` with AI-powered insights
- Creates `docs/onboarding.md` tailored to your tech stack
- Produces initial ADR in `docs/adr/0001-record-architecture-decisions.md`
- Sets up `docs/data-model.md` placeholder

### Create Architecture Decision Records

Generate intelligent ADRs with full project context:

```bash
python -m cursor_init adr "Adopt GraphQL API"
python -m cursor_init adr "Database Migration Strategy" --context "Moving from SQLite to PostgreSQL"
```

**AI Enhancement:**

- Automatically includes relevant project context
- Suggests technical implications based on current stack
- Provides detailed consequences analysis

### Update Documentation

AI-powered documentation maintenance:

```bash
# Analyze what needs updating
python -m cursor_init update

# Apply AI-generated improvements
python -m cursor_init update --apply

# Update specific file
python -m cursor_init update --file architecture.md --apply

# Update by category
python -m cursor_init update --category adr --apply
```

**Smart Analysis:**

- Detects outdated content using heuristics
- Enhances existing documentation without losing important information
- Maintains document structure while improving clarity

### Configure AI Providers

Manage AI provider settings:

```bash
# Interactive configuration
python -m cursor_init configure

# Check current configuration
cat .cursor-init.yaml
```

## 🧠 How AI Analysis Works

### Context Gathering

The AI system analyzes multiple sources:

1. **Cursor Rules**: Reads all `.md` files in `.cursor/rules/`
2. **Project Structure**: Examines directories, key files, and dependencies
3. **Configuration Files**: Analyzes `pyproject.toml`, `package.json`, `requirements.txt`
4. **Existing Documentation**: Reviews current docs for gaps and improvements

### Intelligent Generation

- **Architecture Docs**: Creates comprehensive system overviews based on actual code structure
- **Onboarding Guides**: Generates step-by-step guides tailored to your tech stack
- **ADRs**: Produces decision records with relevant technical context and consequences
- **Enhancement Mode**: Improves existing docs while preserving important content

### Provider Support

| Provider | Models | Features |
|----------|---------|----------|
| **OpenAI** | GPT-4o, GPT-4 | Fast, general-purpose |
| **Anthropic** | Claude 4 Sonnet | Excellent for code analysis |
| **Google Gemini** | Gemini 2.5 Pro | Powerful multimodal AI with latest features |

## 🔄 Migration from Template-Based System

### Automatic Fallback

If AI generation fails, the system automatically falls back to basic templates, ensuring your workflow isn't interrupted.

### Preserved Commands

All existing commands work with enhanced AI capabilities:

- `init` → Now AI-powered with smart template selection
- `adr` → Enhanced with project context analysis
- `update` → Completely rewritten for intelligent analysis
- `check-docs` → Unchanged (still useful for CI)

### Configuration Migration

The system is backward-compatible with existing `.cursor-init.yaml` files and automatically extends them with AI configuration.

## 🚨 Error Handling & Troubleshooting

### Common Issues

**No API Key Found:**

```
AI generation failed: OpenAI API key not found. Set OPENAI_API_KEY environment variable.
```

**Solution:** Set the appropriate environment variable or run `python -m cursor_init configure`

**Rate Limiting:**

```
AI generation failed: Rate limit exceeded
```

**Solution:** Wait and retry, or switch to a different provider

**Network Issues:**

```
AI generation failed: Connection timeout
```

**Solution:** Check internet connection and API endpoint accessibility

### Fallback Mode

When AI fails, the system automatically:

1. Shows the error message
2. Falls back to basic template generation
3. Creates documentation with placeholder content
4. Allows you to retry later

## 🎯 Best Practices

### API Key Security

- Use environment variables instead of config files for API keys
- Consider using `.env` files (added to `.gitignore`)
- For CI/CD, use secure environment variable storage

### Cost Optimization

- Use lower `max_tokens` for shorter documents
- Increase `temperature` slightly (0.3-0.5) for more creative output
- Monitor API usage with your provider's dashboard

### Documentation Quality

- Provide specific context when creating ADRs
- Review AI-generated content before committing
- Use the `--apply` flag only after reviewing preview output
- Regularly update documentation as code evolves

## 🔮 Future Enhancements

### Planned Features

- **Code Integration**: Direct analysis of source code for deeper context
- **Diagram Generation**: AI-powered architecture and sequence diagrams
- **Multi-language Support**: Better detection and handling of polyglot projects
- **Incremental Updates**: Smarter change detection and targeted updates
- **Custom Prompts**: User-defined generation templates and styles

### Contributing

The AI-powered system is designed to be extensible. Key areas for contribution:

- Additional AI provider support
- Enhanced project analysis capabilities
- Custom documentation templates
- Integration with more development tools

---

*This documentation was generated using the AI-powered cursor-init system! 🤖*
