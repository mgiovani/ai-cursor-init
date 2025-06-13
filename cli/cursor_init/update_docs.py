import os
import sys
from .config import load_config
from .detect_framework import detect_project_frameworks
from .generate_diagrams import generate_er_diagram, generate_architecture_diagram
from .init_command import initialize_docs


def update_docs(apply_changes: bool = False, specific_file: str = None, category: str = None) -> str:
    """
    Updates or audits documentation files to sync with current codebase state.
    
    Args:
        apply_changes: If True, applies changes automatically. If False, only reports what needs updating.
        specific_file: If provided, only updates this specific file instead of all documentation.
        category: If provided, only updates files within this category (e.g., 'adr', 'onboarding').
    
    Returns:
        A summary of changes made or needed.
    """
    changes_summary = []
    docs_dir = "docs"
    adr_dir = os.path.join(docs_dir, "adr")
    
    # Handle specific file update
    if specific_file:
        return _update_specific_file(specific_file, apply_changes)
    
    # Handle category-specific update
    if category:
        return _update_category(category, apply_changes)
    
    # Check if docs directory exists
    if not os.path.exists(docs_dir):
        if apply_changes:
            changes_summary.append("Created docs directory structure")
            initialize_docs()
            return "Documentation initialized from scratch.\n" + "\n".join(changes_summary)
        else:
            return "Documentation directory missing. Run with --apply to initialize."
    
    # Load configuration
    config = load_config()
    
    # Detect current project state
    project_info = detect_project_frameworks()
    detected_languages = project_info.get("languages", set())
    detected_frameworks = project_info.get("frameworks", set())
    
    # Check and update core documentation files
    core_files = {
        "architecture.md": _check_architecture_doc,
        "onboarding.md": _check_onboarding_doc,
        "data-model.md": _check_data_model_doc
    }
    
    for filename, check_func in core_files.items():
        filepath = os.path.join(docs_dir, filename)
        needs_update, reason = check_func(filepath, detected_languages, detected_frameworks, config)
        
        if needs_update:
            if apply_changes:
                try:
                    _update_file(filepath, filename, detected_languages, detected_frameworks, config)
                    changes_summary.append(f"Updated {filename}: {reason}")
                except Exception as e:
                    changes_summary.append(f"Failed to update {filename}: {str(e)}")
            else:
                changes_summary.append(f"Needs update - {filename}: {reason}")
    
    # Check ADR directory and initial ADR
    if not os.path.exists(adr_dir):
        if apply_changes:
            os.makedirs(adr_dir, exist_ok=True)
            changes_summary.append("Created ADR directory")
        else:
            changes_summary.append("Needs update - ADR directory missing")
    
    initial_adr = os.path.join(adr_dir, "0001-record-architecture-decisions.md")
    if not os.path.exists(initial_adr):
        if apply_changes:
            _create_initial_adr(initial_adr, config)
            changes_summary.append("Created initial ADR")
        else:
            changes_summary.append("Needs update - Initial ADR missing")
    
    # Update diagrams if applicable
    if "sqlalchemy" in detected_frameworks:
        try:
            if apply_changes:
                generate_er_diagram()
                changes_summary.append("Updated ER diagram from SQLAlchemy models")
            else:
                # Check if ER diagram exists and is recent
                data_model_path = os.path.join(docs_dir, "data-model.md")
                if not os.path.exists(data_model_path):
                    changes_summary.append("Needs update - ER diagram missing")
        except Exception as e:
            if apply_changes:
                changes_summary.append(f"Failed to update ER diagram: {str(e)}")
            else:
                changes_summary.append(f"ER diagram may need update: {str(e)}")
    
    # Generate summary
    if not changes_summary:
        return "Documentation is up to date with current codebase."
    
    action = "Applied changes" if apply_changes else "Changes needed"
    return f"{action}:\n" + "\n".join(f"  - {change}" for change in changes_summary)


def _check_architecture_doc(filepath: str, languages: set, frameworks: set, config) -> tuple[bool, str]:
    """Check if architecture documentation needs updating."""
    if not os.path.exists(filepath):
        return True, "File missing"
    
    # Check if content matches current project state
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Simple checks for outdated content
        if languages and not any(lang in content.lower() for lang in languages):
            return True, "Missing current project languages"
        
        if frameworks and not any(fw in content.lower() for fw in frameworks):
            return True, "Missing current project frameworks"
        
    except Exception:
        return True, "Could not read file"
    
    return False, "Up to date"


