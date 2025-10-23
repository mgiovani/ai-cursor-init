# AI-Cursor-Init API Documentation

**Last Updated:** 2025-10-23  
**Framework Version:** 1.0.0  
**Integration:** Cursor IDE Native

This document provides comprehensive API documentation for the AI-Cursor-Init framework's slash commands, templates, and configuration system.

## 🚀 **Slash Commands API**

### Core Documentation Commands

#### `/init-docs`

Initializes complete documentation structure for your project.

**Syntax:**

```
/init-docs
```

**Behavior:**

1. Analyzes project structure and technology stack
2. Detects relevant documentation types based on project characteristics
3. Creates missing documentation files using appropriate templates
4. Respects configuration in `.cursor-init.yaml` if present

**Generated Documentation:**

- **Always**: `architecture.md`, `onboarding.md`, `adr/`
- **If database models detected**: `data-model.md`
- **If collaborative project**: `contributing.md`, `rfc/`
- **If deployment configs found**: `deployment.md`, `dependencies.md`

**Configuration Support:**

```yaml
documentation:
  core:
    architecture: true    # System architecture
    onboarding: true     # Developer onboarding  
    adr: true           # Architecture Decision Records
  data:
    data_model: true    # Database schema documentation
  development:
    contributing: true  # Contributor guidelines
    api_docs: true     # API documentation
```

#### `/update-docs`

Updates existing documentation to reflect code changes.

**Syntax:**

```
/update-docs
```

**Behavior:**

1. Scans existing documentation files
2. Analyzes recent code changes and project evolution
3. Identifies outdated or missing content
4. Provides specific recommendations for updates
5. Can regenerate content for severely outdated files

**Analysis Areas:**

- Database model changes → Suggest `/gen-er-diagram`
- Architecture changes → Update architecture documentation
- New dependencies → Update onboarding and deployment guides
- API changes → Update API documentation

#### `/check-docs`

Validates documentation quality and freshness.

**Syntax:**

```
/check-docs
```

**Output:**

- Documentation completeness score
- Outdated file identification
- Missing documentation recommendations
- Quality improvement suggestions

### Architecture Decision Records

#### `/adr "Decision Title"`

Creates a new Architecture Decision Record.

**Syntax:**

```
/adr "Title of the architectural decision"
```

**Examples:**

```
/adr "Choose Database Technology"
/adr "Adopt Microservices Architecture"  
/adr "Implement Authentication Strategy"
```

**Template Variants:**

- `nygard_style` (default): Michael Nygard's format
- `madr`: Markdown ADR format
- `full`: Comprehensive format with detailed sections
- `lightweight`: Simplified format for quick decisions

**Configuration:**

```yaml
templates:
  adr: "nygard_style"  # nygard_style|madr|full|lightweight
```

#### `/rfc "RFC Title"`

Creates a new Request for Comments document.

**Syntax:**

```
/rfc "Title of the RFC proposal"
```

**Examples:**

```
/rfc "New API Versioning Strategy"
/rfc "Frontend Architecture Refactor"
/rfc "Data Migration Plan"
```

**Template Variants:**

- `standard` (default): Balanced detail and conciseness
- `minimal`: Brief format for simple proposals
- `detailed`: Comprehensive format for complex proposals

### Diagram Generation Commands

#### `/gen-er-diagram`

Generates Entity Relationship diagram from database models.

**Syntax:**

```
/gen-er-diagram
```

**Detection Capabilities:**

- SQLAlchemy models (Python)
- Django models (Python)
- Sequelize models (JavaScript)
- Database schema files
- Migration files

**Output:**

- Updates `docs/data-model.md` with Mermaid ER diagram
- Includes entity descriptions and relationships
- Documents database constraints and indexes

**Template Variants:**

```yaml
templates:
  data_model: "comprehensive"  # simple|comprehensive
```

#### `/gen-arch-diagram`

Generates system architecture diagram from project structure.

**Syntax:**

```
/gen-arch-diagram
```

**Analysis:**

- Directory structure analysis
- Component identification (frontend, backend, database)
- Service dependencies
- Communication patterns

**Output:**

- Creates or updates architecture documentation
- Mermaid diagram showing system components
- Component descriptions and responsibilities

#### `/gen-onboarding-diagram`

Creates developer onboarding workflow diagram.

**Syntax:**

```
/gen-onboarding-diagram
```

**Analysis:**

- Setup requirements (languages, tools, dependencies)
- Configuration steps
- Testing procedures
- Development workflow

**Output:**

- Flowchart showing onboarding process
- Decision points and troubleshooting paths
- Framework-specific setup instructions

#### `/gen-dependency-diagram`

Visualizes external dependencies and service integrations.

**Syntax:**

```
/gen-dependency-diagram
```

**Detection:**

- Database connections
- External APIs
- Authentication services
- Message queues and caches
- Monitoring and analytics services

**Output:**

- Dependency relationship diagram
- Service classification and descriptions
- Integration details and health checks

