import pytest
from unittest.mock import Mock, create_autospec
from src.fsrs_algorithm import FsrsAlgorithm, Rating
from src.scheduler import Scheduler


@pytest.fixture
def mock_fsrs():
    mock = create_autospec(FsrsAlgorithm, instance=True)
    mock.interval.return_value = 7.0
    return mock

def test_scheduler_uses_fsrs_interval(mock_fsrs):
    card = Mock()
    scheduler = Scheduler(algorithm=mock_fsrs)
    scheduler.review(card, Rating.GOOD)
    mock_fsrs.interval.assert_called_once()
