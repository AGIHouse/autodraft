# AutoDraft

**AutoDraft** is an autonomous research and drafting workflow for scientific papers and high-consequence technical writing.

It applies the **autoresearch** paradigm to **research writing**, shifting the human role away from manually dragging every draft into shape and toward defining the governing objective, structure and evaluation logic for a system that can iterate on its own.

In plain English:

You start with a **raw thesis**, **research direction** or **core hypothesis**.  
AutoDraft decomposes that starting point into working parts, drafts against them, critiques the result, refines the structure and pushes toward a more coherent, more defensible and more submission-ready paper.

This is my wholehearted attempt to operationalize autonomous iteration for structured research writing.

## The Why

A lot of serious research still begins in a familiar mess:

- raw notes
- half-formed claims
- scattered references
- voice memos
- paper fragments
- vague hypotheses
- technical insight that is obvious in your head and nowhere else

Then comes the expensive part.

Someone has to turn all that shit into:

- a structured paper
- a coherent research narrative
- a contribution statement
- a methods section that actually reads like one
- a discussion that doesn’t collapse under its own ambiguity

That process is slow, cognitively expensive + usually bottlenecked by human stamina more than human intelligence.

AutoDraft is built around a different model:

**the human defines the arena, the system does the iteration.**

## Core idea

Karpathy’s autoresearch framing matters because it moves the human up a layer.

Instead of manually editing every draft pass yourself, you define:

- the objective
- the constraints
- the structure
- the search space
- the evaluation standard

Then the agent works inside that boundary.

AutoDraft takes that operating model and points it at **paper drafting**.

So instead of:

- editing training code
- running bounded experiments
- keeping validated improvements
- copying and pasting system + update prompts
- manually hot-swapping + daisy-chaining across LLMs
- hitting yout context window at large, later stage passes 

you get:

- decomposing a thesis
- drafting sections
- critiquing coherence, support and clarity
- keeping stronger revisions and discarding weaker ones

## What AutoDraft is

AutoDraft is best thought of as an **autonomous drafting loop for research papers**.

It is designed to turn a raw idea into a more structured paper through:

1. **decomposition**
2. **section planning**
3. **iterative drafting**
4. **critique and refinement**
5. **retention of stronger outputs**

The system is meant to behave less like a one-shot text generator and more like a compact research org.

## What AutoDraft is not

AutoDraft is **not**:

- a generic paper generator
- a citation hallucination machine
- a “write my whole manuscript” button
- a replacement for scientific judgment
- a replacement for authorial taste
- a shortcut around understanding your own work

The aim is narrower and more serious:

**reduce the structural and iterative burden of turning research thought into usable paper drafts.**

## High level workflow

### 1. Start with a thesis

Everything begins with a compact statement of intent.

That might be:

- a thesis
- a central hypothesis
- a research direction
- a problem statement
- a candidate contribution

The initial input can be gnarly. Usually is.

### 2. Decompose the work

AutoDraft breaks the input into the parts required to produce a coherent paper.

That often includes:

- thesis
- problem framing
- background / related work
- methods
- results or expected results
- discussion
- limitations
- conclusion

### 3. Draft against the structure

Once decomposed, the system drafts section by section or block by block.

This matters because the real failure mode in research writing is often not sentence-level prose quality. It’s structural incoherence.

AutoDraft prioritizes internal logic before polish.

### 4. Critique and refine

A first draft is not the point.

The system can review its own output for:

- weak logic
- unsupported jumps
- missing transitions
- ambiguous technical language
- redundant sections
- poor sequencing
- contribution blur
- hand-wavy discussion

Then it revises.

### 5. Retain stronger outputs

The point is not endless rewriting.  
The point is directional improvement.

Each iteration should move the draft toward:

- clearer structure
- stronger articulation
- better support
- tighter argument flow
- more usable output for a human reviewer

## Paper workflow

AutoDraft is built to function as a paper drafting engine by starting with a thesis and building outward.

