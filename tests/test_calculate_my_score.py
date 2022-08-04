import pytest
from typer.testing import CliRunner

from calculate_my_score.main import app

runner = CliRunner()


@pytest.mark.parametrize(
    "scores, expected",
    [(["80:80", "90:20"], "82.00/100"), (["100:100"], "100.00/100")],
)
def test_app(scores, expected):
    result = runner.invoke(app, scores)
    assert str(expected) in result.output
