# Generate ER Diagram

Generate entity-relationship diagrams from database models found in your project.

## What This Does

Creates a comprehensive ER diagram by analyzing database model definitions in your codebase:

1. **Configuration Check**: Reads `.cursor-init.yaml` to verify if `documentation.data.data_model` is explicitly disabled
2. **Scan for Models**: Searches codebase for database model definitions:
   - SQLAlchemy models (Python)
   - TypeORM/Prisma models (TypeScript/JavaScript)
   - Django models (Python)
   - ActiveRecord models (Ruby)
   - Other ORMs detected automatically
3. **Extract Schema**: Analyzes models to extract:
   - Table names and corresponding classes
   - Column names, data types, and constraints
   - Primary key relationships
   - Foreign key relationships between tables
   - Indexes and unique constraints
4. **Template Selection**: Uses configured data_model template variant (simple or comprehensive)
5. **Generate Mermaid Diagram**: Creates valid Mermaid `erDiagram` with proper syntax
6. **Save Documentation**: Stores diagram in `docs/data-model.md` using selected template

## Supported ORMs

### Python
- SQLAlchemy (declarative, classical mapping)
- Django ORM
- Tortoise ORM
- SQLModel
- Peewee

### JavaScript/TypeScript
- TypeORM
- Prisma
- Sequelize
- Mongoose (MongoDB)

### Ruby
- ActiveRecord (Rails)

### Other Languages
- GORM (Go)
- Entity Framework (C#)
- Hibernate (Java)

## Usage

Basic generation:
```
/gen-er-diagram
```

With specific focus:
```
/gen-er-diagram for user and order tables
```

## Template Variants

Configure via `.cursor-init.yaml`:

```yaml
templates:
  data_model: "comprehensive"  # Options: simple, comprehensive
```

### Simple Template
- Mermaid ER diagram only
- Basic table and relationship visualization
- Minimal explanatory text

### Comprehensive Template (Default)
- Detailed ER diagram
- Table descriptions
- Column documentation
- Relationship explanations
- Index and constraint details
- Database operations guide

## Configuration

Disable if not needed:
```yaml
documentation:
  data:
    data_model: false  # Disables ER diagram generation
```

## Example Output

```markdown
# Data Model

## Overview

This document describes the database schema for the project.

## Entity Relationship Diagram

\`\`\`mermaid
erDiagram
    User ||--o{ Order : places
    User {
        int id PK
        string email UK
        string name
        datetime created_at
    }
    Order ||--|{ OrderItem : contains
    Order {
        int id PK
        int user_id FK
        string status
        decimal total
        datetime created_at
    }
    OrderItem }o--|| Product : references
    OrderItem {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }
    Product {
        int id PK
        string name
        string sku UK
        decimal price
        int stock
    }
\`\`\`

## Table Descriptions

### User
Stores user account information and authentication data.

**Indexes:**
- `email` (unique)
- `created_at`

### Order
Represents customer orders with status tracking.

**Foreign Keys:**
- `user_id` references `User(id)` ON DELETE CASCADE

### OrderItem
Individual line items within an order.

**Foreign Keys:**
- `order_id` references `Order(id)` ON DELETE CASCADE
- `product_id` references `Product(id)` ON DELETE RESTRICT

### Product
Product catalog with inventory tracking.

**Indexes:**
- `sku` (unique)
- `name` (full-text search)
```

## Process

I will:
1. Check `.cursor-init.yaml` for data_model documentation setting
2. If disabled, inform you and skip generation
3. Search codebase for database model files (models.py, entities/, etc.)
4. Parse model definitions to extract schema information
5. Identify relationships between tables
6. Generate Mermaid ER diagram syntax
7. Load data_model template (simple or comprehensive)
8. Replace placeholders with extracted schema information
9. Create or update `docs/data-model.md`
10. Report completion with diagram statistics

## When to Run

Run this command when:
- Database schema has been modified
- New models have been added
- Relationships have changed
- You need to refresh the ER diagram
- Starting documentation for an existing project

## Proactive Suggestion

The proactive documentation rule will automatically suggest running this command when it detects changes to database model files.

---

**Template Location**: `.cursor/cursor-init/templates/diagrams/`
**Configuration File**: `.cursor-init.yaml` (optional)
**Output File**: `docs/data-model.md`
