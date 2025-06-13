import os
import re
from pathlib import Path
from typing import Optional


def sanitize_title(title: str) -> str:
    """Convert title to lowercase kebab-case for filename."""
    sanitized = re.sub(r'[^\w\s-]', '', title.strip())
    sanitized = re.sub(r'[-\s]+', '-', sanitized)
    return sanitized.lower().strip('-')


def create_rfc(title: Optional[str] = None) -> str:
    """Create a new RFC document with the given title."""
    if not title or not title.strip():
        title = 'new-rfc'
        refined_title = 'New RFC'
    else:
        title = title.strip()
        refined_title = title
    
    sanitized_title = sanitize_title(title)
    
    rfc_dir = Path('docs/rfc')
    rfc_dir.mkdir(parents=True, exist_ok=True)
    
    filename = f'{sanitized_title}.md'
    filepath = rfc_dir / filename
    
    if filepath.exists():
        counter = 1
        while True:
            new_filename = f'{sanitized_title}-{counter}.md'
            new_filepath = rfc_dir / new_filename
            if not new_filepath.exists():
                filename = new_filename
                filepath = new_filepath
                break
            counter += 1
    
    rfc_content = f"""### RFC: {refined_title}

**Problem Statement:**
[Describe the problem or opportunity that this RFC addresses.]

**Proposed Solution:**
[Describe the proposed solution or approach to address the problem.]

**Discussion:**
[Include any additional considerations, alternatives considered, implementation notes, or open questions.]
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(rfc_content)
    
    return f'Created RFC document: {filepath}' 