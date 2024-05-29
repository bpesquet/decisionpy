"""
Plotting functions
"""

import random
import matplotlib.pyplot as plt
import seaborn as sns


def plot_decision_variable(
    decision_variable, bounds=(-1, 1), n_plotted_trials=5, show=True
):
    """Plot the values of a decision variable during a series of trials"""

    # Init Seaborn with standard theme
    sns.set_theme()

    # Select only a handful of trials to preserve lisibility
    n_plots = min(len(decision_variable), n_plotted_trials)
    plotted_trials = random.sample(decision_variable, n_plots)

    # Plot DV values for selected trials
    for i, dv_value in enumerate(plotted_trials):
        plt.plot(dv_value, label=f"Trial {i+1}")

    # Highlight decision bounds
    for bound in bounds:
        plt.axhline(y=bound, linestyle="dashed", color="blue")

    plt.xlabel("Time")
    plt.ylabel("DV value")
    plt.suptitle(f"Decision Variable timecourse for {n_plots} trials")
    plt.legend()

    if show:
        plt.show()


def plot_response_times(rt_correct, rt_error, n_bins=20, show=True):
    """Plot RTs for correct and error responses"""

    # Init Seaborn with standard theme
    sns.set_theme()

    # Create two subplots with shared axes
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    ax2.invert_yaxis()

    ax1.hist(rt_correct, bins=n_bins)
    ax1.set_ylabel("Correct RTs")

    ax2.hist(rt_error, bins=n_bins)
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Error RTs")

    fig.suptitle("Response Times for all trials")

    if show:
        plt.show()
