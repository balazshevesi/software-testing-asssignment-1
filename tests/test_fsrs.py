import pytest
from src.fsrs_algorithm import FsrsAlgorithm, Rating
from unittest.mock import Mock, create_autospec

# FSRS formulas
# R(t, s) = (1+ FACTOR * t / S) ** Decay
# I(S, r) = S / Factor * (r** (1 / Decay) - 1)
# S0(G) = w[G - 1]
# D0(G) = calmp(w[4] - (G - 3) * w[5], 1, 10)
