# Create Architecture Decision Record

Create a new Architecture Decision Record (ADR) documenting an architectural decision.

## What This Does

Generates a structured ADR document following industry best practices:

1. **Configuration Check**: Verifies if `documentation.core.adr` is explicitly disabled in `.cursor-init.yaml`
2. **Extract Title**: Gets the decision title from your command (text after `/adr`)
3. **Determine Number**: Scans `docs/adr/` directory for the highest existing ADR number and increments
4. **Template Selection**: Uses configured ADR template variant (nygard_style, full, lightweight, madr)
5. **Context Gathering**: Uses codebase search to find relevant information for the ADR topic
6. **Generate ADR**: Creates numbered ADR file in `docs/adr/` with format `000X-sanitized-title.md`
7. **Populate Content**: Fills template with title, number, date, and gathered context

## Usage

Basic ADR creation:
```
/adr "Database Migration Strategy"
```

With template variant override:
```
/adr lightweight "Quick Technical Decision"
```

Additional examples:
```
/adr "API Authentication Approach"
/adr "Frontend Framework Selection"
/adr "Microservices Communication Pattern"
```

## Template Variants

Configure default variant in `.cursor-init.yaml`:

```yaml
templates:
  adr: "nygard_style"  # Options: nygard_style, full, lightweight, madr
```

### Nygard Style (Default)
Michael Nygard's ADR format - concise and focused.

**Sections:**
- Title
- Status (Proposed, Accepted, Deprecated, Superseded)
- Context
- Decision
- Consequences

### Full Template
Comprehensive ADR with detailed sections.

**Sections:**
- Title
- Status
- Context
- Decision Drivers
- Considered Options
- Decision
- Consequences (Positive, Negative, Neutral)
- Pros and Cons
- Related Decisions
- References

### Lightweight Template
Minimal ADR for quick decisions.

**Sections:**
- Title
- Status
- Decision
- Rationale

### MADR Template
Markdown Architectural Decision Records format.

**Sections:**
- Title
- Status
- Context and Problem Statement
- Decision Drivers
- Considered Options
- Decision Outcome
- Consequences

## Parameter Override

Override default template for specific ADR:

```
/adr lightweight "Use Redis for Session Storage"
/adr full "Adopt Event-Driven Architecture"
/adr madr "Select Database Technology"
```

## Example Output

File: `docs/adr/0006-use-redis-for-session-storage.md`

```markdown
# ADR-0006: Use Redis for Session Storage

**Status:** Proposed

**Context:**
Our application needs to handle user sessions across multiple server instances in a distributed environment. Currently using in-memory sessions, which doesn't work with horizontal scaling.

**Decision:**
Adopt Redis as the session storage backend for distributed session management.

**Consequences:**

**Positive:**
- Enables horizontal scaling of application servers
- Fast session read/write performance (sub-millisecond)
- Built-in expiration for session cleanup
- Widely supported by frameworks

**Negative:**
- Additional infrastructure dependency
- Requires Redis monitoring and maintenance
- Network latency for session operations

**Neutral:**
- Need to implement Redis connection pooling
- Must handle Redis failover scenarios
```

## ADR Numbering

- First ADR: `0001-record-architecture-decisions.md` (meta-ADR)
- Subsequent ADRs: Auto-incremented (0002, 0003, etc.)
- Format: `XXXX-kebab-case-title.md`

## Configuration

Disable ADR creation:
```yaml
documentation:
  core:
    adr: false  # Prevents ADR generation
```

If ADR documentation is disabled, I will inform you and skip creation.

## Process

I will:
1. Check if ADR documentation is disabled in configuration
2. Extract the decision title from your command
3. Sanitize title to kebab-case for filename
4. Check `docs/adr/` for highest number
5. Increment to get new ADR number
6. Load configured ADR template variant
7. Gather context from codebase related to the decision
8. Populate template with:
   - ADR number
   - Title
   - Current date
   - Status: "Proposed"
   - Relevant context from codebase
9. Create file in `docs/adr/000X-title.md`
10. Report creation with ADR number

## When to Create ADRs

Create an ADR when making:
- Technology stack decisions
- Architecture pattern choices
- Database or storage decisions
- API design choices
- Security architecture decisions
- Deployment strategy decisions
- Major library/framework selections

## Best Practices

- Create ADRs early in decision process
- Update status as decision progresses (Proposed → Accepted)
- Link related ADRs together
- Keep focused on one decision per ADR
- Include context even if it seems obvious

---

**Template Location**: `.cursor/cursor-init/templates/adr/`
**Configuration File**: `.cursor-init.yaml` (optional)
**Output Directory**: `docs/adr/`
