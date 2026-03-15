#!/usr/bin/env python3
"""
AutoDraft - Autonomous Research and Drafting Workflow
Hackathon-ready script for AGI House
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


class ModelProvider:
    """Simple abstraction for model providers"""

    def __init__(self, provider_name: str):
        self.provider_name = provider_name.lower()

        if self.provider_name == "openai":
            import openai
            self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview")
        elif self.provider_name == "anthropic":
            import anthropic
            self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            self.model = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5-20250929")
        else:
            raise ValueError(f"Unsupported provider: {provider_name}")

    def generate(self, prompt: str, system: str = None) -> str:
        """Generate text using the configured provider"""

        if self.provider_name == "openai":
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            messages.append({"role": "user", "content": prompt})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=4000
            )
            return response.choices[0].message.content

        elif self.provider_name == "anthropic":
            kwargs = {
                "model": self.model,
                "max_tokens": 4000,
                "temperature": 0.7,
                "messages": [{"role": "user", "content": prompt}]
            }
            if system:
                kwargs["system"] = system

            response = self.client.messages.create(**kwargs)
            return response.content[0].text


class AutoDraft:
    """Main AutoDraft workflow"""

    SCORING_RUBRIC = {
        "clarity": "How clear and understandable is the writing? (1-10)",
        "coherence": "How well do ideas flow and connect? (1-10)",
        "rigor": "How thorough and well-supported are claims? (1-10)",
        "novelty": "How original is the contribution? (1-10)",
        "structure": "How well-organized is the document? (1-10)"
    }

    def __init__(self, provider: ModelProvider, input_dir: Path, output_dir: Path):
        self.provider = provider
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.thesis = None
        self.outline = None
        self.abstract = None
        self.introduction = None
        self.methods = None
        self.critique = None
        self.revised_draft = None
        self.scores = None

    def load_thesis(self):
        """Load the input thesis"""
        thesis_path = self.input_dir / "thesis.md"
        if not thesis_path.exists():
            raise FileNotFoundError(f"Thesis file not found: {thesis_path}")

        self.thesis = thesis_path.read_text().strip()
        print(f"✓ Loaded thesis ({len(self.thesis)} chars)")

    def generate_outline(self):
        """Generate paper outline from thesis"""
        print("\n→ Generating outline...")

        prompt = f"""Given this research thesis:

{self.thesis}

Create a detailed outline for a research paper. Include:
- Main sections (Introduction, Background, Methods, Results, Discussion, Conclusion)
- Key points for each section
- Logical flow of arguments
- Potential subsections

Output the outline in clear markdown format."""

        system = "You are an expert research paper architect. Create structured, logical outlines."

        self.outline = self.provider.generate(prompt, system)
        self._save("outline.md", self.outline)
        print("✓ Outline generated")

    def generate_abstract(self):
        """Generate abstract"""
        print("\n→ Generating abstract...")

        prompt = f"""Research Thesis:
{self.thesis}

Paper Outline:
{self.outline}

Write a concise academic abstract (150-250 words) that:
- States the problem clearly
- Describes the approach
- Summarizes key findings or expected contributions
- Explains significance

Output only the abstract text."""

        system = "You are an expert at writing clear, compelling research abstracts."

        self.abstract = self.provider.generate(prompt, system)
        self._save("abstract.md", self.abstract)
        print("✓ Abstract generated")

    def generate_introduction(self):
        """Generate introduction section"""
        print("\n→ Generating introduction...")

        prompt = f"""Research Thesis:
{self.thesis}

Paper Outline:
{self.outline}

Abstract:
{self.abstract}

Write a comprehensive introduction section that:
- Motivates the problem
- Provides necessary background
- States the research question clearly
- Outlines the contribution
- Previews the paper structure

Write in clear academic prose. Aim for 800-1200 words."""

        system = "You are an expert at writing engaging, rigorous research introductions."

        self.introduction = self.provider.generate(prompt, system)
        self._save("introduction.md", self.introduction)
        print("✓ Introduction generated")

    def generate_methods(self):
        """Generate methods section"""
        print("\n→ Generating methods...")

        prompt = f"""Research Thesis:
{self.thesis}

Paper Outline:
{self.outline}

Write a methods section that:
- Describes the research approach
- Explains key methodologies
- Details experimental design (if applicable)
- Describes evaluation criteria
- Provides enough detail for reproducibility

