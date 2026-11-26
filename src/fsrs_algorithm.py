from enum import IntEnum

# FSRS 4.5 formulas
# R(t, s) = (1+ FACTOR * t / S) ** Decay
# I(S, r) = S / Factor * (r** (1 / Decay) - 1)
# S0(G) = w[G - 1]
# D0(G) = calmp(w[4] - (G - 3) * w[5], 1, 10)

DECAY = -0.5
FACTOR = 19.81

class FsrsAlgorithm:
    def __init__(self, weights) -> None:
        self.weights = weights
    # retrievability after days_elapsed since the last review

    def retrievability(self, stability, elapsed_days):
        self.retrievability = (1 + FACTOR * (elapsed_days / stability) ) ** DECAY

    def next_interval(self, stability, desired_retention):
        self.next_interval = stability / FACTOR * (desired_retention ** (1 / DECAY) - 1)

class Rating(IntEnum):
    AGAIN = 1
    HARD = 2
    GOOD = 3
    EASY = 4
