import argparse
import sys
from . import init_command
from .adr import create_adr
from .rfc import create_rfc
from .generate_diagrams import generate_er_diagram, generate_architecture_diagram
from .ai_update_docs import update_docs_ai
from .check_docs import check_docs, check_specific_file, check_category
from .ai_config import init_ai_config
from . import __version__

def _handle_check_docs(args):
    """Handle check-docs command and return appropriate exit code."""
    if args.file:
        return check_specific_file(args.file)
    elif args.category:
        return check_category(args.category)
    else:
        return check_docs()

def main():
    parser = argparse.ArgumentParser(description="AI-powered Cursor Init CLI for documentation management.")
    parser.add_argument("--version", action="version", version=f"ai-cursor-init {__version__}")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Init command
    init_parser = subparsers.add_parser("init", help="Generate initial project documentation using AI.")
    init_parser.set_defaults(func=init_command.initialize_docs)

    # Configure AI providers command
    config_parser = subparsers.add_parser("configure", help="Configure AI providers and settings.")
    config_parser.set_defaults(func=lambda args: init_ai_config())

    # ADR command
    adr_parser = subparsers.add_parser("adr", help="Create a new Architecture Decision Record using AI.")
    adr_parser.add_argument("title", nargs='?', default="untitled-adr",
                            help="Title of the ADR. Defaults to 'untitled-adr' if not provided.")
    adr_parser.add_argument("--context", type=str, default="",
                            help="Optional context to help AI generate better ADR content.")
    adr_parser.set_defaults(func=lambda args: create_adr(title=args.title, context=args.context))

    # RFC command
    rfc_parser = subparsers.add_parser("rfc", help="Create a new Request For Comments document.")
    rfc_parser.add_argument("title", nargs='?', default="new-rfc",
                            help="Title of the RFC. Defaults to 'new-rfc' if not provided.")
    rfc_parser.set_defaults(func=lambda args: create_rfc(title=args.title))

    # Generate ER Diagram command
    er_diagram_parser = subparsers.add_parser("gen-er-diagram", help="Generate an ER diagram from SQLAlchemy models.")
    er_diagram_parser.set_defaults(func=lambda args: generate_er_diagram())

    # Generate Architecture Diagram command
    arch_diagram_parser = subparsers.add_parser("gen-arch-diagram", help="Generate an architecture diagram from project structure.")
    arch_diagram_parser.set_defaults(func=lambda args: generate_architecture_diagram())

    # AI-powered update documentation command
    update_parser = subparsers.add_parser("update", help="AI-powered documentation analysis and updates.")
    update_parser.add_argument("--apply", action="store_true", 
                              help="Apply AI-generated changes automatically. If not provided, only shows what would be updated.")
    update_parser.add_argument("--file", type=str, 
                              help="Update only a specific file by name (e.g., architecture.md, 0001-record-architecture-decisions.md)")
    update_parser.add_argument("--category", type=str, 
                              help="Update all files within a specific category (e.g., adr, onboarding, architecture, data-model)")
    update_parser.add_argument("--provider", type=str, choices=['openai', 'anthropic', 'azure_openai'],
                              help="Specify AI provider (defaults to auto-detect based on available API keys)")
    update_parser.set_defaults(func=lambda args: update_docs_ai(apply_changes=args.apply, specific_file=args.file, category=args.category, provider_override=getattr(args, 'provider', None)))

    # Check documentation freshness command
    check_parser = subparsers.add_parser("check-docs", help="Check documentation for freshness and completeness (CI-friendly).")
    check_parser.add_argument("--file", type=str, 
                             help="Check only a specific file by path (e.g., docs/architecture.md)")
    check_parser.add_argument("--category", type=str, 
                             help="Check all files within a specific category (e.g., adr, onboarding, architecture, data-model)")
    check_parser.set_defaults(func=lambda args: _handle_check_docs(args))

    args = parser.parse_args()

    if hasattr(args, "func"):
        if args.command == "check-docs":
            # Handle check-docs command with proper exit code
            exit_code = args.func(args)
            sys.exit(exit_code)
        elif args.command in ["adr", "rfc", "gen-er-diagram", "gen-arch-diagram", "update", "configure"]:
            print(args.func(args))
        else:
            args.func()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
