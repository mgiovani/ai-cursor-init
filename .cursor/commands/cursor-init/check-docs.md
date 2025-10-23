# Check Documentation Quality

Validate documentation freshness, completeness, and quality against current codebase state.

## What This Does

Performs a comprehensive analysis of your documentation to identify:

1. **Missing Documentation**: Relevant documentation types that should exist but don't
2. **Stale Documentation**: Docs that are out of sync with current codebase
3. **Quality Issues**: Formatting problems, broken links, missing sections
4. **Coverage Gaps**: Undocumented components, APIs, or features
5. **Configuration Compliance**: Documentation status relative to `.cursor-init.yaml` settings

## Validation Checks

### Relevance Check
- Determines which documentation types are relevant to your project
- Identifies missing documentation for detected technologies
- Example: If database models found, checks for data-model.md

### Freshness Check
- Compares documentation last-modified dates with related code changes
- Identifies docs that haven't been updated after significant code changes
- Suggests which docs need updating

### Completeness Check
- Verifies all required sections are present in documentation
- Checks for placeholder text ({{PLACEHOLDER}}) that wasn't replaced
- Ensures diagrams are properly rendered

### Quality Check
- Validates Mermaid diagram syntax
- Checks for broken internal links
- Verifies markdown formatting
- Ensures consistent style across documents

### Configuration Check
- Confirms documentation aligns with `.cursor-init.yaml` settings
- Identifies files that exist but are disabled in config
- Suggests configuration updates if needed

## Usage

Basic validation:
```
/check-docs
```

With specific focus:
```
/check-docs focus on data documentation
```

Quick check:
```
/check-docs quick
```

## Output Format

### Status Summary
```
Documentation Health Report

Overall Score: 85/100

✅ Good:
- docs/architecture.md (up to date, well-structured)
- docs/onboarding.md (comprehensive, current)
- docs/adr/ (5 records, all current)

⚠️ Needs Attention:
- docs/data-model.md (outdated - models changed 5 days ago)
  → Recommendation: Run /gen-er-diagram

- docs/deployment.md (missing deployment steps for new services)
  → Recommendation: Run /sync-doc deployment

❌ Missing:
- docs/api-documentation.md (API endpoints detected but not documented)
  → Recommendation: Enable in .cursor-init.yaml and run /init-docs

🔧 Quality Issues:
- docs/architecture.md: Contains unreplaced placeholder {{COMPONENT_NAME}}
- docs/data-model.md: Mermaid diagram syntax error on line 42
```

### Detailed Report

For each documentation file, provides:
- **Last Updated**: Timestamp of last modification
- **Relevance**: Whether still relevant to project
- **Freshness**: How current it is relative to codebase
- **Quality Score**: Based on completeness and formatting
- **Specific Issues**: Line numbers for problems
- **Recommendations**: Actionable next steps

## Configuration

Respects `.cursor-init.yaml` settings:

```yaml
documentation:
  core: { architecture: true, onboarding: true, adr: true }
  data: { data_model: true, database_ops: false }

generation:
  include_code_examples: true
  include_diagrams: true
  auto_generate_toc: true
```

Only checks documentation types that are:
- Relevant to the project (based on detected technologies)
- Not explicitly disabled in configuration

## Validation Criteria

### Freshness Scoring
- **Fresh (90-100)**: Updated within last 7 days or no code changes
- **Good (70-89)**: Minor code changes since last update
- **Stale (50-69)**: Significant code changes since last update
- **Outdated (<50)**: Major code changes or very old

### Completeness Scoring
- **Complete (90-100)**: All sections present, no placeholders
- **Good (70-89)**: Most sections present, minor gaps
- **Incomplete (50-69)**: Several missing sections
- **Poor (<50)**: Major sections missing

### Quality Scoring
- **Excellent (90-100)**: No formatting issues, all diagrams valid
- **Good (70-89)**: Minor formatting issues
- **Fair (50-69)**: Several formatting or syntax issues
- **Poor (<50)**: Major problems, broken diagrams

## Process

I will:
1. Read `.cursor-init.yaml` to understand documentation preferences
2. Scan `docs/` directory for existing documentation files
3. Analyze project to determine relevant documentation types
4. Check each relevant documentation file for:
   - Existence (is it missing?)
   - Freshness (is it outdated?)
   - Completeness (are sections missing?)
   - Quality (formatting, diagrams, links)
5. Generate comprehensive health report
6. Provide prioritized recommendations

## Actionable Recommendations

Based on findings, I'll suggest specific commands:
- `/gen-er-diagram` - For outdated database documentation
- `/sync-doc [name]` - For specific outdated documentation
- `/sync-category [category]` - For outdated category
- `/sync-docs` - For comprehensive update
- `/init-docs` - For missing documentation

---

**Template Location**: `.cursor/cursor-init/templates/`
**Configuration File**: `.cursor-init.yaml` (optional)
