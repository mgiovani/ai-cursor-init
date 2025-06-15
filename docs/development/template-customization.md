# Template Customization Guide

The cursor-init framework provides multiple template variants for RFC (Request For Comments) documentation, allowing you to customize the documentation style to match your project's needs.

## Configuration

Create a `.cursor-init.yaml` file in your project root to configure template variants:

```yaml
templates:
  # RFC Templates
  rfc: "standard"              # Options: minimal, standard, detailed
```

## RFC Templates

### `minimal`

- **Description**: Simple RFC for quick proposals
- **Best For**: Informal proposals or brainstorming
- **Length**: ~12 lines
- **Sections**: Problem, Proposed Solution, Discussion

### `standard` (Default)

- **Description**: Standard RFC with structured analysis
- **Best For**: Most RFC scenarios requiring structured evaluation
- **Length**: ~80 lines
- **Sections**: Summary, Problem Statement, Proposed Solution, Implementation Details, Alternatives, Risks, Success Metrics

### `detailed`

- **Description**: Comprehensive RFC with full lifecycle management
- **Best For**: Complex proposals requiring formal approval process
- **Length**: ~300 lines
- **Sections**: Abstract, Motivation, Background, Detailed Design, Implementation Plan, Alternatives, Risk Assessment, Resource Requirements, Testing Strategy, Rollout Plan, Approval Process

## Template Structure

All templates use a consistent placeholder system:

### Common Placeholders

- `{{RFC_TITLE}}` - RFC title
- `{{DATE}}` - Current date
- `{{AUTHOR}}` - Document author

### RFC-Specific Placeholders

- `{{RFC_NUMBER}}` - RFC number (detailed template)
- `{{STATUS}}` - RFC status
- `{{PROBLEM_STATEMENT}}` - Problem description
- `{{PROPOSED_SOLUTION}}` - Solution details

## Command Integration

The `/rfc "Title"` command respects RFC template configuration and will use the configured variant when creating new RFCs.

### Automatic Template Selection

If no `.cursor-init.yaml` exists, commands use the default template: `standard`

## Best Practices

### Template Selection

- **Start Simple**: Begin with minimal for quick ideas, upgrade to standard/detailed as needed
- **Match Complexity**: Choose template complexity based on proposal scope
- **Team Consistency**: Use same templates across team proposals

### Customization

- **Placeholder Values**: Populate placeholders with meaningful content
- **Section Relevance**: Remove irrelevant sections for your proposal
- **Team Input**: Get team feedback on template choices

## Contributing

### Adding New Templates

1. Create template file with appropriate placeholders
2. Add to RFC template directory
3. Update configuration options
4. Document template purpose and usage
5. Test with different proposal scenarios

The cursor-init template system is designed to be flexible and extensible. Choose the templates that best fit your project's documentation needs and customize them as required.
