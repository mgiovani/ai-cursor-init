# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Enhanced configuration options with comprehensive example
- Additional template customization capabilities
- Improved framework detection logic

## [0.1.0] - 2025-06-12

### Added

- Initial release of cursor-init framework
- Zero-installation setup with .cursor rules
- Slash commands for in-IDE documentation generation
- CLI tool for CI/CD integration
- Architecture Decision Records (ADR) support with multiple templates
- ER diagram generation from SQLAlchemy models
- System architecture diagram generation
- Framework-aware templates (Python/FastAPI, TypeScript/React)
- Documentation freshness validation
- Template library with multiple variants
- Security-focused code analysis
- Comprehensive documentation and examples

### Features

- `/init-docs` - Scaffold initial project documentation
- `/update-docs` - Update existing documentation
- `/adr` - Create Architecture Decision Records
- `/gen-er-diagram` - Generate ER diagrams from models
- `/gen-arch-diagram` - Generate system architecture diagrams
- `/check-docs` - Validate documentation quality
- `/sync-docs` - Sync all documentation with codebase
- `/list-templates` - List available templates

### Security

- Static code analysis by default
- Sandboxed execution for advanced features
- No arbitrary code execution without consent
- Resource limits and timeouts
