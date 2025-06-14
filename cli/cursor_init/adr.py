import os
import re
from .ai_service import get_default_ai_service, DocumentationGenerator
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def _sanitize_filename(title: str) -> str:
    # Convert to lowercase and replace spaces/special chars with hyphens
    sanitized = re.sub(r'[^\w\s-]', '', title.lower())
    sanitized = re.sub(r'[-\s]+', '-', sanitized)
    return sanitized.strip('-')

def _get_next_adr_number() -> str:
    adr_dir = 'docs/adr'
    if not os.path.exists(adr_dir):
        return '0001'
    
    # Find existing ADR files and get the highest number
    existing_adrs = []
    for filename in os.listdir(adr_dir):
        if filename.endswith('.md') and filename[:4].isdigit():
            existing_adrs.append(int(filename[:4]))
    
    if not existing_adrs:
        return '0001'
    
    next_number = max(existing_adrs) + 1
    return f'{next_number:04d}'

def create_adr(title: str = 'untitled-adr', context: str = '') -> str:
    try:
        # Initialize AI service
        console.print('[cyan]Generating ADR with AI...[/cyan]')
        ai_service = get_default_ai_service()
        doc_generator = DocumentationGenerator(ai_service)
        
        # Get next ADR number and sanitize title
        adr_number = _get_next_adr_number()
        sanitized_title = _sanitize_filename(title)
        
        # Generate ADR content using AI
        with Progress(
            SpinnerColumn(),
            TextColumn('[progress.description]{task.description}'),
            console=console,
        ) as progress:
            task = progress.add_task(f'Creating ADR {adr_number}: {title}...', total=None)
            adr_content = doc_generator.generate_adr(title, context)
            progress.update(task, completed=True)
        
        # Ensure the content follows ADR format with number
        if not adr_content.startswith('#'):
            adr_content = f'# ADR-{adr_number}: {title}\n\n{adr_content}'
        else:
            # Replace the first header to include the ADR number
            lines = adr_content.split('\n')
            if lines[0].startswith('#'):
                lines[0] = f'# ADR-{adr_number}: {title}'
                adr_content = '\n'.join(lines)
        
        # Create the ADR file
        os.makedirs('docs/adr', exist_ok=True)
        filename = f'{adr_number}-{sanitized_title}.md'
        filepath = os.path.join('docs/adr', filename)
        
        with open(filepath, 'w') as f:
            f.write(adr_content)
        
        console.print(f'[green]✓[/green] Created ADR: {filepath}')
        return f'ADR created successfully: {filepath}'
        
    except Exception as e:
        console.print(f'[red]✗[/red] AI generation failed: {str(e)}')
        console.print('[yellow]Falling back to template generation...[/yellow]')
        return _fallback_adr_creation(title, context)

def _fallback_adr_creation(title: str, context: str) -> str:
    adr_number = _get_next_adr_number()
    sanitized_title = _sanitize_filename(title)
    
    # Basic ADR template
    adr_content = f'''# ADR-{adr_number}: {title}

**Status:** Proposed

**Context:**
{context if context else 'Describe the forces at play, including technological, political, social, and project local factors.'}

**Decision:**
Describe the decision being made and why it was chosen over alternatives.

**Consequences:**
Describe the results of the decision, both positive and negative outcomes.

---
*This ADR was generated using a fallback template. Please update with specific details.*
'''
    
    os.makedirs('docs/adr', exist_ok=True)
    filename = f'{adr_number}-{sanitized_title}.md'
    filepath = os.path.join('docs/adr', filename)
    
    with open(filepath, 'w') as f:
        f.write(adr_content)
    
    console.print(f'[green]✓[/green] Created ADR (fallback): {filepath}')
    return f'ADR created successfully: {filepath}' 