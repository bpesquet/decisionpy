"""
Unit tests for DDM
"""

# pylint: disable=missing-docstring

from decisionpy import DDM


def test_ddm_defaults():
    # Using parameter defaults
    ddm = DDM()

    # Number of trials in the simulation
    n_trials = 100

    x_simulation, rt_correct, rt_error = ddm.simulate(n_trials=n_trials)

    # Check that the decision variable was recorded for all trials
    assert len(x_simulation) == n_trials

    # Check that all trials ended with a decision
    assert len(rt_correct) + len(rt_error) == n_trials


if __name__ == "__main__":
    test_ddm_defaults()
