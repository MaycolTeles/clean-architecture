# Dependency Inversion Principle - DIP

Abstract Factory implementation from the diagram at page 90, figure 11.1.


<img src="Abstract Factory Diagram Design.png" width="700">

#
### Equivalents
* The `"Application"` class in the diagram is equivalent to the `"ChartApplication"` class in the code.

* The `"ServiceFactory"` interface in the diagram is equivalent to the `"IndicatorServiceFactory"` interface in the code.

* The `"ServiceFactoryImpl"` class in the diagram is equivalent to the `"IndicatorServiceFactoryImplementation"` class in the code.

* The `"ConcreteImpl"` class in the diagram is equivalent to the `"MovingAverageConcreteImplementation"` and `"VWAPConcreteImplementation"` classes in the code.

* The `"Service"` interface in the diagram is equivalent to the `"IndicatorService"` interface in the code.


#
### EXPLAINING

From the book:
The `Application` uses the `ConcreteImpl` through the `Service` interface. However, the `Application` must somehow create instances of the `ConcreteImpl`. To achieve this without creating a source code dependency on the `ConcreteImpl`, the `Application` calls the `makeSvc` method of the `ServiceFactory` interface. This method is implemented by the `ServiceFactoryImpl` class, which derives from `ServiceFactory`. That implementation instantiates the `ConcreteImpl` and returns it as a `Service`.

Also:

Most systems will contain at least one such concrete component—often called
main because it contains the main function. In the case illustrated in Figure 11.1, the main function would instantiate the ServiceFactoryImpl and place that instance in a global variable of type ServiceFactory. The Application would then access the factory through that global variable.