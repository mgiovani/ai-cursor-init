# Generate Onboarding Diagram

Generate visual flowcharts for developer onboarding process.

## What This Does

Creates step-by-step visual guides for onboarding new developers:

1. Analyzes project setup requirements (dependencies, tools, env vars)
2. Identifies setup sequence and dependencies
3. Maps development workflow from clone to first contribution
4. Generates Mermaid flowchart of onboarding steps
5. Integrates with `docs/onboarding.md`

## Usage

```
/gen-onboarding-diagram
```

## Example Output

```mermaid
flowchart TD
    Start([New Developer]) --> Clone[Clone Repository]
    Clone --> CheckReqs[Check Requirements]
    CheckReqs --> InstallDeps[Install Dependencies]

    InstallDeps --> Python{Python Project?}
    Python -->|Yes| UV[Install with uv]
    Python -->|No| Node{Node Project?}
    Node -->|Yes| Bun[Install with bun]
    Node -->|No| Other[Follow README]

    UV --> Env[Configure .env]
    Bun --> Env
    Other --> Env

    Env --> DB[Setup Database]
    DB --> Migrate[Run Migrations]
    Migrate --> Test[Run Tests]

    Test --> Pass{Tests Pass?}
    Pass -->|Yes| Dev[Start Development]
    Pass -->|No| Debug[Debug Issues]
    Debug --> Test

    Dev --> FirstPR[Create First PR]
    FirstPR --> Done([Onboarded!])
```

## Configuration

```yaml
documentation:
  core:
    onboarding: true  # Set to false to disable

templates:
  onboarding: "developer"  # Options: developer, contributor, user
```

---

**Output File**: `docs/onboarding.md` (diagram section)
