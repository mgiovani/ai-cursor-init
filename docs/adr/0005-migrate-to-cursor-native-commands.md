# ADR-0005: Migrate to Cursor Native Commands

## Status

Accepted

## Context

The AI-Cursor-Init framework was initially built using Cursor's MDC (Markdown with frontmatter) format in `.cursor/rules/` directory. In September 2025, Cursor released version 1.6 with native support for custom slash commands stored as plain Markdown files in `.cursor/commands/`. This created an opportunity to adopt the official command system while maintaining our framework's capabilities.

### Previous Architecture

**MDC-Based Rules (21 files):**
- All slash commands defined as `.mdc` files in `.cursor/rules/cursor-init/`
- Used frontmatter for metadata (`description`, `globs`, `alwaysApply`)
- Mixed user-invoked commands with always-on context rules
- Templates stored in `.cursor/templates/`
- Heavy reliance on custom MDC format

### Cursor Native Commands

**Official Command System:**
- Plain Markdown files in `.cursor/commands/`
- No frontmatter required
- Appears in `/` autocomplete automatically
- Better integration with Cursor's AI
- Simpler, more maintainable format
- Active development and improvements by Cursor team

### Key Challenge

We needed to distinguish between:
1. **User-invoked commands** - Explicit actions users trigger (e.g., `/init-docs`, `/adr`)
2. **Always-on rules** - Proactive guidance and context (e.g., suggesting updates after changes)

## Decision

We will adopt a **two-tier architecture** that leverages both Cursor commands and rules appropriately:

### Tier 1: User-Invoked Commands (`.cursor/commands/cursor-init/`)

Migrate 16 MDC files to plain Markdown commands:

**Documentation Management (6 commands):**
- `init-docs.md`
- `update-docs.md`
- `sync-docs.md`
- `sync-doc.md`
- `sync-category.md`
- `check-docs.md`

**Creation Commands (2 commands):**
- `adr.md`
- `rfc.md`

**Diagram Generation (6 commands):**
- `gen-er-diagram.md`
- `gen-arch-diagram.md`
- `gen-dependency-diagram.md`
- `gen-deployment-diagram.md`
- `gen-onboarding-diagram.md`
- `gen-security-diagram.md`

**Template Management (2 commands):**
- `list-templates.md`
- `add-template.md`

### Tier 2: Always-On Rules (`.cursor/rules/cursor-init/`)

Keep 5 MDC files as rules for proactive guidance:

**Context Rules:**
- `context/docs-context.mdc` - Explains framework capabilities
- `context/adr-context.mdc` - Provides ADR context
- `context/architecture-context.mdc` - Provides architecture context

**Quality Rules:**
- `quality/code-quality.mdc` - General code quality guidelines

**Proactive Rules:**
- `proactive/proactive-doc-suggest.mdc` - Suggests updates after code changes

### Additional Changes

1. **Template relocation**: Move from `.cursor/templates/` to `.cursor/cursor-init/templates/`
2. **Hybrid configuration**: Keep `.cursor-init.yaml` for defaults, support command parameters for overrides
3. **Plain Markdown format**: Remove all MDC frontmatter from commands
4. **Scoped directory**: All commands under `cursor-init/` subdirectory for organization

## Rationale

### Why Native Commands for User Actions?

1. **Official Support**: Cursor actively maintains and improves the command system
2. **Better UX**: Commands appear in `/` autocomplete automatically
3. **Simpler Format**: Plain Markdown is easier to write and maintain
4. **Future-Proof**: Aligned with Cursor's roadmap
5. **Performance**: Native commands are optimized by Cursor
6. **Discoverability**: Users can easily see all available commands

### Why Keep Rules for Proactive Guidance?

1. **Always-On Behavior**: Rules with `alwaysApply: true` monitor for changes
2. **Context Injection**: Rules provide framework context without explicit invocation
3. **Proactive Suggestions**: Detect code changes and suggest relevant documentation updates
4. **Background Operations**: Monitor state and suggest actions at appropriate times
5. **Separation of Concerns**: Clear distinction between user actions and system guidance

### Why Hybrid Configuration?

1. **Project Defaults**: `.cursor-init.yaml` provides consistent project-wide settings
2. **Per-Command Flexibility**: Parameters allow one-off overrides (e.g., `/adr lightweight "Title"`)
3. **Backward Compatibility**: Existing configurations continue to work
4. **Best of Both Worlds**: Configuration for consistency, parameters for flexibility

## Consequences

### Positive

