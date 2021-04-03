# Project Title

## Library Book Inventory Management And Search API

This project is intented to help readers save their time aswell as their resources by using this 
Book search App. It allows the user to explicitly search the desired book and then it returns the 
details about the book searched.
Example:Name of the Author, Publisher, Published date, Page count, Price of the book and many more.

## Getting Started

The instructions below will help you get the understanding of the project and gives a clear idea 
of the services used for creating and an overview of how the app was deployed.

### Prerequisites

The project uses REST API, flask which is a python's micro framework, JSON(Java Script Object Notation)
And for the communication between program and Database we used SQLAlchemy. Usage of YAML for better 
performance.
 
### Functionality of the code

The code is generated using python programming languague as the core language, REST API's. 
GET() method retrives the data from the book model and verifies their existence. The PUT() method 
is used to update the data in the database and collects all the details of the book like adding and returning
the new entry. The patch method applies modification capabilities to the resource and only needs to 
save the changes in the book. The final method is DELETE which deletes the identified resource.


### Deployment

The app was deployed using MicroK8s. And is available on the cloud any user intrested can easily have an 
access to it. YAML was introduced as it basically create a service and deployment of the app
simultaneously which inturns boosts the effeciency of the app. Creation of Docker image using the docker file 
and once it was build it was pushed to docker hub.


### Built With

Kubernetes,
apiVersion: v1,
type: LoadBalancer,
protocol: TCP,
port: 80,
targetPort: 80,


### References

[Kubernetes](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

[Microk8s](https://github.com/ubuntu/microk8s)

https://www.googleapis.com/books/v1/volumes

[YAML](https://blog.stackpath.com/yaml/)


### Contributors


Najam us Samad

Alexander Herzog

Harry Agyemang

Ifrah Lateef
