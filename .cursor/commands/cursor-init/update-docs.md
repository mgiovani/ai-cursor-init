# Update Documentation

Analyze the current codebase and determine which documentation is relevant, then suggest updates unless explicitly disabled in configuration.

## What This Does

1. **Read Configuration**: Checks `.cursor-init.yaml` to understand which documentation types are explicitly disabled
2. **Analyze Project Relevance**: Examines the codebase to determine which documentation types are relevant based on detected technologies, frameworks, and project structure
3. **Check Documentation Freshness**: Examines relevant documentation files (unless disabled) and compares them with the current codebase state
4. **Load Current Templates**: For each relevant documentation type (not disabled), reads the current template configuration and identifies template variants
5. **Provide Specific Recommendations**: Suggests specific updates for outdated or missing documentation

## Analysis Process

### Data Model Analysis (if models detected, unless disabled)
- Checks if `docs/data-model.md` exists
- Verifies if database/ORM models have been modified
- Suggests `/gen-er-diagram` if ER diagram needs updating
- Skipped if `documentation.data.data_model: false`

### Architecture Documentation (unless disabled)
- Verifies that `docs/architecture.md` reflects current project structure
- Checks for new components, services, or major structural changes
- Suggests updates if architecture has evolved
- Skipped if `documentation.core.architecture: false`

### ADR Review (unless disabled)
- Checks if new architectural decisions should be documented
- Suggests creating new ADRs for recent major decisions
- Skipped if `documentation.core.adr: false`

### Onboarding Guide (unless disabled)
- Ensures onboarding documentation reflects current setup process
- Checks for new dependencies, tools, or setup steps
- Skipped if `documentation.core.onboarding: false`

### Infrastructure Docs (if deployment configs detected, unless disabled)
- Reviews deployment, dependencies, and security documentation
- Checks if infrastructure has changed
- Skipped if respective infrastructure docs are disabled

### Development Docs (if collaborative project detected, unless disabled)
- Reviews RFC, contributing, and API documentation
- Checks for API changes or new contribution guidelines
- Skipped if respective development docs are disabled

## Usage

Basic analysis:
```
/update-docs
```

With specific focus:
```
/update-docs focus on database changes
```

## Output

I will provide a detailed report including:
- **Current Documentation Status**: What exists and what's missing
- **Staleness Analysis**: Which docs are out of sync with code
- **Specific Recommendations**: Actionable suggestions with slash commands
- **Priority Ordering**: Most critical updates first

## Example Output

```
Documentation Update Analysis

✅ Up to Date:
- docs/onboarding.md (last updated 2 days ago)
- docs/adr/ (5 records, all current)

⚠️ Needs Update:
- docs/data-model.md (database models modified 3 days ago)
  → Run: /gen-er-diagram

- docs/architecture.md (new services added recently)
  → Manual update recommended

❌ Missing:
- docs/api-documentation.md (API endpoints detected)
  → Run: /init-docs to generate

Recommendations:
1. Update ER diagram first (highest impact)
2. Review architecture doc for new services
3. Consider adding API documentation
```

## Configuration

Respects `.cursor-init.yaml` settings:

```yaml
documentation:
  core: { architecture: true, onboarding: true, adr: true }
  data: { data_model: true }

templates:
  architecture: "google_style"
```

Only analyzes documentation types that are:
- Relevant to the project (based on detected technologies)
- Not explicitly disabled in configuration

---

**Template Location**: `.cursor/cursor-init/templates/`
**Configuration File**: `.cursor-init.yaml` (optional)
