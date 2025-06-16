# Contributing to cursor-init

Thank you for your interest in contributing to `cursor-init`! This guide will help you get started with adding templates, slash commands, and extending the framework.

## Quick Start

1. **Fork the repository** and create a feature branch
2. **Make your changes** following the guidelines below
3. **Test your changes** manually and with the test suite
4. **Submit a pull request** with a clear description

## Understanding the Architecture

`cursor-init` is built around three main components:

1. **AI-Powered Documentation Generation**: All documentation is now generated using AI that analyzes your codebase
2. **Cursor Rules**: Slash commands that provide in-IDE functionality
3. **CLI Tool**: Command-line interface for CI integration and offline usage

## Adding New Documentation Types

Since all documentation is AI-generated, adding new document types is simpler:

### 1. Add AI Generation Logic

Create generation methods in `cli/cursor_init/ai_service.py`:

```python
def generate_security_docs(self, project_root: str = '.') -> str:
    cursor_rules = self._read_cursor_rules(project_root)
    project_structure = self._analyze_project_structure(project_root)
    
    system_prompt = '''You are an expert in security documentation. Generate comprehensive security documentation based on the project analysis.'''
    
    user_prompt = f'''Generate security documentation for this project:

Project Structure: {json.dumps(project_structure, indent=2)}
Cursor Rules: {cursor_rules}

Include security best practices, threat modeling, and security architecture relevant to this specific technology stack.'''

    return self.ai_service.generate_content(system_prompt, user_prompt)
```

### 2. Add CLI Command

Add the command to your main CLI in `cli/cursor_init/__main__.py`:

```python
security_parser = subparsers.add_parser('security', help='Generate security documentation')
security_parser.set_defaults(func=lambda args: generate_security_docs())
```

### 3. Create Cursor Rule

Add `.cursor/rules/cursor-init/security.mdc`:

```markdown
---
description: "Generate comprehensive security documentation"
alwaysApply: true
---

@if(user_message.starts_with("/security")) {
  "I will generate comprehensive security documentation by analyzing your project's technology stack, architecture, and security requirements.
  
  This will include:
  1. **Security Architecture**: How security is implemented in your system
  2. **Threat Model**: Potential security risks and mitigations
  3. **Best Practices**: Security guidelines specific to your tech stack
  4. **Compliance**: Relevant security standards and requirements
  
  Let me analyze your project and generate tailored security documentation..."
}
```

## Extending Detection Logic

Framework detection is primarily used to provide **context to AI** rather than selecting specific templates.

### Current Detection Strategy

The AI-powered analysis automatically detects and adapts to any project structure, automatically identifying:

- **Programming Languages**: Through intelligent code analysis
- **Frameworks and Libraries**: Via dependency and import analysis  
- **Database Systems**: Through model and schema detection
- **Project Architecture**: Based on file structure and patterns

### Adding New Technology Detection

To improve AI context for new technologies:

1. **Update `_detect_technologies()` in `ai_service.py`**:

```python
# Add new framework detection
if 'spring-boot' in content_lower:
    technologies['frameworks'].add('Spring Boot')
if 'kubernetes' in content_lower or 'k8s' in content_lower:
    technologies['tools'].add('Kubernetes')
```

2. **Update `_analyze_imports()` for new languages**:

```python
elif file_path.endswith('.go'):
    # Extract Go imports
    go_imports = re.findall(r'import\s+["\']([^"\']+)', content)
    for imp in go_imports:
        if not imp.startswith('.'):
            imports['go'].append(imp.split('/')[0])
```

### Philosophy: AI-First Approach

- **No Hardcoded Templates**: AI generates content based on project analysis
- **Universal Support**: Works with any programming language or framework
- **Context-Aware**: Detection provides rich context to AI for better generation
- **Extensible**: Easy to add support for new technologies

## Adding New Slash Commands

Slash commands provide in-IDE functionality through Cursor rules.

### Creating a New Slash Command

1. **Create the rule file** in `.cursor/rules/cursor-init/[command].mdc`:

