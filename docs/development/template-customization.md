# Template Customization Guide

The cursor-init framework provides multiple template variants for onboarding documentation, allowing you to customize the documentation style to match your project's needs.

## Configuration

Create a `.cursor-init.yaml` file in your project root to configure template variants:

```yaml
templates:
  # Onboarding Templates
  onboarding: "developer"       # Options: developer, contributor, user
```

## Onboarding Templates

### `developer` (Default)

- **Description**: Comprehensive guide for new developers
- **Best For**: Technical onboarding for software engineers
- **Length**: ~200 lines
- **Sections**: Setup, Development Workflow, Project Structure, Testing, Troubleshooting, Resources

### `contributor`

- **Description**: Guide for open source contributors
- **Best For**: Open source projects welcoming external contributions
- **Length**: ~240 lines
- **Sections**: Contribution Types, Workflow, PR Guidelines, Community Guidelines, Recognition, Support

### `user`

- **Description**: End-user focused documentation
- **Best For**: Product documentation for end users
- **Length**: ~180 lines
- **Sections**: Installation, Getting Started, Features, Configuration, Troubleshooting, Support

## Template Structure

All templates use a consistent placeholder system:

### Common Placeholders

- `{{PROJECT_NAME}}` - Project name
- `{{DATE}}` - Current date
- `{{AUTHOR}}` - Document author

### Onboarding-Specific Placeholders

- `{{INSTALL_COMMANDS}}` - Installation commands
- `{{TEST_COMMANDS}}` - Testing commands
- `{{COMMUNICATION_CHANNEL}}` - Team communication channel

## Command Integration

The `/init-docs` command respects onboarding template configuration and will use the configured variant when creating initial documentation.

### Automatic Template Selection

If no `.cursor-init.yaml` exists, commands use the default template: `developer`

## Best Practices

### Template Selection

- **Start Simple**: Begin with default templates and upgrade as needed
- **Match Audience**: Choose template based on your primary audience
- **Team Consistency**: Use same templates across team projects

### Customization

- **Placeholder Values**: Populate placeholders with meaningful content
- **Section Relevance**: Remove irrelevant sections for your project
- **Team Input**: Get team feedback on template choices

## Contributing

### Adding New Templates

1. Create template file with appropriate placeholders
2. Add to onboarding template directory
3. Update configuration options
4. Document template purpose and usage
5. Test with different project scenarios

The cursor-init template system is designed to be flexible and extensible. Choose the templates that best fit your project's documentation needs and customize them as required.
