# 📚 AI-Powered Documentation Framework

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

### Core Documentation

- `/init-docs` - Set up complete documentation structure
- `/update-docs` - Refresh documentation with code changes
- `/check-docs` - Validate documentation quality

### Architecture Decision Records

- `/adr "Decision Title"` - Create new ADR with context
- `/rfc "RFC Title"` - Create new Request for Comments document
- Example: `/adr "Choose Database Technology"`

### Diagram Generation

- `/gen-er-diagram` - Database schema diagrams
- `/gen-arch-diagram` - System architecture diagrams
- `/gen-onboarding-diagram` - Setup flow diagrams
- `/gen-dependency-diagram` - External service diagrams
- `/gen-security-diagram` - Security flow diagrams
- `/gen-deployment-diagram` - Infrastructure diagrams

### Template Management

- `/add-template TemplateName path/to/template.md` - Add custom template
- `/list-templates` - Show available templates

### Maintenance

- `/sync-docs` - Sync all documentation
- `/sync-doc filename.md` - Sync specific document
- `/sync-category category` - Sync specific category (adr, architecture, etc.)

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

## 📚 **Learn More**

- **Full Documentation**: [AI-Cursor-Init Repository](https://github.com/mgiovani/ai-cursor-init)
- **Template Library**: Browse `.cursor/templates/` for all available templates
- **Configuration Reference**: See `.cursor-init.example.yaml` for all options

---

**🎉 Happy Documenting!** This framework saves hours per project by generating professional, contextual documentation automatically.
