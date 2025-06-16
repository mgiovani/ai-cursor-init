# Documentation Linting Strategy

This document outlines the approach for validating documentation quality and ensuring content freshness in the AI-Cursor-Init framework.

## Overview

Documentation linting helps maintain high-quality, up-to-date documentation by automatically detecting:

1. **Placeholder content** that needs completion
2. **Outdated information** that needs updating
3. **Missing sections** in documentation templates
4. **Format inconsistencies** across documents

## Placeholder Detection Patterns

### Primary Markers

The system searches for these common placeholder indicators:

1. **`TBD`** - To Be Determined
2. **`TODO`** - To Do items
3. **`FIXME`** - Items that need fixing
4. **`XXX`** - Generic attention markers
5. **`[TODO]`** and **`[TBD]`** - Bracketed variants
6. **`{{...}}`** - Template placeholders that weren't replaced
7. **`To be determined`** and **`To be decided`** - Full phrases
8. **`Coming soon`** and **`Under construction`** - Work-in-progress indicators

### Secondary Indicators

Additional patterns that suggest incomplete content:

- **Short sections** with minimal content
- **Empty code blocks** without implementation
- **Missing dates** in documentation headers
- **Default template values** that weren't customized

## Quality Validation

### Content Completeness

The linter checks for:

- **Minimum content length** per section
- **Required sections** based on document type
- **Proper markdown structure** with appropriate headers
- **Valid Mermaid diagrams** with correct syntax

### Template Conformance

Validates that documents follow template structure:

- **Expected sections** are present
- **Placeholder replacement** is complete
- **Consistent formatting** across similar documents
- **Proper metadata** in document headers

## Freshness Checks

### Automated Detection

The system identifies documents that may need updates:

- **Modified dates** compared to recent code changes
- **Technology references** that may be outdated
- **Dependency versions** mentioned in documentation
- **API changes** that affect documented interfaces

### Manual Review Triggers

Flags documents for manual review when:

- **Major framework changes** are detected
- **New dependencies** are added to the project
- **Significant architecture changes** occur
- **Long periods** since last documentation update

## Implementation Strategy

### Template-Based Validation

Each template type has specific validation rules:

**Architecture Documents:**

- Must include system overview
- Should have component diagrams
- Technology stack must be current

**ADR Documents:**

- Must have decision, context, and consequences
- Should include alternatives considered
- Status must be valid (Proposed, Accepted, Deprecated)

**Onboarding Documents:**

- Setup instructions must be testable
- Prerequisites must be current
- Examples must work with current codebase

### Cursor IDE Integration

Validation runs through slash commands:

- **`/check-docs`** - Comprehensive documentation validation
- **`/check-docs --file filename.md`** - Single file validation
- **`/check-docs --category adr`** - Category-specific validation

## Reporting

### Validation Output

The linter provides detailed reports:

```
📋 Documentation Validation Report

✅ PASSED (3 files)
- docs/architecture.md
- docs/onboarding.md  
- docs/adr/0001-record-architecture-decisions.md

⚠️  WARNINGS (1 file)
- docs/data-model.md: Contains placeholder text "TBD"

❌ FAILED (1 file)
- docs/adr/0002-database-choice.md: Missing consequences section
```

### Integration with Development Workflow

Validation can be integrated into:

- **Pre-commit hooks** for quality gates
- **Code review process** for documentation changes
- **Regular maintenance** schedules for freshness checks
- **Template development** for ensuring quality

## Best Practices

### For Template Authors

- **Include validation hints** in template comments
- **Provide clear placeholder instructions**
- **Test templates** with validation tools
- **Document template-specific requirements**

### For Documentation Writers

- **Run validation** before submitting documentation
- **Replace all placeholders** with actual content
- **Follow template structure** for consistency
- **Update dates** when making changes

### For Project Maintainers

- **Set up regular validation** schedules
- **Monitor validation reports** for trends
- **Update validation rules** as templates evolve
- **Train team members** on validation tools

## Future Enhancements

### Advanced Validation

Planned improvements include:

- **Semantic analysis** of content relevance
- **Cross-reference validation** between documents
- **Link checking** for internal and external references
- **Style guide enforcement** for writing consistency

### Automation

Additional automation opportunities:

- **Automatic placeholder detection** in new templates
- **Smart suggestions** for content updates
- **Integration with version control** for change tracking
- **Custom validation rules** per project type

This linting strategy ensures that generated documentation maintains high quality and stays current with the evolving codebase.
