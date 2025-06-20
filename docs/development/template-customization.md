# Template Customization Guide

This guide helps you customize documentation templates for the AI-Cursor-Init framework to match your team's specific needs and standards.

## Template Structure

### Basic Template Anatomy

Every template follows this structure:

```markdown
<!-- Template metadata -->
---
template_variant: "comprehensive"
last_updated: "2024-01-15"
framework_support: ["universal"]
---

# {{DOCUMENT_TITLE}}

**Last Updated:** {{DATE}}
**Generated by:** AI-Cursor-Init Framework

## Overview

{{OVERVIEW_CONTENT}}

<!-- Template sections with placeholders -->
## {{SECTION_NAME}}

{{SECTION_CONTENT}}
```

### Placeholder System

Templates use double curly braces for dynamic content:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{PROJECT_NAME}}` | Project name from package.json/pyproject.toml | `my-awesome-app` |
| `{{DATE}}` | Current date in YYYY-MM-DD format | `2024-01-15` |
| `{{FRAMEWORK}}` | Detected framework | `Web API`, `Frontend`, `Backend` |
| `{{AUTHOR}}` | Git configuration name | `John Doe` |
| `{{TECH_STACK}}` | Comma-separated technologies | `Backend API, Database, Frontend` |

### Custom Placeholders

You can create custom placeholders for your templates:

```markdown
## Database Configuration

**Database Type:** {{DB_TYPE}}
**Connection String:** {{DB_CONNECTION}}
**Migration Tool:** {{MIGRATION_TOOL}}
```

## Template Categories

### 1. Architecture Templates

Location: `templates/architecture/`

Available variants:

- `google_style.md` - Google's technical writing style
- `enterprise.md` - Enterprise architecture documentation
- `arc42.md` - Arc42 architecture template
- `minimal.md` - Lightweight architecture overview

### 2. ADR Templates

Location: `templates/adr/`

Available variants:

- `nygard_style.md` - Michael Nygard's classic ADR format
- `madr.md` - Markdown Architecture Decision Records
- `comprehensive.md` - Detailed decision documentation
- `lightweight.md` - Minimal decision recording

### 3. Onboarding Templates

Location: `templates/onboarding/`

Available variants:

- `developer.md` - Technical developer onboarding
- `contributor.md` - Open source contributor guide
- `user.md` - End-user documentation

### 4. Data Model Templates

Location: `templates/data-model/`

Available variants:

- `simple.md` - Basic ER diagram documentation
- `comprehensive.md` - Detailed database documentation

## Creating Custom Templates

### Step 1: Choose Template Category

Decide which category your template belongs to:

```bash
templates/
├── architecture/
├── adr/
├── onboarding/
├── data-model/
└── custom/          # Your custom templates
```

### Step 2: Create Template File

Create a new `.md` file with descriptive name:

```bash
# Example: Custom security template
templates/custom/security-comprehensive.md
```

### Step 3: Add Template Metadata

Include metadata at the top:

```markdown
---
template_variant: "comprehensive"
category: "security"
framework_support: ["universal"]
description: "Comprehensive security documentation template"
author: "Your Team"
version: "1.0.0"
---
```

### Step 4: Write Template Content

Use placeholders and structured sections:

```markdown
# {{PROJECT_NAME}} Security Documentation

**Last Updated:** {{DATE}}
**Security Contact:** {{SECURITY_CONTACT}}

## Security Overview

This document outlines the security measures implemented in {{PROJECT_NAME}}.

### Technology Stack Security

- **Framework:** {{FRAMEWORK}}
- **Database:** {{DATABASE_TYPE}}
- **Authentication:** {{AUTH_METHOD}}
- **Deployment:** {{DEPLOYMENT_PLATFORM}}

## Threat Model

### Assets
- {{ASSET_LIST}}

### Threats
- {{THREAT_LIST}}

### Mitigations
- {{MITIGATION_LIST}}
```

## Template Configuration

### Global Configuration

Configure template preferences in `.cursor-init.yaml`:

```yaml
templates:
  architecture: "google_style"
  adr: "nygard_style"
  onboarding: "developer"
  data_model: "comprehensive"
  
