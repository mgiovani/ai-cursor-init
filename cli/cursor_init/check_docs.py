import os
import glob
from typing import List


def check_docs() -> int:
    """
    Check documentation files for freshness and completeness.
    
    Returns:
        0 if documentation is fresh and complete
        1 if stale or incomplete documentation is found
    """
    docs_dir = "docs"
    issues_found = []
    
    if not os.path.exists(docs_dir):
        print("ERROR: Documentation directory 'docs' not found.")
        return 1
    
    # Check all markdown files in docs directory and subdirectories
    markdown_files = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    
    if not markdown_files:
        print("WARNING: No markdown files found in documentation directory.")
        return 1
    
    # Check each markdown file for issues
    for file_path in markdown_files:
        file_issues = _check_file_freshness(file_path)
        if file_issues:
            issues_found.extend(file_issues)
    
    # Check for missing core documentation files
    core_files = [
        'docs/architecture.md',
        'docs/onboarding.md',
        'docs/adr/0001-record-architecture-decisions.md'
    ]
    
    for core_file in core_files:
        if not os.path.exists(core_file):
            issues_found.append(f"Missing core documentation file: {core_file}")
    
    # Report results
    if issues_found:
        print("Documentation freshness check FAILED:")
        for issue in issues_found:
            print(f"  - {issue}")
        print(f"\nFound {len(issues_found)} issue(s). Documentation needs attention.")
        return 1
    else:
        print("Documentation freshness check PASSED: All documentation is up to date.")
        return 0


def _check_file_freshness(file_path: str) -> List[str]:
    """
    Check a single file for freshness issues.
    
    Args:
        file_path: Path to the markdown file to check
        
    Returns:
        List of issues found in the file
    """
    issues = []
    relative_path = os.path.relpath(file_path)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for empty files
        if not content.strip():
            issues.append(f"{relative_path}: File is empty")
            return issues
        
        # Check for placeholder content
        stale_indicators = [
            'TBD',
            'TODO',
            'FIXME',
            'XXX',
            '{{',  # Template placeholders
            '[TODO]',
            '[TBD]',
            'To be determined',
            'To be decided',
            'Coming soon',
            'Under construction'
        ]
        
        lines = content.split('\n')
        for line_num, line in enumerate(lines, 1):
            line_lower = line.lower()
            for indicator in stale_indicators:
                if indicator.lower() in line_lower:
                    issues.append(f"{relative_path}:{line_num}: Contains '{indicator}' - {line.strip()}")
        
        # Check for very short files that might be incomplete
        if len(content.strip()) < 50:
            issues.append(f"{relative_path}: File appears incomplete (less than 50 characters)")
        
        # Check for files with only headers and no content
        lines_with_content = [line for line in lines if line.strip() and not line.strip().startswith('#')]
        if len(lines_with_content) < 3:
            issues.append(f"{relative_path}: File appears to have minimal content")
            
    except Exception as e:
        issues.append(f"{relative_path}: Error reading file - {str(e)}")
    
    return issues


def check_specific_file(file_path: str) -> int:
    """
    Check a specific file for freshness issues.
    
    Args:
        file_path: Path to the specific file to check
        
    Returns:
        0 if file is fresh, 1 if issues found
    """
    if not os.path.exists(file_path):
        print(f"ERROR: File '{file_path}' not found.")
        return 1
    
    if not file_path.endswith('.md'):
        print(f"WARNING: File '{file_path}' is not a markdown file.")
        return 0
    
    issues = _check_file_freshness(file_path)
    
    if issues:
        print(f"File check FAILED for {file_path}:")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    else:
        print(f"File check PASSED for {file_path}: File is up to date.")
        return 0


def check_category(category: str) -> int:
    """
    Check all files in a specific category for freshness issues.
    
    Args:
        category: Category to check (adr, architecture, onboarding, data-model)
        
    Returns:
        0 if all files in category are fresh, 1 if issues found
    """
    docs_dir = "docs"
    issues_found = []
    
    category_mappings = {
        'adr': 'docs/adr/*.md',
        'architecture': 'docs/architecture.md',
        'onboarding': 'docs/onboarding.md',
        'data-model': 'docs/data-model.md'
    }
    
    if category not in category_mappings:
        print(f"ERROR: Unknown category '{category}'. Available: {', '.join(category_mappings.keys())}")
        return 1
    
    pattern = category_mappings[category]
    
    if '*' in pattern:
        # Handle directory patterns
        files = glob.glob(pattern)
    else:
        # Handle single file patterns
        files = [pattern] if os.path.exists(pattern) else []
    
    if not files:
        print(f"WARNING: No files found for category '{category}'.")
        return 1
    
    for file_path in files:
        file_issues = _check_file_freshness(file_path)
        if file_issues:
            issues_found.extend(file_issues)
    
    if issues_found:
        print(f"Category check FAILED for '{category}':")
        for issue in issues_found:
            print(f"  - {issue}")
        return 1
    else:
        print(f"Category check PASSED for '{category}': All files are up to date.")
        return 0 