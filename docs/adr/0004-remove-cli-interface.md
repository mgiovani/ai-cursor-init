# ADR-0004: Remove CLI Interface and Focus on Pure Cursor IDE Integration

## Status

Accepted

## Context

The project initially included both a command-line interface (CLI) and Cursor IDE slash commands for documentation generation. This dual approach created several challenges:

1. **Maintenance Overhead**: Maintaining two different interfaces for the same functionality required duplicate code and documentation
2. **User Confusion**: Users were unsure which interface to use, leading to fragmented adoption
3. **Dependency Complexity**: The CLI required Python dependencies and installation steps, contradicting our zero-dependency goal
4. **IDE Integration Focus**: The core value proposition is seamless integration within the Cursor IDE workflow

The project's mission is to provide effortless, AI-powered documentation generation directly within the development environment. The CLI, while functional, diverted focus from this core mission and added unnecessary complexity.

## Decision

We will completely remove the CLI interface and focus exclusively on Cursor IDE slash commands:

1. **Remove CLI Codebase**: Delete all Python CLI modules, setup files, and related infrastructure
2. **Pure Slash Commands**: Maintain only the `/init-docs`, `/adr`, `/gen-er-diagram`, `/update-docs`, etc. commands
3. **Zero Dependencies**: Achieve true zero-dependency operation through AI-powered analysis
4. **Template-Based**: Rely entirely on Cursor rules and templates for functionality
5. **Documentation Cleanup**: Remove all CLI references from documentation while preserving the engaging style

## Consequences

### Positive Outcomes

- **Simplified Architecture**: Single interface reduces complexity and maintenance burden
- **True Zero Dependencies**: No Python installation or package management required
- **Better User Experience**: Seamless workflow entirely within Cursor IDE
- **Focused Development**: All effort directed toward improving slash command functionality
- **Easier Onboarding**: Users only need to learn slash commands, not CLI syntax
- **Universal Compatibility**: Works with any project type without language-specific setup

### Negative Outcomes

- **CLI Users**: Existing CLI users must migrate to slash commands
- **Automation Limitations**: No programmatic access outside of Cursor IDE
- **CI/CD Integration**: Cannot be used in automated pipelines (by design choice)

### Mitigation Strategies

- **Migration Guide**: Provide clear mapping from CLI commands to slash commands
- **Enhanced Slash Commands**: Ensure slash commands provide all CLI functionality
- **Documentation**: Update all references to reflect slash-command-only approach

## Implementation

- Remove `cli/` directory and all Python modules
- Delete `pyproject.toml`, `requirements.txt`, and setup files
- Update README, CONTRIBUTING, and all documentation
- Preserve project's engaging documentation style
- Maintain all template and rule functionality

This decision aligns with our vision of providing the most seamless, zero-friction documentation experience possible within the Cursor IDE ecosystem.
