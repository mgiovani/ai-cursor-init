# {{PROJECT_NAME}} - Data Model Documentation

**Last Updated:** {{DATE}}  
**Version:** {{VERSION}}  
**Maintainer:** {{MAINTAINER}}

## Overview

{{OVERVIEW}}

This document describes the core data model and entity relationships for {{PROJECT_NAME}}.

## Database Information

| Property | Value |
|----------|-------|
| **Database Type** | {{DATABASE_TYPE}} |
| **Version** | {{DATABASE_VERSION}} |
| **Schema Version** | {{SCHEMA_VERSION}} |
| **Last Migration** | {{LAST_MIGRATION}} |

## Entity Relationship Diagram

```mermaid
erDiagram
{{ER_DIAGRAM_CONTENT}}
```

## Entity Definitions

### {{ENTITY_1}}

{{ENTITY_1_DESCRIPTION}}

#### Attributes

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| {{ENTITY_1_ATTR_1}} | {{TYPE_1}} | {{CONSTRAINTS_1}} | {{DESC_1}} |
| {{ENTITY_1_ATTR_2}} | {{TYPE_2}} | {{CONSTRAINTS_2}} | {{DESC_2}} |
| {{ENTITY_1_ATTR_3}} | {{TYPE_3}} | {{CONSTRAINTS_3}} | {{DESC_3}} |

#### Relationships

- {{RELATIONSHIP_1}}
- {{RELATIONSHIP_2}}

#### Business Rules

- {{BUSINESS_RULE_1}}
- {{BUSINESS_RULE_2}}

### {{ENTITY_2}}

{{ENTITY_2_DESCRIPTION}}

#### Attributes

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| {{ENTITY_2_ATTR_1}} | {{TYPE_1}} | {{CONSTRAINTS_1}} | {{DESC_1}} |
| {{ENTITY_2_ATTR_2}} | {{TYPE_2}} | {{CONSTRAINTS_2}} | {{DESC_2}} |
| {{ENTITY_2_ATTR_3}} | {{TYPE_3}} | {{CONSTRAINTS_3}} | {{DESC_3}} |

#### Relationships

- {{RELATIONSHIP_1}}
- {{RELATIONSHIP_2}}

#### Business Rules

- {{BUSINESS_RULE_1}}
- {{BUSINESS_RULE_2}}

## Domain Models

### {{DOMAIN_1}}

{{DOMAIN_1_DESCRIPTION}}

**Entities:** {{DOMAIN_1_ENTITIES}}  
**Key Relationships:** {{DOMAIN_1_RELATIONSHIPS}}

### {{DOMAIN_2}}

{{DOMAIN_2_DESCRIPTION}}

**Entities:** {{DOMAIN_2_ENTITIES}}  
**Key Relationships:** {{DOMAIN_2_RELATIONSHIPS}}

## Data Types

### Custom Types

| Type | Definition | Usage |
|------|------------|-------|
| {{CUSTOM_TYPE_1}} | {{DEFINITION_1}} | {{USAGE_1}} |
| {{CUSTOM_TYPE_2}} | {{DEFINITION_2}} | {{USAGE_2}} |

### Enumerations

```sql
{{ENUMS}}
```

## Key Constraints

### Primary Keys

| Table | Primary Key | Type |
|-------|-------------|------|
| {{TABLE_1}} | {{PK_1}} | {{PK_TYPE_1}} |
| {{TABLE_2}} | {{PK_2}} | {{PK_TYPE_2}} |

### Foreign Keys

| Child Table | Foreign Key | Parent Table | Parent Key | On Delete | On Update |
|-------------|-------------|--------------|------------|-----------|-----------|
| {{CHILD_1}} | {{FK_1}} | {{PARENT_1}} | {{PK_1}} | {{DELETE_1}} | {{UPDATE_1}} |
| {{CHILD_2}} | {{FK_2}} | {{PARENT_2}} | {{PK_2}} | {{DELETE_2}} | {{UPDATE_2}} |

### Unique Constraints

| Table | Columns | Description |
|-------|---------|-------------|
| {{TABLE_1}} | {{COLUMNS_1}} | {{UNIQUE_DESC_1}} |
| {{TABLE_2}} | {{COLUMNS_2}} | {{UNIQUE_DESC_2}} |

## Related Documentation

- [Database Operations](database-operations.md) - Performance, migrations, and troubleshooting
- [Data Security](data-security.md) - Security policies and access control
- [Architecture Overview](architecture.md) - System design and component relationships

## Notes

{{ADDITIONAL_NOTES}}

---

*This diagram was generated from database models. Update the models and regenerate to keep this documentation current.*
