from typing import List

import rich
import typer

app = typer.Typer()


@app.command()
def main(
    scores: List[str] = typer.Argument(
        ...,
        show_default=False,
        help="Pairs of score in the format of SCORE:WEIGHT",
    )
):
    """Calculate your score in a course."""
    score_pairs = [map(float, score.split(":")) for score in scores]
    scores_for_weight, total = 0.0, 0.0
    for score, weight in score_pairs:
        total += weight
        scores_for_weight += score * weight
    score_made = scores_for_weight / total
    rich.print(f"🎉 Your score is {score_made:.2f}/{total:.0f} 🎉 ")
