# Sync Documentation

Synchronize all relevant documentation files with the current codebase state, generating documentation based on project analysis unless explicitly disabled in configuration.

## What This Does

Performs a full documentation synchronization by:

1. **Read Configuration**: Checks `.cursor-init.yaml` to understand which documentation types are explicitly disabled
2. **Analyze Current Codebase**: Detects languages, frameworks, and project structure using codebase search
3. **Determine Relevant Documentation**: Based on project analysis, identifies which documentation types are relevant:
   - **Core**: architecture, onboarding, adr (always relevant)
   - **Data**: data_model, database_ops, data_security (if database/models detected)
   - **Infrastructure**: deployment, dependencies, security (if deployment configs detected)
   - **Development**: rfc, contributing, api_docs (if collaborative development detected)
4. **Filter by Configuration**: Skips any relevant documentation types that are explicitly disabled (`false` in config)
5. **Check Documentation Status**: Compares existing relevant docs with current code state
6. **Load Templates**: For each relevant documentation type (not disabled), loads the appropriate template from `.cursor/cursor-init/templates/` or custom paths
7. **Update Relevant Files**: Creates/updates documentation files that are relevant to the project and not disabled
8. **Replace Placeholders**: For each document, replaces template placeholders ({{PROJECT_NAME}}, {{DATE}}, etc.) with current project information
9. **Refresh Diagrams**: Updates ER diagrams from database models unless data_model is disabled
10. **Sync Content**: Ensures documentation reflects current project configuration and relevant features

## Documentation Sync Scope

### Core Documentation (Always Synced Unless Disabled)
- `docs/architecture.md` - System architecture
- `docs/onboarding.md` - Developer onboarding
- `docs/adr/` - Architecture Decision Records

### Data Documentation (Synced if Database Detected)
- `docs/data-model.md` - Database schema & ER diagrams
- `docs/database-ops.md` - Database operations (if enabled)
- `docs/data-security.md` - Data security (if enabled)

### Infrastructure Documentation (Synced if Configs Detected)
- `docs/deployment.md` - Deployment procedures (if enabled)
- `docs/dependencies.md` - External dependencies (if enabled)
- `docs/security.md` - Security architecture (if enabled)

### Development Documentation (Synced if Collaborative Project)
- `docs/rfc/` - RFC documents (if enabled)
- `docs/contributing.md` - Contribution guidelines (if enabled)
- `docs/api-documentation.md` - API docs (if enabled)

## Usage

Full sync:
```
/sync-docs
```

With additional context:
```
/sync-docs after major refactoring
```

## Process

**Initiating full documentation synchronization. This may take a moment...**

I will:
1. Read `.cursor-init.yaml` configuration
2. Analyze current codebase structure and technologies
3. Determine which documentation types are relevant
4. Filter out explicitly disabled documentation types
5. Check status of all relevant documentation files
6. Load appropriate templates with configured variants
7. Update or create all relevant documentation files
8. Refresh all diagrams (ER, architecture, deployment, etc.)
9. Ensure all content is current and consistent
10. Report sync results

## Configuration

Uses `.cursor-init.yaml` for settings:

```yaml
documentation:
  core: { architecture: true, onboarding: true, adr: true }
  data: { data_model: true, database_ops: false }
  infrastructure: { deployment: true, dependencies: false, security: false }
  development: { rfc: false, contributing: true, api_docs: false }

templates:
  architecture: "google_style"
  adr: "nygard_style"
  onboarding: "developer"
  data_model: "comprehensive"
```

## Output

After completion, you'll receive:
- List of documentation files created
- List of documentation files updated
- List of documentation files skipped (disabled or not relevant)
- Summary of changes made

## Zero-Config Behavior

If `.cursor-init.yaml` doesn't exist:
- Generates all relevant documentation based on project analysis
- Uses default template variants
- Core docs (architecture, onboarding, ADRs) always generated
- Other docs generated only if relevant technologies detected

---

**Template Location**: `.cursor/cursor-init/templates/`
**Configuration File**: `.cursor-init.yaml` (optional)
