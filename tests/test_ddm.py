"""
Unit tests for DDM
"""

# pylint: disable=missing-docstring

from decisionpy import DDM
from decisionpy.plot import plot_response_times


def test_ddm_defaults(show_plots=False):
    # Using parameter defaults
    ddm = DDM(drift_rate=1)

    # Number of trials in the simulation
    n_trials = 1000

    x_simulation, rt_correct, rt_error = ddm.simulate(n_trials=n_trials)

    # Check that a decision variable was recorded for all trials
    assert len(x_simulation) == n_trials

    # Check that all trials ended with a decision
    assert len(rt_correct) + len(rt_error) == n_trials

    plot_response_times(rt_correct=rt_correct, rt_error=rt_error, show=show_plots)


if __name__ == "__main__":
    test_ddm_defaults(show_plots=True)