✅ **Better Integration**: Native Cursor commands with official support
✅ **Improved UX**: Commands in `/` autocomplete menu
✅ **Clearer Architecture**: Separation between commands and rules
✅ **Easier Maintenance**: Plain Markdown is simpler than MDC
✅ **Proactive Guidance**: Rules automatically suggest updates after changes
✅ **Future-Proof**: Aligned with Cursor's development direction
✅ **Reduced Complexity**: Fewer files in rules directory (5 vs 21)
✅ **Better Organization**: Scoped under `cursor-init/` subdirectory
✅ **Flexibility**: Template override via parameters

### Negative

❌ **Two Systems**: Must understand both commands and rules
❌ **Migration Effort**: Requires converting 16 MDC files to Markdown
❌ **Documentation Updates**: README, CLAUDE.md, examples need updates
❌ **User Education**: Users need to learn new command locations

### Neutral

- MDC frontmatter removed (description, globs, alwaysApply)
- Templates moved to `.cursor/cursor-init/templates/`
- Commands scoped under `cursor-init/` subdirectory
- Proactive rule behavior remains unchanged

## Implementation

### Phase 1: Directory Restructure

```bash
# Create new directory structure
mkdir -p .cursor/commands/cursor-init
mkdir -p .cursor/cursor-init/templates

# Reorganize rules
mkdir -p .cursor/rules/cursor-init/{context,quality,proactive}
mv .cursor/rules/cursor-init/documentation/proactive-doc-suggest.mdc \
   .cursor/rules/cursor-init/proactive/
```

### Phase 2: Template Migration

```bash
# Move templates to new location
cp -r .cursor/templates/* .cursor/cursor-init/templates/
```

### Phase 3: Command Conversion

Convert 16 MDC files to plain Markdown commands:
- Remove frontmatter
- Format as clear instructional Markdown
- Add usage examples
- Document configuration integration
- Include parameter override examples

### Phase 4: Documentation Updates

Update all references to new structure:
- Update `docs-context.mdc` with new command list
- Create this ADR (0005)
- Update README.md
- Update CLAUDE.md
- Update docs/architecture.md

### Phase 5: Testing

Test each command and rule:
- Verify commands appear in `/` menu
- Test command execution
- Validate template loading
- Confirm proactive rules trigger correctly
- Check YAML configuration integration

## Migration Path

### For Users

1. **Slash commands remain the same**: `/init-docs`, `/adr "Title"`, etc. work identically
2. **Configuration unchanged**: `.cursor-init.yaml` continues to work
3. **New feature**: Can override templates per-command (e.g., `/adr full "Title"`)
4. **Proactive suggestions**: Now automatically suggested after code changes

### For Contributors

1. **New commands**: Add to `.cursor/commands/cursor-init/` as plain Markdown
2. **Rules**: Add to `.cursor/rules/cursor-init/` subdirectories for always-on behavior
3. **Templates**: Add to `.cursor/cursor-init/templates/` with variant naming
4. **No MDC**: Use plain Markdown for commands

## Alternatives Considered

### Alternative 1: Stay with MDC Rules

**Pros:**
- No migration effort required
- Existing system works
- Familiar to current users

**Cons:**
- Not leveraging official Cursor commands
- Missing improved UX of `/` autocomplete
- Not aligned with Cursor's roadmap
- Mixing concerns (commands + context)

**Decision:** Rejected. Native commands provide better UX and future-proofing.

### Alternative 2: Convert Everything to Commands

**Pros:**
- Single system (commands only)
- Maximum simplicity
- All slash commands

**Cons:**
- Lose proactive guidance capability
- No way to provide always-on context
- Can't automatically suggest updates
- Manual invocation required for all features

**Decision:** Rejected. Proactive documentation suggestions are valuable.

### Alternative 3: Pure Configuration (No YAML)

**Pros:**
- Simpler (no configuration file)
- All settings via parameters
- Fewer files to manage

**Cons:**
- No project-wide defaults
- Repetitive parameter passing
- Team inconsistency
- Loss of existing configurations

**Decision:** Rejected. Hybrid approach balances flexibility and consistency.

## Related Decisions

- **ADR-0001**: Record Architecture Decisions (established ADR practice)
- **ADR-0002**: Adopt AI-Powered Documentation Generation (core framework principle)
- **ADR-0003**: Test AI-Generated ADR (template testing)
- **ADR-0004**: Remove CLI Interface (focus on Cursor IDE integration)

## References

- [Cursor Commands Documentation](https://cursor.com/docs/agent/chat/commands)
- [Cursor 1.6 Changelog](https://cursor.com/changelog/1-6)
- [AI-Cursor-Init Migration Plan](../architecture.md#migration-to-native-commands)

## Timeline

- **October 21, 2025**: Migration completed
- **Previous**: MDC-based rules system (June 2025 - October 2025)
- **Current**: Native commands + proactive rules hybrid architecture

---

This decision modernizes our framework architecture while preserving proactive guidance capabilities that make AI-Cursor-Init unique.
