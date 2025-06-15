# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2025-06-15

### Added

- **Enhanced Architecture Templates**: Added Google, Enterprise, and Arc42 template variants for comprehensive architecture documentation
- **Multiple Onboarding Template Variants**:
  - Developer template for technical onboarding (~200 lines)
  - Contributor template for open source projects (~240 lines)
  - User template for end-user documentation (~180 lines)
- **RFC Template System**: Added minimal, standard, and detailed RFC template variants with lifecycle support
- **Comprehensive Template Improvements**: Enhanced component diagrams and ER diagram templates with detailed content
- **Template Configuration Support**: Added `.cursor-init.yaml` configuration for template selection and customization
- **Data Model Template Variants**: Set comprehensive data model template as default for enhanced documentation

### Changed

- Replaced old general/python/frontend onboarding templates with new variant system
- Updated configuration system to support template selection across all document types
- Enhanced template documentation with customization guides

### Improved

- Template content quality with more comprehensive sections and examples
- Configuration flexibility for different project needs and documentation styles
- Documentation generation with better structure and professional formatting

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
