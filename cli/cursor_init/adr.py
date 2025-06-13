import re
import os
from .config import load_config

def create_adr(title: str = "untitled-adr", context: str = "") -> str:
    """
    Creates a new Architecture Decision Record (ADR) file.

    Args:
        title: The title of the ADR. Defaults to "untitled-adr".
        context: Optional context to pre-fill the ADR.

    Returns:
        A success message including the path to the newly created ADR.
    """
    adr_dir = "docs/adr/"
    os.makedirs(adr_dir, exist_ok=True)
    
    config = load_config()
    template_path = config.get_template_path('adr')
    if not template_path or not os.path.exists(template_path):
        template_path = "templates/adr/adr_template_nygard.md"

    next_adr_number = _get_next_adr_number(adr_dir)
    sanitized_title = _sanitize_title(title)
    filename = f"{next_adr_number:04d}-{sanitized_title}.md"
    file_path = os.path.join(adr_dir, filename)

    adr_content = _generate_adr_content(next_adr_number, title, template_path, context)

    with open(file_path, "w") as f:
        f.write(adr_content)

    return f"Successfully created ADR: {file_path}"

def _get_next_adr_number(adr_dir: str) -> int:
    """
    Determines the next sequential ADR number by scanning the adr_dir.
    """
    max_number = 0
    if os.path.exists(adr_dir):
        for filename in os.listdir(adr_dir):
            match = re.match(r"(\d{4})-.*\.md", filename)
            if match:
                max_number = max(max_number, int(match.group(1)))
    return max_number + 1

def _sanitize_title(title: str) -> str:
    """
    Sanitizes the title to be lowercase and kebab-case.
    """
    title = title.lower()
    title = re.sub(r"[^a-z0-9\s-]", "", title)
    title = re.sub(r"\s+", "-", title)
    return title.strip("-")

def _generate_adr_content(adr_number: int, title: str, template_path: str, context: str) -> str:
    """
    Generates the content for the ADR file by loading from a template and populating placeholders.
    """
    with open(template_path, "r") as f:
        template_content = f.read()

    adr_content = template_content.replace("{{ADR_NUMBER}}", f"{adr_number:04d}")
    adr_content = adr_content.replace("{{ADR_TITLE}}", title)
    adr_content = adr_content.replace("{{CONTEXT}}", context)

    return adr_content 