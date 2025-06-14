import os
from .ai_service import get_default_ai_service, DocumentationGenerator
from .config import load_config
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def initialize_docs():
    docs_dir = 'docs'
    adr_dir = os.path.join(docs_dir, 'adr')

    # Create docs/ and docs/adr/ directories
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(adr_dir, exist_ok=True)

    console.print(f'[green]✓[/green] Created directory: {docs_dir}')
    console.print(f'[green]✓[/green] Created directory: {adr_dir}')

    try:
        # Initialize AI service
        console.print('[cyan]Initializing AI service...[/cyan]')
        ai_service = get_default_ai_service()
        doc_generator = DocumentationGenerator(ai_service)

        # Generate documentation using AI
        with Progress(
            SpinnerColumn(),
            TextColumn('[progress.description]{task.description}'),
            console=console,
        ) as progress:
            
            # Generate architecture documentation
            task1 = progress.add_task('Generating architecture documentation...', total=None)
            architecture_content = doc_generator.generate_architecture_docs()
            progress.update(task1, completed=True)
            
            # Generate onboarding documentation  
            task2 = progress.add_task('Generating onboarding documentation...', total=None)
            onboarding_content = doc_generator.generate_onboarding_docs()
            progress.update(task2, completed=True)
            
            # Generate initial ADR
            task3 = progress.add_task('Generating initial ADR...', total=None)
            adr_content = doc_generator.generate_adr(
                'Record Architecture Decisions',
                'Initial ADR documenting the adoption of Architecture Decision Records for this project'
            )
            progress.update(task3, completed=True)

        # Create placeholder data model (can be enhanced later with AI analysis)
        data_model_content = _create_data_model_placeholder()

        # Create and populate files
        files_to_create = {
            os.path.join(docs_dir, 'architecture.md'): architecture_content,
            os.path.join(adr_dir, '0001-record-architecture-decisions.md'): adr_content,
            os.path.join(docs_dir, 'onboarding.md'): onboarding_content,
            os.path.join(docs_dir, 'data-model.md'): data_model_content,
        }

        for filepath, content in files_to_create.items():
            if not os.path.exists(filepath):
                with open(filepath, 'w') as f:
                    f.write(content)
                console.print(f'[green]✓[/green] Created file: {filepath}')
            else:
                console.print(f'[yellow]⚠[/yellow] File already exists, skipping: {filepath}')

        console.print('\n[bold green]Documentation initialization complete![/bold green]')
        console.print('Generated AI-powered documentation based on your project structure and cursor rules.')

    except Exception as e:
        console.print(f'[red]✗[/red] AI generation failed: {str(e)}')
        console.print('[yellow]Falling back to basic template generation...[/yellow]')
        _fallback_template_generation(docs_dir, adr_dir)


def _create_data_model_placeholder() -> str:
    return '''# Project Data Model

This document contains the Entity Relationship Diagram (ERD) for the project's data model.

```mermaid
erDiagram
    %% Database schema will be analyzed and updated automatically
    %% Use /gen-er-diagram command to generate from SQLAlchemy models
    %% Or manually add your entities and relationships here
    %%
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
'''


def _fallback_template_generation(docs_dir: str, adr_dir: str):
    console.print('Using basic template fallback...')
    
    # Basic fallback templates
    architecture_content = '''# Project Architecture

## Overview
This document describes the architecture of the project.

## Components
- Core application components
- External dependencies
- Data flow

## Technology Stack
- Programming languages and frameworks
- Databases and storage
- Infrastructure and deployment

*This document was generated automatically. Please update with project-specific details.*
'''

    onboarding_content = '''# Project Onboarding

## Getting Started
Welcome to the project! This guide will help you get up and running.

## Prerequisites
- Required software and tools
- Development environment setup

## Installation
1. Clone the repository
2. Install dependencies
3. Configure environment

## Development Workflow
- Coding standards
- Testing procedures
- Deployment process

*This document was generated automatically. Please update with project-specific details.*
'''

    adr_content = '''# ADR-0001: Record Architecture Decisions

**Status:** Accepted

**Context:**
We need to record the architectural decisions made on this project.

**Decision:**
We will use Architecture Decision Records (ADRs) to document significant architectural decisions.

**Consequences:**
- Better documentation of design decisions
- Improved understanding for new team members
- Historical context for future changes
'''

    data_model_content = _create_data_model_placeholder()

    files_to_create = {
        os.path.join(docs_dir, 'architecture.md'): architecture_content,
        os.path.join(adr_dir, '0001-record-architecture-decisions.md'): adr_content,
        os.path.join(docs_dir, 'onboarding.md'): onboarding_content,
        os.path.join(docs_dir, 'data-model.md'): data_model_content,
    }

    for filepath, content in files_to_create.items():
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                f.write(content)
            console.print(f'[green]✓[/green] Created file: {filepath}')
        else:
            console.print(f'[yellow]⚠[/yellow] File already exists, skipping: {filepath}') 