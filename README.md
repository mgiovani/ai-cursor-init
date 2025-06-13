# cursor-init

AI-driven in-IDE documentation framework for generating and maintaining project documentation, diagrams, and Architecture Decision Records (ADRs).

## Overview

`cursor-init` provides seamless documentation generation directly within Cursor IDE through custom slash commands, plus a CLI tool for CI/CD integration. All documentation is generated as Markdown with Mermaid diagrams, keeping everything version-controlled alongside your code.

## Features

- **Zero Installation**: Works immediately with just `.cursor` rules and templates in your project
- **Self-Contained**: No external dependencies required for in-IDE functionality
- **Automated Diagrams**: Generate ER diagrams from SQLAlchemy models and architecture diagrams from code structure
- **Template Library**: Pre-built templates for ADRs, architecture docs, onboarding guides, and more
- **CI Integration**: CLI tool for automated documentation validation and updates
- **Framework-Aware**: Tailored templates for Python/FastAPI and TypeScript/React projects

## Slash Commands

| Command | Description |
|---------|-------------|
| `/init-docs` | Scaffold initial project documentation |
| `/update-docs` | Update existing documentation to reflect code changes |
| `/adr` | Create a new Architecture Decision Record |
| `/gen-er-diagram` | Generate ER diagram from SQLAlchemy models |
| `/gen-arch-diagram` | Generate system architecture diagram |
| `/check-docs` | Validate documentation freshness and report issues |
| `/sync-docs` | Sync all documentation with current codebase |
| `/list-templates` | List all available documentation templates |

## Quick Start

### Manual Installation (Zero Dependencies)

To enable `cursor-init` functionality in your project without any installation:

1. **Copy the required directories** from this repository to your project root:

   ```bash
   # From the cursor-init repository directory
   cp -r .cursor/ /path/to/your-project/
   cp -r templates/ /path/to/your-project/
   ```

2. **Verify the structure** in your project:

   ```
   your-project/
   ├── .cursor/
   │   └── rules/
   │       ├── init-docs.mdc
   │       ├── adr.mdc
   │       ├── check-docs.mdc
   │       └── ... (other rule files)
   ├── templates/
   │   ├── adr/
   │   ├── architecture/
   │   ├── onboarding/
   │   └── ... (other template directories)
   └── ... (your project files)
   ```

3. **Start using slash commands** in Cursor:
   - Type `/init-docs` to scaffold initial documentation
   - Use `/gen-er-diagram` for database schemas
   - Run `/check-docs` to validate documentation quality

### Alternative: CLI Installation

For CI/CD integration and advanced features, install the CLI tool:

```bash
pip install cursor-init
```

## CLI Usage

For CI/CD integration and non-interactive use:

```bash
# Install the CLI tool
pip install cursor-init

# Initialize documentation
cursor-init init

# Update documentation
cursor-init update --apply

# Check documentation freshness (CI-friendly)
cursor-init check-docs

# Generate specific diagrams
cursor-init gen-er-diagram
cursor-init gen-arch-diagram
```

## Security Considerations

### Secure Code Parsing

The `cursor-init` tool analyzes your project code to generate documentation and diagrams while maintaining strict security boundaries:

**Primary Approach: Static Analysis**

- Uses Abstract Syntax Tree (AST) parsing to analyze code structure
- Performs text-based analysis of configuration files
- No arbitrary code execution during analysis
- Safe for use on untrusted codebases

**Limited Dynamic Imports**
For certain advanced features (e.g., full SQLAlchemy model introspection), the CLI may need to import your project's code:

⚠️ **Security Notice**: The `cursor-init` CLI may, for certain advanced features (e.g., full introspection of ORM models), temporarily import your project's code. While designed with security in mind, always exercise caution when running on untrusted code.

**Security Safeguards:**

- Isolated execution environments with timeouts
- Explicit user consent required for dynamic imports
- Graceful fallback to static analysis when possible
- No network access during code analysis
- Resource limits and sandboxing

**Best Practices:**

- Review generated documentation before committing
- Use static analysis features when working with untrusted code
- Report security concerns through our security channels

## Documentation Structure

Generated documentation follows this structure:

```
docs/
├── architecture.md          # System architecture overview
├── onboarding.md           # Project setup and onboarding
├── data-model.md           # ER diagrams and data model
└── adr/                    # Architecture Decision Records
    ├── 0001-record-architecture-decisions.md
    └── ...
```

## Templates

The tool includes templates for:

- **Architecture Decision Records (ADRs)**: Multiple formats (Nygard, MADR, comprehensive)
- **Architecture Documentation**: System overviews, component diagrams
- **Onboarding Guides**: Framework-specific setup instructions
- **Data Models**: ER diagrams with Mermaid syntax
- **API Documentation**: Endpoint summaries and integration guides

## Framework Support

Currently supports:

- **Python**: FastAPI, SQLAlchemy, Django
- **TypeScript**: React, Next.js, Node.js
- **Databases**: PostgreSQL, MySQL, SQLite (via SQLAlchemy)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:

- Adding new documentation templates
- Extending framework detection logic  
- Creating new slash commands
- Testing and submitting pull requests

## License

Released under the MIT License. See [LICENSE](LICENSE) for details.

## Support

- **Documentation**: See `docs/` directory for detailed guides
- **Issues**: Report bugs and feature requests on GitHub
- **Security**: Report security issues privately through our security channels

---

**Note**: This tool prioritizes security and will never execute untrusted code without explicit user consent and proper sandboxing.
