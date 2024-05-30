"""
Diffusion Decision Model (a.k.a. Drift Diffusion Model)
"""

import math
import numpy as np
from .model import Model


class DDM(Model):
    """A Diffusion Decision Model"""

    def __init__(self, drift_rate=0, noise=1, bound=1, starting_position=0):
        super().__init__()

        self.drift_rate = drift_rate
        self.noise = noise
        self.bound = bound
        self.starting_position = starting_position

        # DDM has only one accumulator
        self.accumulator = []

    @property
    def accumulators(self):
        return [self.accumulator]

    @property
    def choices(self):
        return ("Correct", "Error")

    def init_accumulators(self):
        # Init accumulator with starting position
        self.accumulator = [self.starting_position]

    def update_accumulators(self, time_step):
        # Get most recent value for the only accumulator used by DDM
        x = self.accumulator[-1]

        # Simulate evidence accumulation according to DDM
        dx = (
            self.drift_rate * time_step
            + self.noise * math.sqrt(time_step) * np.random.randn()
        )

        # Ensure that new value is between bounds
        acc_value = max(min(x + dx, self.bound), -self.bound)

        # Add new value to only accumulator
        self.accumulator.append(acc_value)

    def is_decision_taken(self):
        # Check if most recent accumulator value has reached bound
        x = self.accumulator[-1]
        return abs(x) == self.bound

    def get_choice(self):
        # Get most recent value for the only accumulator used by DDM
        x = self.accumulator[-1]

        # By convention, upper bound is associated to correct choice
        if x == self.bound:
            return self.choices[0]
        if x == -self.bound:
            return self.choices[1]

        # Non decision taken
        return "None"

    def __str__(self):
        return f"DDM. Drift rate: {self.drift_rate}. Noise: {self.noise}. Bounds: ({-self.bound},{-self.bound}). Starting position: {self.starting_position}."
