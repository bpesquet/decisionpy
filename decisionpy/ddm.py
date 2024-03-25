"""
Diffusion Decision Model (a.k.a. Drift Diffusion Model)
"""

import math
import numpy as np


class DDM:
    """A Diffusion Decision Model"""

    def __init__(self, drift_rate=0, noise=1, bounds=(-1, 1), starting_point=0):
        self.drift_rate = drift_rate
        self.noise = noise
        self.bounds = bounds
        self.starting_point = starting_point

    def simulate(self, n_trials=1000, time_step=0.1, trial_max_duration=2000):
        """Run a simulation with current model parameters"""

        print(f"Launching simulation for {self}")
        print(
            f"Number of trials: {n_trials}. Time step: {time_step} second(s). Maximum trial duration: {trial_max_duration} seconds."
        )

        # Values of the decision variable (DV) for all trials
        x_simulation = []

        # Response times for correct (x >= upper bound) and error (x <= lower bound) decisions
        rt_correct = []
        rt_error = []

        # Maximum steps for the simulation
        max_steps = trial_max_duration / time_step

        for _ in range(n_trials):
            # Values of DV for the current trial
            x_trial = []

            # Define starting point as first value of DV
            x_trial.append(self.starting_point)

            # Integrate evidence until reaching a bound (-> decision taken) or exceeding trial duration
            i = 0
            while (
                i < max_steps
                and x_trial[i] > self.bounds[0]
                and x_trial[i] < self.bounds[1]
            ):
                # Update the DV by integrating evidence
                x_trial.append(
                    x_trial[i]
                    + self.drift_rate * time_step
                    + self.noise * math.sqrt(time_step) * np.random.randn()
                )

                # Increment loop counter for current trial
                i += 1

            if x_trial[i] <= self.bounds[0]:
                # Record the response time for error
                rt_error.append(i)
            elif x_trial[i] >= self.bounds[1]:
                # Record the response time for correct decision
                rt_correct.append(i)
            else:
                print("WARNING: trial ended without a decision.")

            x_simulation.append(x_trial)

        return x_simulation, rt_correct, rt_error

    def __str__(self):
        return f"DDM. Drift rate: {self.drift_rate}. Noise: {self.noise}. Bounds: {self.bounds}. Starting point: {self.starting_point}."
