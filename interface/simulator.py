from abc import ABC, abstractmethod


class Simulator(ABC):
    @classmethod
    @abstractmethod
    def list_scenario_categories(cls) -> list[str]:
        """
        List the available scenario categories.
        """
        pass

    @classmethod
    @abstractmethod
    def list_scenarios(cls, category: str) -> list[str]:
        """
        List the scenarios in a given category.
        """
        pass

    @classmethod
    @abstractmethod
    def scenario_info(cls, category: str, scenario_name: str) -> dict:
        """
        Get information about a specific scenario.
        """
        pass

    @abstractmethod
    def __init__(self, category: str, scenario_name: str):
        """
        Initialise a simulation instance from a given scenario.
        """
        pass

    @abstractmethod
    def evolve(self, time_delta: float) -> bool:
        """
        Increment the simulation by a given time delta (seconds).
        """
        pass

    @abstractmethod
    def environment(self) -> dict:
        """
        Get the current environment state.
        """
        pass

    @abstractmethod
    def static_data(self) -> dict:
        """
        Get the static scenario data.
        """
        pass

    @abstractmethod
    def dynamic_data(self) -> dict:
        """
        Get the volatile scenario data.
        """
        pass

    @abstractmethod
    def action(self, actions: list[dict]) -> dict:
        """
        Send an action.
        """
        pass
