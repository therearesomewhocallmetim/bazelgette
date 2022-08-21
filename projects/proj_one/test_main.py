import pytest
import sys
import random
import time


def test_main():
    # raise RuntimeError(f"Current system version is {sys.version}")
    time.sleep(5)
    assert random.choice([True, False, False])


if __name__ == "__main__":
    sys.exit(pytest.main())