def _check_onboarding_doc(filepath: str, languages: set, frameworks: set, config) -> tuple[bool, str]:
    """Check if onboarding documentation needs updating."""
    if not os.path.exists(filepath):
        return True, "File missing"
    
    # Check if the template variant matches current project
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        
        if "python" in languages and "python" not in content.lower():
            return True, "Python project but no Python setup instructions"
        
        if "typescript" in languages and "npm" not in content.lower():
            return True, "TypeScript project but no npm setup instructions"
        
    except Exception:
        return True, "Could not read file"
    
    return False, "Up to date"


def _check_data_model_doc(filepath: str, languages: set, frameworks: set, config) -> tuple[bool, str]:
    """Check if data model documentation needs updating."""
    if "sqlalchemy" in frameworks and not os.path.exists(filepath):
        return True, "SQLAlchemy detected but no data model documentation"
    
    return False, "Up to date"


def _update_file(filepath: str, filename: str, languages: set, frameworks: set, config):
    """Update a specific documentation file."""
    if filename == "architecture.md":
        template_path = config.get_template_path('architecture') or ".cursor/templates/architecture/architecture_google.md"
        _create_from_template(filepath, template_path, languages, frameworks)
    elif filename == "onboarding.md":
        # Choose appropriate onboarding template
        if "python" in languages:
            template_path = ".cursor/templates/onboarding/onboarding_python.md"
        elif "typescript" in languages:
            template_path = ".cursor/templates/onboarding/onboarding_frontend.md"
        else:
            template_path = config.get_template_path('onboarding') or ".cursor/templates/onboarding/onboarding_general.md"
        _create_from_template(filepath, template_path, languages, frameworks)
    elif filename == "data-model.md":
        if "sqlalchemy" in frameworks:
            generate_er_diagram()


def _create_from_template(filepath: str, template_path: str, languages: set, frameworks: set):
    """Create a file from a template with project-specific information."""
    try:
        with open(template_path, 'r') as f:
            content = f.read()
        
        # Inject project information
        language_info = ", ".join(languages) if languages else "N/A"
        framework_info = ", ".join(frameworks) if frameworks else "N/A"
        
        if "**Context and Scope**" in content:
            content = content.replace(
                "**Context and Scope**", 
                f"**Context and Scope**\n\nProject Languages: {language_info}\nProject Frameworks: {framework_info}\n"
            )
        
        with open(filepath, 'w') as f:
            f.write(content)
            
    except Exception as e:
        raise Exception(f"Failed to create from template {template_path}: {str(e)}")


def _create_initial_adr(filepath: str, config):
    """Create the initial ADR about adopting ADRs."""
    template_path = config.get_template_path('adr') or ".cursor/templates/adr/adr_template_nygard.md"
    
    try:
        with open(template_path, 'r') as f:
            content = f.read()
        
        # Replace placeholders for initial ADR
        content = content.replace("{{ADR_NUMBER}}", "0001")
        content = content.replace("{{ADR_TITLE}}", "record-architecture-decisions")
        content = content.replace("{{CONTEXT}}", 
            "We need to record the architectural decisions made on this project.")
        
        # Replace the decision and consequences sections
        content = content.replace(
            "[Describe the decision being made, and why it was chosen over alternatives.]",
            "We will use Architecture Decision Records, as described by Michael Nygard in this article: http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions"
        )
        content = content.replace(
            "[Describe the results of the decision, good or bad.]",
            "See Michael Nygard's article, linked above. For a lightweight ADR toolset, see Nat Pryce's adr-tools at https://github.com/npryce/adr-tools."
        )
        
        with open(filepath, 'w') as f:
            f.write(content)
            
    except Exception as e:
        raise Exception(f"Failed to create initial ADR: {str(e)}")


