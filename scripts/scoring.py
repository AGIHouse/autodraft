"""
Scoring rubric and evaluation logic for AutoDraft
"""

SCORING_RUBRIC = {
    "clarity": {
        "name": "Clarity",
        "description": "How clear and understandable is the writing?",
        "scale": {
            "1-3": "Confusing, impenetrable",
            "4-6": "Somewhat clear, some confusion",
            "7-8": "Clear, minor issues",
            "9-10": "Exceptionally clear"
        }
    },
    "coherence": {
        "name": "Coherence",
        "description": "How well do ideas flow and connect?",
        "scale": {
            "1-3": "Disjointed, no clear flow",
            "4-6": "Reasonable flow, some gaps",
            "7-8": "Good flow, well-connected",
            "9-10": "Seamless logical progression"
        }
    },
    "rigor": {
        "name": "Rigor",
        "description": "How thorough and well-supported are claims?",
        "scale": {
            "1-3": "Weak support, many gaps",
            "4-6": "Adequate support, some gaps",
            "7-8": "Well-supported, minor gaps",
            "9-10": "Exceptionally rigorous"
        }
    },
    "novelty": {
        "name": "Novelty",
        "description": "How original is the contribution?",
        "scale": {
            "1-3": "Derivative, no clear novelty",
            "4-6": "Incremental contribution",
            "7-8": "Solid novel contribution",
            "9-10": "Groundbreaking"
        }
    },
    "structure": {
        "name": "Structure",
        "description": "How well-organized is the document?",
        "scale": {
            "1-3": "Poorly organized",
            "4-6": "Adequate organization",
            "7-8": "Well-organized",
            "9-10": "Exemplary structure"
        }
    }
}


def format_rubric() -> str:
    """Format the scoring rubric as a string"""
    lines = ["## Scoring Rubric\n"]

    for key, criterion in SCORING_RUBRIC.items():
        lines.append(f"### {criterion['name']} (1-10)")
        lines.append(criterion['description'])
        for range_desc, desc in criterion['scale'].items():
            lines.append(f"- {range_desc}: {desc}")
        lines.append("")

    return "\n".join(lines)


def parse_scores(score_text: str) -> dict:
    """Parse scores from generated score text (basic extraction)"""
    # This is a simple implementation
    # In production, you'd use more robust parsing
    scores = {}

    for criterion in SCORING_RUBRIC.keys():
        # Look for patterns like "Clarity: 8/10" or "Clarity (1-10): 8"
        # This is a placeholder - actual implementation would be more robust
        scores[criterion] = None

    return scores
