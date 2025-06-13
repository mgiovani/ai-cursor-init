import os
from .detect_framework import detect_project_frameworks
from .config import load_config

def _read_template_content(filepath: str) -> str:
    with open(filepath, 'r') as f:
        return f.read()

def initialize_docs():
    docs_dir = "docs"
    adr_dir = os.path.join(docs_dir, "adr")

    # Create docs/ and docs/adr/ directories
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(adr_dir, exist_ok=True)

    print(f"Created directory: {docs_dir}")
    print(f"Created directory: {adr_dir}")

    # Detect project languages and frameworks
    project_info = detect_project_frameworks()
    detected_languages = project_info.get("languages", set())
    detected_frameworks = project_info.get("frameworks", set())

    # Load configuration to get template preferences
    config = load_config()
    
    # Get template paths from configuration with fallbacks
    architecture_template_path = config.get_template_path('architecture') or ".cursor/templates/architecture/architecture_google.md"
    adr_template_path = config.get_template_path('adr') or ".cursor/templates/adr/adr_template_nygard.md"
    data_model_template_path = ".cursor/templates/diagrams/er_diagram.md"

    # Choose onboarding template based on configuration and detected languages
    onboarding_variant = config.get_template_variant('onboarding')
    if onboarding_variant == 'python' or "python" in detected_languages:
        onboarding_template_path = ".cursor/templates/onboarding/onboarding_python.md"
    elif onboarding_variant == 'frontend' or "typescript" in detected_languages:
        onboarding_template_path = ".cursor/templates/onboarding/onboarding_frontend.md"
    else:
        onboarding_template_path = config.get_template_path('onboarding') or ".cursor/templates/onboarding/onboarding_general.md"

    architecture_content = _read_template_content(architecture_template_path)
    adr_content = _read_template_content(adr_template_path)
    onboarding_content = _read_template_content(onboarding_template_path)
    
    # Always create data-model.md with proper content
    if "sqlalchemy" in detected_frameworks:
        # If SQLAlchemy is detected, try to generate actual ER diagram
        from .generate_diagrams import generate_er_diagram
        try:
            generate_er_diagram()
            data_model_content = None  # File already created by generate_er_diagram
        except Exception:
            # Fallback to template if generation fails
            data_model_content = _create_data_model_template()
    else:
        # Create placeholder template
        data_model_content = _create_data_model_template()

    # Basic language and framework-specific injection for architecture.md
    language_info = ", ".join(detected_languages) if detected_languages else "N/A"
    framework_info = ", ".join(detected_frameworks) if detected_frameworks else "N/A"

    architecture_content = architecture_content.replace(
        "**Context and Scope**", 
        f"**Context and Scope**\n\nProject Languages: {language_info}\nProject Frameworks: {framework_info}\n"
    )

    # Create and populate template files
    files_to_create = {
        os.path.join(docs_dir, "architecture.md"): architecture_content,
        os.path.join(adr_dir, "0001-record-architecture-decisions.md"): adr_content,
        os.path.join(docs_dir, "onboarding.md"): onboarding_content,
    }

    # Only add data-model.md if we have content to write (not already created by generate_er_diagram)
    if data_model_content is not None:
        files_to_create[os.path.join(docs_dir, "data-model.md")] = data_model_content

    for filepath, content in files_to_create.items():
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(content)
            print(f"Created file: {filepath}")
        else:
            print(f"File already exists, skipping: {filepath}")

def _create_data_model_template() -> str:
    """Creates a placeholder data model template with proper formatting."""
    return """# Project Data Model

This document contains the Entity Relationship Diagram (ERD) for the project's data model.

```mermaid
erDiagram
    %% No SQLAlchemy models or relationships detected.
    %% Add your entities and relationships here
    %% Example:
    %%   USER {
    %%       id int PK
    %%       name string
    %%       email string
    %%   }
    %%   ORDER {
    %%       id int PK
    %%       user_id int FK
    %%       total decimal
    %%   }
    %%   USER ||--o{ ORDER : places
```
""" 