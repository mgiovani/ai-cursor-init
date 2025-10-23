# Generate Architecture Diagram

Generate system architecture diagrams showing components, services, and their relationships.

## What This Does

Creates comprehensive architecture visualization by analyzing your project structure:

1. **Configuration Check**: Reads `.cursor-init.yaml` for architecture documentation settings
2. **Project Analysis**: Examines codebase to identify:
   - Major components and modules
   - Services and microservices
   - Frontend/backend separation
   - External integrations
   - Data flow patterns
3. **Component Discovery**: Detects:
   - API endpoints and routes
   - Background workers/tasks
   - Message queues
   - Cache layers
   - Database connections
   - Third-party services
4. **Template Selection**: Uses configured architecture template variant
5. **Generate Diagrams**: Creates Mermaid diagrams showing:
   - System context (C4 model level 1)
   - Component relationships
   - Data flow
   - Deployment architecture
6. **Update Documentation**: Saves to `docs/architecture.md`

## Diagram Types

### System Context Diagram
Shows your system and its interactions with external systems and users.

### Component Diagram
Shows major components within your system and how they interact.

### Data Flow Diagram
Illustrates how data moves through the system.

### Deployment Diagram
Shows how components are deployed across infrastructure.

## Usage

Basic generation:
```
/gen-arch-diagram
```

With specific focus:
```
/gen-arch-diagram for microservices architecture
```

Specific diagram type:
```
/gen-arch-diagram component diagram only
```

## Template Variants

Configure via `.cursor-init.yaml`:

```yaml
templates:
  architecture: "google_style"  # Options: google_style, enterprise, arc42
```

### Google Style Template
- Clean, minimal design
- Focus on key components
- Decision logs integrated
- Goals and non-goals explicit

### Enterprise Template
- Comprehensive documentation
- Security and compliance sections
- Detailed deployment information
- SLA and monitoring details

### Arc42 Template
- Structured architecture documentation
- Follows arc42.org standard
- Building block view
- Runtime view
- Deployment view

## Example Output

```markdown
# System Architecture

## System Context

\`\`\`mermaid
graph TD
    User[User/Browser]
    Admin[Admin Dashboard]

    API[API Gateway]
    Frontend[React Frontend]
    Backend[FastAPI Backend]
    Worker[Celery Workers]

    DB[(PostgreSQL)]
    Cache[(Redis)]
    Queue[/RabbitMQ\]
    Storage[S3 Storage]

    Email[Email Service]
    Payment[Stripe API]

    User --> Frontend
    Admin --> Frontend
    Frontend --> API
    API --> Backend
    Backend --> DB
    Backend --> Cache
    Backend --> Queue
    Queue --> Worker
    Worker --> DB
    Worker --> Email
    Backend --> Payment
    Backend --> Storage
\`\`\`

## Component Architecture

### Frontend Layer
- React 18 with TypeScript
- Redux for state management
- Tailwind CSS for styling

### API Layer
- FastAPI REST API
- JWT authentication
- Rate limiting middleware

### Business Logic Layer
- Service-oriented architecture
- Domain-driven design patterns
- Async/await for I/O operations

### Data Layer
- PostgreSQL for relational data
- Redis for caching and sessions
- S3 for file storage

### Background Processing
- Celery for async tasks
- RabbitMQ message broker
- Scheduled jobs for cleanup
```

## Configuration

Respects `.cursor-init.yaml` settings:

```yaml
documentation:
  core:
    architecture: true  # Set to false to disable

templates:
  architecture: "google_style"

project:
  preferences:
    diagram_style: "mermaid"
```

## Process

I will:
1. Check configuration for architecture documentation setting
2. Analyze project structure and identify major components
3. Scan for:
   - API routes/endpoints
   - Service definitions
   - Database connections
   - External integrations
   - Configuration files (docker-compose.yml, k8s configs)
4. Identify technology stack from dependencies
5. Determine architecture patterns (monolith, microservices, serverless)
6. Generate appropriate Mermaid diagrams
7. Load configured architecture template
8. Populate template with discovered architecture
9. Create or update `docs/architecture.md`
10. Report completion with component count

## Detected Architectures

### Monolithic
- Single deployment unit
- Shared database
- Layered architecture

### Microservices
- Multiple services
- Service discovery
- API gateway pattern

### Serverless
- Function-as-a-Service
- Event-driven
- Managed services

### Jamstack
- Static frontend
- API backend
- CDN delivery

## When to Run

Run this command when:
- New major components added
- Architecture has evolved
- Need to onboard new team members
- Preparing architecture review
- Documenting system for stakeholders

---

**Template Location**: `.cursor/cursor-init/templates/architecture/`
**Configuration File**: `.cursor-init.yaml` (optional)
**Output File**: `docs/architecture.md`
