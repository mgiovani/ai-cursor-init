# Changelog

All notable changes to this project will be documented in this file.

## [0.7.0] - 2025-06-16

### Added

- **AI-Driven Documentation Generation**: Intelligent analysis of project structure to determine relevant documentation types
- **True Opt-Out Configuration**: Zero-config operation with ability to disable specific documentation types
- **Template System Integration**: Proper template loading from `.cursor/templates/` with variant support
- **Custom Template Paths**: Support for user-defined template locations and custom templates
- **Placeholder Replacement System**: Dynamic content replacement using `{{PLACEHOLDER}}` syntax
- **Comprehensive Configuration Examples**: Updated `.cursor-init.example.yaml` with all documentation types and usage examples

### Changed

- **Token Optimization**: Reduced token usage by ~90% by converting 20+ rules from always-applied to agent-requestable
- **Rule Loading**: Only 2 essential rules remain always-applied, others loaded on-demand based on context
- **Documentation Behavior**: Changed from "opt-in" to "opt-out" - AI determines relevance, users can disable
- **Template Loading**: RFC and ADR commands now use proper template system instead of hardcoded content
- **Configuration Structure**: Enhanced YAML structure with clear categorization (core, data, infrastructure, development)
- **Command Behavior**: All slash commands now respect `.cursor-init.yaml` configuration settings

### Fixed

- **Template System**: RFC and ADR commands now properly load templates with variants
- **Configuration Respect**: All commands now check configuration before generating documentation
- **Copy Command**: Fixed incorrect copy command in README (`cp -r path/to/ai-cursor-init/.cursor/ your-project/.cursor/`)
- **Consistent Language**: Unified "opt-out" terminology across all rules and documentation

### Performance

- **Memory Usage**: Reduced memory footprint through on-demand rule loading
- **Load Time**: Faster rule processing and template loading
- **Token Efficiency**: Massive reduction in token consumption while maintaining full functionality

### Documentation

- **Rule Descriptions**: Added YAML frontmatter with clear descriptions for when each rule should be used
- **Template Variants**: Documented all available template options and customization paths
- **AI Behavior**: Clear explanation of AI-driven relevance detection and opt-out semantics
- **Migration Guide**: Comprehensive guidance for existing users (no breaking changes)

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