Write in clear, technical prose. Aim for 600-1000 words."""

        system = "You are an expert at writing clear, reproducible research methods."

        self.methods = self.provider.generate(prompt, system)
        self._save("methods.md", self.methods)
        print("✓ Methods generated")

    def generate_critique(self):
        """Generate critique of current draft"""
        print("\n→ Generating critique...")

        full_draft = f"""# Abstract
{self.abstract}

# Introduction
{self.introduction}

# Methods
{self.methods}
"""

        prompt = f"""Review this research paper draft:

{full_draft}

Original Thesis:
{self.thesis}

Provide a critical analysis addressing:

1. **Structural Issues**
   - Logic gaps
   - Missing transitions
   - Poor sequencing
   - Redundancies

2. **Content Issues**
   - Weak arguments
   - Unsupported claims
   - Ambiguous language
   - Missing evidence

3. **Clarity Issues**
   - Confusing passages
   - Jargon overuse
   - Unclear explanations

4. **Coherence Issues**
   - Disconnect from thesis
   - Inconsistent framing
   - Misaligned sections

Be specific and constructive. Quote problematic passages."""

        system = "You are a rigorous research paper reviewer. Provide sharp, constructive criticism."

        self.critique = self.provider.generate(prompt, system)
        self._save("critique.md", self.critique)
        print("✓ Critique generated")

    def generate_revised_draft(self):
        """Generate revised draft based on critique"""
        print("\n→ Generating revised draft...")

        full_draft = f"""# Abstract
{self.abstract}

# Introduction
{self.introduction}

# Methods
{self.methods}
"""

        prompt = f"""Original Draft:
{full_draft}

Critique:
{self.critique}

Original Thesis:
{self.thesis}

Revise the entire draft addressing all critique points. Produce a cohesive, improved version that:
- Fixes structural issues
- Strengthens weak arguments
- Improves clarity
- Enhances coherence
- Better supports the thesis

Output the full revised draft with all sections."""

        system = "You are an expert research writer. Revise drafts to address critiques while maintaining rigor."

        self.revised_draft = self.provider.generate(prompt, system)
        self._save("revised_draft.md", self.revised_draft)
        print("✓ Revised draft generated")

    def generate_scores(self):
        """Score the revised draft"""
        print("\n→ Generating scores...")

        rubric_text = "\n".join([f"- {k}: {v}" for k, v in self.SCORING_RUBRIC.items()])

        prompt = f"""Revised Draft:
{self.revised_draft}

Original Thesis:
{self.thesis}

Score this draft using the following rubric:
{rubric_text}

For each criterion:
1. Provide a score (1-10)
2. Give a brief justification (2-3 sentences)
3. Suggest one specific improvement

Also provide:
- Overall score (average)
- Summary assessment
- Top 3 strengths
- Top 3 areas for improvement

Format as clear markdown."""

        system = "You are an expert research evaluator. Score papers fairly using explicit criteria."

        self.scores = self.provider.generate(prompt, system)
        self._save("scores.md", self.scores)
        print("✓ Scores generated")

    def _save(self, filename: str, content: str):
        """Save content to output file"""
        path = self.output_dir / filename
        path.write_text(content)
        print(f"  Saved: {path}")

    def run(self):
        """Execute the full AutoDraft workflow"""
        print("=" * 60)
        print("AutoDraft - Autonomous Research Workflow")
        print("=" * 60)

        self.load_thesis()
        self.generate_outline()
        self.generate_abstract()
        self.generate_introduction()
        self.generate_methods()
        self.generate_critique()
        self.generate_revised_draft()
        self.generate_scores()

        print("\n" + "=" * 60)
        print("✓ AutoDraft workflow complete!")
        print(f"  Output directory: {self.output_dir}")
        print("=" * 60)


def main():
    """CLI entry point"""
    # Configuration
    provider_name = os.getenv("MODEL_PROVIDER", "anthropic")
    input_dir = project_root / "input"
    output_dir = project_root / "output"

    # Validate environment
    if provider_name == "openai" and not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not set in .env file")
        sys.exit(1)
    elif provider_name == "anthropic" and not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not set in .env file")
        sys.exit(1)

    # Initialize and run
    try:
        provider = ModelProvider(provider_name)
        autodraft = AutoDraft(provider, input_dir, output_dir)
        autodraft.run()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