custom_template_paths:
  security: "templates/custom/security-comprehensive.md"
  api_docs: "templates/custom/api-documentation.md"

framework_detection:
  # AI-powered detection replaces manual framework configuration
# Detection is automatic based on project analysis
```

### Per-Project Configuration

Override global settings per project:

```yaml
# project-specific .cursor-init.yaml
project:
  name: "my-awesome-project"
  type: "web-api"
  
templates:
  architecture: "enterprise"  # Override global setting
  custom_security: true       # Enable custom template
  
placeholders:
  SECURITY_CONTACT: "security@company.com"
  DB_TYPE: "PostgreSQL"
  AUTH_METHOD: "JWT + OAuth2"
```

## Advanced Customization

### Conditional Content

Use conditional blocks for framework-specific content:

```markdown
## Setup Instructions

{% if FRAMEWORK == "Web API" %}
```bash
# Install detected API framework dependencies
# Start development server
```

{% elif FRAMEWORK == "Frontend" %}

```bash
# Install detected frontend dependencies
# Start development server
```

{% endif %}

```

### Template Inheritance

Create base templates that others can extend:

```markdown
<!-- base-architecture.md -->
# {{PROJECT_NAME}} Architecture

## Base Sections
<!-- Common content for all architecture docs -->

<!-- Include point for specialized content -->
{{SPECIALIZED_CONTENT}}
```

### Multi-Language Support

Create language-specific variants:

```
templates/
├── architecture/
│   ├── google_style.md
│   ├── google_style.es.md  # Spanish version
│   └── google_style.pt.md  # Portuguese version
```

## Template Testing

### Validation

Test your templates with different project types:

```bash
# Test template with different project types
/test-template architecture custom-web-api

# Test template with frontend project  
/test-template architecture custom-frontend
```

### Quality Checks

Ensure templates meet quality standards:

- ✅ All placeholders have fallback values
- ✅ Sections are logically organized
- ✅ Examples are framework-appropriate
- ✅ Mermaid diagrams have valid syntax
- ✅ Markdown formatting is consistent

## Template Sharing

### Internal Sharing

Share templates within your organization:

```yaml
# team-templates.yaml
shared_templates:
  company_architecture: "https://internal.git/templates/arch.md"
  security_standard: "https://internal.git/templates/security.md"
```

### Community Sharing

Contribute templates to the community:

1. Fork the repository
2. Add your template to appropriate category
3. Update template registry
4. Submit pull request

### Template Registry

Register your templates for easy discovery:

```yaml
# templates/registry.yaml
architecture:
  - name: "Google Style"
    file: "google_style.md"
    description: "Google's technical writing approach"
    frameworks: ["universal"]
  - name: "Your Custom Style"
    file: "custom_style.md"
    description: "Your team's architecture template"
    frameworks: ["universal"]
```

## Best Practices

### Template Design

- **Keep it focused** - One template per document type
- **Use clear placeholders** - Self-documenting placeholder names
- **Provide examples** - Show expected content format
- **Include instructions** - Guide users with comments
- **Test thoroughly** - Validate with real projects

### Content Guidelines

- **Write for your audience** - Match your team's expertise level
- **Be consistent** - Use same terminology across templates
- **Stay current** - Update templates with technology changes
- **Include metadata** - Track versions and dependencies

### Maintenance

- **Version your templates** - Track changes over time
- **Review regularly** - Ensure templates stay relevant
- **Gather feedback** - Improve based on user experience
- **Document changes** - Keep changelog for template updates

## Troubleshooting

### Common Issues

**Placeholder not replaced:**

- Check placeholder spelling and case sensitivity
- Ensure placeholder is defined in configuration
- Verify framework detection is working

**Template not found:**

- Check file path in configuration
- Verify template file exists
- Ensure proper YAML syntax in config

**Formatting issues:**

- Validate Markdown syntax
- Check Mermaid diagram syntax
- Ensure consistent spacing and structure

### Getting Help

- Check template examples in `templates/` directory
- Review existing templates for patterns
- Test with minimal project setup
- Ask for help in project discussions

This guide should help you create effective, maintainable templates that serve your team's documentation needs.
