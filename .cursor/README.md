# 📚 AI-Powered Documentation Framework

**Version:** 1.0.0  
**Architecture:** Native Commands + Proactive Rules

This folder contains an intelligent documentation generation system that works seamlessly within Cursor IDE.

## 🚀 **Quick Start (Zero Configuration)**

**Just copy this `.cursor/` folder to your project root and start using it immediately!**

```bash
# Copy the .cursor/ folder to your project
cp -r path/to/ai-cursor-init/.cursor/ your-project/.cursor/

# Open your project in Cursor and type:
/init-docs
```

**That's it!** The system analyzes your project and generates useful documentation automatically:

- **Always**: Architecture overview, onboarding guide, ADRs
- **If database models found**: ER diagrams with relationships
- **If frameworks detected**: Framework-specific documentation

## 📋 **Available Commands**

The framework provides **16 native Cursor commands** that appear in the `/` autocomplete menu:

### Documentation Management (6 commands)

- `/init-docs` - Set up complete documentation structure
- `/update-docs` - Refresh documentation with code changes
- `/sync-docs` - Sync all documentation with current codebase
- `/sync-doc [filename]` - Sync specific documentation file
- `/sync-category [category]` - Sync category (core, data, infrastructure, development)
- `/check-docs` - Validate documentation quality

### Creation Commands (2 commands)

- `/adr "Decision Title"` - Create new ADR with context
- `/adr [variant] "Decision Title"` - Override template variant (e.g., `/adr lightweight "Title"`)
- `/rfc "RFC Title"` - Create new Request for Comments document
- Example: `/adr "Choose Database Technology"`

### Diagram Generation (6 commands)

- `/gen-er-diagram` - Database schema diagrams from ORM models
- `/gen-arch-diagram` - System architecture diagrams
- `/gen-onboarding-diagram` - Developer setup flow diagrams
- `/gen-dependency-diagram` - External service dependency diagrams
- `/gen-security-diagram` - Security architecture flow diagrams
- `/gen-deployment-diagram` - Deployment infrastructure diagrams

### Template Management (2 commands)

- `/list-templates` - Show all available templates and variants
- `/add-template [type]` - Add custom template variant

## 🤖 **Proactive Rules (5 always-on)**

The framework includes **5 proactive rules** that continuously monitor and suggest:

- **Context Rules (3)**: Provide framework knowledge, ADR context, architecture guidance
- **Quality Rules (1)**: Enforce code quality standards (DRY, SOLID)
- **Proactive Suggestions (1)**: Automatically suggest documentation updates after code changes

## ⚙️ **Opt-Out Configuration (Optional)**

**Zero configuration works great for most projects!** Only create a config file if you want to customize template styles or disable certain documentation types.

Create `.cursor-init.yaml` to customize documentation:

```yaml
# Optional configuration - only if you want to customize defaults
templates:
  adr: "nygard_style"        # Options: nygard_style, full, lightweight, madr
  architecture: "google_style"  # Options: google_style, enterprise, arc42
  onboarding: "developer"    # Options: developer, contributor, user
  data_model: "comprehensive" # Options: simple, comprehensive

documentation:
  data:
    data_model: false        # Disable ER diagram generation
```

### **Configuration Examples**

#### **Minimal Documentation Only**

```yaml
documentation:
  core: { architecture: true, onboarding: true, adr: true }
  data: { data_model: false }
```

#### **Open Source Project Template Customization**

```yaml
templates:
  onboarding: "contributor"  # Contributor-focused onboarding
  architecture: "google_style"  # Google-style architecture docs
```

## 📁 **Generated Documentation Structure**

```
docs/
├── 📋 architecture.md              # System overview & components
├── 🚀 onboarding.md               # Setup guide for developers
├── 🗂️ data-model.md               # Database schema & ER diagrams
├── adr/                           # Architecture Decision Records
│   ├── 0001-record-architecture-decisions.md
│   ├── 0002-choose-database-technology.md
│   └── 0003-api-authentication-strategy.md
└── rfc/                           # Request for Comments
    ├── new-feature-proposal.md
    └── api-versioning-strategy.md
```

## 🎯 **Smart Features**

### **Automatic Detection**

- **Languages**: Any programming language via AI analysis
- **Frameworks**: Any web, mobile, or backend framework
- **Databases**: Any database system with model definitions
- **Project Structure**: Automatically adapts to your codebase

### **Context-Aware Generation**

- Analyzes your actual codebase for relevant examples
- Generates technology-specific documentation
- Creates appropriate diagrams for your architecture
- Maintains consistency across all documents

### **Professional Quality**

- Industry best practices (Google, ThoughtWorks, Microsoft)
- Mermaid diagrams for visual documentation
- Cross-referenced documentation structure
- Version-controlled alongside your code

## 🔧 **Template Variants**

Choose different styles for each document type:

- **ADRs**: Nygard, MADR, Comprehensive, Lightweight
- **Architecture**: Google Style, Enterprise, Arc42
- **Onboarding**: Developer, Contributor, User
- **Data Model**: Simple, Comprehensive

## 🆘 **Troubleshooting**

### **Common Issues**

**Q: Commands not working?**  
A: Make sure the `.cursor/` folder is in your project root and you're using Cursor IDE.

**Q: Want different documentation types?**  
A: Copy `.cursor-init.example.yaml` to `.cursor-init.yaml` and customize the `documentation` section.

**Q: Need custom templates?**  
A: Check the template customization guide in the documentation.

**Q: Documentation seems outdated?**  
A: Run `/update-docs` or `/sync-docs` to refresh with current code.

## 🏗️ **Framework Architecture**

### Two-Tier System

1. **Native Commands** (`.cursor/commands/cursor-init/`) - 16 plain Markdown files for user actions
2. **Proactive Rules** (`.cursor/rules/cursor-init/`) - 5 MDC files for always-on guidance

### Template System

- **21 built-in templates** in `.cursor/cursor-init/templates/`
- Multiple variants per document type
- Support for custom templates

## 📚 **Learn More**

- **Full Documentation**: [AI-Cursor-Init Repository](https://github.com/mgiovani/ai-cursor-init)
- **Template Library**: Browse `.cursor/cursor-init/templates/` for all 21 available templates
- **Configuration Reference**: See `.cursor-init.example.yaml` for all options
- **Architecture Details**: See ADR-0005 for native commands migration rationale

---

**🎉 Happy Documenting!** This framework saves hours per project by generating professional, contextual documentation automatically.
