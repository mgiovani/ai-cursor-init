import os
import re

def _parse_sqlalchemy_models(project_root: str) -> dict:
    """
    Parses SQLAlchemy models to extract table and relationship information.
    This is a simplified implementation. A robust solution would involve
    more sophisticated AST parsing or using libraries like `eralchemy`.
    """
    tables = {}
    relationships = []

    for root, _, files in os.walk(project_root):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", errors="ignore") as f:
                        content = f.read()

                    # Check if file contains SQLAlchemy imports
                    if not any(keyword in content for keyword in ["from sqlalchemy", "import sqlalchemy", "declarative_base", "Base"]):
                        continue

                    # Look for classes that inherit from Base or have __tablename__
                    class_pattern = r"class\s+(\w+)\s*\([^)]*Base[^)]*\)\s*:(.*?)(?=\nclass|\Z)"
                    class_matches = re.findall(class_pattern, content, re.DOTALL)
                    
                    # Also look for classes with __tablename__ attribute
                    tablename_pattern = r"class\s+(\w+)\s*\([^)]*\)\s*:(.*?__tablename__\s*=\s*['\"](\w+)['\"].*?)(?=\nclass|\Z)"
                    tablename_matches = re.findall(tablename_pattern, content, re.DOTALL)
                    
                    all_matches = []
                    for class_name, class_content in class_matches:
                        # Extract table name from __tablename__ or use class name
                        tablename_match = re.search(r"__tablename__\s*=\s*['\"](\w+)['\"]", class_content)
                        table_name = tablename_match.group(1) if tablename_match else class_name.lower()
                        all_matches.append((class_name, class_content, table_name))
                    
                    for class_name, class_content, table_name in tablename_matches:
                        if not any(match[0] == class_name for match in all_matches):
                            all_matches.append((class_name, class_content, table_name))

                    for class_name, class_content, table_name in all_matches:
                        tables[table_name] = {"columns": [], "pk": [], "fk": []}

                        # Extract columns (looks for ' = Column(')
                        # Improved regex to handle nested parentheses properly
                        column_pattern = r"(\w+)\s*=\s*Column\(((?:[^()]|\([^()]*\))*)\)"
                        column_matches = re.findall(column_pattern, class_content)
                        for col_name, col_args in column_matches:
                            col_type = "string"  # Default type
                            if "Integer" in col_args: 
                                col_type = "int"
                            elif "String" in col_args: 
                                col_type = "string"
                            elif "Boolean" in col_args: 
                                col_type = "bool"
                            elif "DateTime" in col_args: 
                                col_type = "datetime"

                            tables[table_name]["columns"].append(f"{col_name} {col_type}")

                            if "primary_key=True" in col_args:
                                tables[table_name]["pk"].append(col_name)

                            # Basic foreign key detection
                            if "ForeignKey(" in col_args:
                                fk_match = re.search(r"ForeignKey\(['\"](\w+)\.(\w+)['\"]\)", col_args)
                                if fk_match:
                                    target_table = fk_match.group(1)
                                    relationships.append(f"{table_name} ||--o{{ {target_table} : references")

                except Exception as e:
                    # For debugging, you might want to print the error
                    pass
    
    return {"tables": tables, "relationships": relationships}

def _analyze_project_structure(project_root: str = ".") -> dict:
    """
    Analyzes the project structure to identify main components and their relationships.
    """
    components = {}
    
    # Get top-level directories, excluding hidden and common non-component dirs
    exclude_dirs = {'.git', '.github', '__pycache__', '.pytest_cache', 'node_modules', '.venv', 'venv', '.DS_Store'}
    
    try:
        items = os.listdir(project_root)
        for item in items:
            item_path = os.path.join(project_root, item)
            if os.path.isdir(item_path) and item not in exclude_dirs and not item.startswith('.'):
                components[item] = _classify_component(item, item_path)
    except Exception:
        pass
    
    return components

def _classify_component(dir_name: str, dir_path: str) -> dict:
    """
    Classifies a directory component based on its name and contents.
    """
    component_type = "module"
    description = ""
    
    # Classify based on directory name patterns
    if dir_name in ['docs', 'documentation']:
        component_type = "documentation"
        description = "Project documentation"
    elif dir_name in ['cli', 'cmd', 'commands']:
        component_type = "cli"
        description = "Command-line interface"
    elif dir_name in ['templates', 'template']:
        component_type = "templates"
        description = "Template files"
    elif dir_name in ['src', 'source']:
        component_type = "source"
        description = "Source code"
    elif dir_name in ['tests', 'test']:
        component_type = "tests"
        description = "Test files"
    elif dir_name in ['config', 'configuration']:
        component_type = "config"
        description = "Configuration"
    elif dir_name in ['api', 'apis']:
        component_type = "api"
        description = "API layer"
    elif dir_name in ['frontend', 'ui', 'web']:
        component_type = "frontend"
        description = "Frontend/UI"
    elif dir_name in ['backend', 'server']:
        component_type = "backend"
        description = "Backend services"
    elif dir_name in ['database', 'db', 'models']:
        component_type = "database"
        description = "Database layer"
    else:
        # Try to infer from contents
        try:
            files = os.listdir(dir_path)
            if any(f.endswith('.py') for f in files):
                component_type = "python_module"
                description = f"Python module ({dir_name})"
            elif any(f.endswith(('.js', '.ts', '.jsx', '.tsx')) for f in files):
                component_type = "js_module"
                description = f"JavaScript/TypeScript module ({dir_name})"
            elif any(f.endswith('.md') for f in files):
                component_type = "documentation"
                description = f"Documentation ({dir_name})"
            else:
                description = f"Project component ({dir_name})"
        except Exception:
            description = f"Project component ({dir_name})"
    
    return {"type": component_type, "description": description}

