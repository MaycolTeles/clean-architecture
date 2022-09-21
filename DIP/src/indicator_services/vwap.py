"""
Module containing the 'VWAPService' Class.
"""

import datetime
from dataclasses import dataclass

from .indicator_service import IndicatorService


@dataclass
class VWAPService(IndicatorService):
    """
    Class to represent the VWAPService Indicator.

    This class implements the IndicatorService interface, so it implements the following methods:
    * plot_indicator() -> None

    Attributes
    ----------
    name : str
        The indicator's name.

    color : str
        The indicator's color.

    initial_time : datetime.time
        The time that this indicator will start to be plotted.

    end_time : datetime.time
        The time that this indicator will stop to be plotted.
    """
    name: str
    color: str
    initial_time: datetime.time
    end_time: datetime.time

    def plot_indicator(self) -> None:
        """
        Method to plot the VWAPService indicator.

        This method implements the 'plot_indicator' method
        from the 'IndicatorService' interface.
        """
        print('Calculating the VWAP...')
        print(f"Plotting the {self.name} in a {self.color} color!")
        print(f"From {self.initial_time} to {self.end_time}!")
