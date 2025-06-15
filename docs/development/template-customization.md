### Template Customization Guide

This guide explains how to customize documentation templates used by cursor-init slash commands.

## Overview

cursor-init supports multiple template variants for different documentation types, allowing you to choose the style that best fits your team's needs. Templates can be configured globally via `.cursor-init.yaml` or selected per command.

## Available Template Types

### Architecture Decision Records (ADRs)

The `/adr` command supports four template variants:

#### 1. Nygard Style (Default)

**Template:** `adr_template_nygard.md`
**Best for:** Classic Michael Nygard style ADRs
**Sections:** Context, Decision, Consequences

```yaml
templates:
  adr: "nygard_style"
```

#### 2. Full Template

**Template:** `adr_template_full.md`
**Best for:** Complex architectural decisions requiring thorough analysis
**Sections:** Problem Statement, Context, Assumptions, Options Analysis, Implementation Plan, Success Metrics, Risk Assessment

```yaml
templates:
  adr: "full"
```

#### 3. Lightweight Template

**Template:** `adr_template_lightweight.md`
**Best for:** Simple decisions that don't require extensive documentation
**Sections:** Problem, Decision, Alternatives, Consequences

```yaml
templates:
  adr: "lightweight"
```

#### 4. MADR Template

**Template:** `adr_template_madr.md`
**Best for:** Teams following MADR (Markdown ADR) conventions
**Sections:** Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Pros/Cons Analysis

```yaml
templates:
  adr: "madr"
```

### Architecture Documentation

The `/init-docs` and `/update-docs` commands support three architecture template variants:

#### 1. Google Style (Default)

**Template:** `architecture_google.md`
**Best for:** Teams following Google's documentation standards
**Sections:** Overview, System Context, Goals/Non-Goals, Design Details, Technology Stack, Security, Performance, Operations

```yaml
templates:
  architecture: "google_style"
```

#### 2. Enterprise Template

**Template:** `architecture_enterprise.md`
**Best for:** Large organizations requiring comprehensive business and technical documentation
**Sections:** Executive Summary, Business Architecture, Application Architecture, Data Architecture, Technology Architecture, Governance, Risk Management

```yaml
templates:
  architecture: "enterprise"
```

#### 3. Arc42 Template

**Template:** `architecture_arc.md`
**Best for:** Teams following the Arc42 documentation standard
**Sections:** 12 standardized Arc42 sections including Introduction/Goals, Constraints, Context, Solution Strategy, Building Blocks, Runtime View, Deployment, Cross-cutting Concepts

```yaml
templates:
  architecture: "arc42"
```

## Configuration

### Global Configuration

Create a `.cursor-init.yaml` file in your project root to set default templates:

```yaml
# Template preferences - choose your preferred style for each document type
templates:
  # ADR (Architecture Decision Record) templates
  adr: "nygard_style" # Options: nygard_style, full, lightweight, madr

  # Architecture documentation templates
  architecture: "google_style" # Options: google_style, enterprise, arc42

  # Onboarding guide templates
  onboarding: "general" # Options: general, python, frontend

# Custom template paths - add your own templates
custom_template_paths:
  # Example: Add a custom security ADR template
  - name: "security_adr"
    path: ".cursor/templates/custom/security-adr.md"
    
  # Example: Add a custom microservices architecture template
  - name: "microservices_arch"
    path: ".cursor/templates/custom/microservices-architecture.md"
```

### Per-Command Selection

Some commands allow you to specify the template variant directly:

```bash
# CLI examples (when available)
cursor-init adr --template=full "Choose database technology"
cursor-init adr --template=lightweight "Update logging format"
```

## Template Structure

### Placeholder System

All templates use a consistent placeholder system:

- `{{ADR_NUMBER}}` - Auto-numbered sequentially (0001, 0002, etc.)
- `{{ADR_TITLE}}` - Sanitized from user input
- `{{CONTEXT}}` - Pre-filled from codebase search
- `{{DATE}}` - Current date in ISO format
- `{{AUTHORS}}` - Project contributors (when available)
- `{{STAKEHOLDERS}}` - Key decision stakeholders

### Template Locations

Default templates are stored in:

