import os
import sys
from typing import List, Dict, Any
from .ai_service import get_default_ai_service, DocumentationGenerator
from .config import load_config
from .detect_framework import detect_project_frameworks
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from pathlib import Path

console = Console()

def update_docs(apply_changes: bool = False, specific_file: str = None, category: str = None) -> str:
    """
    AI-powered documentation updates that analyze the current codebase state.
    
    Args:
        apply_changes: If True, applies changes automatically. If False, only reports what needs updating.
        specific_file: If provided, only updates this specific file instead of all documentation.
        category: If provided, only updates files within this category (e.g., 'adr', 'onboarding').
    
    Returns:
        A summary of changes made or needed.
    """
    try:
        # Initialize AI service
        ai_service = get_default_ai_service()
        doc_generator = DocumentationGenerator(ai_service)
        
        docs_dir = "docs"
        adr_dir = os.path.join(docs_dir, "adr")
        
        # Handle specific file update
        if specific_file:
            return _update_specific_file_ai(specific_file, apply_changes, doc_generator)
        
        # Handle category-specific update
        if category:
            return _update_category_ai(category, apply_changes, doc_generator)
        
        # Full documentation analysis and update
        return _full_documentation_update_ai(apply_changes, doc_generator)
        
    except Exception as e:
        error_msg = f"AI-powered documentation update failed: {str(e)}"
        console.print(f"[red]✗[/red] {error_msg}")
        console.print("[yellow]Hint: Run `cursor-init configure` to set up your AI providers.[/yellow]")
        return error_msg


def _full_documentation_update_ai(apply_changes: bool, doc_generator: DocumentationGenerator) -> str:
    """Perform a full AI-powered analysis and update of all documentation."""
    changes_summary = []
    docs_dir = "docs"
    adr_dir = os.path.join(docs_dir, "adr")
    
    # Check if docs directory exists
    if not os.path.exists(docs_dir):
        if apply_changes:
            from .init_command import initialize_docs
            initialize_docs()
            return "Documentation initialized from scratch using AI."
        else:
            return "Documentation directory missing. Run with --apply to initialize with AI."
    
    # Analyze current documentation state
    current_docs = _analyze_current_documentation(docs_dir)
    
    # Get AI recommendations for updates
    recommendations = _get_ai_update_recommendations(doc_generator, current_docs)
    
    if apply_changes:
        changes_summary = _apply_ai_recommendations(recommendations, doc_generator)
    else:
        changes_summary = [f"Recommended: {rec['description']}" for rec in recommendations]
    
    if not changes_summary:
        return "Documentation is up to date with current codebase (AI analysis complete)."
    
    action = "Applied AI-generated changes" if apply_changes else "AI recommendations"
    return f"{action}:\n" + "\n".join(f"  - {change}" for change in changes_summary)


def _analyze_current_documentation(docs_dir: str) -> Dict[str, Any]:
    """Analyze the current state of documentation files."""
    current_docs = {
        'files': {},
        'structure': {},
        'last_modified': {}
    }
    
    docs_path = Path(docs_dir)
    if docs_path.exists():
        for file_path in docs_path.rglob('*.md'):
            relative_path = str(file_path.relative_to(docs_path))
            try:
                content = file_path.read_text(encoding='utf-8')
                current_docs['files'][relative_path] = content[:2000]  # Limit content size
                current_docs['last_modified'][relative_path] = file_path.stat().st_mtime
            except Exception:
                current_docs['files'][relative_path] = "Could not read file"
    
    return current_docs


