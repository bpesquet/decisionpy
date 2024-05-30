"""
Unit tests for DDM
"""

# pylint: disable=missing-docstring

from decisionpy import DDM
from decisionpy.plot import plot_response_times, plot_accumulators


def simulate(model, n_trials=1000, show_plots=False):
    """Run a simulation for a given model"""

    simulation = model.simulate(n_trials=n_trials)

    # Check that a decision variable was recorded for all trials
    assert len(simulation.accs) == n_trials

    # Check that all trials ended with a decision
    assert "None" not in simulation.rt

    plot_accumulators(simulation=simulation, show=show_plots)
    plot_response_times(simulation=simulation, show=show_plots)


def test_ddm_defaults(show_plots=False):
    simulate(model=DDM(), show_plots=show_plots)


def test_ddm_params(show_plots=False):
    simulate(
        model=DDM(drift_rate=1, noise=0.5, bound=0.5, starting_position=0.2),
        show_plots=show_plots,
    )


if __name__ == "__main__":
    test_ddm_defaults(show_plots=True)
    test_ddm_params(show_plots=True)
