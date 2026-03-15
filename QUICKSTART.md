# AutoDraft - Quickstart Guide

Get AutoDraft running in 3 minutes for the AGI House Hackathon.

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment

Copy the example env file:
```bash
cp .env.example .env
```

Edit `.env` and add your API key:

**For Anthropic (default):**
```bash
MODEL_PROVIDER=anthropic
ANTHROPIC_API_KEY=your_key_here
ANTHROPIC_MODEL=claude-sonnet-4-5-20250929
```

**For OpenAI:**
```bash
MODEL_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4-turbo-preview
```

### 3. Add your thesis

Edit `input/thesis.md` with your research idea, hypothesis, or thesis.

## Run

```bash
python scripts/run_loop.py
```

## Outputs

The script generates 7 files in `output/`:

1. **outline.md** - Paper structure and logical flow
2. **abstract.md** - Concise summary (150-250 words)
3. **introduction.md** - Problem motivation and framing
4. **methods.md** - Research approach and methodology
5. **critique.md** - Critical analysis of the draft
6. **revised_draft.md** - Improved version addressing critique
7. **scores.md** - Evaluation using explicit rubric

## Scoring Rubric

The system evaluates drafts on:
- **Clarity** (1-10): How understandable is the writing?
- **Coherence** (1-10): How well do ideas flow and connect?
- **Rigor** (1-10): How thorough and well-supported are claims?
- **Novelty** (1-10): How original is the contribution?
- **Structure** (1-10): How well-organized is the document?

## Workflow

```
thesis.md → outline → abstract → introduction → methods
                                                    ↓
                                                critique
                                                    ↓
                                            revised_draft
                                                    ↓
                                                 scores
```

## Tips

- Start with a clear, specific thesis
- Keep your thesis under 500 words for best results
- Review outputs iteratively
- Use the critique to understand weaknesses
- Check scores for quantitative assessment

## Troubleshooting

**Import errors?**
```bash
pip install -r requirements.txt
```

**API key issues?**
```bash
# Check your .env file exists and has the right keys
cat .env
```

**No output?**
```bash
# Check the output/ directory was created
ls -la output/
```

## Hackathon Notes

This is a lean, hackathon-ready implementation. Future enhancements:
- Parallel generation for speed
- Configurable section generation
- Citation integration
- Multi-iteration refinement loops
- Human-in-the-loop review
- Custom rubric definitions
