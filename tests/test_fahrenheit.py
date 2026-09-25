import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from temperature import celsius_to_fahrenheit


@pytest.mark.parametrize(
    ("celsius", "fahrenheit"),
    [(-40, -40), (0, 32), (100, 212)],
)
def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert celsius_to_fahrenheit(celsius) == fahrenheit