#### `/gen-security-diagram`

Creates security architecture and authentication flow diagrams.

**Syntax:**

```
/gen-security-diagram
```

**Analysis:**

- Authentication mechanisms
- Authorization patterns
- Security layers and controls
- Data protection measures

**Output:**

- Authentication flow sequence diagrams
- Security architecture overview
- Threat model and mitigations

#### `/gen-deployment-diagram`

Generates deployment architecture and infrastructure diagrams.

**Syntax:**

```
/gen-deployment-diagram
```

**Detection:**

- Container configurations (Docker, Kubernetes)
- CI/CD pipelines
- Cloud services and infrastructure
- Load balancers and scaling

**Output:**

- Deployment topology diagram
- Environment configurations
- Scaling and monitoring setup

### Template Management Commands

#### `/list-templates`

Lists all available documentation templates.

**Syntax:**

```
/list-templates
```

**Output:**

- Template categories and variants
- Configuration options
- Usage examples and descriptions

#### `/add-template TemplateName path/to/template.md`

Adds a custom template to the framework.

**Syntax:**

```
/add-template TemplateName path/to/template.md
```

**Examples:**

```
/add-template CustomAPI ./templates/api-custom.md
/add-template SecurityGuide ./templates/security-guide.md
```

### Maintenance Commands

#### `/sync-docs`

Synchronizes all documentation with current codebase.

**Syntax:**

```
/sync-docs
```

**Behavior:**

- Analyzes all existing documentation
- Updates content based on code changes
- Regenerates outdated sections
- Maintains document history and versioning

#### `/sync-doc filename.md`

Synchronizes a specific documentation file.

**Syntax:**

```
/sync-doc filename.md
```

**Examples:**

```
/sync-doc architecture.md
/sync-doc data-model.md
/sync-doc adr/0001-database-choice.md
```

#### `/sync-category category`

Synchronizes all documents in a specific category.

**Syntax:**

```
/sync-category category
```

**Categories:**

- `adr` - Architecture Decision Records
- `architecture` - Architecture documentation
- `data` - Data model and database documentation
- `development` - Development and contribution guides

**Examples:**

```
/sync-category adr
/sync-category architecture
/sync-category data
```

## 🔧 **Configuration API**

### `.cursor-init.yaml` Schema

#### Documentation Types Configuration

Controls which documentation types are generated:

```yaml
documentation:
  # Core documentation (always relevant)
  core:
    architecture: true    # System architecture overview
    onboarding: true     # Developer onboarding guide
    adr: true           # Architecture Decision Records
  
  # Data documentation (auto-generated if models detected)
  data:
    data_model: true      # Database schema & ER diagrams
    database_ops: false   # Database operations guide
    data_security: false  # Data security policies
  
  # Infrastructure documentation (auto-generated if configs detected)
  infrastructure:
    deployment: false     # CI/CD & deployment procedures
    dependencies: false   # External service dependencies
    security: false      # Security architecture & flows
  
  # Development documentation (auto-generated if collaborative)
  development:
    rfc: false           # Request For Comments documents
    contributing: false  # Contributor guidelines
    api_docs: false     # API documentation
```

#### Template Variants Configuration

Selects specific template styles:

```yaml
templates:
  # Architecture Decision Records
  adr: "nygard_style"          # nygard_style|madr|full|lightweight
  
  # Architecture documentation  
  architecture: "google_style" # google_style|enterprise|arc42
  
  # Onboarding guides
  onboarding: "developer"      # developer|contributor|user
  
  # Data model documentation
  data_model: "comprehensive"  # simple|comprehensive
  
  # Request For Comments
  rfc: "standard"             # minimal|standard|detailed
```

#### Custom Template Paths

Define custom template locations:

```yaml
templates:
  custom_template_paths:
    security: "templates/custom/security-comprehensive.md"
    api_docs: "templates/custom/api-documentation.md"
    deployment: "templates/custom/deployment-k8s.md"
```

#### Project Settings

Project-specific configuration:

```yaml
project:
  name: "my-awesome-project"     # Override auto-detected name
  description: "Brief project description"
  type: "web-api"               # Hint for template selection
  
preferences:
  diagram_style: "mermaid"      # Diagram format preference
  documentation_style: "professional"  # Writing style
```

#### Generation Settings

Control content generation behavior:

```yaml
generation:
  # Content options
  include_code_examples: true    # Include code snippets
  include_diagrams: true        # Generate Mermaid diagrams
  auto_generate_toc: true       # Generate table of contents
  
  # Analysis depth
  analysis_depth: "standard"    # basic|standard|comprehensive
  
  # Quality controls
  quality:
    min_content_length: 500     # Minimum content length
    max_retries: 3             # Max generation attempts
    validate_generation: true   # Validate output quality
```

## 🎨 **Template API**

### Template Structure

Templates use placeholder-based content generation:

