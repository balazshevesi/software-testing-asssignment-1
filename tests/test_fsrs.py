import pytest
from src.fsrs_algorithm import FsrsAlgorithm, Rating
from unittest.mock import Mock, create_autospec

fsrs = create_autospec(FsrsAlgorithm, instance=True)
fsrs.interval.return_value = 7.0
fsrs.interval(12.0, 0.9)
fsrs

@pytest.fixture
def fsrs():
    return