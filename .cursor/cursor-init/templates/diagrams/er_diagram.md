# {{PROJECT_NAME}} - Entity Relationship Diagram

**Last Updated:** {{DATE}}  
**Version:** {{VERSION}}  
**Generated From:** {{SOURCE_MODELS}}

## Database Overview

This document provides the entity relationship diagram for {{PROJECT_NAME}} database schema.

### Entity Relationship Diagram

```mermaid
erDiagram
    %% Example entities - replace with actual database entities
    USER {
        uuid id PK "Primary Key"
        string email UK "Unique email address"
        string password_hash "Encrypted password"
        string first_name "User first name"
        string last_name "User last name"
        timestamp created_at "Account creation date"
        timestamp updated_at "Last modification date"
        boolean is_active "Account status"
    }
    
    PROFILE {
        uuid id PK "Primary Key"
        uuid user_id FK "Reference to USER"
        string bio "User biography"
        string avatar_url "Profile picture URL"
        string phone "Phone number"
        timestamp created_at "Profile creation date"
        timestamp updated_at "Last modification date"
    }
    
    ROLE {
        uuid id PK "Primary Key"
        string name UK "Role name"
        string description "Role description"
        json permissions "Role permissions"
        timestamp created_at "Role creation date"
    }
    
    USER_ROLE {
        uuid user_id FK "Reference to USER"
        uuid role_id FK "Reference to ROLE"
        timestamp assigned_at "Role assignment date"
        uuid assigned_by FK "User who assigned role"
    }
    
    %% Relationships
    USER ||--o| PROFILE : "has profile"
    USER ||--o{ USER_ROLE : "has roles"
    ROLE ||--o{ USER_ROLE : "assigned to users"
    USER ||--o{ USER_ROLE : "assigns roles"
    
    %% Replace with actual entities and relationships:
    {{ER_DIAGRAM_CONTENT}}
```

## Entity Descriptions

### {{ENTITY_1}}

{{ENTITY_1_DESCRIPTION}}

**Primary Key:** {{ENTITY_1_PK}}  
**Table Name:** `{{ENTITY_1_TABLE}}`

#### Attributes

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| {{ATTR_1}} | {{TYPE_1}} | {{CONSTRAINTS_1}} | {{DESC_1}} |
| {{ATTR_2}} | {{TYPE_2}} | {{CONSTRAINTS_2}} | {{DESC_2}} |
| {{ATTR_3}} | {{TYPE_3}} | {{CONSTRAINTS_3}} | {{DESC_3}} |

#### Relationships

- **{{RELATIONSHIP_1}}:** {{REL_DESC_1}}
- **{{RELATIONSHIP_2}}:** {{REL_DESC_2}}

### {{ENTITY_2}}

{{ENTITY_2_DESCRIPTION}}

**Primary Key:** {{ENTITY_2_PK}}  
**Table Name:** `{{ENTITY_2_TABLE}}`

#### Attributes

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| {{ATTR_1}} | {{TYPE_1}} | {{CONSTRAINTS_1}} | {{DESC_1}} |
| {{ATTR_2}} | {{TYPE_2}} | {{CONSTRAINTS_2}} | {{DESC_2}} |
| {{ATTR_3}} | {{TYPE_3}} | {{CONSTRAINTS_3}} | {{DESC_3}} |

#### Relationships

- **{{RELATIONSHIP_1}}:** {{REL_DESC_1}}
- **{{RELATIONSHIP_2}}:** {{REL_DESC_2}}

## Relationship Details

### One-to-One Relationships

| Parent Entity | Child Entity | Foreign Key | Description |
|---------------|--------------|-------------|-------------|
| {{PARENT_1}} | {{CHILD_1}} | {{FK_1}} | {{REL_DESC_1}} |

### One-to-Many Relationships

| Parent Entity | Child Entity | Foreign Key | Description |
|---------------|--------------|-------------|-------------|
| {{PARENT_1}} | {{CHILD_1}} | {{FK_1}} | {{REL_DESC_1}} |
| {{PARENT_2}} | {{CHILD_2}} | {{FK_2}} | {{REL_DESC_2}} |

### Many-to-Many Relationships

| Entity 1 | Entity 2 | Junction Table | Description |
|----------|----------|----------------|-------------|
| {{ENTITY_1}} | {{ENTITY_2}} | {{JUNCTION_1}} | {{REL_DESC_1}} |

## Database Constraints

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

### Check Constraints

| Table | Constraint | Description |
|-------|------------|-------------|
| {{TABLE_1}} | {{CHECK_1}} | {{CHECK_DESC_1}} |
| {{TABLE_2}} | {{CHECK_2}} | {{CHECK_DESC_2}} |

## Indexes

### Performance Indexes

| Table | Index Name | Columns | Type | Purpose |
|-------|------------|---------|------|---------|
| {{TABLE_1}} | {{INDEX_1}} | {{COLUMNS_1}} | {{TYPE_1}} | {{PURPOSE_1}} |
| {{TABLE_2}} | {{INDEX_2}} | {{COLUMNS_2}} | {{TYPE_2}} | {{PURPOSE_2}} |

## Data Types Used

### Standard Types

| Type | Usage | Description |
|------|-------|-------------|
| {{TYPE_1}} | {{USAGE_1}} | {{TYPE_DESC_1}} |
| {{TYPE_2}} | {{USAGE_2}} | {{TYPE_DESC_2}} |

### Custom Types

{{CUSTOM_TYPES}}

## Business Rules

### Entity Rules

- **{{ENTITY_1}}:** {{BUSINESS_RULE_1}}
- **{{ENTITY_2}}:** {{BUSINESS_RULE_2}}

### Relationship Rules

- {{RELATIONSHIP_RULE_1}}
- {{RELATIONSHIP_RULE_2}}

## Migration Notes

### Schema Version

**Current Version:** {{SCHEMA_VERSION}}  
**Last Migration:** {{LAST_MIGRATION_DATE}}

### Migration History

| Version | Date | Description | Script |
|---------|------|-------------|--------|
| {{VERSION_1}} | {{DATE_1}} | {{MIGRATION_DESC_1}} | {{SCRIPT_1}} |
| {{VERSION_2}} | {{DATE_2}} | {{MIGRATION_DESC_2}} | {{SCRIPT_2}} |

## References

- [Database Documentation]({{DB_DOCS_LINK}})
- [ORM Models]({{ORM_DOCS_LINK}})
- [Migration Scripts]({{MIGRATION_DOCS_LINK}})

## Notes

{{ADDITIONAL_NOTES}}

---

*This diagram was generated from database models. Update the models and regenerate to keep this documentation current.*
