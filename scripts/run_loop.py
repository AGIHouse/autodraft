#!/usr/bin/env python3
"""
AutoDraft - Autonomous Research and Drafting Workflow
Refactored modular version
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.providers import ModelProvider, validate_provider_config
from scripts.scoring import format_rubric
from scripts.utils import (
    load_file, save_file, load_prompt_template, fill_prompt_template,
    log_run, print_header, print_step, print_success, print_error
)


class AutoDraft:
    """Main AutoDraft workflow using prompt templates"""

    def __init__(self, provider: ModelProvider, project_root: Path):
        self.provider = provider
        self.project_root = project_root
        self.input_dir = project_root / "input"
        self.output_dir = project_root / "output"
        self.prompts_dir = project_root / "prompts"

        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Input data
        self.thesis = None
        self.notes = None
        self.references = None

        # Generated outputs
        self.outline = None
        self.abstract = None
        self.introduction = None
        self.methods = None
        self.full_draft = None
        self.critique = None
        self.revised_draft = None
        self.scores = None

    def load_inputs(self):
        """Load all input files"""
        print_step("Loading inputs")

        self.thesis = load_file(self.input_dir / "thesis.md")
        self.notes = load_file(self.input_dir / "notes.md")
        self.references = load_file(self.input_dir / "references.md")

        if not self.thesis:
            raise FileNotFoundError("thesis.md is empty or missing")

        print_success(f"Loaded thesis ({len(self.thesis)} chars)")
        if self.notes:
            print_success(f"Loaded notes ({len(self.notes)} chars)")
        if self.references:
            print_success(f"Loaded references ({len(self.references)} chars)")

    def generate_outline(self):
        """Generate paper outline from thesis"""
        print_step("Generating outline")

        template = load_prompt_template("decompose", self.project_root)
        prompt = fill_prompt_template(
            template,
            thesis=self.thesis,
            notes=self.notes or "No additional notes provided."
        )
        system = load_file(self.prompts_dir / "system.md")

        self.outline = self.provider.generate(prompt, system)
        save_file(self.output_dir / "outline.md", self.outline)
        print_success("Outline generated")

    def generate_abstract(self):
        """Generate abstract"""
        print_step("Generating abstract")

        template = load_prompt_template("draft_abstract", self.project_root)
        prompt = fill_prompt_template(
            template,
            thesis=self.thesis,
            outline=self.outline
        )
        system = load_file(self.prompts_dir / "system.md")

        self.abstract = self.provider.generate(prompt, system)
        save_file(self.output_dir / "abstract.md", self.abstract)
        print_success("Abstract generated")

    def generate_introduction(self):
        """Generate introduction section"""
        print_step("Generating introduction")

        template = load_prompt_template("draft_introduction", self.project_root)
        prompt = fill_prompt_template(
            template,
            thesis=self.thesis,
            outline=self.outline,
            abstract=self.abstract,
            references=self.references or "No references provided."
        )
        system = load_file(self.prompts_dir / "system.md")

        self.introduction = self.provider.generate(prompt, system)
        save_file(self.output_dir / "introduction.md", self.introduction)
        print_success("Introduction generated")

    def generate_methods(self):
        """Generate methods section"""
        print_step("Generating methods")

        template = load_prompt_template("draft_methods", self.project_root)
        prompt = fill_prompt_template(
            template,
            thesis=self.thesis,
            outline=self.outline,
            notes=self.notes or "No additional notes provided."
        )
        system = load_file(self.prompts_dir / "system.md")

        self.methods = self.provider.generate(prompt, system)
        save_file(self.output_dir / "methods.md", self.methods)
        print_success("Methods generated")

    def compile_full_draft(self):
        """Compile full draft from sections"""
        print_step("Compiling full draft")

        self.full_draft = f"""# Abstract
{self.abstract}

# Introduction
{self.introduction}

# Methods
{self.methods}
"""
        save_file(self.output_dir / "draft_full.md", self.full_draft)
        print_success("Full draft compiled")

    def generate_critique(self):
        """Generate critique of current draft"""
        print_step("Generating critique")

        template = load_prompt_template("critique", self.project_root)
        prompt = fill_prompt_template(
            template,
            full_draft=self.full_draft,
            thesis=self.thesis
        )
        system = load_file(self.prompts_dir / "system.md")

        self.critique = self.provider.generate(prompt, system)
        save_file(self.output_dir / "critique.md", self.critique)
        print_success("Critique generated")

    def generate_revised_draft(self):
        """Generate revised draft based on critique"""
        print_step("Generating revised draft")

        template = load_prompt_template("revise", self.project_root)
        prompt = fill_prompt_template(
            template,
            full_draft=self.full_draft,
            critique=self.critique,
            thesis=self.thesis
        )
        system = load_file(self.prompts_dir / "system.md")

        self.revised_draft = self.provider.generate(prompt, system)
        save_file(self.output_dir / "revised_draft.md", self.revised_draft)
        print_success("Revised draft generated")

    def generate_scores(self):
        """Score the revised draft"""
        print_step("Generating scores")

        template = load_prompt_template("score", self.project_root)
        prompt = fill_prompt_template(
            template,
            revised_draft=self.revised_draft,
            thesis=self.thesis
        )
        system = load_file(self.prompts_dir / "system.md")

        self.scores = self.provider.generate(prompt, system)
        save_file(self.output_dir / "scores.md", self.scores)
        print_success("Scores generated")

    def log_run_info(self, provider_name: str):
        """Log run information"""
        log_data = {
            "provider": provider_name,
            "model": self.provider.model,
            "thesis_length": len(self.thesis),
            "outputs_generated": [
                "outline.md",
                "abstract.md",
                "introduction.md",
                "methods.md",
                "draft_full.md",
                "critique.md",
                "revised_draft.md",
                "scores.md"
            ]
        }
        log_run(log_data, self.output_dir)

    def run(self, provider_name: str):
        """Execute the full AutoDraft workflow"""
        print_header("AutoDraft - Autonomous Research Workflow")

        self.load_inputs()
        self.generate_outline()
        self.generate_abstract()
        self.generate_introduction()
        self.generate_methods()
        self.compile_full_draft()
        self.generate_critique()
        self.generate_revised_draft()
        self.generate_scores()
        self.log_run_info(provider_name)

        print()
        print_header("✓ AutoDraft workflow complete!")
        print(f"  Output directory: {self.output_dir}")
        print("=" * 60)


def main():
    """CLI entry point"""
    # Configuration
    provider_name = os.getenv("MODEL_PROVIDER", "anthropic")

    # Validate environment
    if not validate_provider_config(provider_name):
        print_error(f"{provider_name.upper()}_API_KEY not set in .env file")
        print(f"\nPlease set your API key in .env:")
        print(f"  MODEL_PROVIDER={provider_name}")
        print(f"  {provider_name.upper()}_API_KEY=your_key_here")
        sys.exit(1)

    # Initialize and run
    try:
        provider = ModelProvider(provider_name)
        autodraft = AutoDraft(provider, project_root)
        autodraft.run(provider_name)
    except FileNotFoundError as e:
        print_error(str(e))
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
