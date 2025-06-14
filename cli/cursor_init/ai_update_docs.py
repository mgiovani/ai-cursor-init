import os
from pathlib import Path
from typing import Dict, List, Optional
from .ai_service import get_default_ai_service, DocumentationGenerator
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

console = Console()

class DocumentationAnalyzer:
    def __init__(self, ai_service):
        self.ai_service = ai_service
        self.doc_generator = DocumentationGenerator(ai_service)
    
    def analyze_documentation_freshness(self, project_root: str = '.') -> Dict[str, Dict]:
        """Analyze existing documentation and determine what needs updating."""
        docs_dir = Path(project_root) / 'docs'
        if not docs_dir.exists():
            return {}
        
        analysis = {}
        
        # Find all markdown files in docs
        for doc_file in docs_dir.rglob('*.md'):
            relative_path = str(doc_file.relative_to(project_root))
            
            try:
                content = doc_file.read_text(encoding='utf-8')
                analysis[relative_path] = {
                    'exists': True,
                    'size': len(content),
                    'last_modified': doc_file.stat().st_mtime,
                    'needs_ai_review': self._needs_ai_review(content),
                    'content': content[:2000]  # First 2000 chars for analysis
                }
            except Exception as e:
                analysis[relative_path] = {
                    'exists': False,
                    'error': str(e)
                }
        
        return analysis
    
    def _needs_ai_review(self, content: str) -> bool:
        """Determine if content needs AI review based on heuristics."""
        indicators = [
            'TODO', 'FIXME', 'TBD', 'placeholder',
            'automatically generated', 'update with specific details',
            'add your', 'describe the', 'fill in'
        ]
        
        content_lower = content.lower()
        return any(indicator.lower() in content_lower for indicator in indicators)
    
    def generate_updated_content(self, doc_path: str, current_content: str, project_root: str = '.') -> str:
        """Generate updated content for a specific document using AI."""
        
        doc_type = self._determine_doc_type(doc_path)
        
        if doc_type == 'architecture':
            return self.doc_generator.generate_architecture_docs(project_root)
        elif doc_type == 'onboarding':
            return self.doc_generator.generate_onboarding_docs(project_root)
        elif doc_type == 'adr':
            # For ADRs, we enhance rather than replace
            return self._enhance_adr_content(current_content, project_root)
        else:
            # Generic documentation improvement
            return self._improve_generic_documentation(doc_path, current_content, project_root)
    
    def _determine_doc_type(self, doc_path: str) -> str:
        """Determine the type of documentation based on path and filename."""
        path_lower = doc_path.lower()
        
        if 'architecture' in path_lower:
            return 'architecture'
        elif 'onboarding' in path_lower:
            return 'onboarding'
        elif '/adr/' in path_lower or 'adr-' in path_lower:
            return 'adr'
        elif 'data-model' in path_lower or 'er-diagram' in path_lower:
            return 'data-model'
        else:
            return 'generic'
    
    def _enhance_adr_content(self, current_content: str, project_root: str) -> str:
        """Enhance existing ADR content rather than replace it."""
        system_prompt = '''You are an expert in Architecture Decision Records. Review and enhance the provided ADR content based on current project context.

Maintain the existing structure and decisions, but:
1. Improve clarity and detail
2. Add relevant technical context
3. Enhance consequences section
4. Ensure proper ADR format

Do not change the core decision or status unless clearly outdated.'''

        cursor_rules = self.doc_generator._read_cursor_rules(project_root)
        project_structure = self.doc_generator._analyze_project_structure(project_root)
        
        user_prompt = f'''Review and enhance this ADR content:

## Current ADR Content:
{current_content}

## Project Context:
{cursor_rules}

## Project Structure:
{project_structure}

Improve the ADR while maintaining its core decision and structure.'''

        return self.ai_service.generate_completion(user_prompt, system_prompt)
    
    def _improve_generic_documentation(self, doc_path: str, current_content: str, project_root: str) -> str:
        """Improve generic documentation using AI."""
        system_prompt = '''You are an expert technical documentation writer. Review and improve the provided documentation based on current project context.

Maintain the existing structure and key information, but:
1. Improve clarity and organization
2. Add missing details based on project context
3. Update outdated information
4. Ensure consistency with project standards

Focus on making the documentation more useful and accurate.'''

        cursor_rules = self.doc_generator._read_cursor_rules(project_root)
        project_structure = self.doc_generator._analyze_project_structure(project_root)
        
        user_prompt = f'''Improve this documentation file ({doc_path}):

## Current Content:
{current_content}

## Project Context:
{cursor_rules}

## Project Structure:
{project_structure}

Enhance the documentation while preserving important existing information.'''

        return self.ai_service.generate_completion(user_prompt, system_prompt)


