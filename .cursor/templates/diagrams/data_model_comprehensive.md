# {{PROJECT_NAME}} - Data Model Documentation

**Last Updated:** {{DATE}}  
**Version:** {{VERSION}}  
**Maintainer:** {{MAINTAINER}}

## Overview

{{OVERVIEW}}

This document describes the data model and database design for {{PROJECT_NAME}}.

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

#### Indexes

```sql
{{ENTITY_1_INDEXES}}
```

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

#### Indexes

```sql
{{ENTITY_2_INDEXES}}
```

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

## Constraints and Validations

### Database Constraints

```sql
{{DATABASE_CONSTRAINTS}}
```

### Application-Level Validations

{{APPLICATION_VALIDATIONS}}

## Performance Considerations

### Indexing Strategy

{{INDEXING_STRATEGY}}

### Query Optimization

{{QUERY_OPTIMIZATION}}

### Partitioning

{{PARTITIONING_STRATEGY}}

## Security and Access Control

### Data Classification

| Entity | Classification | Access Control |
|--------|----------------|----------------|
| {{ENTITY_1}} | {{CLASSIFICATION_1}} | {{ACCESS_1}} |
| {{ENTITY_2}} | {{CLASSIFICATION_2}} | {{ACCESS_2}} |

### Encryption

{{ENCRYPTION_STRATEGY}}

### Audit Trail

{{AUDIT_STRATEGY}}

## Migration and Versioning

### Migration Strategy

{{MIGRATION_STRATEGY}}

### Version History

| Version | Date | Changes | Migration Script |
|---------|------|---------|------------------|
| {{VERSION_1}} | {{DATE_1}} | {{CHANGES_1}} | {{SCRIPT_1}} |
| {{VERSION_2}} | {{DATE_2}} | {{CHANGES_2}} | {{SCRIPT_2}} |

### Rollback Procedures

{{ROLLBACK_PROCEDURES}}

## Data Lifecycle

### Data Retention

{{DATA_RETENTION_POLICY}}

### Archival Strategy

{{ARCHIVAL_STRATEGY}}

### Backup and Recovery

{{BACKUP_STRATEGY}}

## API Integration

### ORM Mapping

{{ORM_MAPPING}}

### API Endpoints

| Entity | Endpoint | Operations |
|--------|----------|------------|
| {{ENTITY_1}} | {{ENDPOINT_1}} | {{OPERATIONS_1}} |
| {{ENTITY_2}} | {{ENDPOINT_2}} | {{OPERATIONS_2}} |

## Testing Strategy

### Test Data

{{TEST_DATA_STRATEGY}}

### Database Testing

{{DATABASE_TESTING}}

### Performance Testing

{{PERFORMANCE_TESTING}}

## Monitoring and Observability

### Key Metrics

{{KEY_METRICS}}

### Alerting

{{ALERTING_STRATEGY}}

### Logging

{{LOGGING_STRATEGY}}

## Troubleshooting

### Common Issues

{{COMMON_ISSUES}}

### Diagnostic Queries

```sql
{{DIAGNOSTIC_QUERIES}}
```

## References

- [Database Documentation]({{DB_DOCS_LINK}})
- [ORM Documentation]({{ORM_DOCS_LINK}})
- [API Documentation]({{API_DOCS_LINK}})

## Appendices

### Appendix A: Full Schema DDL

```sql
{{FULL_SCHEMA_DDL}}
```

### Appendix B: Seed Data

```sql
{{SEED_DATA}}
```
