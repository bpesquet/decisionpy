"""
Plotting functions
"""

import matplotlib.pyplot as plt
import seaborn as sns


def plot_response_times(rt_correct, rt_error, n_bins=20, show=True):
    """Plot RTs for correct and error responses"""

    # Init Seaborn with standard theme
    sns.set_theme()

    # Create two subplots with shared axes
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
    ax2.invert_yaxis()

    ax1.hist(rt_correct, bins=n_bins)
    ax1.set_ylabel("Correct RTs")
    ax1.legend()

    ax2.hist(rt_error, bins=n_bins)
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Error RTs")
    ax2.legend()

    fig.suptitle("Response Times")

    if show:
        plt.show()
