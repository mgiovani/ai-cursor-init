# 🚀 AI Cursor Init

> **Stop writing documentation. Start generating it.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
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

## 📸 **Visual Showcase**

### 🏗️ System Architecture Documentation

Auto-generated architecture overview with intelligent component mapping:

![System Architecture Example](images/system-architecture-example.png)

### 🚀 Onboarding Guide Generation  

Context-aware onboarding documentation tailored to your project:

![Onboarding Doc Example](images/onboarding-doc-example.png)

### 📋 Advanced Onboarding Features

Comprehensive setup guides with framework-specific instructions:

![Onboarding Doc Example 2](images/onboarding-doc-example-2.png)

### 🗂️ Data Model Generation

Professional ER diagrams and database schema documentation:

![Data Model Generation](images/data-model-generation.png)

---

## 🚀 **Quick Start** *(2 minutes to awesome docs)*

### Zero Configuration *(Recommended)*

```bash
# 1. Clone this repo
git clone https://github.com/mgiovani/ai-cursor-init.git

# 2. Copy to your project (ONLY ONE FOLDER!)
cp -r ai-cursor-init/.cursor/ your-project/

# 3. Open your project in Cursor and type:
/init-docs
```

**That's it!** The framework analyzes your project and generates all useful documentation automatically:

- **Always**: Architecture overview, onboarding guide, ADRs
- **If database models found**: ER diagrams, database operations guide  
- **If API endpoints found**: API documentation, security flows
- **If deployment configs found**: Infrastructure and deployment docs
- **If open source/team project**: Contributing guidelines, RFC templates

### Opt-Out Configuration *(Optional)*

Don't want certain documentation? Create `.cursor-init.yaml` to disable specific types:

```yaml
# .cursor-init.yaml (optional - only to disable unwanted docs)
documentation:
  data:
    database_ops: false     # Skip database operations guide
  infrastructure:
    deployment: false       # Skip deployment documentation
    security: false         # Skip security flow diagrams
  development:
    rfc: false             # Skip RFC template setup
```

### Option 2: AI-Powered CLI for Power Users

```bash
pip install ai-cursor-init

# Configure AI provider (OpenAI, Anthropic, or Google Gemini)
ai-cursor-init configure

# Generate intelligent documentation with AI
ai-cursor-init init  # AI-powered docs generation
ai-cursor-init adr "Database Migration Strategy"  # Context-aware ADRs
ai-cursor-init update --apply  # Smart documentation updates
```

📖 **[Complete AI CLI Documentation →](AI_DOCUMENTATION.md)**

---

## 🎯 **What You Get**

| Command | What It Does | AI Enhancement | Time Saved |
|---------|-------------|----------------|------------|
| `/init-docs` | Complete documentation scaffold | **Context-aware generation** | **2-3 hours** |
| `/adr "Decision"` | Architecture Decision Record | **Project-specific insights** | **30-45 min** |
| `/gen-er-diagram` | Database schema visualization | **Auto-detection & relationships** | **1-2 hours** |
| `/gen-arch-diagram` | System architecture diagram | **Intelligent component mapping** | **1-2 hours** |
| `/update-docs` | Sync docs with code changes | **Smart content enhancement** | **30-60 min** |
| `/check-docs` | Quality validation & freshness | **Semantic analysis** | **15-30 min** |

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

## 🎨 **Smart Templates & Configuration**

### **Zero-Config Defaults**

Works immediately with smart detection:

- **Python/FastAPI** → API-focused architecture docs
- **TypeScript/React** → Component-based system diagrams  
- **SQLAlchemy** → Detailed ER diagrams with relationships
- **Django** → Model-centric documentation

### **Optional Configuration**

Choose exactly what documentation you need:

```yaml
# .cursor-init.yaml (optional customization)
documentation:
  core:
    architecture: true    # System overview
    onboarding: true     # Developer setup guide
    adr: true           # Architecture decisions
  data:
    data_model: true    # Database schema
    database_ops: false # Performance & operations
    data_security: false # Security policies
  infrastructure:
    deployment: false   # CI/CD & infrastructure
    dependencies: false # External services
    security: false    # Security flows
  development:
    rfc: false         # Request for Comments
    contributing: false # Contribution guides
    api_docs: false    # API documentation
```

### **Template Variants**

- **ADRs**: Nygard, MADR, Comprehensive, Lightweight
- **Architecture**: Google Style, Enterprise, Arc42
- **Onboarding**: Developer, Contributor, User
- **Data Model**: Simple, Comprehensive

### **Common Configurations**

**Startup/Small Team:**

```yaml
documentation:
  core: { architecture: true, onboarding: true, adr: true }
  data: { data_model: true }
  development: { contributing: true }
```

**Enterprise/Large Team:**

```yaml
documentation:
  core: { architecture: true, onboarding: true, adr: true }
  data: { data_model: true, database_ops: true, data_security: true }
  infrastructure: { deployment: true, dependencies: true, security: true }
  development: { rfc: true, contributing: true, api_docs: true }
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

## 📄 **License**

MIT License - see [LICENSE](LICENSE) for details.

---

## ⭐ **Star This Repo**

If this tool saved you time, give us a star! It helps other developers discover the project.

[![GitHub stars](https://img.shields.io/github/stars/mgiovani/ai-cursor-init?style=social)](https://github.com/mgiovani/ai-cursor-init/stargazers)

---

**Built with ❤️ for developers who hate writing docs but love having them.**
