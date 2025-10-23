# Create Request For Comments

Create a new RFC (Request For Comments) document for proposing and discussing changes.

## What This Does

Generates a structured RFC document for collaborative decision-making:

1. **Configuration Check**: Verifies if `documentation.development.rfc` is explicitly disabled
2. **Extract Title**: Gets the RFC title from your command (text after `/rfc`)
3. **Determine Number**: Scans `docs/rfc/` directory for the highest existing RFC number and increments
4. **Template Selection**: Uses configured RFC template variant (minimal, standard, detailed)
5. **Context Gathering**: Analyzes codebase to understand current state related to the proposal
6. **Generate RFC**: Creates numbered RFC file in `docs/rfc/` with format `RFC-000X-sanitized-title.md`
7. **Populate Content**: Fills template with title, number, author, date, and initial content

## Usage

Basic RFC creation:
```
/rfc "Add GraphQL API Support"
```

With template variant override:
```
/rfc detailed "Migration to Microservices Architecture"
```

Additional examples:
```
/rfc "Implement Rate Limiting"
/rfc "Add Multi-Tenancy Support"
/rfc "Refactor Authentication System"
```

## Template Variants

Configure default variant in `.cursor-init.yaml`:

```yaml
templates:
  rfc: "standard"  # Options: minimal, standard, detailed
```

### Minimal Template
Quick proposal format for small changes.

**Sections:**
- Summary
- Motivation
- Proposal
- Open Questions

### Standard Template (Default)
Balanced RFC for most changes.

**Sections:**
- Summary
- Motivation
- Proposal
- Rationale and Alternatives
- Implementation Plan
- Testing Plan
- Migration Strategy
- Open Questions
- Timeline

### Detailed Template
Comprehensive RFC for major changes.

**Sections:**
- Summary
- Background and Motivation
- Goals and Non-Goals
- Proposal
- Detailed Design
- Rationale and Alternatives
- Implementation Plan
- Testing and Quality Assurance
- Migration and Rollout Strategy
- Monitoring and Metrics
- Security Considerations
- Performance Implications
- Open Questions and Risks
- Timeline and Milestones
- Appendices

## Parameter Override

Override default template for specific RFC:

```
/rfc minimal "Update Logging Format"
/rfc detailed "Adopt Event Sourcing Pattern"
```

## Example Output

File: `docs/rfc/RFC-0003-add-graphql-api-support.md`

```markdown
# RFC-0003: Add GraphQL API Support

**Author:** Developer Team
**Status:** Draft
**Created:** 2025-10-21
**Last Updated:** 2025-10-21

## Summary

Propose adding GraphQL API support alongside our existing REST API to improve frontend data fetching efficiency and reduce over-fetching.

## Motivation

Current REST API challenges:
- Multiple round trips for related data
- Over-fetching of unnecessary fields
- Under-fetching requiring additional requests
- Frontend teams requesting more flexible API

## Proposal

Implement a GraphQL API using Apollo Server that:
1. Maintains backwards compatibility with REST API
2. Provides strongly-typed schema
3. Enables efficient data fetching
4. Supports real-time subscriptions

## Rationale and Alternatives

**Why GraphQL:**
- Single request for complex data requirements
- Frontend can specify exact fields needed
- Strong typing and introspection
- Active ecosystem and tooling

**Alternatives Considered:**
1. **REST with field filtering** - Less powerful than GraphQL
2. **gRPC** - Better for service-to-service, not web clients
3. **Stay with current REST** - Doesn't solve over/under-fetching

## Implementation Plan

1. Set up Apollo Server
2. Define GraphQL schema
3. Implement resolvers for existing data
4. Add authentication middleware
5. Update frontend clients
6. Deploy behind feature flag

## Testing Plan

- Unit tests for resolvers
- Integration tests for queries
- Performance benchmarks
- Load testing

## Open Questions

- Should we deprecate some REST endpoints?
- What's the migration timeline for frontend clients?
- Do we need GraphQL caching strategy?

## Timeline

- Week 1-2: Schema design and setup
- Week 3-4: Resolver implementation
- Week 5-6: Frontend integration
- Week 7: Testing and optimization
- Week 8: Production rollout
```

## RFC Workflow

### Status Progression
1. **Draft** - Initial proposal, gathering feedback
2. **In Review** - Under discussion, modifications being made
3. **Accepted** - Approved for implementation
4. **Implemented** - Changes have been deployed
5. **Rejected** - Not moving forward with proposal
6. **Withdrawn** - Author withdrew the proposal

### Discussion Process
1. Create RFC in Draft status
2. Share with team for feedback
3. Incorporate feedback and iterate
4. Move to In Review when ready
5. Final decision by stakeholders
6. Update status to Accepted/Rejected

## Configuration

Enable/disable RFC documentation:
```yaml
documentation:
  development:
    rfc: true  # Set to false to disable
```

If RFC documentation is disabled, I will inform you and skip creation.

## Process

I will:
1. Check if RFC documentation is disabled in configuration
2. Extract the proposal title from your command
3. Sanitize title to kebab-case for filename
4. Check `docs/rfc/` for highest RFC number
5. Increment to get new RFC number
6. Load configured RFC template variant
7. Gather context from codebase related to the proposal
8. Populate template with:
   - RFC number
   - Title
   - Author (from git config if available)
   - Current date
   - Status: "Draft"
   - Initial sections with context
9. Create file in `docs/rfc/RFC-000X-title.md`
10. Report creation with RFC number

## When to Create RFCs

Create an RFC when proposing:
- Major feature additions
- Significant refactorings
- Architecture changes
- Breaking API changes
- New technology adoptions
- Process changes
- Performance optimizations with trade-offs

## Best Practices

- Write RFCs before starting implementation
- Include concrete examples
- Address potential concerns proactively
- Update RFC as you receive feedback
- Link to related ADRs or other RFCs
- Keep language clear and accessible
- Define success criteria

---

**Template Location**: `.cursor/cursor-init/templates/rfc/`
**Configuration File**: `.cursor-init.yaml` (optional)
**Output Directory**: `docs/rfc/`
