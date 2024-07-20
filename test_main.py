import pytest
from main import create_range

@pytest.mark.parametrize("input_str, expected_output", [
    ("<=6.3.3, >3.1.0", "[3.1.1, 6.3.3]"),
    ("<=1.0.0, >1.0.0", "[1.0.1, 1.0.0]"),
    (">2.1.0, <3.0.0", "(2.1.1, 2.9.9)"),
    (">=2.0.0, <=2.0.0", "[2.0.0, 2.0.0]"),
    (">1.1.1, <1.2.0", "(1.1.2, 1.1.9)")
])
def test_create_range(input_str, expected_output):
    assert create_range(input_str) == expected_output

if __name__ == "__main__":
    pytest.main()
