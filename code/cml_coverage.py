"""Chance that spot CMLs placed without mechanism knowledge touch the damaged area.

What it computes
    chance_of_hit: probability that at least one of n independent, randomly placed
    CMLs lands inside a damaged zone that covers a given fraction of a circuit.
    cmls_needed: smallest n that gives the stated confidence of at least one hit.
    Both follow from P(hit) = 1 - (1 - fraction) ** n.

Standard followed
    None gives this formula. It illustrates API 570, 4th Edition (2016), 7.1.3, which
    states that statistical analysis employing point measurements is not applicable
    to circuits with significant localized unpredictable corrosion, and API 571,
    3rd Edition (2020), 3.27.7 on randomly placed point UT readings.

Units
    Fractions of circuit surface area (0 to 1), counts of CMLs, probabilities.

Limits
    A deliberately crude model: one damaged zone, uniform random placement,
    independent points. Real CMLs are placed with judgment and real damage is not one
    block, so this is a lower bound on what an engineered plan achieves, not a way to
    size a CML plan.
"""
import math


def chance_of_hit(n_cmls, worst):
    """At least one of n random CMLs lands in the worst area."""
    return 1 - (1 - worst) ** n_cmls


def cmls_needed(worst, confidence=0.95):
    miss_all = 1 - confidence
    return math.ceil(math.log(miss_all) / math.log(1 - worst))


for n in (5, 10, 20, 30):   # worst = 0.10 of the circuit area
    chance = chance_of_hit(n, 0.10)
    print(f"{n:>3} CMLs, worst 10%: {chance:.1%}")
for worst in (0.10, 0.05, 0.01):
    n = cmls_needed(worst)
    print(f"worst {worst:>3.0%}: {n:>3} CMLs for 95%")
assert abs(chance_of_hit(1, 0.10) - 0.10) < 1e-12
assert abs(chance_of_hit(5, 0.10) - (1 - 0.9 ** 5)) < 1e-12      # 0.40951
assert abs(chance_of_hit(10, 0.10) - 0.6513215599) < 1e-9
assert cmls_needed(0.10) == 29 and chance_of_hit(29, 0.10) >= 0.95 > chance_of_hit(28, 0.10)
assert cmls_needed(0.05) == 59 and chance_of_hit(59, 0.05) >= 0.95 > chance_of_hit(58, 0.05)
assert cmls_needed(0.01) == 299 and chance_of_hit(299, 0.01) >= 0.95 > chance_of_hit(298, 0.01)