def _update_specific_file(filename: str, apply_changes: bool) -> str:
    """
    Updates a specific documentation file.
    
    Args:
        filename: Name of the file to update (e.g., 'architecture.md', '0001-record-architecture-decisions.md')
        apply_changes: If True, applies changes automatically. If False, only reports what needs updating.
    
    Returns:
        A summary of changes made or needed for the specific file.
    """
    docs_dir = "docs"
    adr_dir = os.path.join(docs_dir, "adr")
    
    # Load configuration and detect project state
    config = load_config()
    project_info = detect_project_frameworks()
    detected_languages = project_info.get("languages", set())
    detected_frameworks = project_info.get("frameworks", set())
    
    # Determine file location and type
    file_path = None
    file_type = None
    
    # Check if it's an ADR file (starts with digits)
    if filename.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')) and filename.endswith('.md'):
        file_path = os.path.join(adr_dir, filename)
        file_type = 'adr'
    # Check common documentation files
    elif filename in ['architecture.md', 'onboarding.md', 'data-model.md']:
        file_path = os.path.join(docs_dir, filename)
        file_type = filename.replace('.md', '')
    # Search in docs directory and subdirectories
    else:
        for root, dirs, files in os.walk(docs_dir):
            if filename in files:
                file_path = os.path.join(root, filename)
                # Determine type based on location
                if 'adr' in root:
                    file_type = 'adr'
                elif filename == 'architecture.md':
                    file_type = 'architecture'
                elif filename == 'onboarding.md':
                    file_type = 'onboarding'
                elif filename == 'data-model.md':
                    file_type = 'data-model'
                else:
                    file_type = 'unknown'
                break
    
    if not file_path:
        return f"File '{filename}' not found in documentation directory."
    
    # Check if file needs updating
    try:
        if file_type == 'architecture':
            needs_update, reason = _check_architecture_doc(file_path, detected_languages, detected_frameworks, config)
        elif file_type == 'onboarding':
            needs_update, reason = _check_onboarding_doc(file_path, detected_languages, detected_frameworks, config)
        elif file_type == 'data-model':
            needs_update, reason = _check_data_model_doc(file_path, detected_languages, detected_frameworks, config)
        elif file_type == 'adr':
            # For ADR files, check if they exist and are readable
            if os.path.exists(file_path):
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    if 'TBD' in content or '{{' in content:
                        needs_update, reason = True, "Contains placeholder content"
                    else:
                        needs_update, reason = False, "Up to date"
                except Exception:
                    needs_update, reason = True, "Could not read file"
            else:
                needs_update, reason = True, "File missing"
        else:
            needs_update, reason = False, "Unknown file type, no update logic available"
        
        if needs_update:
            if apply_changes:
                try:
                    if file_type in ['architecture', 'onboarding', 'data-model']:
                        _update_file(file_path, f"{file_type}.md", detected_languages, detected_frameworks, config)
                        return f"Successfully updated {filename}: {reason}"
                    elif file_type == 'adr':
                        # For ADR files, we don't auto-update content, just report
                        return f"ADR file {filename} needs attention: {reason}. ADR content should be manually reviewed."
                    else:
                        return f"Cannot update {filename}: Unknown file type"
                except Exception as e:
                    return f"Failed to update {filename}: {str(e)}"
            else:
                return f"File {filename} needs update: {reason}"
        else:
            return f"File {filename} is up to date."
            
    except Exception as e:
        return f"Error checking {filename}: {str(e)}"


def _update_category(category: str, apply_changes: bool) -> str:
    """
    Updates all documentation files within a specific category.
    
    Args:
        category: The category to update (e.g., 'adr', 'onboarding', 'architecture')
        apply_changes: If True, applies changes automatically. If False, only reports what needs updating.
    
    Returns:
        A summary of changes made or needed for the category.
    """
    docs_dir = "docs"
    changes_summary = []
    
    # Load configuration and detect project state
    config = load_config()
    project_info = detect_project_frameworks()
    detected_languages = project_info.get("languages", set())
    detected_frameworks = project_info.get("frameworks", set())
    
    # Define category mappings
    category_mappings = {
        'adr': {
            'directory': os.path.join(docs_dir, 'adr'),
            'file_pattern': '*.md',
            'description': 'Architecture Decision Records'
        },
        'onboarding': {
            'directory': docs_dir,
            'files': ['onboarding.md'],
            'description': 'Onboarding documentation'
        },
        'architecture': {
            'directory': docs_dir,
            'files': ['architecture.md'],
            'description': 'Architecture documentation'
        },
        'data-model': {
            'directory': docs_dir,
            'files': ['data-model.md'],
            'description': 'Data model documentation'
        }
    }
    
    if category not in category_mappings:
        return f"Unknown category '{category}'. Available categories: {', '.join(category_mappings.keys())}"
    
    category_info = category_mappings[category]
    category_desc = category_info['description']
    
    if not os.path.exists(docs_dir):
        return f"Documentation directory '{docs_dir}' does not exist. Run initialization first."
    
    # Handle different category types
    if category == 'adr':
        return _update_adr_category(category_info, apply_changes, config, detected_languages, detected_frameworks)
    elif category in ['onboarding', 'architecture', 'data-model']:
        return _update_single_file_category(category, category_info, apply_changes, config, detected_languages, detected_frameworks)
    else:
        return f"Category '{category}' update logic not implemented yet."


