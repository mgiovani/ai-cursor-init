import os
from .ai_service import get_default_ai_service, DocumentationGenerator
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

            # Generate data model documentation
            task4 = progress.add_task('Generating data model documentation...', total=None)
            data_model_content = doc_generator.generate_data_model_docs()
            progress.update(task4, completed=True)

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
        console.print('[red]Unable to generate documentation without AI. Please check your AI configuration and try again.[/red]')
        console.print('[yellow]Hint: Run `cursor-init configure` to set up your AI providers.[/yellow]')
        raise SystemExit(1) 