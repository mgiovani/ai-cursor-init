import os
import re

def detect_project_frameworks(project_root: str = ".") -> dict:
    """
    Detects the primary languages and frameworks of the project.

    Args:
        project_root: The root directory of the project.

    Returns:
        A dictionary containing detected languages and frameworks.
        Example: {'languages': {'python', 'typescript'}, 'frameworks': {'fastapi', 'react', 'sqlalchemy'}}
    """
    detected_languages = set()
    detected_frameworks = set()

    # Files to check for language/framework presence
    python_indicators = ["requirements.txt", "pyproject.toml"]
    typescript_indicators = ["package.json", "tsconfig.json"]

    # Walk through the project directory to detect indicators
    for root, dirs, files in os.walk(project_root):
        # Limit depth to avoid scanning entire large projects
        if root.count(os.sep) - project_root.count(os.sep) > 3:  # Increased depth slightly for better scanning
            del dirs[:]
            continue

        # Language Detection
        for indicator in python_indicators:
            if indicator in files:
                detected_languages.add("python")
        for indicator in typescript_indicators:
            if indicator in files:
                detected_languages.add("typescript")

        for file in files:
            if file.endswith(".py"):
                detected_languages.add("python")
                # FastAPI and SQLAlchemy detection within Python files
                try:
                    with open(os.path.join(root, file), "r", errors="ignore") as f:
                        content = f.read(10000)  # Read first 10KB for efficiency
                        if "from fastapi import FastAPI" in content or "import fastapi" in content:
                            detected_frameworks.add("fastapi")
                        if "import sqlalchemy" in content or "from sqlalchemy" in content or \
                           re.search(r'(Base|DeclarativeBase)', content):
                            detected_frameworks.add("sqlalchemy")
                except Exception: # Catch permission or reading errors
                    pass

            elif file.endswith((".ts", ".tsx", ".js", ".jsx")):
                detected_languages.add("typescript")

        # Framework detection via package.json for JS/TS projects
        if "package.json" in files:
            try:
                import json
                with open(os.path.join(root, "package.json"), "r", errors="ignore") as f:
                    package_json = json.load(f)
                    dependencies = package_json.get("dependencies", {})
                    dev_dependencies = package_json.get("devDependencies", {})

                    if "react" in dependencies or "react" in dev_dependencies:
                        detected_frameworks.add("react")
                    if "next" in dependencies or "next" in dev_dependencies:
                        detected_frameworks.add("next.js")

            except Exception:
                pass # Ignore JSON parsing errors or file not found
        
        # Check for specific directories for frameworks
        if "pages" in dirs and "typescript" in detected_languages: # Next.js specific dir
            detected_frameworks.add("next.js")

    # Further checks based on detected languages and frameworks
    # If Python is detected, check requirements.txt/pyproject.toml for framework names
    if "python" in detected_languages:
        for req_file in [f for f in files if f in python_indicators]:
            try:
                with open(os.path.join(root, req_file), "r", errors="ignore") as f:
                    content = f.read()
                    if "fastapi" in content:
                        detected_frameworks.add("fastapi")
                    if "sqlalchemy" in content:
                        detected_frameworks.add("sqlalchemy")
            except Exception:
                pass

    return {"languages": detected_languages, "frameworks": detected_frameworks} 