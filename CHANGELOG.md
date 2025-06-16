# Changelog

All notable changes to this project will be documented in this file.

## [0.6.0] - 2025-06-15

### Removed

- **CLI Interface**: Completely removed command-line interface to focus on pure Cursor IDE integration
- **Python Dependencies**: Eliminated all Python CLI modules, setup files, and external dependencies
- **Framework-Specific References**: Removed hardcoded framework mentions (Python, TypeScript, FastAPI, React, etc.)

### Changed

- **Universal Framework Support**: Made project completely language/framework agnostic through AI-powered detection
- **Documentation**: Updated all documentation to reflect AI-powered universal detection instead of specific frameworks
- **Configuration**: Made all configuration examples generic and framework-neutral
- **Issue Templates**: Updated to be language-agnostic

### Added

- **ADR-0004**: Architecture Decision Record documenting CLI removal rationale
- **Pure Cursor IDE Workflow**: Streamlined to slash-commands-only approach
- **Zero-Dependency Operation**: True zero-installation setup with no external requirements

## [0.5.0] - 2025-06-15

### Added

- **Template System**: Comprehensive documentation templates with multiple variants
- **Framework Detection**: Automatic technology stack detection and template adaptation
- **AI Enhancement**: Context-aware content generation through Cursor IDE integration

### Changed

- **Project Focus**: Streamlined to template-based documentation framework
- **Architecture**: Simplified to Cursor IDE native integration

### Removed

- **External Dependencies**: Eliminated CLI dependencies for zero-installation setup

## [0.4.0] - 2025-06-12

### Added

- Zero-installation framework for Cursor IDE
- Template-based documentation generation
- Slash command integration
- Framework-aware content generation
- Multiple template variants per document type

### Documentation

- Updated architecture documentation to reflect template-based approach
- Comprehensive onboarding guide for template development
- Updated data model documentation for current implementation

---

*Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)*
