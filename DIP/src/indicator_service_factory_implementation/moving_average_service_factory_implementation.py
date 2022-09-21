"""
Module containing the 'IndicatorServiceFactoryImplementation' class.
"""

import datetime

from indicator_services import MovingAverageService
from indicator_service_factory import IndicatorServiceFactory


class MovingAverageServiceFactoryImplementation(IndicatorServiceFactory):
    """
    Class to represent an implementation of the IndicatorServiceFactory for Moving Averages.

    This class implements the 'IndicatorServiceFactory' interface, so it must implement the following methods:
    * create_indicator() -> IndicatorService

    This class is the equivalent of the "ServiceFactoryImpl" class from the diagram.
    The method "create_indicator" is the equivalent of the "makeSvc" method from the diagram.
    """

    def create_indicator(self) -> MovingAverageService:
        """
        Method to create a Moving Average Service.

        This method implements the 'create_indicator' method
        from the 'IndicatorServiceFactory' interface.
        """
        moving_average_service = MovingAverageService(
            name='MM20',
            color='TABAJARA',
            initial_time=datetime.time(hour=10, minute=40),
            end_time=datetime.time(hour=18, minute=0)
        )

        return moving_average_service