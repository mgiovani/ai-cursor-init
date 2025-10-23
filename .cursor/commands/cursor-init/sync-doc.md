# Sync Specific Documentation

Synchronize a specific documentation file with the current codebase state.

## What This Does

Updates a single documentation file based on current project state, respecting configuration settings.

1. **Identify Document**: Determines which documentation file to sync based on the provided name
2. **Check Configuration**: Verifies if the documentation type is explicitly disabled in `.cursor-init.yaml`
3. **Check Relevance**: Determines if the documentation type is relevant to the current project
4. **Load Template**: Reads the appropriate template variant from `.cursor/cursor-init/templates/`
5. **Analyze Codebase**: Gathers current information related to the specific documentation type
6. **Update Content**: Refreshes the documentation file with current information
7. **Replace Placeholders**: Updates template placeholders with current project data

## Supported Documentation Types

### Core Documentation
- `architecture` - System architecture overview
- `onboarding` - Developer onboarding guide

### Data Documentation
- `data-model` - Database schema & ER diagrams
- `database-ops` - Database operations guide
- `data-security` - Data security policies

### Infrastructure Documentation
- `deployment` - CI/CD & deployment procedures
- `dependencies` - External service dependencies
- `security` - Security architecture

### Development Documentation
- `contributing` - Contributor guidelines
- `api-documentation` - API documentation

## Usage

Sync architecture documentation:
```
/sync-doc architecture
```

Sync data model:
```
/sync-doc data-model
```

Sync onboarding guide:
```
/sync-doc onboarding
```

With additional context:
```
/sync-doc architecture after adding microservices
```

## Configuration Check

Before syncing, I will:
1. Check if the documentation type is explicitly disabled in `.cursor-init.yaml`
2. Inform you if the documentation type is disabled
3. Skip syncing if disabled (`false` in config)
4. Only sync if enabled or not explicitly disabled

Example configuration:
```yaml
documentation:
  core:
    architecture: true
    onboarding: true
  data:
    data_model: true
    database_ops: false  # This would prevent sync-doc database-ops
```

## Process

I will:
1. Parse the documentation name from your command
2. Check `.cursor-init.yaml` to verify if this doc type is disabled
3. If disabled, inform you and skip syncing
4. If enabled, load the appropriate template variant
5. Analyze relevant parts of the codebase
6. Update the specific documentation file
7. Report what was changed

## Output

You'll receive:
- Confirmation of which file was updated
- Summary of changes made
- Note if file was skipped (disabled or not relevant)

## Examples

```
/sync-doc architecture
→ Updates docs/architecture.md with current system structure

/sync-doc data-model
→ Regenerates docs/data-model.md with current database schema

/sync-doc deployment
→ Updates docs/deployment.md with current deployment configuration
```

---

**Template Location**: `.cursor/cursor-init/templates/`
**Configuration File**: `.cursor-init.yaml` (optional)
