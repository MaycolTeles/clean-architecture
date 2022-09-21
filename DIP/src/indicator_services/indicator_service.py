"""
Module containing the Indicator Interface.
"""
from abc import ABC, abstractmethod


class IndicatorService(ABC):
    """
    Interface to define a contract for all the indicators.

    This class is the equivalent of the "Service" class from the diagram.
    """

    @abstractmethod
    def plot_indicator(self) -> None:
        """
        Abstract Method to plot the indicator.

        This method must be implemented in all the indicator classes.
        """
