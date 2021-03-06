"""Djlint tests for html pre tag.

run:

    pytest tests/test_html/test_tag_pre.py --cov=src/djlint --cov-branch \
          --cov-report xml:coverage.xml --cov-report term-missing

    pytest tests/test_html/test_tag_pre.py::test_pre_tag

"""
# pylint: disable=C0116
from typing import TextIO

from click.testing import CliRunner

from tests.conftest import reformat


def test_pre_tag(runner: CliRunner, tmp_file: TextIO) -> None:
    # added for https://github.com/Riverside-Healthcare/djLint/issues/187
    output = reformat(
        tmp_file,
        runner,
        b"""{% if a %}
    <div>
        <pre><code>asdf</code></pre>
        <pre><code>asdf
            </code></pre>
        <!-- other html -->
        <h2>title</h2>
    </div>
{% endif %}""",
    )
    assert output.exit_code == 0
