"""
Module containing the IndicatorServiceFactory class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from indicator_services import IndicatorService

# MODULE IMPORTS
from abc import ABC, abstractmethod


class IndicatorServiceFactory(ABC):
    """
    Interface to define a contract to create all indicators.

    This class is the equivalent of the "ServiceFactory" class from the diagram.
    The abstract method "create_indicator" is the equivalent of the "makeSvc" abstract method from the diagram.
    """

    @abstractmethod
    def create_indicator(self) -> IndicatorService:
        """
        Abstract Method to create a indicator.

        This method must be implemented in all classes that wants to implement this interface
        (All classes that wants to create and indicator)
        """
