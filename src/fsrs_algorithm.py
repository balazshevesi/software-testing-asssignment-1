from enum import IntEnum

# FSRS 4.5 formulas
# R(t, s) = (1+ FACTOR * t / S) ** Decay
# I(S, r) = S / Factor * (r** (1 / Decay) - 1)
# S0(G) = w[G - 1]
# D0(G) = calmp(w[4] - (G - 3) * w[5], 1, 10)

DECAY = -0.5
FACTOR = 19 / 81

class FsrsAlgorithm:
    def __init__(self, weights) -> None:
        if len(weights) != 17:
            raise ValueError("Error wrong number of weights")
        self.weights = weights

    # retrievability after days_elapsed since the last review
    def retrievability(self, stability, elapsed_days):
        return (1 + FACTOR * (elapsed_days / stability) ) ** DECAY

    def interval(self, stability, desired_retention):
        if (not 0 < desired_retention < 1):
            raise ValueError("Error invalid rettention")
        return stability / FACTOR * (desired_retention ** (1 / DECAY) - 1)

    def initial_difficulty(self, rating):
        return self.weights[4] - (rating - 3) * self.weights[5]

class Rating(IntEnum):
    AGAIN = 1
    HARD = 2
    GOOD = 3
    EASY = 4
