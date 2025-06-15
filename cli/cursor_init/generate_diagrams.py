import os
import re
from .ai_service import get_default_ai_service, DocumentationGenerator
from rich.console import Console

console = Console()

# Keep the legacy parsing functions for backward compatibility but they won't be used
def _parse_sqlalchemy_models(project_root: str) -> dict:
    """Legacy function - kept for backward compatibility but not used in AI-powered generation."""
    return {"tables": {}, "relationships": []}

def _analyze_project_structure(project_root: str = ".") -> dict:
    """Legacy function - kept for backward compatibility but not used in AI-powered generation."""
    return {}

def _classify_component(dir_name: str, dir_path: str) -> dict:
    """Legacy function - kept for backward compatibility but not used in AI-powered generation."""
    return {"type": "module", "description": ""}

def _analyze_database_models_comprehensive(project_root: str) -> str:
    """
    Comprehensive analysis of database models in the project.
    """
    from pathlib import Path
    
    root_path = Path(project_root)
    model_analysis = []
    
    # Look for database model files with expanded patterns
    model_patterns = [
        '**/*model*.py',      # Python models
        '**/*schema*.py',     # Schema files
        '**/*entity*.py',     # Entity files
        '**/*table*.py',      # Table files
        '**/*models*.ts',     # TypeScript models
        '**/*schema*.ts',     # TypeScript schema
        '**/*entity*.ts',     # TypeScript entities
        '**/migration*.py',   # Migration files
        '**/migration*.sql',  # SQL migrations
        '**/*.sql',          # SQL files
    ]
    
    for pattern in model_patterns:
        for file_path in root_path.glob(pattern):
            if file_path.is_file():
                try:
                    content = file_path.read_text(encoding='utf-8')
                    
                    # Check for database-related keywords
                    db_keywords = [
                        'sqlalchemy', 'django.db', 'model', 'table', 'column', 
                        'primarykey', 'foreignkey', 'relationship', 'backref',
                        'create table', 'alter table', 'schema', 'entity',
                        'sequelize', 'typeorm', 'prisma', 'knex'
                    ]
                    
                    if any(keyword in content.lower() for keyword in db_keywords):
                        # Include more context for better AI analysis
                        model_analysis.append(f'''
## {file_path.name}
**Path:** {file_path.relative_to(root_path)}
**Size:** {len(content)} characters

```{file_path.suffix[1:] if file_path.suffix else 'text'}
{content[:2000]}{"..." if len(content) > 2000 else ""}
```
''')
                except Exception:
                    continue
    
    if model_analysis:
        return '\n'.join(model_analysis)
    else:
        return '''No database models found in the project. This analysis searched for:
- SQLAlchemy models (Python)
- Django models (Python)
- TypeORM entities (TypeScript)
- Sequelize models (JavaScript/TypeScript)
- Prisma schema files
- SQL migration files
- Schema definition files

The project appears to not have explicit database schema definitions, or they may be in a format not covered by this analysis.'''

