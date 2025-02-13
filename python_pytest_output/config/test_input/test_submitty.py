import sys

import pytest


def test_hello_world(capsys):
    # Import here so the print statement is executed inside the test function
    import submission  # noqa: F401

    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n", "Program output does not match expected"


if __name__ == "__main__":
    exit_code = pytest.main(["--tb=short", "--no-header", "test_submitty.py"])
    print(exit_code, file=sys.stderr)
    sys.exit(int(exit_code.value))
