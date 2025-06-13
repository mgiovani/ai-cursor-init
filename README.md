# 🚀 AI Cursor Init

> **Stop writing documentation. Start generating it.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**The AI-powered documentation framework that lives inside your IDE.** Generate Architecture Decision Records, system diagrams, and onboarding guides with simple slash commands. No installations, no setup, no excuses.

---

## ✨ **What Makes This Special?**

🎯 **Zero Installation** → Copy 1 folder, start documenting  
🤖 **AI-Powered** → Analyzes your code to generate contextual docs  
⚡ **Instant Results** → Type `/init-docs` and watch magic happen  
🔄 **Always Fresh** → Docs that sync with your codebase automatically  
🛡️ **Security First** → Static analysis by default, no code execution  

## 🎬 **See It In Action**

```bash
# In Cursor IDE, just type:
/init-docs          # 📚 Scaffold complete documentation
/adr "Use GraphQL"  # 📝 Create architecture decision record  
/gen-er-diagram     # 🗂️ Generate database schema diagram
/check-docs         # ✅ Validate documentation quality
```

**Result:** Professional documentation that would take hours to write, generated in seconds.

---

## 🚀 **Quick Start** *(2 minutes to awesome docs)*

### Option 1: Zero Installation *(Recommended)*

```bash
# 1. Clone this repo
git clone https://github.com/mgiovani/ai-cursor-init.git

# 2. Copy to your project (ONLY ONE FOLDER!)
cp -r ai-cursor-init/.cursor/ your-project/

# 3. (Optional) Customize configuration
cp ai-cursor-init/.cursor-init.example.yaml your-project/.cursor-init.yaml

# 4. Open your project in Cursor and type:
/init-docs
```

**That's it.** No pip install, no dependencies, just ONE folder to copy!

### Option 2: CLI for Power Users

```bash
pip install cursor-init
cursor-init init  # Generate docs from command line
```

---

## 🎯 **What You Get**

| Command | What It Does | Time Saved |
|---------|-------------|------------|
| `/init-docs` | Complete documentation scaffold | **2-3 hours** |
| `/adr "Decision"` | Architecture Decision Record | **30-45 min** |
| `/gen-er-diagram` | Database schema visualization | **1-2 hours** |
| `/gen-arch-diagram` | System architecture diagram | **1-2 hours** |
| `/update-docs` | Sync docs with code changes | **30-60 min** |
| `/check-docs` | Quality validation & freshness | **15-30 min** |

**Total time saved per project: 6-10 hours** ⏰

---

## 🏗️ **Generated Documentation Structure**

```
docs/
├── 📋 architecture.md          # System overview & components
├── 🚀 onboarding.md           # Setup guide for new developers  
├── 🗂️ data-model.md           # ER diagrams & database schema
└── adr/                       # Architecture Decision Records
    ├── 0001-record-architecture-decisions.md
    ├── 0002-choose-database-technology.md
    └── 0003-api-authentication-strategy.md
```

**Every file is:**

- ✅ **Contextual** - Generated from your actual code
- ✅ **Professional** - Follows industry best practices  
- ✅ **Maintainable** - Updates automatically with code changes
- ✅ **Version Controlled** - Markdown files alongside your code

---

## 🎨 **Smart Templates**

### Framework-Aware Generation

- **Python/FastAPI** → API-focused architecture docs
- **TypeScript/React** → Component-based system diagrams  
- **SQLAlchemy** → Detailed ER diagrams with relationships
- **Django** → Model-centric documentation

### Multiple Template Styles

- **ADRs**: Nygard, MADR, Comprehensive formats
- **Architecture**: Google, Enterprise, Arc42 styles
- **Onboarding**: General, Python, Frontend variants

### Customizable Everything

```yaml
# .cursor-init.yaml (copy from .cursor-init.example.yaml)
templates:
  adr: "nygard_style"           # Your preferred ADR format
  architecture: "google_style"  # Documentation style
  onboarding: "python"          # Framework-specific guides

# Add your own templates
custom_template_paths:
  - name: "security_adr"
    path: ".cursor/templates/custom/security-adr.md"
```

---

## 🛡️ **Security & Trust**

**Safe by Design:**

- 🔒 **Static Analysis Only** - No code execution by default
- 🏖️ **Sandboxed Operations** - Isolated environment for advanced features
- ⏱️ **Resource Limits** - Timeouts and memory constraints
- 🔍 **Transparent Operations** - See exactly what's being analyzed

**Enterprise Ready:**

- ✅ MIT Licensed
- ✅ No external API calls
- ✅ Works offline
- ✅ No data collection

---

## 🔧 **Advanced Features**

### CI/CD Integration

```yaml
# .github/workflows/docs.yml
- name: Validate Documentation
  run: cursor-init check-docs --fail-on-stale
```

### Custom Templates

```bash
/add-template MyTemplate path/to/template.md
/list-templates  # See all available templates
```

### Bulk Operations

```bash
/sync-docs          # Update all documentation
/sync-category adr  # Update only ADRs
```

---

## 🤝 **Contributing**

We're building the future of developer documentation. Join us!

- 🐛 **Found a bug?** [Open an issue](https://github.com/mgiovani/ai-cursor-init/issues)
- 💡 **Have an idea?** [Start a discussion](https://github.com/mgiovani/ai-cursor-init/discussions)
- 🔧 **Want to contribute?** Check our [Contributing Guide](CONTRIBUTING.md)

### Quick Contribution Ideas

- 📝 Add templates for new frameworks (Vue, Angular, Spring Boot)
- 🎨 Create new documentation styles
- 🔧 Improve framework detection logic
- 📚 Write tutorials and examples

---

## 📊 **Project Stats**

- 🏗️ **18 Built-in Templates** across 5 document types
- 🎯 **8 Slash Commands** for instant documentation
- 🔧 **3 Framework Integrations** (Python, TypeScript, SQL)
- ⚡ **0 Dependencies** for basic functionality
- 🛡️ **100% Static Analysis** for security

---

## 🗺️ **Roadmap**

- [ ] **VS Code Extension** - Bring slash commands to VS Code
- [ ] **More Frameworks** - Spring Boot, Vue, Angular support
- [ ] **Team Features** - Shared templates and standards
- [ ] **API Documentation** - Auto-generate from OpenAPI specs
- [ ] **Confluence Integration** - Sync docs to Confluence
- [ ] **Slack Bot** - Generate docs from Slack commands

---

## 📄 **License**

MIT License - see [LICENSE](LICENSE) for details.

---

## ⭐ **Star This Repo**

If this tool saved you time, give us a star! It helps other developers discover the project.

[![GitHub stars](https://img.shields.io/github/stars/mgiovani/ai-cursor-init?style=social)](https://github.com/mgiovani/ai-cursor-init/stargazers)

---

**Built with ❤️ for developers who hate writing docs but love having them.**
