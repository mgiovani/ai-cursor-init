# Secure Code Parsing Strategy

## Overview

The `cursor-init` tool must analyze project code to generate documentation, diagrams, and insights while maintaining strict security boundaries. This document outlines our approach to secure code parsing that prevents execution of untrusted project code.

## Core Principles

### 1. Static Analysis First

**Primary Approach: Abstract Syntax Tree (AST) Parsing**

The tool prioritizes static analysis methods over dynamic code execution:

- **AST Parsing**: Use Python's `ast` module to parse source code into syntax trees
- **Pattern Matching**: Identify code structures through AST node analysis
- **Text-Based Analysis**: Use regex and string parsing for configuration files
- **Metadata Inspection**: Leverage framework-specific metadata when available

### 2. No Arbitrary Code Execution

**Prohibited Operations:**

- Direct `import` of user modules without strict controls
- `exec()` or `eval()` of user-provided code
- Dynamic loading of user-defined classes or functions
- Execution of user scripts or commands

**Rationale:**

- Prevents execution of malicious code
- Reduces supply chain attack surface
- Eliminates risk of side effects during analysis
- Ensures predictable, sandboxed operation

### 3. Limited Dynamic Imports (When Absolutely Necessary)

**Controlled Import Scenarios:**

For certain advanced features (e.g., SQLAlchemy model introspection), limited dynamic imports may be necessary:

**Strict Controls:**

- **Isolated Environment**: Use separate Python processes or virtual environments
- **Limited Scope**: Import only specific, well-known modules (e.g., SQLAlchemy metadata)
- **Timeout Protection**: Implement execution timeouts to prevent hanging
- **Error Isolation**: Catch and handle all exceptions gracefully
- **User Consent**: Require explicit user acknowledgment for dynamic imports

**Implementation Pattern:**

```python
# Preferred: AST-based analysis
def analyze_models_ast(file_path: str) -> List[ModelInfo]:
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
    # Analyze AST nodes for class definitions, relationships, etc.
    
# Fallback: Controlled dynamic import (with warnings)
def analyze_models_dynamic(file_path: str) -> List[ModelInfo]:
    # Only if AST analysis is insufficient
    # Implement strict sandboxing and user warnings
```

## Implementation Guidelines

### SQLAlchemy Model Analysis

**Primary Method: AST Parsing**

- Parse Python files to identify `class` definitions inheriting from SQLAlchemy base classes
- Extract column definitions, relationships, and constraints from AST nodes
- Build ER diagrams from statically analyzed metadata

**Fallback Method: Metadata Inspection**

- If AST parsing is insufficient, use SQLAlchemy's reflection capabilities
- Implement in isolated subprocess with timeout protection
- Require explicit user consent with security warnings

### Framework Detection

**Safe Detection Methods:**

- File system analysis (presence of `requirements.txt`, `package.json`, etc.)
- Configuration file parsing (JSON, YAML, TOML)
- Import statement analysis via AST parsing
- Directory structure pattern matching

**Examples:**

```python
# Safe: File-based detection
def detect_fastapi() -> bool:
    return any([
        'fastapi' in read_requirements(),
        'FastAPI' in ast_scan_imports(),
        os.path.exists('app.py') and 'fastapi' in read_file('app.py')
    ])

# Unsafe: Dynamic import
def detect_fastapi_unsafe() -> bool:
    try:
        import app  # DON'T DO THIS
        return hasattr(app, 'FastAPI')
    except ImportError:
        return False
```

### Route and API Analysis

**Static Analysis Approach:**

- Parse source files for route decorator patterns
- Extract endpoint definitions from AST nodes
- Identify URL patterns and HTTP methods through text analysis
- Build API documentation from statically analyzed code

## Security Boundaries

### File System Access

**Allowed:**

- Read access to project files within the working directory
- Parse configuration files (JSON, YAML, TOML, INI)
- Analyze source code as text

**Prohibited:**

- Write access outside designated documentation directories
- Execution of shell commands with user input
- Access to files outside the project directory

### Network Access

**Prohibited:**

- All outbound network connections during code analysis
- Downloading or executing remote code
- Sending project data to external services

### Process Isolation

**Requirements:**

- Run analysis in separate processes when dynamic imports are necessary
- Implement resource limits (memory, CPU, time)
- Use subprocess sandboxing where available
- Graceful degradation on analysis failures

## User Communication

### Security Warnings

When dynamic imports are necessary, display clear warnings:

```
⚠️  SECURITY NOTICE
The cursor-init tool needs to import your project's code to fully analyze SQLAlchemy models.
This involves loading Python modules from your project.

• Only proceed if you trust the codebase
• Avoid running on untrusted or third-party code
• The tool will run in an isolated environment with timeouts

Continue? [y/N]
```

### Documentation Requirements

All user-facing documentation must include:

- Clear explanation of the tool's parsing approach
- Security considerations and limitations
- Guidance on when to avoid using dynamic features
- Instructions for reporting security concerns

## Error Handling

### Graceful Degradation

When secure parsing fails:

- Fall back to simpler analysis methods
- Generate partial documentation with clear limitations
- Provide helpful error messages explaining what couldn't be analyzed
- Never fail silently or expose internal errors

### Security Incident Response

If security issues are discovered:

- Immediately disable affected features
- Document the issue and mitigation steps
- Update security guidelines and user warnings
- Implement additional safeguards

## Testing and Validation

### Security Testing Requirements

- Test with malicious code samples to ensure no execution
- Verify sandboxing and isolation mechanisms
- Validate timeout and resource limit enforcement
- Test error handling with corrupted or malicious files

### Code Review Guidelines

All code analysis features must undergo security-focused code review:

- Verify no dynamic execution of user code
- Confirm proper error handling and isolation
- Validate user warnings and consent mechanisms
- Test with adversarial inputs

## Future Considerations

### Enhanced Sandboxing

Future improvements may include:

- Container-based isolation for dynamic analysis
- WebAssembly-based code execution sandboxes
- Integration with security scanning tools
- Formal verification of parsing logic

### Community Security

- Establish security reporting channels
- Regular security audits of parsing logic
- Community review of security-sensitive changes
- Documentation of security best practices for contributors

## Compliance and Standards

This strategy aligns with:

- OWASP secure coding practices
- Python security best practices
- Open source security guidelines
- Industry standards for static analysis tools

The secure parsing strategy ensures that `cursor-init` can provide powerful code analysis capabilities while maintaining the highest security standards for users working with sensitive or untrusted codebases.