```markdown
# {{PROJECT_NAME}} - {{DOCUMENT_TYPE}}

**Last Updated:** {{DATE}}  
**Version:** {{VERSION}}  
**Maintainer:** {{MAINTAINER}}

## Overview

{{PROJECT_DESCRIPTION}}

## {{SECTION_TITLE}}

{{SECTION_CONTENT}}

### Subsection

{{SUBSECTION_CONTENT}}

## Diagrams

```mermaid
{{MERMAID_DIAGRAM}}
```

## Configuration

{{CONFIGURATION_DETAILS}}

## References

{{REFERENCES}}

```

### Available Placeholders

#### Project Information
- `{{PROJECT_NAME}}` - Project name (auto-detected)
- `{{PROJECT_DESCRIPTION}}` - Project description
- `{{VERSION}}` - Current version
- `{{MAINTAINER}}` - Project maintainer
- `{{DATE}}` - Current date
- `{{REPOSITORY_URL}}` - Git repository URL

#### Technical Details
- `{{TECH_STACK}}` - Detected technology stack
- `{{FRAMEWORK}}` - Primary framework
- `{{DATABASE_TYPE}}` - Database technology
- `{{DEPLOYMENT_PLATFORM}}` - Deployment platform

#### Content Sections
- `{{ARCHITECTURE_DIAGRAM}}` - System architecture diagram
- `{{ER_DIAGRAM}}` - Entity relationship diagram
- `{{SECURITY_DIAGRAM}}` - Security flow diagram
- `{{DEPLOYMENT_DIAGRAM}}` - Deployment architecture
- `{{ONBOARDING_STEPS}}` - Setup instructions

#### Dynamic Content
- `{{DEPENDENCIES}}` - Project dependencies
- `{{API_ENDPOINTS}}` - API documentation
- `{{DATABASE_SCHEMA}}` - Database structure
- `{{CONFIGURATION}}` - Configuration details

### Template Categories

#### Architecture Templates
- `google_style.md` - Google's architecture documentation format
- `enterprise.md` - Enterprise architecture template
- `arc42.md` - Arc42 architecture template

#### ADR Templates  
- `nygard_style.md` - Michael Nygard's ADR format
- `madr.md` - Markdown ADR format
- `full.md` - Comprehensive ADR format
- `lightweight.md` - Simplified ADR format

#### Onboarding Templates
- `developer.md` - Developer-focused onboarding
- `contributor.md` - Open source contributor guide
- `user.md` - End-user onboarding

#### Data Model Templates
- `simple.md` - Basic data model documentation
- `comprehensive.md` - Detailed data model with full schema

## 🔒 **Security API**

### Safe Operations

The framework operates with security-first principles:

**Static Analysis Only:**
- File system analysis (read-only)
- Configuration file parsing
- Import statement analysis via AST parsing
- Directory structure pattern matching

**Prohibited Operations:**
- Code execution or dynamic imports
- Network requests during analysis
- File modification outside `docs/` directory
- Access to files outside project directory

### Security Boundaries

**Allowed File Access:**
- Read access to project files within working directory
- Write access only to documentation directories
- Parse configuration files (JSON, YAML, TOML, INI)

**Process Isolation:**
- Sandboxed operations for advanced analysis
- Resource limits (memory, CPU, time)
- Graceful degradation on analysis failures

## 📊 **Response Formats**

### Command Responses

All slash commands provide structured responses:

```json
{
  "status": "success|warning|error",
  "message": "Human-readable status message",
  "actions_taken": [
    "Created docs/architecture.md",
    "Updated docs/data-model.md",
    "Generated ER diagram"
  ],
  "recommendations": [
    "Consider running /gen-er-diagram to update database schema",
    "Update deployment documentation with new services"
  ],
  "next_steps": [
    "Review generated documentation",
    "Customize templates if needed",
    "Share with team for feedback"
  ]
}
```

### Error Handling

Graceful error handling with helpful messages:

```json
{
  "status": "error",
  "error_type": "configuration_error|template_error|analysis_error",
  "message": "Detailed error description",
  "suggestions": [
    "Check .cursor-init.yaml syntax",
    "Ensure required templates exist",
    "Verify project structure"
  ],
  "recovery_options": [
    "Use default configuration",
    "Skip problematic sections",
    "Request manual intervention"
  ]
}
```

## 🔄 **API Versioning**

### Current Version: 1.0.0

The API follows semantic versioning:

- **Major**: Breaking changes to slash command syntax or behavior
- **Minor**: New features, new templates, enhanced detection
- **Patch**: Bug fixes, template improvements, documentation updates

### Backward Compatibility

- Existing slash commands maintain compatibility
- Configuration file format is stable
- Template placeholder syntax is consistent
- Generated documentation structure is preserved

### Deprecation Policy

- 6-month notice for breaking changes
- Clear migration paths for deprecated features
- Comprehensive changelog documentation
- Community feedback integration

---

*This API documentation is automatically updated with framework changes. For the latest information, see the [GitHub repository](https://github.com/mgiovani/ai-cursor-init).*