def generate_architecture_diagram(project_root: str = ".") -> str:
    """
    Generates a Mermaid architecture diagram based on the project's top-level structure.

    Args:
        project_root: The root directory of the project.

    Returns:
        A string containing the Mermaid architecture diagram.
    """
    components = _analyze_project_structure(project_root)
    
    mermaid_diagram = "```mermaid\ngraph TD\n"
    
    if not components:
        mermaid_diagram += "    %% No major components detected.\n"
        mermaid_diagram += "    %% Add your architecture components here\n"
        mermaid_diagram += "    %% Example:\n"
        mermaid_diagram += "    %%   Frontend[\"Frontend (React)\"]\n"
        mermaid_diagram += "    %%   Backend[\"Backend (FastAPI)\"]\n"
        mermaid_diagram += "    %%   Database[\"Database (PostgreSQL)\"]\n"
        mermaid_diagram += "    %%   Frontend --> Backend\n"
        mermaid_diagram += "    %%   Backend --> Database\n"
    else:
        # Add nodes for each component
        for comp_name, comp_info in components.items():
            safe_name = comp_name.replace('-', '_').replace('.', '_')
            description = comp_info['description']
            mermaid_diagram += f"    {safe_name}[\"{description}\"]\n"
        
        # Add basic relationships based on common patterns
        comp_names = list(components.keys())
        safe_names = {name: name.replace('-', '_').replace('.', '_') for name in comp_names}
        
        # Common architectural patterns
        if 'frontend' in comp_names and 'backend' in comp_names:
            mermaid_diagram += f"    {safe_names['frontend']} --> {safe_names['backend']}\n"
        
        if 'cli' in comp_names and any(name in comp_names for name in ['src', 'backend']):
            target = 'src' if 'src' in comp_names else 'backend'
            mermaid_diagram += f"    {safe_names['cli']} --> {safe_names[target]}\n"
        
        if any(name in comp_names for name in ['backend', 'src']) and any(name in comp_names for name in ['database', 'models']):
            source = 'backend' if 'backend' in comp_names else 'src'
            target = 'database' if 'database' in comp_names else 'models'
            mermaid_diagram += f"    {safe_names[source]} --> {safe_names[target]}\n"
        
        if 'docs' in comp_names and 'templates' in comp_names:
            mermaid_diagram += f"    {safe_names['templates']} --> {safe_names['docs']}\n"
    
    mermaid_diagram += "```\n"
    
    return mermaid_diagram

def generate_er_diagram(project_root: str = ".") -> str:
    """
    Generates a Mermaid ER diagram from SQLAlchemy models found in the project.

    Args:
        project_root: The root directory of the project.

    Returns:
        A string containing the Mermaid ER diagram, wrapped in a markdown code block.
    """
    er_data = _parse_sqlalchemy_models(project_root)
    tables = er_data["tables"]
    relationships = er_data["relationships"]

    # Create the complete markdown content with title
    markdown_content = "# Project Data Model\n\n"
    markdown_content += "This document contains the Entity Relationship Diagram (ERD) for the project's data model.\n\n"
    
    mermaid_diagram = "```mermaid\nerDiagram\n"

    if not tables and not relationships:
        mermaid_diagram += "    %% No SQLAlchemy models or relationships detected.\n"
        mermaid_diagram += "    %% Add your entities and relationships here\n"
        mermaid_diagram += "    %% Example:\n"
        mermaid_diagram += "    %%   USER {\n"
        mermaid_diagram += "    %%       id int PK\n"
        mermaid_diagram += "    %%       name string\n"
        mermaid_diagram += "    %%       email string\n"
        mermaid_diagram += "    %%   }\n"
        mermaid_diagram += "    %%   ORDER {\n"
        mermaid_diagram += "    %%       id int PK\n"
        mermaid_diagram += "    %%       user_id int FK\n"
        mermaid_diagram += "    %%       total decimal\n"
        mermaid_diagram += "    %%   }\n"
        mermaid_diagram += "    %%   USER ||--o{ ORDER : places\n"
    else:
        for table_name, details in tables.items():
            mermaid_diagram += f"    {table_name} {{\n"
            for col in details["columns"]:
                # Add PK notation for primary keys
                if any(pk in col for pk in details["pk"]):
                    col_parts = col.split()
                    if len(col_parts) >= 2:
                        mermaid_diagram += f"        {col_parts[0]} {col_parts[1]} PK\n"
                    else:
                        mermaid_diagram += f"        {col} PK\n"
                else:
                    mermaid_diagram += f"        {col}\n"
            mermaid_diagram += f"    }}\n"

        for rel in relationships:
            mermaid_diagram += f"    {rel}\n"

    mermaid_diagram += "```\n"
    
    # Combine title and diagram
    full_content = markdown_content + mermaid_diagram

    # Write to docs/data-model.md
    docs_dir = "docs"
    os.makedirs(docs_dir, exist_ok=True)
    data_model_path = os.path.join(docs_dir, "data-model.md")
    with open(data_model_path, "w") as f:
        f.write(full_content)

    return f"Successfully generated ER diagram in {data_model_path}" 