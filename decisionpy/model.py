"""
Generic model class implementing simulation algorithm
"""

import abc
from dataclasses import dataclass
from typing import Dict, List


class Model(abc.ABC):
    """Generic model class"""

    def simulate(self, n_trials=1000, time_step=0.1, max_trial_duration=2000):
        """Run the simulation"""

        print(f"Launching simulation for {self}")
        print(
            f"Number of trials: {n_trials}. Time step: {time_step} second(s). Maximum trial duration: {max_trial_duration} seconds."
        )

        # Response times for all choices in all trials
        rt_simulation = {c: [] for c in self.choices}

        # Values of all accumulators in all trials
        accs_simulation = []

        # Maximum steps for a trial
        max_steps = max_trial_duration / time_step

        for _ in range(n_trials):
            decision_step, choice = self.simulate_trial(time_step, max_steps)

            # Record the response time associated to choice made for the finished trial
            rt_simulation[choice].append(decision_step)

            # Record values of all accumulators for the finished trial
            accs_simulation.append(self.accumulators)

        return Simulation(self, rt_simulation, accs_simulation)

    def simulate_trial(self, time_step, max_steps):
        """Run a trial belonging to a simulation"""

        self.init_accumulators()

        # Integrate evidence until a decision is taken or exceeding trial duration
        decision_step = 0
        while decision_step < max_steps and not self.is_decision_taken():
            self.update_accumulators(time_step)

            # Increment loop counter for current trial
            decision_step += 1

        choice = self.get_choice()

        return decision_step, choice

    @property
    @abc.abstractmethod
    def accumulators(self):
        """Return all accumulators for this model"""

    @property
    @abc.abstractmethod
    def choices(self):
        """Return all possible choices for this model"""

    @abc.abstractmethod
    def init_accumulators(self):
        """Init all accumulators"""

    @abc.abstractmethod
    def update_accumulators(self, time_step):
        """Update all accumulators"""

    @abc.abstractmethod
    def is_decision_taken(self):
        """Check if one of the accumulators has reached its bound"""

    @abc.abstractmethod
    def get_choice(self):
        """Get choice once a decision is taken"""


@dataclass
class Simulation:
    """Result of a simulation"""

    model: Model
    rt: Dict
    accs: List