def _update_adr_category(category_info: dict, apply_changes: bool, config, detected_languages: set, detected_frameworks: set) -> str:
    """Update all ADR files in the category."""
    import glob
    
    adr_dir = category_info['directory']
    changes_summary = []
    
    if not os.path.exists(adr_dir):
        if apply_changes:
            os.makedirs(adr_dir, exist_ok=True)
            changes_summary.append("Created ADR directory")
            
            # Create initial ADR
            initial_adr = os.path.join(adr_dir, "0001-record-architecture-decisions.md")
            _create_initial_adr(initial_adr, config)
            changes_summary.append("Created initial ADR")
        else:
            return "ADR directory missing. Run with --apply to create."
    
    # Find all ADR files
    adr_files = glob.glob(os.path.join(adr_dir, "*.md"))
    
    if not adr_files:
        if apply_changes:
            # Create initial ADR if none exist
            initial_adr = os.path.join(adr_dir, "0001-record-architecture-decisions.md")
            _create_initial_adr(initial_adr, config)
            changes_summary.append("Created initial ADR")
        else:
            changes_summary.append("No ADR files found. Consider creating an initial ADR.")
    else:
        # Check each ADR file
        for adr_file in sorted(adr_files):
            filename = os.path.basename(adr_file)
            try:
                with open(adr_file, 'r') as f:
                    content = f.read()
                
                needs_update = False
                reason = ""
                
                if 'TBD' in content:
                    needs_update = True
                    reason = "Contains TBD placeholders"
                elif '{{' in content and '}}' in content:
                    needs_update = True
                    reason = "Contains template placeholders"
                elif not content.strip():
                    needs_update = True
                    reason = "File is empty"
                
                if needs_update:
                    if apply_changes:
                        # For ADRs, we don't auto-update content, just report
                        changes_summary.append(f"ADR {filename} needs attention: {reason}")
                    else:
                        changes_summary.append(f"Needs review - {filename}: {reason}")
                        
            except Exception as e:
                changes_summary.append(f"Error reading {filename}: {str(e)}")
    
    if not changes_summary:
        return "All ADR files are up to date."
    
    action = "Processed ADR category" if apply_changes else "ADR category review needed"
    return f"{action}:\n" + "\n".join(f"  - {change}" for change in changes_summary)


def _update_single_file_category(category: str, category_info: dict, apply_changes: bool, config, detected_languages: set, detected_frameworks: set) -> str:
    """Update single-file categories like onboarding, architecture, data-model."""
    changes_summary = []
    
    for filename in category_info['files']:
        filepath = os.path.join(category_info['directory'], filename)
        
        # Check if file needs updating using existing logic
        if category == 'onboarding':
            needs_update, reason = _check_onboarding_doc(filepath, detected_languages, detected_frameworks, config)
        elif category == 'architecture':
            needs_update, reason = _check_architecture_doc(filepath, detected_languages, detected_frameworks, config)
        elif category == 'data-model':
            needs_update, reason = _check_data_model_doc(filepath, detected_languages, detected_frameworks, config)
        else:
            needs_update, reason = False, "Unknown category"
        
        if needs_update:
            if apply_changes:
                try:
                    _update_file(filepath, filename, detected_languages, detected_frameworks, config)
                    changes_summary.append(f"Updated {filename}: {reason}")
                except Exception as e:
                    changes_summary.append(f"Failed to update {filename}: {str(e)}")
            else:
                changes_summary.append(f"Needs update - {filename}: {reason}")
        else:
            changes_summary.append(f"{filename} is up to date")
    
    if not changes_summary:
        return f"All {category} files are up to date."
    
    action = f"Applied changes to {category} category" if apply_changes else f"Changes needed in {category} category"
    return f"{action}:\n" + "\n".join(f"  - {change}" for change in changes_summary)