def generate_architecture_diagram(project_root: str = ".") -> str:
    """
    Generates an AI-powered Mermaid architecture diagram based on the project's structure and code analysis.

    Args:
        project_root: The root directory of the project.

    Returns:
        A string containing the result message.
    """
    try:
        console.print('[cyan]Analyzing project structure with AI...[/cyan]')
        
        # Initialize AI service
        ai_service = get_default_ai_service()
        doc_generator = DocumentationGenerator(ai_service)
        
        # Get comprehensive project analysis
        cursor_rules = doc_generator._read_cursor_rules(project_root)
        project_structure = doc_generator._analyze_project_structure(project_root)
        
        system_prompt = '''You are an expert system architect. Generate a comprehensive Mermaid architecture diagram that visualizes the system's components and their relationships.

Your output should be a complete markdown document with:
1. A title and description
2. A properly formatted Mermaid diagram using `graph TD` syntax
3. Meaningful component names and relationships
4. Proper Mermaid syntax (avoid special characters, use quotes for labels)

Focus on the actual architecture revealed by the project structure, dependencies, and code organization.'''

        user_prompt = f'''Generate an architecture diagram for this project:

## Cursor Rules Context:
{cursor_rules}

## Project Analysis:
{str(project_structure)}

Create a comprehensive architecture diagram that shows:
- Main system components
- Data flow between components
- External dependencies
- Technology stack relationships

Use proper Mermaid syntax and make it visually clear and informative.'''

        # Generate AI-powered diagram
        diagram_content = doc_generator.ai_service.generate_completion(user_prompt, system_prompt)
        
        # Save to docs/architecture.md or update existing file
        docs_dir = "docs"
        os.makedirs(docs_dir, exist_ok=True)
        arch_file = os.path.join(docs_dir, "architecture.md")
        
        # If architecture.md exists, append the diagram section
        if os.path.exists(arch_file):
            with open(arch_file, 'r') as f:
                existing_content = f.read()
            
            # Check if it already has a diagram section
            if '## Architecture Diagram' not in existing_content and '```mermaid' not in existing_content:
                # Append the diagram
                updated_content = existing_content + '\n\n## Architecture Diagram\n\n' + diagram_content
                with open(arch_file, 'w') as f:
                    f.write(updated_content)
                return f"Successfully added architecture diagram to existing {arch_file}"
            else:
                # Replace existing diagram section
                # Replace from ## Architecture Diagram to the end or next ## section
                pattern = r'(## Architecture Diagram.*?)(?=\n## |\Z)'
                if re.search(pattern, existing_content, re.DOTALL):
                    updated_content = re.sub(pattern, f'## Architecture Diagram\n\n{diagram_content}', existing_content, flags=re.DOTALL)
                else:
                    # Replace mermaid diagram
                    pattern = r'```mermaid.*?```'
                    if re.search(pattern, existing_content, re.DOTALL):
                        updated_content = re.sub(pattern, diagram_content, existing_content, flags=re.DOTALL)
                    else:
                        updated_content = existing_content + '\n\n## Architecture Diagram\n\n' + diagram_content
                
                with open(arch_file, 'w') as f:
                    f.write(updated_content)
                return f"Successfully updated architecture diagram in {arch_file}"
        else:
            # Create new file with full architecture documentation
            full_content = doc_generator.generate_architecture_docs(project_root)
            with open(arch_file, 'w') as f:
                f.write(full_content)
            return f"Successfully generated architecture documentation with diagram in {arch_file}"
            
    except Exception as e:
        error_msg = f"AI-powered architecture diagram generation failed: {str(e)}"
        console.print(f"[red]✗[/red] {error_msg}")
        return error_msg

def generate_er_diagram(project_root: str = ".") -> str:
    """
    Generates an AI-powered Mermaid ER diagram by analyzing the project's database models and schema.

    Args:
        project_root: The root directory of the project.

    Returns:
        A string containing the result message.
    """
    try:
        console.print('[cyan]Analyzing database models with AI...[/cyan]')
        
        # Initialize AI service
        ai_service = get_default_ai_service()
        doc_generator = DocumentationGenerator(ai_service)
        
        # Get comprehensive project analysis
        cursor_rules = doc_generator._read_cursor_rules(project_root)
        project_structure = doc_generator._analyze_project_structure(project_root)
        
        # Analyze database models more thoroughly
        model_analysis = _analyze_database_models_comprehensive(project_root)
        
        system_prompt = '''You are an expert database architect. Generate a comprehensive Mermaid ER diagram that visualizes the database schema and entity relationships.

Your output should be a complete markdown document with:
1. A title and overview of the data model
2. A properly formatted Mermaid ER diagram using `erDiagram` syntax
3. Proper entity definitions with attributes and types
4. Relationship definitions with cardinality
5. Key constraints (PK, FK) clearly marked

Focus on the actual database schema revealed by the code analysis.'''

        user_prompt = f'''Generate an ER diagram for this project's database:

## Cursor Rules Context:
{cursor_rules}

## Project Analysis:
{str(project_structure)}

## Database Models Analysis:
{model_analysis}

Create a comprehensive ER diagram that shows:
- All entities/tables with their attributes
- Primary keys and foreign keys
- Relationships between entities with proper cardinality
- Data types for each attribute

Use proper Mermaid ER diagram syntax.'''

        # Generate AI-powered ER diagram
        diagram_content = doc_generator.ai_service.generate_completion(user_prompt, system_prompt)
        
        # Save to docs/data-model.md
        docs_dir = "docs"
        os.makedirs(docs_dir, exist_ok=True)
        data_model_path = os.path.join(docs_dir, "data-model.md")
        
        with open(data_model_path, 'w') as f:
            f.write(diagram_content)
        
        return f"Successfully generated AI-powered ER diagram in {data_model_path}"
        
    except Exception as e:
        error_msg = f"AI-powered ER diagram generation failed: {str(e)}"
        console.print(f"[red]✗[/red] {error_msg}")
        return error_msg 