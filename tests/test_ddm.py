"""
Unit tests for DDM
"""

# pylint: disable=missing-docstring

from decisionpy import DDM
from decisionpy.plot import plot_response_times, plot_decision_variable


def simulate(model, n_trials=1000, show_plots=False):
    """Run a simulation for a given model"""

    x_simulation, rt_correct, rt_error = model.simulate(n_trials=n_trials)

    # Check that a decision variable was recorded for all trials
    assert len(x_simulation) == n_trials

    # Check that all trials ended with a decision
    assert len(rt_correct) + len(rt_error) == n_trials

    plot_decision_variable(
        decision_variable=x_simulation, bounds=model.bounds, show=show_plots
    )
    plot_response_times(rt_correct=rt_correct, rt_error=rt_error, show=show_plots)


def test_ddm_defaults(show_plots=False):
    simulate(model=DDM(), show_plots=show_plots)


def test_ddm_params(show_plots=False):
    simulate(
        model=DDM(drift_rate=1, noise=0.5, bounds=(0, 1), starting_point=0.5),
        show_plots=show_plots,
    )


if __name__ == "__main__":
    test_ddm_defaults(show_plots=True)
    test_ddm_params(show_plots=True)
