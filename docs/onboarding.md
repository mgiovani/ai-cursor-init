# AI-Cursor-Init Project Onboarding Guide

This guide provides essential information for contributors to the AI-Cursor-Init project - an AI-powered documentation framework for Cursor IDE.

## Overview and Goals

* **Project Name:** AI-Cursor-Init
* **Purpose:** Provide an AI-powered documentation framework that works seamlessly within Cursor IDE and as a standalone CLI tool
* **Key Goals:**
  * Enable intelligent documentation generation using multiple AI providers (OpenAI, Anthropic, Gemini)
  * Provide framework-aware documentation templates and content generation
  * Offer seamless integration with Cursor IDE through slash commands
  * Support automated diagram generation (ER diagrams, architecture diagrams)
  * Maintain documentation freshness through CI-friendly validation tools

## Contacts

* **Primary Maintainer:** [GitHub: @mgiovani](https://github.com/mgiovani)
* **Email:** <e@mgiovani.com>
* **Issues:** [GitHub Issues](https://github.com/mgiovani/ai-cursor-init/issues)
* **Repository:** [GitHub Repository](https://github.com/mgiovani/ai-cursor-init)

## Development Philosophy

* **Code Quality:** Follow PEP 8 for Python. Use type hints, single quotes, and avoid unnecessary comments/docstrings
* **Version Control:** Use Git with feature branches. All changes go through pull requests
* **Code Reviews:** All code requires review before merging
* **Testing:** Write unit tests for critical business logic; ensure tests are isolated and fast
* **AI Integration:** Responsible AI usage with proper error handling and user consent

## Development Environment Setup

### Prerequisites

* **Python 3.12+** (required for modern typing features)
* **Git** for version control
* **Cursor IDE** (recommended for testing slash commands)
* **AI Provider API Keys** (optional, for testing AI features):
  * OpenAI API key
  * Anthropic API key  
  * Google Gemini API key

### Setup Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/mgiovani/ai-cursor-init.git
    cd ai-cursor-init
    ```

2. **Set up Python Environment:**

    ```bash
    # Create virtual environment
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    
    # Install dependencies
    pip install -r requirements.txt
    
    # Install in development mode
    pip install -e ./cli
    ```

3. **Configure AI Providers (Optional):**

    ```bash
    # Create .env file with your API keys
    cp .env.example .env
    
    # Edit .env with your API keys:
    # OPENAI_API_KEY=your_openai_key_here
    # ANTHROPIC_API_KEY=your_anthropic_key_here
    # GEMINI_API_KEY=your_gemini_key_here
    ```

4. **Test the Installation:**

    ```bash
    # Test CLI commands
    ai-cursor-init --version
    ai-cursor-init init
    
    # Test in Cursor IDE by opening the project and trying slash commands like:
    # /init-docs
    # /adr "Test ADR"
    ```

## Project Structure

* **`/cli`:** Main CLI application source code
  * `/cli/cursor_init`: Python package with core functionality
  * `/cli/cursor_init/ai_service.py`: AI provider integration
  * `/cli/cursor_init/detect_framework.py`: Framework detection logic
  * `/cli/cursor_init/generate_diagrams.py`: Diagram generation
* **`/.cursor/rules`:** Cursor IDE integration rules for slash commands
* **`/.cursor/templates`:** Documentation templates organized by type
* **`/docs`:** Project documentation (this serves as an example)
  * `/docs/adr`: Architecture Decision Records
  * `/docs/development`: Development guides and patterns
* **`/tests`:** Test suite (to be expanded)

## Key Features to Understand

### AI Integration

- Multi-provider support with fallback mechanisms
* Context-aware documentation generation
* Intelligent framework detection and content customization

### Template System

- Framework-specific templates (Python/FastAPI, TypeScript/React)
* Multiple variants per document type
* Custom template support via configuration

### Cursor IDE Integration

- Slash commands for in-IDE documentation workflow
* Zero-installation setup through Cursor rules
* Seamless integration with existing project workflows

### Diagram Generation

- Mermaid-based diagrams stored as version-controlled text
* ER diagrams from SQLAlchemy model analysis
* Architecture diagrams from project structure analysis

## Development Workflow

1. **Create Feature Branch:** `git checkout -b feature/your-feature-name`
2. **Make Changes:** Follow coding standards and write tests
3. **Test Thoroughly:** Test both CLI and Cursor IDE integration
4. **Update Documentation:** Update relevant docs if needed
5. **Submit PR:** Create pull request with clear description
6. **Address Review:** Respond to code review feedback
7. **Merge:** Maintainer will merge approved changes

## Testing Guidelines

* **Unit Tests:** Test individual functions and classes
* **Integration Tests:** Test AI provider integrations (with mocking)
* **End-to-End Tests:** Test complete workflows (CLI commands, slash commands)
* **Documentation Tests:** Verify generated documentation is valid

## Resources and Links

* **GitHub Repository:** [https://github.com/mgiovani/ai-cursor-init](https://github.com/mgiovani/ai-cursor-init)
* **PyPI Package:** [https://pypi.org/project/ai-cursor-init/](https://pypi.org/project/ai-cursor-init/)
* **Architecture Overview:** [docs/architecture.md](./architecture.md)
* **ADR Log:** [docs/adr/](./adr/)
* **Development Patterns:** [docs/development/](./development/)
* **Issue Templates:** [GitHub Issues](https://github.com/mgiovani/ai-cursor-init/issues)

## Contributing

We welcome contributions! Please:

1. **Read the Code:** Understand the existing patterns and architecture
2. **Start Small:** Begin with bug fixes or small feature additions
3. **Ask Questions:** Use GitHub Issues for clarification
4. **Follow Standards:** Maintain code quality and test coverage
5. **Document Changes:** Update relevant documentation

---

*This onboarding guide is maintained using the ai-cursor-init framework itself - a living example of the tool in action.*
