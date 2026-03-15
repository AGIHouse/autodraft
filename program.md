# AutoDraft Program Specification

## Purpose

AutoDraft is an autonomous research drafting system that transforms raw research ideas into structured academic papers through iterative decomposition, drafting, critique, and revision.

## Core Workflow

1. **Decompose** - Break thesis into structured outline
2. **Draft** - Generate section-by-section content
3. **Critique** - Analyze structural and content issues
4. **Revise** - Improve based on critique
5. **Score** - Evaluate against explicit rubric

## System Architecture

### Input Layer
- `thesis.md` - Core research idea/hypothesis
- `notes.md` - Supporting notes and ideas
- `references.md` - Literature and citations

### Processing Layer
- Prompt-driven generation using configurable LLM providers
- Sequential section drafting (outline → abstract → intro → methods)
- Self-critique loop
- Revision engine

### Output Layer
- Structured drafts (outline, abstract, introduction, methods)
- Full draft compilation
- Critique analysis
- Revised draft
- Quantitative scores
- Run logs (JSON)

## Design Principles

1. **Modularity** - Separate prompts, logic, and providers
2. **Transparency** - Explicit scoring rubrics and critique criteria
3. **Configurability** - Support multiple LLM providers
4. **Iteration** - Built for refinement cycles
5. **Simplicity** - Hackathon-ready, no over-engineering

## Scoring Rubric

- **Clarity** (1-10): Writing understandability
- **Coherence** (1-10): Logical flow and connection
- **Rigor** (1-10): Claim support and thoroughness
- **Novelty** (1-10): Contribution originality
- **Structure** (1-10): Document organization

## Extension Points

- Custom prompt templates
- Additional section types
- Multi-iteration loops
- Citation integration
- Literature synthesis
