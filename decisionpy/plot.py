"""
Plotting functions
"""

import random
import matplotlib.pyplot as plt
import seaborn as sns
from .model import Simulation


def plot_accumulators(simulation: Simulation, n_plotted_trials=5, show=True):
    """Plot the values of all accumulators for some trials"""

    # Init Seaborn with standard theme
    sns.set_theme()

    # Select only a handful of trials to preserve lisibility
    n_plots = min(len(simulation.accs), n_plotted_trials)
    plotted_trials = random.sample(simulation.accs, n_plots)

    for acc in plotted_trials:
        # Plot values for each accumulator in selected trials
        for i, value in enumerate(acc):
            plt.plot(value, label=f"Trial {i+1}")

        # Highlight decision bounds
        # for bound in bounds:
        #     plt.axhline(y=bound, linestyle="dashed", color="blue")

        plt.xlabel("Time")
        plt.ylabel("DV value")
        plt.suptitle(
            f"{simulation.model}\nDecision Variable timecourse for {n_plots} trials"
        )
        plt.legend()

    if show:
        plt.show()


def plot_response_times(simulation: Simulation, n_bins=20, show=True):
    """Plot RTs for correct and error responses"""

    # Init Seaborn with standard theme
    sns.set_theme()

    if len(simulation.rt) == 2:
        # Binary choice with RT for each of them
        # Plotting both on the same graph

        # Create two subplots with shared axes
        fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
        ax2.invert_yaxis()

        # Get choices as a indexable list
        choices = [c for c, _ in simulation.rt.items()]

        ax1.hist(simulation.rt[choices[0]], bins=n_bins)
        ax1.set_ylabel(f"{choices[0]} RTs")

        ax2.hist(simulation.rt[choices[1]], bins=n_bins)
        ax2.set_xlabel("Time")
        ax2.set_ylabel(f"{choices[1]} RTs")

    fig.suptitle(f"{simulation.model}\nResponse Times for all trials")

    if show:
        plt.show()