def update_docs_ai(apply_changes: bool = False, specific_file: Optional[str] = None, category: Optional[str] = None, provider_override: Optional[str] = None) -> str:
    """AI-powered documentation update command."""
    try:
        console.print('[cyan]Initializing AI documentation analysis...[/cyan]')
        ai_service = get_default_ai_service(provider_override)
        analyzer = DocumentationAnalyzer(ai_service)
        
        # Analyze current documentation
        with Progress(
            SpinnerColumn(),
            TextColumn('[progress.description]{task.description}'),
            console=console,
        ) as progress:
            task = progress.add_task('Analyzing documentation...', total=None)
            analysis = analyzer.analyze_documentation_freshness()
            progress.update(task, completed=True)
        
        if not analysis:
            console.print('[yellow]No documentation found. Run "init" first.[/yellow]')
            return 'No documentation found'
        
        # Filter based on specific file or category
        files_to_update = {}
        
        if specific_file:
            # Find matching file
            for path, info in analysis.items():
                if specific_file in path:
                    files_to_update[path] = info
                    break
            if not files_to_update:
                console.print(f'[red]File not found: {specific_file}[/red]')
                return f'File not found: {specific_file}'
        
        elif category:
            # Filter by category
            for path, info in analysis.items():
                if category.lower() in path.lower():
                    files_to_update[path] = info
        else:
            # All files that need review
            files_to_update = {path: info for path, info in analysis.items() 
                             if info.get('needs_ai_review', False)}
        
        if not files_to_update:
            console.print('[green]All documentation appears up to date![/green]')
            return 'Documentation is up to date'
        
        # Display analysis table
        table = Table(title='Documentation Analysis')
        table.add_column('File', style='cyan')
        table.add_column('Status', style='yellow')
        table.add_column('Action', style='green')
        
        for path, info in files_to_update.items():
            status = 'Needs Review' if info.get('needs_ai_review') else 'Current'
            action = 'Update' if apply_changes else 'Preview'
            table.add_row(path, status, action)
        
        console.print(table)
        
        if not apply_changes:
            console.print('\n[yellow]Use --apply to update files automatically[/yellow]')
            return 'Analysis complete. Use --apply to update files.'
        
        # Update files with AI
        updated_files = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn('[progress.description]{task.description}'),
            console=console,
        ) as progress:
            
            for path, info in files_to_update.items():
                task = progress.add_task(f'Updating {path}...', total=None)
                
                try:
                    new_content = analyzer.generate_updated_content(
                        path, 
                        info.get('content', ''),
                        '.'
                    )
                    
                    # Write updated content
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    updated_files.append(path)
                    progress.update(task, completed=True)
                    
                except Exception as e:
                    console.print(f'[red]Failed to update {path}: {str(e)}[/red]')
                    continue
        
        console.print(f'\n[bold green]Updated {len(updated_files)} files successfully![/bold green]')
        
        for file in updated_files:
            console.print(f'[green]✓[/green] {file}')
        
        return f'Successfully updated {len(updated_files)} files'
        
    except Exception as e:
        console.print(f'[red]AI update failed: {str(e)}[/red]')
        return f'Update failed: {str(e)}' 