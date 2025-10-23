# Sync Documentation Category

Synchronize all documentation files within a specific category (core, data, infrastructure, or development).

## What This Does

Updates all documentation files in a category based on current project state, respecting configuration settings.

1. **Identify Category**: Determines which category to sync (core, data, infrastructure, development)
2. **Check Configuration**: Verifies which documentation types within the category are explicitly disabled
3. **Check Relevance**: Determines which documentation types in the category are relevant to the project
4. **Load Templates**: Reads appropriate template variants for all relevant docs in the category
5. **Analyze Codebase**: Gathers information related to the category
6. **Update Files**: Refreshes all relevant documentation files in the category
7. **Skip Disabled**: Skips any documentation types explicitly disabled in configuration

## Documentation Categories

### Core Category
Always relevant unless explicitly disabled:
- `docs/architecture.md` - System architecture
- `docs/onboarding.md` - Developer onboarding
- `docs/adr/` - Architecture Decision Records

### Data Category
Relevant if database/models detected:
- `docs/data-model.md` - Database schema & ER diagrams
- `docs/database-ops.md` - Database operations guide
- `docs/data-security.md` - Data security policies

### Infrastructure Category
Relevant if deployment configs detected:
- `docs/deployment.md` - CI/CD & deployment procedures
- `docs/dependencies.md` - External service dependencies
- `docs/security.md` - Security architecture

### Development Category
Relevant if collaborative project:
- `docs/rfc/` - Request For Comments documents
- `docs/contributing.md` - Contributor guidelines
- `docs/api-documentation.md` - API documentation

## Usage

Sync core documentation:
```
/sync-category core
```

Sync data documentation:
```
/sync-category data
```

Sync infrastructure documentation:
```
/sync-category infrastructure
```

Sync development documentation:
```
/sync-category development
```

With additional context:
```
/sync-category data after schema migration
```

## Configuration Behavior

Example `.cursor-init.yaml`:
```yaml
documentation:
  core:
    architecture: true
    onboarding: true
    adr: true
  data:
    data_model: true
    database_ops: false    # Skipped in sync
    data_security: false   # Skipped in sync
  infrastructure:
    deployment: true
    dependencies: false    # Skipped in sync
    security: true
```

When you run `/sync-category data`:
- ✅ Syncs `docs/data-model.md` (enabled)
- ❌ Skips `docs/database-ops.md` (disabled)
- ❌ Skips `docs/data-security.md` (disabled)

## Process

I will:
1. Parse the category name from your command
2. Read `.cursor-init.yaml` to check which docs in the category are disabled
3. Determine which documentation types in the category are relevant to the project
4. Load appropriate template variants for all relevant, non-disabled docs
5. Analyze codebase for category-specific information
6. Update all relevant, non-disabled documentation files in the category
7. Report what was synced and what was skipped

## Output

You'll receive:
- List of files updated in the category
- List of files skipped (disabled or not relevant)
- Summary of changes made

## Examples

```
/sync-category core
→ Updates docs/architecture.md, docs/onboarding.md, and docs/adr/

/sync-category data
→ Updates data-related documentation (data-model, database-ops, data-security)
→ Only updates files that are enabled and relevant

/sync-category infrastructure
→ Updates deployment, dependencies, and security documentation
→ Skips files that are disabled in configuration
```

---

**Template Location**: `.cursor/cursor-init/templates/`
**Configuration File**: `.cursor-init.yaml` (optional)
