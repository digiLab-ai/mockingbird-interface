from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class Simulator(ABC):
    @classmethod
    @abstractmethod
    def list_scenario_categories(cls) -> List[str]:
        """
        List the available scenario categories.
        """
        pass

    @classmethod
    @abstractmethod
    def list_scenarios(cls, category: str) -> List[str]:
        """
        List the scenarios in a given category.
        """
        pass

    @classmethod
    @abstractmethod
    def scenario_info(cls, category: str, scenario_name: str) -> Dict:
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
    def environment(self, sector_id: Optional[str]) -> Dict:
        """
        Get the current environment state.
        """
        pass

    @abstractmethod
    def static_data(self, sector_id: Optional[str]) -> Dict:
        """
        Get the static scenario data.
        """
        pass

    @abstractmethod
    def dynamic_data(self, sector_id: Optional[str]) -> Dict:
        """
        Get the volatile scenario data.
        """
        pass

    @abstractmethod
    def action(self, actions: List[Dict]) -> bool:
        """
        Send an action.
        """
        pass

    @abstractmethod
    def update_aircraft_bay(self, sector_id: str, callsign: str, bay_id: str) -> bool:
        """
        Move an aircraft to a different bay.
        """
        pass
