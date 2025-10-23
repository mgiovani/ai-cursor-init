# List Available Templates

Show all available documentation templates and their variants.

## What This Does

Displays a comprehensive list of all documentation templates available in the framework, including:

1. Lists all template types (architecture, ADR, onboarding, etc.)
2. Shows available variants for each template type
3. Displays current configuration settings from `.cursor-init.yaml`
4. Indicates which template variants are currently selected
5. Shows template file locations
6. Provides usage examples for each template type

## Usage

```
/list-templates
```

List templates for specific type:
```
/list-templates adr
/list-templates architecture
```

## Example Output

```
Available Documentation Templates

Template Location: .cursor/cursor-init/templates/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📐 ARCHITECTURE TEMPLATES

Current Selection: google_style ⭐

Available Variants:
  • google_style    - Google's documentation standards (clean, minimal)
  • enterprise      - Comprehensive enterprise documentation
  • arc42           - Follows arc42.org architecture standard

Usage: /gen-arch-diagram
Config: templates.architecture: "google_style"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ADR (ARCHITECTURE DECISION RECORD) TEMPLATES

Current Selection: nygard_style ⭐

Available Variants:
  • nygard_style    - Michael Nygard's concise format (recommended)
  • full            - Comprehensive ADR with detailed sections
  • lightweight     - Minimal ADR for quick decisions
  • madr            - Markdown ADR format

Usage: /adr "Decision Title"
Override: /adr full "Decision Title"
Config: templates.adr: "nygard_style"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👥 ONBOARDING TEMPLATES

Current Selection: developer ⭐

Available Variants:
  • developer       - Developer-focused onboarding guide
  • contributor     - Open source contributor guide
  • user            - End-user documentation

Usage: /init-docs
Config: templates.onboarding: "developer"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🗄️ DATA MODEL TEMPLATES

Current Selection: comprehensive ⭐

Available Variants:
  • simple          - Basic ER diagram with minimal text
  • comprehensive   - Detailed data model documentation

Usage: /gen-er-diagram
Config: templates.data_model: "comprehensive"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 RFC (REQUEST FOR COMMENTS) TEMPLATES

Current Selection: standard ⭐

Available Variants:
  • minimal         - Quick proposal for small changes
  • standard        - Balanced RFC for most changes
  • detailed        - Comprehensive RFC for major changes

Usage: /rfc "Proposal Title"
Override: /rfc detailed "Proposal Title"
Config: templates.rfc: "standard"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 CUSTOM TEMPLATES

You can configure custom template paths in .cursor-init.yaml:

templates:
  custom_template_paths:
    adr: "path/to/custom/adr-template.md"
    architecture: "path/to/custom/architecture-template.md"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Template Configuration

Current configuration (.cursor-init.yaml):

templates:
  architecture: "google_style"
  adr: "nygard_style"
  onboarding: "developer"
  data_model: "comprehensive"
  rfc: "standard"

To change templates, edit .cursor-init.yaml or create it if it doesn't exist.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Process

I will:
1. Read `.cursor-init.yaml` to get current template configuration
2. Scan `.cursor/cursor-init/templates/` directory for available templates
3. Group templates by type (architecture, adr, onboarding, etc.)
4. Identify all variants for each template type
5. Highlight currently selected variants
6. Display template file paths
7. Show usage examples for each template type
8. Include configuration examples

## Template File Locations

Templates are organized by type:

```
.cursor/cursor-init/templates/
├── adr/
│   ├── adr_template_nygard.md
│   ├── adr_template_full.md
│   ├── adr_template_lightweight.md
│   └── adr_template_madr.md
├── architecture/
│   ├── architecture_google.md
│   ├── architecture_enterprise.md
│   └── architecture_arc.md
├── onboarding/
│   ├── onboarding_developer.md
│   ├── onboarding_contributor.md
│   └── onboarding_user.md
├── rfc/
│   ├── rfc_template_minimal.md
│   ├── rfc_template_standard.md
│   └── rfc_template_detailed.md
├── diagrams/
│   ├── data_model_simple.md
│   ├── data_model_comprehensive.md
│   └── er_diagram.md
└── [other template directories]
```

## Configuration

If `.cursor-init.yaml` doesn't exist, I will show default template selections.

---

**Template Location**: `.cursor/cursor-init/templates/`
**Configuration File**: `.cursor-init.yaml` (optional)
