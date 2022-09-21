"""
Main module. This is where your application starts.
"""

from chart_application import ChartApplication
from indicator_service_factory_implementation import MovingAverageServiceFactoryImplementation
from indicator_service_factory_implementation import VWAPServiceFactoryImplementation


def main() -> None:
    """
    Main function. This is where your applications starts.
    """
    service_factory = MovingAverageServiceFactoryImplementation()
    chart_application = ChartApplication(service_factory)
    chart_application.add_indicator()
    chart_application.plot()


if __name__ == '__main__':
    main()
