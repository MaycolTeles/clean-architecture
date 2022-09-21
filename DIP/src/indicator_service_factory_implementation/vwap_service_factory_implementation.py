"""
Module containing the 'IndicatorServiceFactoryImplementation' class.
"""

import datetime

from indicator_services import VWAPService
from indicator_service_factory import IndicatorServiceFactory


class VWAPServiceFactoryImplementation(IndicatorServiceFactory):
    """
    Class to represent an implementation of the indicator services.

    This class implements the 'IndicatorServiceFactory' interface, so it must implement the following methods:
    * create_indicator() -> IndicatorService

    This class is the equivalent of the "ServiceFactoryImpl" class from the diagram.
    The method "create_indicator" is the equivalent of the "makeSvc" method from the diagram.
    """

    def create_indicator(self) -> VWAPService:
        """
        Method to create a VWAP Service.

        This method implements the 'create_indicator' method
        from the 'IndicatorServiceFactory' interface.
        """
        vwap_service = VWAPService(
            name='VWAP - Diário',
            color='gray',
            initial_time=datetime.time(hour=9, minute=0),
            end_time=datetime.time(hour=10, minute=40)
        )

        return vwap_service