```markdown
---
description: "Creates a new [document type] from AI analysis"
alwaysApply: true
---

@if(user_message.starts_with("/[command]")) {
  "I will create a new [document type] based on AI analysis of your project.
  
  [Detailed instructions for the AI agent about what to analyze and generate]"
}
```

2. **Implement AI generation** in `cli/cursor_init/ai_service.py`:

```python
def generate_[document_type](self, project_root: str = '.') -> str:
    """Generate [document type] using AI analysis."""
    cursor_rules = self._read_cursor_rules(project_root)
    project_structure = self._analyze_project_structure(project_root)
    
    system_prompt = '''Expert prompt for generating this document type'''
    user_prompt = f'''Generate content based on: {project_structure}'''
    
    return self.ai_service.generate_content(system_prompt, user_prompt)
```

3. **Integrate with CLI** in `cli/cursor_init/__main__.py`:

```python
[command]_parser = subparsers.add_parser("[command]", help="Generate [document type].")
[command]_parser.set_defaults(func=lambda args: generate_[document_type]())
```

## Testing Your Contributions

### Manual Testing

1. **Test AI Generation**:

```bash
cd cli
python -m cursor_init init
python -m cursor_init update
python -m cursor_init gen-er-diagram
python -m cursor_init gen-arch-diagram
```

2. **Test in Cursor IDE**:
   - Try slash commands: `/init-docs`, `/adr "Test Decision"`, `/gen-er-diagram`
   - Verify AI-generated content is relevant and accurate

3. **Test with Different Project Types**:
   - Test with various programming languages
   - Test with different frameworks and architectures
   - Test with diverse project structures

### Automated Testing

When adding tests (future enhancement):

```python
def test_ai_generation():
    # Mock AI service
    # Test generation functions
    # Assert content quality and relevance
    pass
```

## Code Style and Standards

### Python Code Style

- **Follow PEP 8** for Python code formatting
- **Use type hints** for function parameters and return values
- **Keep functions focused** and single-purpose
- **Use descriptive variable names**
- **Prefer composition over complex inheritance**

### AI Integration Guidelines

- **Provide Rich Context**: Include project structure, cursor rules, and detected technologies
- **Use Specific Prompts**: Tailor system prompts for each document type
- **Handle Errors Gracefully**: Always provide fallback behavior for AI failures
- **Respect Rate Limits**: Implement appropriate delays and error handling

## Pull Request Guidelines

### Before Submitting

- [ ] Test AI generation with multiple project types
- [ ] Ensure code follows project style
- [ ] Update documentation if needed
- [ ] Verify slash commands work in Cursor IDE

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New AI generation capability
- [ ] New slash command
- [ ] Framework detection improvement
- [ ] Bug fix
- [ ] Documentation update

## Testing
- [ ] Manual testing completed with different project types
- [ ] AI generation produces quality content
- [ ] Slash commands work correctly
- [ ] Edge cases considered

## AI Integration
- [ ] Appropriate system prompts created
- [ ] Rich project context provided
- [ ] Error handling implemented
- [ ] Rate limiting considered
```

## Philosophy and Design Principles

### AI-First Documentation

- **Smart Generation**: AI analyzes your specific codebase and generates tailored documentation
- **No Generic Templates**: Every piece of documentation is customized to your project
- **Technology Agnostic**: Works with any programming language or framework
- **Context Aware**: Leverages project structure, dependencies, and coding patterns

### Developer Experience

- **Zero Configuration**: Works out of the box with any project
- **IDE Integration**: Seamless integration through Cursor slash commands
- **Continuous Improvement**: Documentation stays fresh as code evolves
- **Extensible**: Easy to add new document types and capabilities

## Getting Help

- **Issues**: Report bugs or request features via GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Check project documentation for implementation details

## License

By contributing to `cursor-init`, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to `cursor-init`! Your contributions help make AI-powered documentation accessible to developers everywhere.

### What We Support

The framework automatically detects and adapts to any codebase through AI analysis:

- **Languages**: Any programming language with AI-powered analysis
- **Frameworks**: Universal framework support via intelligent detection
- **Databases**: Any database system with model or schema definitions
- **Project Types**: Web apps, mobile apps, APIs, libraries, and more