```
.cursor/templates/
├── adr/
│   ├── adr_template_nygard.md
│   ├── adr_template_full.md
│   ├── adr_template_lightweight.md
│   └── adr_template_madr.md
├── architecture/
│   ├── architecture_google.md
│   ├── architecture_enterprise.md
│   └── architecture_arc.md
└── onboarding/
    └── ...
```

## Creating Custom Templates

### 1. Create Template File

Create your custom template in `.cursor/templates/custom/`:

```markdown
### {{ADR_NUMBER}}-{{ADR_TITLE}}

**Status:** Proposed
**Security Level:** {{SECURITY_LEVEL}}
**Compliance:** {{COMPLIANCE_REQUIREMENTS}}

## Security Context

{{SECURITY_CONTEXT}}
[Describe security implications and requirements]

## Threat Analysis

{{THREAT_ANALYSIS}}
[Identify potential security threats]

## Decision

{{DECISION}}
[Security-focused decision with risk mitigation]

## Security Consequences

{{SECURITY_CONSEQUENCES}}
[Security implications of this decision]
```

### 2. Register Custom Template

Add to your `.cursor-init.yaml`:

```yaml
custom_template_paths:
  - name: "security_adr"
    path: ".cursor/templates/custom/security-adr.md"
```

### 3. Use Custom Template

Reference in configuration:

```yaml
templates:
  adr: "security_adr"  # Use your custom template
```

## Template Development Guidelines

### 1. Placeholder Conventions

- Use `{{UPPERCASE_WITH_UNDERSCORES}}` for placeholders
- Provide descriptive inline guidance: `[Describe what goes here]`
- Include examples where helpful

### 2. Section Structure

- Use consistent markdown heading levels
- Bold important metadata: `**Status:** Proposed`
- Group related information logically

### 3. Content Guidance

- Provide clear instructions for each section
- Include examples of good content
- Explain the purpose of each section

### 4. Template Validation

Test your templates by:

1. Creating a test ADR: `/adr "Test Decision"`
2. Checking placeholder replacement works correctly
3. Verifying the generated markdown is well-formatted
4. Ensuring all sections have appropriate guidance

## Advanced Customization

### Framework-Specific Templates

Templates can be customized based on detected frameworks:

```yaml
templates:
  adr: "nygard_style"

# Override for specific frameworks
framework_overrides:
  python_framework: "fastapi"
  
# Framework-specific template variants
framework_templates:
  fastapi:
    adr: "api_focused_adr"
```

### Conditional Sections

Templates can include conditional content:

```markdown
## API Impact
{{#IF_API_CHANGE}}
{{API_IMPACT}}
[Describe impact on API contracts and versioning]
{{/IF_API_CHANGE}}
```

### Template Inheritance

Extend existing templates:

```yaml
custom_template_paths:
  - name: "enhanced_nygard"
    path: ".cursor/templates/custom/enhanced-nygard.md"
    extends: "nygard_style"  # Inherit from base template
```

## Troubleshooting

### Common Issues

1. **Template not found**: Check file path and spelling in `.cursor-init.yaml`
2. **Placeholders not replaced**: Ensure proper `{{PLACEHOLDER}}` format
3. **Configuration ignored**: Verify `.cursor-init.yaml` is valid YAML

### Debug Template Selection

Use the `/list-templates` command to see available templates and current configuration:

```
/list-templates
```

This will show:

- Available default templates
- Configured custom templates  
- Current template preferences
- Template file locations

## Contributing Templates

To contribute new templates to the project:

1. **Create Template**: Follow the guidelines above
2. **Add Documentation**: Update this guide with your template details
3. **Update Configuration**: Add to default options
4. **Test Thoroughly**: Ensure placeholders work correctly
5. **Submit PR**: Include template file, documentation updates, and tests

### Template Contribution Checklist

- [ ] Template follows placeholder conventions
- [ ] Includes clear section guidance
- [ ] Tested with `/adr` command
- [ ] Documentation updated
- [ ] Configuration files updated
- [ ] Added to available options lists

## Resources

- **Template Examples**: [.cursor/templates/](../.cursor/templates/)
- **Configuration Reference**: [.cursor-init.example.yaml](../.cursor-init.example.yaml)
- **ADR Best Practices**: [adr/0001-record-architecture-decisions.md](../adr/0001-record-architecture-decisions.md)
- **Contributing Guide**: [CONTRIBUTING.md](../../CONTRIBUTING.md)
