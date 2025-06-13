# Documentation Linter Strategy

## Purpose

The Documentation Linter ensures documentation quality and completeness by identifying placeholders, stale content, and other issues that may impact the usefulness and accuracy of project documentation.

## Linting Rules

### Placeholder Detection

The linter identifies the following placeholder patterns (case-insensitive):

1. **`TBD`** - To Be Determined
2. **`TODO`** - To Do items
3. **`FIXME`** - Items that need fixing
4. **`XXX`** - Generic attention markers
5. **`[TODO]`** and **`[TBD]`** - Bracketed variants
6. **`{{}}`** - Template placeholders
7. **`To be determined`** and **`To be decided`** - Full phrases
8. **`Coming soon`** and **`Under construction`** - Work-in-progress indicators

### Content Quality Checks

1. **Empty Files**: Files with no content or only whitespace
2. **Minimal Content**: Files with less than 50 characters (may be incomplete)
3. **Header-Only Files**: Files with only headers and no substantial content (less than 3 non-header lines)

### Future Enhancement: Stale Content Detection

For future implementation, the linter may include:

- **Date-based staleness**: Check front-matter dates against current date
- **Last-modified tracking**: Compare file modification times with code changes
- **Version-specific references**: Detect outdated version numbers or deprecated references

## Target Scope

### Included Files

- All `.md` files in the `docs/` directory and its subdirectories
- Recursive scanning to catch documentation in nested folders

### Core Documentation Files

The linter specifically checks for the presence of:

- `docs/architecture.md` - System architecture overview
- `docs/onboarding.md` - Project onboarding guide  
- `docs/adr/0001-record-architecture-decisions.md` - Initial ADR

## Implementation Approach

### CLI Integration

- Command: `cursor-init check-docs`
- Exit codes: `0` for success (no issues), `1` for issues found
- Optional flags: `--file` for single file check, `--category` for category-specific checks

### Output Format

- Clear, actionable error messages with file paths and line numbers
- Summary of total issues found
- CI-friendly output for automated pipelines

### Performance Considerations

- File scanning optimized for repositories up to 50,000 lines of code
- Execution target: under 5 seconds for typical codebases under 100 files
- Memory-efficient processing of large documentation sets

## Integration Points

### Cursor IDE Integration

- Slash command: `/check-docs`
- Real-time feedback during documentation editing
- Integration with existing documentation workflow

### CI/CD Integration

- Non-zero exit codes for pipeline failures
- Structured output for issue reporting
- Compatible with GitHub Actions and other CI systems
