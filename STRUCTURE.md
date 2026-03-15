# AutoDraft Project Structure

```
autodraft/
├── README.md                    # Project overview and philosophy
├── QUICKSTART.md                # 3-minute setup guide
├── STRUCTURE.md                 # This file - project structure
├── program.md                   # Program specification
├── .env.example                 # Environment configuration template
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
│
├── input/                       # Research inputs
│   ├── thesis.md               # Core research thesis/hypothesis
│   ├── notes.md                # Supporting notes and ideas
│   └── references.md           # Literature and citations
│
├── prompts/                     # Prompt templates
│   ├── system.md               # System prompt
│   ├── decompose.md            # Outline generation
│   ├── draft_abstract.md       # Abstract drafting
│   ├── draft_introduction.md   # Introduction drafting
│   ├── draft_methods.md        # Methods drafting
│   ├── critique.md             # Critique generation
│   ├── revise.md               # Revision prompt
│   └── score.md                # Scoring prompt
│
├── output/                      # Generated outputs
│   ├── outline.md              # Paper outline
│   ├── abstract.md             # Abstract draft
│   ├── introduction.md         # Introduction draft
│   ├── methods.md              # Methods draft
│   ├── draft_full.md           # Compiled full draft
│   ├── critique.md             # Critique analysis
│   ├── revised_draft.md        # Revised draft
│   ├── scores.md               # Evaluation scores
│   └── run_log.json            # Run metadata
│
├── scripts/                     # Core implementation
│   ├── run_loop.py             # Main workflow script
│   ├── providers.py            # LLM provider abstraction
│   ├── scoring.py              # Scoring rubric and logic
│   └── utils.py                # Utility functions
│
├── examples/                    # Sample inputs and outputs
│   ├── sample_thesis.md        # Example thesis
│   └── sample_output/          # Example generated output
│       ├── outline.md
│       ├── abstract.md
│       └── revised_draft.md
│
└── .claude/                     # Claude Code settings
    └── settings.local.json     # Project metadata
```

## Key Components

### Input Layer
- **thesis.md**: Your research idea, hypothesis, or core contribution
- **notes.md**: Supporting research notes and observations
- **references.md**: Relevant literature and citations

### Processing Layer
- **prompts/**: Modular prompt templates for each workflow stage
- **scripts/**: Modular Python implementation
  - `providers.py`: Multi-provider support (OpenAI, Anthropic, Hyperbolic)
  - `scoring.py`: Explicit evaluation rubrics
  - `utils.py`: File I/O and logging utilities
  - `run_loop.py`: Main orchestration

### Output Layer
- **output/**: All generated artifacts
  - Draft sections (outline, abstract, intro, methods)
  - Full draft compilation
  - Critique analysis
  - Revised draft
  - Quantitative scores
  - Run logs (JSON)

## Workflow

```
thesis.md → decompose → outline
                          ↓
                        abstract
                          ↓
                      introduction
                          ↓
                        methods
                          ↓
                      draft_full
                          ↓
                       critique
                          ↓
                    revised_draft
                          ↓
                        scores
```

## Configuration

All configuration is environment-based via `.env`:
- `MODEL_PROVIDER`: openai, anthropic, or hyperbolic
- Provider-specific API keys and model selections

## Modularity

The architecture is designed for easy extension:
- Add new sections by creating prompt templates
- Swap providers by implementing provider interface
- Customize scoring by editing rubrics in `scoring.py`
- Modify prompts without touching code
