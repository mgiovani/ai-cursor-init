# AI-Cursor-Init Framework Onboarding Guide

**Last Updated:** 2025-06-15  
**Project Type:** Cursor IDE Documentation Framework  
**Current State:** Template & Rule-based System

This guide provides essential information for contributors to the AI-Cursor-Init project - a documentation framework that integrates with Cursor IDE.

## Overview and Goals

* **Project Name:** AI-Cursor-Init
* **Purpose:** Provide a template-based documentation framework that works seamlessly within Cursor IDE
* **Key Goals:**
  * Enable intelligent documentation generation through structured templates
  * Provide framework-aware documentation templates and content generation  
  * Offer seamless integration with Cursor IDE through slash commands
  * Support automated diagram generation using Mermaid
  * Maintain documentation freshness through template-based generation

## Contacts

* **Primary Maintainer:** [GitHub: @mgiovani](https://github.com/mgiovani)
* **Email:** <e@mgiovani.com>
* **Issues:** [GitHub Issues](https://github.com/mgiovani/ai-cursor-init/issues)
* **Repository:** [GitHub Repository](https://github.com/mgiovani/ai-cursor-init)

## Development Philosophy

* **Template-Driven:** Structured, consistent documentation through templates
* **Version Control:** Use Git with feature branches. All changes go through pull requests
* **Code Reviews:** All template and rule changes require review before merging
* **Documentation as Code:** Version-controlled alongside templates and rules
* **AI Integration:** Leverage Cursor's AI capabilities for intelligent content generation

## Development Environment Setup

### Prerequisites

* **Cursor IDE** (required for testing the framework)
* **Git** for version control
* **Markdown Editor** (optional, for template development)
* **Understanding of:**
  * Cursor IDE rules and templates
  * Mermaid diagram syntax
  * YAML configuration

### Setup Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/mgiovani/ai-cursor-init.git
    cd ai-cursor-init
    ```

2. **Open in Cursor IDE:**

    ```bash
    cursor .
    ```

3. **Test the Framework:**

    Try the slash commands in Cursor IDE:

    ```
    /init-docs
    /adr "Test ADR"
    /gen-arch-diagram
    /sync-docs
    ```

4. **Explore the Structure:**

    * `.cursor/rules/` - Slash command definitions
    * `.cursor/templates/` - Documentation templates
    * `docs/` - Example documentation (living examples)
    * `.cursor-init.example.yaml` - Configuration example

## Project Structure

* **`/.cursor/rules`:** Cursor IDE integration rules for slash commands
  * `/cursor-init/` - Framework-specific rules
  * Command handlers for documentation generation
* **`/.cursor/templates`:** Documentation templates organized by type
  * `/architecture/` - Architecture documentation variants
  * `/adr/` - Architecture Decision Record templates
  * `/onboarding/` - Onboarding guide templates
  * `/diagrams/` - Diagram-focused templates
  * `/security/` - Security documentation templates
* **`/docs`:** Project documentation (serves as living examples)
  * `/adr/` - Architecture Decision Records
  * `/development/` - Development guides and patterns
* **Configuration:**
  * `.cursor-init.example.yaml` - Configuration template
  * Various `.md` files with project documentation

## Key Features to Understand

### Template System

* Framework-specific templates with multiple variants
* YAML-based configuration for template selection
* Context-aware placeholder replacement
* Support for custom templates via configuration

### Cursor IDE Integration

* Slash commands for in-IDE documentation workflow
* Zero-installation setup through Cursor rules
* Seamless integration with existing project workflows
* AI-powered content generation through Cursor's system

### Diagram Generation

* Mermaid-based diagrams stored as version-controlled text
* Architecture diagrams from project structure analysis
* Support for ER diagrams, deployment diagrams, etc.
* Template-driven diagram generation

### Configuration System

* `.cursor-init.yaml` for project-specific settings
* Template variant selection
* Auto-detection configuration
* Quality control parameters

## Development Workflow

1. **Create Feature Branch:** `git checkout -b feature/your-feature-name`
2. **Make Changes:** Edit templates, rules, or documentation
3. **Test in Cursor:** Verify slash commands work correctly
4. **Update Examples:** Update `docs/` if needed to reflect changes
5. **Submit PR:** Create pull request with clear description
6. **Address Review:** Respond to feedback on templates/rules
7. **Merge:** Maintainer will merge approved changes

## Testing Guidelines

* **Template Testing:** Test template rendering with various project types
* **Rule Testing:** Verify slash commands work correctly in Cursor IDE  
* **Integration Testing:** Test complete workflows (init → update → sync)
* **Documentation Testing:** Verify generated documentation is valid and useful

## Template Development

### Template Structure

* Use `{{PLACEHOLDER}}` syntax for variable substitution
* Follow consistent markdown formatting
* Include Mermaid diagrams where appropriate
* Provide multiple variants for different use cases

### Template Categories

* **Architecture:** System design documentation
* **ADR:** Architecture Decision Records
* **Onboarding:** Developer setup guides
* **Data Model:** Database and schema documentation
* **Security:** Security policies and compliance
* **Deployment:** Infrastructure and deployment guides

### Rule Development

* Rules are defined in `.cursor/rules/` directory
* Use Markdown Control (MDC) format
* Include clear command descriptions and examples
* Test with various project configurations

## Resources and Links

* **GitHub Repository:** [https://github.com/mgiovani/ai-cursor-init](https://github.com/mgiovani/ai-cursor-init)
* **Architecture Overview:** [docs/architecture.md](./architecture.md)
* **ADR Log:** [docs/adr/](./adr/)
* **Development Patterns:** [docs/development/](./development/)
* **Template Examples:** [.cursor/templates/](./.cursor/templates/)
* **Issue Templates:** [GitHub Issues](https://github.com/mgiovani/ai-cursor-init/issues)

## Contributing

We welcome contributions! Please:

1. **Understand the Framework:** Learn how templates and rules work together
2. **Start Small:** Begin with template improvements or new variants
3. **Ask Questions:** Use GitHub Issues for clarification
4. **Follow Standards:** Maintain template quality and consistency
5. **Document Changes:** Update relevant documentation and examples

## Current Project Status

This project is currently in **template-based framework** state:

* ✅ Template system with multiple variants
* ✅ Cursor IDE integration via rules
* ✅ Configuration system
* ✅ Living documentation examples
* ⚠️ Limited to Cursor IDE environment

---

*This onboarding guide is maintained using the ai-cursor-init framework itself - a living example of the tool in action.*
