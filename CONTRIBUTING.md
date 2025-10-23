# Contributing to AI-Cursor-Init

**Version:** 1.0.0  
**Last Updated:** 2025-10-23

Thank you for your interest in contributing to the AI-Cursor-Init framework! This guide will help you understand how to contribute effectively to this documentation generation system.

## 🎯 **Project Overview**

AI-Cursor-Init is a template-driven documentation framework that integrates with Cursor IDE to provide intelligent, contextual documentation generation through slash commands.

**Core Components:**

- **Native Commands**: 16 slash commands appearing in `/` autocomplete menu
- **Proactive Rules**: 5 always-on rules for context and quality guidance
- **Templates**: 21 documentation templates with multiple variants
- **Framework Detection**: AI-powered analysis of project structures
- **Documentation Generation**: Context-aware content creation

## 🚀 **Quick Start for Contributors**

### Prerequisites

- **Cursor IDE** (required for testing framework functionality)
- **Git** for version control
- **Markdown knowledge** for template development
- **Understanding of:**
  - Cursor IDE native commands and rules system
  - Mermaid diagram syntax  
  - YAML configuration
  - Markdown (for commands and templates)

### Setup Steps

1. **Fork and Clone:**

   ```bash
   git clone https://github.com/your-username/ai-cursor-init.git
   cd ai-cursor-init
   ```

2. **Create Development Branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Test the Framework:**

   ```bash
   # Copy framework to a test project
   cp -r .cursor/ ../test-project/.cursor/
   
   # Open test project in Cursor and try:
   # /init-docs
   # /gen-arch-diagram
   # /adr "Test Decision"
   ```

## 🛠️ **Contributing Areas**

### 1. **Template Development**

Add new documentation templates or improve existing ones:

**Template Structure:**

```
.cursor/cursor-init/templates/
├── architecture/
│   ├── architecture_google.md     # Google's architecture template
│   ├── architecture_enterprise.md # Enterprise architecture template
│   └── architecture_arc.md        # Arc42 architecture template
├── adr/
│   ├── adr_template_nygard.md     # Michael Nygard's ADR format
│   ├── adr_template_full.md       # Comprehensive ADR
│   ├── adr_template_lightweight.md # Simplified ADR format
│   └── adr_template_madr.md       # Markdown ADRs
├── onboarding/
│   ├── onboarding_developer.md    # Developer-focused onboarding
│   ├── onboarding_contributor.md  # Contributor onboarding
│   └── onboarding_user.md         # End-user onboarding
└── rfc/
    ├── rfc_template_minimal.md    # Minimal RFC
    ├── rfc_template_standard.md   # Standard RFC
    └── rfc_template_detailed.md   # Detailed RFC
```

**Adding a New Template:**

1. Create template file in appropriate category
2. Use `{{PLACEHOLDER}}` syntax for dynamic content
3. Include Mermaid diagrams where beneficial
4. Test with multiple project types

**Example Template:**

````markdown
# {{PROJECT_NAME}} - Custom Documentation

**Last Updated:** {{DATE}}
**Version:** {{VERSION}}

## Overview

{{PROJECT_DESCRIPTION}}

## Architecture

```mermaid
graph TD
    {{ARCHITECTURE_DIAGRAM}}
```

## Implementation Details

{{IMPLEMENTATION_DETAILS}}

````

### 2. **Cursor Rules Enhancement**

Improve slash command functionality by enhancing Cursor rules:

**Rule Structure:**

```markdown
---
description: When the user types `/command-name` to perform specific action
globs: 
alwaysApply: false
---
# Rule Title

Detailed instructions for the AI agent on how to handle this command.

1. **Analysis Phase:** What to analyze in the project
2. **Processing Phase:** How to process the information  
3. **Generation Phase:** What content to generate
4. **Integration Phase:** How to integrate with existing docs

Let me [specific action]...

I will use the [tool_name] tool to [specific functionality].
```

**Key Areas for Rule Enhancement:**

- **Framework Detection**: Improve technology stack identification
- **Content Generation**: Enhance AI prompts for better output
- **Integration Logic**: Better handling of existing documentation
- **Error Handling**: Graceful degradation and helpful error messages

### 3. **Framework Detection**

Improve the AI's ability to detect and adapt to different project types:

**Detection Categories:**

- **Language Detection**: Python, TypeScript, Go, Rust, etc.
- **Framework Detection**: FastAPI, Next.js, React, Django, etc.
- **Database Detection**: PostgreSQL, MongoDB, SQLite, etc.
- **Infrastructure Detection**: Docker, Kubernetes, AWS, etc.

**Enhancement Areas:**

- Pattern recognition for new frameworks
- Configuration file parsing improvements
- Dependency analysis enhancements
- Project structure classification

### 4. **Documentation Improvements**

Help improve project documentation:

- **README Updates**: Keep installation and usage instructions current
- **Template Documentation**: Document template variants and customization
- **Rule Documentation**: Explain slash command functionality
- **Configuration Guide**: Improve `.cursor-init.yaml` documentation

## 📋 **Contribution Guidelines**

### Code Quality Standards

- **Template Consistency**: Follow established placeholder patterns
- **Mermaid Syntax**: Ensure all diagrams use valid Mermaid syntax
- **Markdown Quality**: Use consistent formatting and structure
- **Testing**: Test templates with multiple project types

### Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch from `main`
3. **Make** your changes with clear, focused commits
4. **Test** your changes manually with different project types
5. **Update** documentation if needed
6. **Submit** pull request with clear description

### PR Template

Use this template for pull requests:

```markdown
## Description
Brief description of changes made

## Type of Change
- [ ] New template variant
- [ ] Rule enhancement  
- [ ] Framework detection improvement
- [ ] Documentation update
- [ ] Bug fix

## Testing Done
- [ ] Tested with Python project
- [ ] Tested with TypeScript project
- [ ] Tested with database models
- [ ] Tested slash commands
- [ ] Validated Mermaid diagrams

## Documentation Impact
- [ ] Updated README
- [ ] Updated template documentation
- [ ] Added example usage
- [ ] Updated configuration guide
```

### Commit Message Format

Use conventional commit format:

```
type(scope): description

feat(templates): add comprehensive security template
fix(rules): improve database model detection
docs(readme): update installation instructions
```

## 🧪 **Testing Your Contributions**

### Manual Testing Process

1. **Template Testing:**

   ```bash
   # Test template with different project types
   cp -r .cursor/ ../python-project/.cursor/
   cp -r .cursor/ ../react-project/.cursor/  
   cp -r .cursor/ ../api-project/.cursor/
   
   # In each project, test relevant commands
   ```

2. **Rule Testing:**
   - Test slash commands in different project contexts
   - Verify AI prompts generate appropriate content
   - Check error handling with missing dependencies

3. **Integration Testing:**
   - Test with existing documentation
   - Verify template selection logic
   - Check placeholder replacement accuracy

### Quality Checklist

Before submitting PR:

- [ ] **Template Syntax**: All placeholders follow `{{PLACEHOLDER}}` format
- [ ] **Mermaid Diagrams**: Valid syntax, renders correctly
- [ ] **Markdown Quality**: Proper formatting, no broken links
- [ ] **Multi-Project Testing**: Works with different project types
- [ ] **Documentation**: Changes are documented appropriately

## 🎨 **Design Principles**

### Template Design

- **Placeholder-Driven**: Use placeholders for all dynamic content
- **Framework-Agnostic**: Templates adapt to any technology stack
- **Professional Quality**: Output should match industry standards
- **Maintainable**: Clear structure, easy to understand and modify

### Rule Design

- **Context-Aware**: Analyze project before generating content
- **Intelligent Defaults**: Smart choices without user configuration
- **Graceful Degradation**: Handle missing information elegantly
- **User-Friendly**: Clear instructions and helpful error messages

### AI Integration

- **Rich Context**: Provide comprehensive project analysis to AI
- **Specific Prompts**: Clear, detailed instructions for content generation
- **Quality Control**: Validation and error handling for AI output
- **Template Integration**: Seamless integration with template system

## 🏆 **Recognition**

Contributors are recognized in:

- **CHANGELOG.md**: All contributions documented
- **README.md**: Major contributors highlighted
- **Git History**: All commits properly attributed
- **GitHub**: Contributor graphs and statistics

## 💬 **Getting Help**

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and community discussion
- **Code Review**: Detailed feedback on pull requests
- **Documentation**: Comprehensive guides and examples

## 📚 **Resources**

### Learning Resources

- **Cursor IDE Documentation**: Understanding the platform
- **Mermaid Documentation**: Diagram syntax and examples
- **Template Examples**: Study existing templates for patterns
- **AI Prompt Engineering**: Best practices for AI instructions

### Development Tools

- **Cursor IDE**: Primary development and testing environment
- **Markdown Editors**: For template development
- **Git**: Version control and collaboration
- **Mermaid Live Editor**: For diagram testing

## 🔧 **Technical Implementation Notes**

### Philosophy: AI-First Approach

- **No Hardcoded Templates**: AI generates content based on project analysis
- **Universal Support**: Works with any programming language or framework
- **Context-Aware**: Detection provides rich context to AI for better generation
- **Extensible**: Easy to add support for new technologies

### Framework Architecture

The AI-powered analysis automatically detects and adapts to any project structure, automatically identifying:

- **Programming Languages**: Through intelligent code analysis
- **Frameworks and Libraries**: Via dependency and import analysis  
- **Database Systems**: Through model and schema detection
- **Project Architecture**: Based on file structure and patterns

### Security Considerations

The framework operates with security-first principles:

**Static Analysis Only:**

- File system analysis (read-only)
- Configuration file parsing
- Import statement analysis via AST parsing
- Directory structure pattern matching

**Prohibited Operations:**

- Code execution or dynamic imports
- Network requests during analysis
- File modification outside `docs/` directory
- Access to files outside project directory

## 📄 **License**

By contributing to AI-Cursor-Init, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the AI-Cursor-Init framework! Your contributions help developers worldwide create better documentation more efficiently.

### What We Support

The framework automatically detects and adapts to any codebase through AI analysis:

- **Languages**: Any programming language with AI-powered analysis
- **Frameworks**: Universal framework support via intelligent detection
- **Databases**: Any database system with model or schema definitions
- **Project Types**: Web apps, mobile apps, APIs, libraries, and more
