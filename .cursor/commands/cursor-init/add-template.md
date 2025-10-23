# Add Custom Template

Add a custom documentation template variant to the framework.

## What This Does

Helps you create custom template variants for documentation types:

1. **Identify Template Type**: Determines which documentation type (adr, architecture, etc.)
2. **Create Template File**: Guides you through creating a custom template
3. **Explain Placeholder System**: Shows available placeholders for the template type
4. **Save Template**: Stores custom template in appropriate directory
5. **Update Configuration**: Optionally updates `.cursor-init.yaml` to use the new template

## Usage

Add custom template:
```
/add-template adr
/add-template architecture
/add-template onboarding
```

## Supported Template Types

- `adr` - Architecture Decision Records
- `architecture` - System architecture documentation
- `onboarding` - Developer onboarding guides
- `rfc` - Request For Comments documents
- `data_model` - Database schema documentation

## Placeholder System

Templates use placeholders that get automatically replaced:

### Common Placeholders (All Templates)
- `{{PROJECT_NAME}}` - Project name (from directory or config)
- `{{DATE}}` - Current date (YYYY-MM-DD)
- `{{VERSION}}` - Project version (from package.json/pyproject.toml)
- `{{AUTHORS}}` - Project authors/maintainers

### ADR-Specific Placeholders
- `{{ADR_NUMBER}}` - ADR number (auto-incremented)
- `{{ADR_TITLE}}` - Decision title
- `{{CONTEXT}}` - Gathered context from codebase

### Architecture-Specific Placeholders
- `{{ARCHITECTURE_OVERVIEW}}` - High-level system description
- `{{SYSTEM_CONTEXT}}` - External system interactions
- `{{TECHNOLOGY_STACK}}` - Detected technologies
- `{{COMPONENT_NAME}}` - Component names
- `{{HIGH_LEVEL_DESIGN}}` - System design overview

### RFC-Specific Placeholders
- `{{RFC_NUMBER}}` - RFC number (auto-incremented)
- `{{RFC_TITLE}}` - Proposal title
- `{{AUTHOR}}` - RFC author (from git config)
- `{{STATUS}}` - RFC status (Draft, In Review, Accepted, etc.)

## Example: Custom ADR Template

File: `.cursor/cursor-init/templates/adr/adr_template_custom.md`

```markdown
# {{ADR_NUMBER}}: {{ADR_TITLE}}

**Date:** {{DATE}}
**Status:** Proposed
**Stakeholders:** Engineering Team

## Problem Statement

[Describe the problem we're trying to solve]

## Context

{{CONTEXT}}

## Proposed Solution

[Describe the proposed solution]

## Alternative Solutions

### Alternative 1
**Pros:**
- [Advantage]

**Cons:**
- [Disadvantage]

### Alternative 2
**Pros:**
- [Advantage]

**Cons:**
- [Disadvantage]

## Decision

[Final decision with rationale]

## Impact Assessment

**Technical Impact:**
- [Impact on codebase]

**Team Impact:**
- [Impact on development process]

**Timeline:**
- [Implementation timeline]

## Success Criteria

- [Criterion 1]
- [Criterion 2]

## Follow-up Actions

- [ ] Action item 1
- [ ] Action item 2
```

## Configuration

After creating a custom template, configure it in `.cursor-init.yaml`:

```yaml
templates:
  adr: "custom"  # Uses adr_template_custom.md

  # OR use custom path
  custom_template_paths:
    adr: "path/to/my-custom-adr-template.md"
```

## File Naming Convention

Template files must follow this naming pattern:

```
{type}_template_{variant}.md
```

Examples:
- `adr_template_custom.md`
- `architecture_template_mycompany.md`
- `rfc_template_engineering.md`

## Process

I will:
1. Ask which template type you want to customize
2. Show available placeholders for that template type
3. Provide a base template structure to start from
4. Guide you on creating the template file
5. Show where to save the template file
6. Explain how to configure `.cursor-init.yaml` to use it
7. Provide usage examples with the new template

## Example Workflow

```
You: /add-template adr

Me: I'll help you create a custom ADR template.

Available placeholders for ADR templates:
- {{ADR_NUMBER}} - Auto-incremented ADR number
- {{ADR_TITLE}} - Decision title
- {{DATE}} - Current date
- {{PROJECT_NAME}} - Project name
- {{CONTEXT}} - Gathered context from codebase

Create your template file at:
.cursor/cursor-init/templates/adr/adr_template_custom.md

Here's a starting point:
[Shows template structure]

After creating the file, configure it in .cursor-init.yaml:

templates:
  adr: "custom"

Then use it with:
/adr "Your Decision Title"
```

## Template Best Practices

### Structure
- Use clear section headers
- Include placeholder comments where customization is needed
- Provide examples in comments
- Use consistent markdown formatting

### Placeholders
- Always include date and project name
- Use specific placeholders over generic ones
- Add new custom placeholders as needed
- Document custom placeholders in comments

### Content
- Balance structure with flexibility
- Don't over-prescribe content
- Include helpful prompts and questions
- Reference relevant examples

## Custom Template Storage

You can store custom templates:

1. **In framework**: `.cursor/cursor-init/templates/{type}/{type}_template_custom.md`
2. **In project**: Anywhere, use `custom_template_paths` config
3. **Global**: `~/.cursor-init/templates/` (if you want to share across projects)

---

**Template Location**: `.cursor/cursor-init/templates/`
**Configuration File**: `.cursor-init.yaml` (required for custom templates)
