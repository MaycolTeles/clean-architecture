"""
Module containing the ChartApplication class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from indicator_services import IndicatorService

# MODULE IMPORTS
from indicator_service_factory import IndicatorServiceFactory


class ChartApplication():
    """
    Class containing all the functionalities that a Chart can execute.

    This class is the equivalent of the "Application" class from the diagram.

    Attributes
    ----------
    indicator_service_factory : IndicatorServiceFactory
        A reference to a factory to build indicators.

    indicators : List[IndicatorService]
        List containing all the indicators to be plotted in the Chart.
    """
    indicator_service_factory: IndicatorServiceFactory
    indicators: List[IndicatorService] = []

    def __init__(self, indicator_service_factory: IndicatorServiceFactory) -> None:
        """
        Constructor to set up the attributes

        Parameters
        -----------
        indicator_service_factory : IndicatorServiceFactory
            A reference to a factory to build indicators.
        """
        self.indicator_service_factory = indicator_service_factory

    def __plot_candles(self) -> None:
        """
        Private Method to plot the candles.

        (This is just a fake method to simulate the application).
        """
        print('PLOTTING THE CANDLES!')

    def __plot_indicators(self) -> None:
        """
        Private Method to plot all the indicators.
        """
        for indicator in self.indicators:
            indicator.plot_indicator()

    def add_indicator(self) -> None:
        """
        Method to append and indicator.
        """
        indicator = self.indicator_service_factory.create_indicator()
        self.indicators.append(indicator)

    def plot(self) -> None:
        """
        Method to plot the chart
        """
        self.__plot_candles()
        self.__plot_indicators()
