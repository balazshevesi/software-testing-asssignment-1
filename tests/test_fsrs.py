import pytest
from src.fsrs_algorithm import FsrsAlgorithm, Rating
from unittest.mock import Mock, create_autospec

# FSRS formulas
# R(t, s) = (1+ FACTOR * t / S) ** Decay
# I(S, r) = S / Factor * (r** (1 / Decay) - 1)
# S0(G) = w[G - 1]
# D0(G) = calmp(w[4] - (G - 3) * w[5], 1, 10)

TEST_weigts = [
    0.5, 1.5, 4.0, 14.0,  # w0-w3 initial stability for again, hard, good, easy
    5.0, 1.0, # w4, w5 initial difficulty
    0.9, 0.03, 1.6, 0.14, 1.0, 2.1, 0.08, 0.32, 1.6, 0.23, 2.9,
]

@pytest.fixture
def fsrs():
    return FsrsAlgorithm(weights=TEST_weigts)

def test_rating_values():
    assert Rating.AGAIN == 1
    assert Rating.HARD == 2
    assert Rating.GOOD == 3
    assert Rating.EASY == 4

def test_mock_weights_used():
    assert fsrs.weights == TEST_weigts

@pytest.mark.parametrize("weights", [[], [1.0] * 16, [1.0] * 18])
def test_wrong_number_of_weights(weights):
    with pytest.raises(ValueError):
        FsrsAlgorithm(weights=weights)

def test_retrievability_decreases_over_time(fsrs):
    r1 = fsrs.retrievability(elapsed_days=1, stability=10.0)
    r5 = fsrs.retrievability(elapsed_days=5, stability=10.0)
    r30 = fsrs.retrievability(elapsed_days=30, stability=10.0)
    assert 1.0 > r1 > r5 > r30 > 0.0

def test_higher_stability_means_higher_retrievability(fsrs):
    low = fsrs.retrievability(elapsed_days=5, stability=2.0)
    high = fsrs.retrievability(elapsed_days=5, stability=20.0)
    assert high > low

def test_interval_known_value(fsrs):
    # 10 / (19/81) * (0.8 ** -2 - 1) = 23.9802...
    assert fsrs.interval(stability=10.0, desired_retention=0.8) == pytest.approx(23.9802, rel=1e-4)

def test_interval_inverse_of_retrievability(fsrs):
    days = fsrs.interval(stability=7.0, desired_retention=0.85)
    assert fsrs.retrievability(elapsed_days=days, stability=7.0) == pytest.approx(0.85)

# Boundary values: retention must be strictly between 0 and 1.
@pytest.mark.parametrize("retention", [-0.1, 0.0, 1.0, 1.1])
def test_interval_invalid_retention_error(fsrs, retention):
    with pytest.raises(ValueError):
        fsrs.interval(stability=10.0, desired_retention=retention)
