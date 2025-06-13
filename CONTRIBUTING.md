# Contributing to cursor-init

Thank you for your interest in contributing to `cursor-init`! This guide will help you understand how to extend the tool with new templates, add support for additional languages/frameworks, and contribute effectively to the project.

## Table of Contents

- [Getting Started](#getting-started)
- [Adding New Templates](#adding-new-templates)
- [Extending Detection Logic](#extending-detection-logic)
- [Adding New Slash Commands](#adding-new-slash-commands)
- [Testing Your Contributions](#testing-your-contributions)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Code Style and Standards](#code-style-and-standards)

## Getting Started

1. **Fork the repository** and clone your fork locally
2. **Install in development mode**:

   ```bash
   pip install -e .
   ```

3. **Verify the installation**:

   ```bash
   cursor-init --version
   ```

## Adding New Templates

Templates are the foundation of `cursor-init`'s documentation generation. They're organized by document type in the `.cursor/templates/` directory.

### Template Directory Structure

```
.cursor/templates/
├── adr/                    # Architecture Decision Records
├── architecture/           # System architecture documentation
├── onboarding/            # Project onboarding guides
├── rfc/                   # Request For Comments documents
└── diagrams/              # Diagram templates
```

### Adding Templates for Existing Document Types

1. **Navigate to the appropriate directory** (e.g., `.cursor/templates/adr/`)
2. **Create a new template file** following the naming convention:
   - Use descriptive names: `adr_template_[variant].md`
   - Examples: `adr_template_nygard.md`, `adr_template_comprehensive.md`
3. **Write your template** using Markdown with placeholders:

   ```markdown
   ### ADR: [Title]
   
   **Status:** [Status]
   
   **Context:**
   [Describe the context and problem statement]
   ```

### Adding New Document Types

1. **Create a new directory** under `.cursor/templates/` (e.g., `.cursor/templates/security/`)
2. **Add template variants** following the naming convention
3. **Update detection logic** in `cli/cursor_init/detect_framework.py`
4. **Consider adding a new slash command** (see [Adding New Slash Commands](#adding-new-slash-commands))

### Template Best Practices

- Use clear, descriptive section headings
- Include placeholder text in brackets: `[Description]`
- Provide guidance comments where helpful
- Include Mermaid diagram placeholders when relevant:

  ```markdown
  ```mermaid
  graph TD
      A[Component A] --> B[Component B]
  ```

  ```
- Keep templates focused and concise
- Test templates with real projects

## Extending Detection Logic

Detection logic determines which templates and configurations to use based on the project's technology stack.

### Framework Detection

The main detection logic is in `cli/cursor_init/detect_framework.py`. To add support for a new framework:

1. **Add detection function**:

   ```python
   def detect_spring_boot() -> bool:
       """Detect Spring Boot projects."""
       return (
           Path('pom.xml').exists() or 
           Path('build.gradle').exists()
       ) and any(
           'spring-boot' in line.lower()
           for file_path in ['pom.xml', 'build.gradle']
           if Path(file_path).exists()
           for line in Path(file_path).read_text().splitlines()
       )
   ```

2. **Update the main detection function**:

   ```python
   def detect_project_type() -> Dict[str, Any]:
       frameworks = {
           'spring_boot': detect_spring_boot(),
           'fastapi': detect_fastapi(),
           # ... existing frameworks
       }
   ```

3. **Add template mapping** in relevant modules:

   ```python
   FRAMEWORK_TEMPLATES = {
       'spring_boot': {
           'onboarding': 'onboarding_spring.md',
           'architecture': 'architecture_enterprise.md'
       }
   }
   ```

### Common Detection Patterns

- **Package files**: `package.json`, `pyproject.toml`, `pom.xml`, `Cargo.toml`
- **Dependency analysis**: Search for specific packages in dependency files
- **File structure**: Look for conventional directories (`src/`, `app/`, `controllers/`)
- **Import statements**: Parse source files for framework-specific imports
- **Configuration files**: `.env`, `config/`, framework-specific configs

### Example: Adding Django Support

```python
def detect_django() -> bool:
    """Detect Django projects."""
    # Check for Django in requirements
    if Path('requirements.txt').exists():
        requirements = Path('requirements.txt').read_text()
        if 'django' in requirements.lower():
            return True
    
    # Check for Django project structure
    return (
        Path('manage.py').exists() or
        any(Path(p).exists() for p in ['settings.py', 'settings/'])
    )
```

## Adding New Slash Commands

Slash commands provide in-IDE functionality through Cursor rules.

### Creating a New Slash Command

1. **Create the rule file** in `.cursor/rules/[command].mdc`:

   ```markdown
   description: "Creates a new [document type] from template"
   alwaysApply: true

   @if(user_message.starts_with("/[command]")) {
     "I will create a new [document type] based on your input.
     
     [Detailed instructions for the AI agent]"
   }
   ```

2. **Implement CLI counterpart** in `cli/cursor_init/[command].py`:

   ```python
   def create_[document](title: Optional[str] = None) -> str:
       """Create a new [document type] with the given title."""
       # Implementation logic
       return f'Created [document]: {filepath}'
   ```

3. **Integrate with main CLI** in `cli/cursor_init/__main__.py`:

   ```python
   # Import the function
   from .[command] import create_[document]
   
   # Add parser
   [command]_parser = subparsers.add_parser("[command]", help="Create a new [document type].")
   [command]_parser.add_argument("title", nargs='?', default="new-[document]")
   [command]_parser.set_defaults(func=lambda args: create_[document](title=args.title))
   
   # Update command handling
   elif args.command in ["adr", "rfc", "[command]", ...]:
   ```

## Testing Your Contributions

### Manual Testing

1. **Test CLI commands**:

   ```bash
   cursor-init [command] "Test Title"
   ls docs/[document-type]/
   cat docs/[document-type]/test-title.md
   ```

2. **Test detection logic**:

   ```bash
   # Create test project structure
   mkdir test-project && cd test-project
   # Add framework-specific files
   touch package.json  # or pom.xml, etc.
   # Test detection
   cursor-init init
   ```

3. **Test in Cursor IDE**:
   - Copy `.cursor/` to a test project (templates are now included!)
   - Try slash commands: `/init-docs`, `/adr`, etc.
   - Verify generated content

### Automated Testing

When adding tests (future enhancement):

```python
def test_detect_spring_boot():
    # Create temporary project structure
    # Test detection function
    # Assert expected results
    pass
```

## Pull Request Guidelines

### Before Submitting

- [ ] Test your changes manually
- [ ] Ensure code follows project style
- [ ] Update documentation if needed
- [ ] Add examples for new features

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New template
- [ ] Framework detection
- [ ] New slash command
- [ ] Bug fix
- [ ] Documentation update

## Testing
- [ ] Manual testing completed
- [ ] Examples provided
- [ ] Edge cases considered

## Checklist
- [ ] Code follows project style
- [ ] Self-review completed
- [ ] Documentation updated
```

### Commit Message Format

Use clear, descriptive commit messages:

```
feat: add Spring Boot detection and templates
fix: handle edge case in title sanitization
docs: update contributing guide with new examples
```

## Code Style and Standards

### Python Code Style

- **Follow PEP 8** for Python code formatting
- **Use type hints** for function parameters and return values
- **Keep functions focused** and single-purpose
- **Use descriptive variable names**
- **Avoid unnecessary comments** - code should be self-documenting

### Example Code Style

```python
from pathlib import Path
from typing import Optional, Dict, Any

def detect_framework(project_path: Path) -> Dict[str, bool]:
    """Detect frameworks used in the project."""
    return {
        'fastapi': _has_dependency('fastapi', project_path),
        'react': _has_dependency('react', project_path),
    }

def _has_dependency(package: str, project_path: Path) -> bool:
    """Check if package exists in project dependencies."""
    requirements_file = project_path / 'requirements.txt'
    if requirements_file.exists():
        content = requirements_file.read_text().lower()
        return package.lower() in content
    return False
```

### Template Style

- Use consistent Markdown formatting
- Include clear section headings
- Provide helpful placeholder text
- Use Mermaid for diagrams when appropriate

### Rule File Style

- Include descriptive YAML front-matter
- Provide clear instructions for the AI agent
- Use consistent trigger patterns
- Include examples in instructions

## Getting Help

- **Issues**: Report bugs or request features via GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Check `docs/implementation_plan.md` for architectural details

## License

By contributing to `cursor-init`, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to `cursor-init`! Your contributions help make documentation easier for developers everywhere.
