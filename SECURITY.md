# Security Policy

## Supported Versions

We actively support the following versions of cursor-init:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Security Philosophy

cursor-init is designed with security as a core principle:

### Static Analysis First

- **Default Behavior**: All code analysis is performed statically using AST parsing
- **No Code Execution**: By default, no user code is executed during analysis
- **Safe for Untrusted Code**: Can safely analyze codebases from unknown sources

### Sandboxed Operations

For advanced features that require dynamic analysis:

- **Explicit Consent**: User must explicitly opt-in to dynamic analysis
- **Isolated Environment**: Operations run in sandboxed environments
- **Resource Limits**: Strict timeouts and memory constraints
- **Graceful Fallback**: Falls back to static analysis if dynamic analysis fails

### Data Privacy

- **No External Calls**: No data is sent to external services
- **Local Processing**: All analysis happens locally on your machine
- **No Telemetry**: No usage data or analytics are collected
- **Offline Capable**: Works completely offline

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue, please follow these steps:

### For Non-Critical Issues

- Open a [GitHub Issue](https://github.com/mgiovani/ai-cursor-init/issues) with the "security" label
- Provide a clear description of the vulnerability
- Include steps to reproduce if applicable

### For Critical Security Issues

- **DO NOT** open a public issue
- Email the maintainers directly (check the latest commit for contact info)
- Include "SECURITY" in the subject line
- Provide detailed information about the vulnerability

### What to Include

- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Suggested fix (if you have one)
- Your contact information for follow-up

## Response Timeline

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 1 week
- **Fix Development**: Depends on severity (1-4 weeks)
- **Public Disclosure**: After fix is released and users have time to update

## Security Best Practices for Users

### When Using cursor-init

1. **Review Generated Content**: Always review generated documentation before committing
2. **Use Static Mode**: Stick to static analysis features when working with untrusted code
3. **Keep Updated**: Use the latest version for security fixes
4. **Validate Templates**: Review custom templates before using them

### In CI/CD Environments

1. **Pin Versions**: Use specific version numbers, not "latest"
2. **Isolated Runners**: Run in isolated CI environments
3. **Review Changes**: Always review documentation changes in PRs
4. **Access Controls**: Limit who can modify documentation generation workflows

## Security Features

### Built-in Protections

- **Input Validation**: All user inputs are validated and sanitized
- **Path Traversal Protection**: File operations are restricted to project directories
- **Resource Limits**: Memory and CPU usage limits prevent resource exhaustion
- **Timeout Protection**: Operations have strict time limits

### Audit Trail

- All file modifications are logged
- Template usage is tracked
- Configuration changes are recorded

## Threat Model

### In Scope

- Malicious templates that could execute code
- Path traversal attacks
- Resource exhaustion attacks
- Information disclosure through generated documentation

### Out of Scope

- Physical access to the machine
- Social engineering attacks
- Vulnerabilities in dependencies (reported to respective maintainers)
- Issues with the Cursor IDE itself

## Security Updates

Security updates will be:

- Released as patch versions (e.g., 0.1.1 → 0.1.2)
- Announced in the CHANGELOG.md
- Tagged with "security" labels in GitHub releases
- Communicated through GitHub security advisories for critical issues

## Contact

For security-related questions or concerns:

- Check existing [GitHub Issues](https://github.com/mgiovani/ai-cursor-init/issues?q=label%3Asecurity)
- Review our [Contributing Guidelines](CONTRIBUTING.md)
- Follow responsible disclosure practices outlined above