### Example flow

1. input thesis
2. identify core contributions
3. define major sections
4. map evidence and references to each section
5. draft each section
6. run critique pass
7. refine argument flow
8. produce a consolidated draft

### Typical outputs

- abstract draft
- introduction draft
- methods scaffold
- results scaffold
- discussion scaffold
- contribution summary
- literature-backed research memo
- full draft skeleton
- revision suggestions

## Research org framing

One of the more important ideas behind AutoDraft is that the human is no longer just writing text.

The human is defining the **research org logic**.

That includes:

- what the system is trying to produce
- how it should decompose the problem
- what counts as improvement
- what kinds of revisions are allowed
- what standards should govern critique

This is the real shift.

You are no longer only drafting.  
You are programming the drafting organization.

## Why this matters

The significance of this approach is not that AI can write paragraphs. Everybody knows that already.

The significance is that **autonomous iteration can be applied to research writing**, not just model training loops.

That opens up a new operating model for:

- researchers
- labs
- deep-tech teams
- solo founders writing technical papers
- applied scientists
- anyone turning raw technical thinking into structured manuscripts

The bottleneck becomes less about first-pass generation and more about whether the research org itself is well designed.

## Design philosophy

AutoDraft is built around a few assumptions.

### Structure before polish

A technically correct paragraph in the wrong place is still bad writing.

### Iteration beats one-shot generation

The right draft usually emerges through refinement, not first-pass magic.

### Raw input is normal

Notes are allowed to be chaotic. The system exists because they usually are.

### Research writing needs operational discipline

Artifact quality matters because the ideas do.

### Human judgment still matters

AutoDraft can compress labor. It does not remove the need for actual scientific judgment.

## Who this is for

AutoDraft is relevant to people doing work where structure, precision and iteration actually matter.

### Good fit

- researchers
- deep-tech founders writing technical papers
- applied scientists
- independent builders publishing research
- technical strategists
- labs exploring autonomous research workflows

### Bad fit

- casual content generation
- generic marketing copy
- low-precision writing tasks
- users expecting zero oversight on serious technical output

## Example use cases

### Research paper draft from thesis

Input:

> We hypothesize that multimodal neural signal fusion improves noninvasive cognitive state classification under noisy real-world conditions.

Potential outputs:

- abstract
- introduction scaffold
- methods structure
- contribution framing
- limitations section
- next revision pass

### Position paper from research direction

Input:

> Frontier AI systems need provenance-aware autonomous drafting loops for scientific communication.

Potential outputs:

- problem framing
- thesis articulation
- supporting arguments
- section outline
- draft introduction
- concluding synthesis

### Experimental paper from rough notes

Input:

> Notes on model performance, ablations, signal preprocessing and observed tradeoffs across runs.

Potential outputs:

- result organization
- methods cleanup
- findings summary
- discussion structure
- draft-ready narrative flow

## Roadmap direction

Potential future directions include:

- explicit programmatic drafting specs
- configurable critique agents
- evaluation logic for paper quality
- provenance and revision tracking
- citation-aware drafting flows
- section-specific drafting modes
- stronger literature synthesis
- human-in-the-loop review layers

## Current thesis

The broader thesis behind this repo is simple:

**paper drafting is research work.**  
It deserves the same level of operational rigor, iteration design and agent orchestration now being applied to code and model experimentation.

Karpathy’s autoresearch paradigm showed that the human can move from directly conducting experiments to defining the operating structure that governs them.

AutoDraft asks:

**what happens when that same shift is applied to papers?**

## Status

Early, but serious.

This repo is a working exploration of autonomous drafting as a research operating model, not just a prompt demo or wrapper UI.

## Contributing

If you are interested in:

- autonomous research systems
- paper drafting automation
- structured critique loops
- agentic writing systems
- research workflow design

open an issue, fork the repo or reach out.

Good ideas welcome. Sharp criticism also welcome.

## License

MIT
