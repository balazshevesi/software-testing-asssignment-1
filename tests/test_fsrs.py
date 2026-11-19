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

@pytest_fixture
def fsrs():
    return FsrsAlgorithm(weights=TEST_weigts)