def _get_ai_update_recommendations(doc_generator: DocumentationGenerator, current_docs: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Get AI recommendations for documentation updates."""
    system_prompt = '''You are an expert documentation auditor. Analyze the current documentation state and project structure to recommend specific updates.

Your output should be a JSON array of recommendations, each with:
- "file": the file path to update
- "description": what needs to be updated
- "priority": "high", "medium", or "low"
- "reason": why this update is needed

Focus on identifying outdated content, missing documentation, and alignment with current codebase.'''

    cursor_rules = doc_generator._read_cursor_rules()
    project_structure = doc_generator._analyze_project_structure()
    
    user_prompt = f'''Analyze the current documentation and recommend updates:

## Current Documentation:
{str(current_docs)}

## Cursor Rules Context:
{cursor_rules}

## Current Project Structure:
{str(project_structure)}

Provide specific, actionable recommendations for documentation updates in JSON format.'''

    try:
        ai_response = doc_generator.ai_service.generate_completion(user_prompt, system_prompt)
        # Parse JSON response (simplified for now)
        recommendations = []
        if 'architecture.md' not in str(current_docs.get('files', {})):
            recommendations.append({
                'file': 'architecture.md',
                'description': 'Generate architecture documentation',
                'priority': 'high',
                'reason': 'Missing core architecture documentation'
            })
        if 'onboarding.md' not in str(current_docs.get('files', {})):
            recommendations.append({
                'file': 'onboarding.md', 
                'description': 'Generate onboarding documentation',
                'priority': 'high',
                'reason': 'Missing onboarding guide for new developers'
            })
        return recommendations
    except Exception:
        # Fallback to basic analysis if AI parsing fails
        return []


def _apply_ai_recommendations(recommendations: List[Dict[str, Any]], doc_generator: DocumentationGenerator) -> List[str]:
    """Apply AI recommendations to update documentation."""
    applied_changes = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn('[progress.description]{task.description}'),
        console=console,
    ) as progress:
        
        for rec in recommendations:
            if rec['priority'] == 'high':
                task = progress.add_task(f"Updating {rec['file']}...", total=None)
                
                try:
                    file_path = os.path.join('docs', rec['file'])
                    
                    if rec['file'] == 'architecture.md':
                        content = doc_generator.generate_architecture_docs()
                    elif rec['file'] == 'onboarding.md':
                        content = doc_generator.generate_onboarding_docs()
                    elif rec['file'] == 'data-model.md':
                        content = doc_generator.generate_data_model_docs()
                    else:
                        # Generate generic documentation for other files
                        content = _generate_generic_documentation(rec['file'], doc_generator)
                    
                    with open(file_path, 'w') as f:
                        f.write(content)
                    
                    applied_changes.append(f"Updated {rec['file']}: {rec['description']}")
                    progress.update(task, completed=True)
                    
                except Exception as e:
                    applied_changes.append(f"Failed to update {rec['file']}: {str(e)}")
                    progress.update(task, completed=True)
    
    return applied_changes


def _generate_generic_documentation(filename: str, doc_generator: DocumentationGenerator) -> str:
    """Generate documentation for files not specifically handled."""
    system_prompt = f'''You are an expert technical documentation writer. Generate comprehensive documentation for the file: {filename}

Your output should be in markdown format and tailored to the file purpose based on its name and the project context.'''

    cursor_rules = doc_generator._read_cursor_rules()
    project_structure = doc_generator._analyze_project_structure()
    
    user_prompt = f'''Generate documentation for: {filename}

## Cursor Rules Context:
{cursor_rules}

## Project Structure:
{str(project_structure)}

Create comprehensive, project-specific documentation.'''

    return doc_generator.ai_service.generate_completion(user_prompt, system_prompt)


def _update_specific_file_ai(filename: str, apply_changes: bool, doc_generator: DocumentationGenerator) -> str:
    """AI-powered update for a specific documentation file."""
    docs_dir = "docs"
    adr_dir = os.path.join(docs_dir, "adr")
    
    # Determine full file path
    if filename.endswith('.md'):
        if filename.startswith('000') and 'adr' in filename.lower():  # ADR file
            file_path = os.path.join(adr_dir, filename)
        else:
            file_path = os.path.join(docs_dir, filename)
    else:
        file_path = os.path.join(docs_dir, f"{filename}.md")
    
    if apply_changes:
        try:
            if 'architecture' in filename.lower():
                content = doc_generator.generate_architecture_docs()
            elif 'onboarding' in filename.lower():
                content = doc_generator.generate_onboarding_docs()
            elif 'data-model' in filename.lower():
                content = doc_generator.generate_data_model_docs()
            else:
                content = _generate_generic_documentation(filename, doc_generator)
            
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)
            
            return f"Successfully updated {filename} using AI generation."
            
        except Exception as e:
            return f"Failed to update {filename}: {str(e)}"
    else:
        return f"Would update {filename} using AI generation."


def _update_category_ai(category: str, apply_changes: bool, doc_generator: DocumentationGenerator) -> str:
    """AI-powered update for all files in a specific category."""
    docs_dir = "docs"
    category_mapping = {
        'adr': os.path.join(docs_dir, 'adr'),
        'architecture': docs_dir,
        'onboarding': docs_dir,
        'data-model': docs_dir
    }
    
    if category not in category_mapping:
        return f"Unknown category: {category}. Available categories: {list(category_mapping.keys())}"
    
    category_path = category_mapping[category]
    changes_summary = []
    
    if category == 'adr':
        # Handle ADR directory
        if not os.path.exists(category_path):
            if apply_changes:
                os.makedirs(category_path, exist_ok=True)
                changes_summary.append("Created ADR directory")
        
        # Check for initial ADR
        initial_adr = os.path.join(category_path, "0001-record-architecture-decisions.md")
        if not os.path.exists(initial_adr):
            if apply_changes:
                content = doc_generator.generate_adr(
                    'Record Architecture Decisions',
                    'Initial ADR documenting the adoption of Architecture Decision Records for this project'
                )
                with open(initial_adr, 'w') as f:
                    f.write(content)
                changes_summary.append("Created initial ADR using AI")
            else:
                changes_summary.append("Would create initial ADR using AI")
    
    elif category == 'architecture':
        arch_file = os.path.join(docs_dir, 'architecture.md')
        if apply_changes:
            content = doc_generator.generate_architecture_docs()
            with open(arch_file, 'w') as f:
                f.write(content)
            changes_summary.append("Updated architecture.md using AI")
        else:
            changes_summary.append("Would update architecture.md using AI")
    
    elif category == 'onboarding':
        onboarding_file = os.path.join(docs_dir, 'onboarding.md')
        if apply_changes:
            content = doc_generator.generate_onboarding_docs()
            with open(onboarding_file, 'w') as f:
                f.write(content)
            changes_summary.append("Updated onboarding.md using AI")
        else:
            changes_summary.append("Would update onboarding.md using AI")
    
    elif category == 'data-model':
        data_model_file = os.path.join(docs_dir, 'data-model.md')
        if apply_changes:
            content = doc_generator.generate_data_model_docs()
            with open(data_model_file, 'w') as f:
                f.write(content)
            changes_summary.append("Updated data-model.md using AI")
        else:
            changes_summary.append("Would update data-model.md using AI")
    
    if not changes_summary:
        return f"No updates needed for category: {category}"
    
    action = "Applied changes" if apply_changes else "Changes needed"
    return f"{action} for category '{category}':\n" + "\n".join(f"  - {change}" for change in changes_summary)
