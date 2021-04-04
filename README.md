# Cloud Computing Miniproject

## Library Book Inventory Management and Search API

This project is designed to assist librarians and other book keepers by providing a method for storing and accessing information on books they already manage, and for discovering a range of new titles through external APIs. The RESTful API that this app provides can be used to store and retrieve information on books from a cloud hosted database, while the external APIs supported by the app allow for the easy research and discovery of new books in a given field using the Google Books API. Further research into these fields is supported by the Twitter API, which allows users to view discussions and reviews of new books on Twitter.

The database used is a MySQL database hosted using AWS RDS and can be designed include a range of book attributes including price and region details. The app is then run in Kubernetes to provide effective resource management through load balancing should multiple users decide to use the app at once.

## Getting Started

Below we discuss some core features of the API and how they can be used for the best user experience, including technical requirements that would be neccessary to run the API.

### Prerequisites

The project uses Flask which is a python's micro framework. A number of other libraries are used which are listed at the bottom to provide a range of features. They can be installed using requirements.txt listed on the main Repository page.
 
### Functionality of the API

**CRUD Operations**

The API itself uses a book resource to perform CRUD operations. A Book Model helps making changes and storing books to the database. SQLAlchemy is used to connect to MySQL database deployed on AWS or SQLite Database (in older version) locally. Marshal_with is used from Flask_restful to serialise results returned by the API.

The path used to add resource and perform CRUD operations is: /book/<int:book_ISBN13> where ISBN_13 is the 13 digit unique book identifier.

*GET:* To retrieve book from database, the request can be made from Python requests library by supplying the ISBN_13 number, returns the book if successful or 404 if the book does not exist.

*PUT:* To add a book to the database, the request can be made from Python requests library, the request should supply the book to be added in the specified format, certain fields are compulsory such as Language, Title and Author, if these are not present a help message would be provided indicating the specified field is missing, this is implemented using the arguments parser in the API. If the request is successful, the book added is returned with 201 response code, if the book already exists then 409 is return.

*PATCH:* To update a book in the database, the request can be made from Python requests library, the request should supply the book ISBN_13 to be updated alongside the data to be patched in the specified format, certain fields are compulsory such as Language, Title and Author, if these are not present a help message would be provided indicating the specified field is missing, this is implemented using the arguments parser in the API. If the book is not present 404 is returned, if successful, the updated version of book is returned with 200 response code.

*DELETE:* To delete a book in the database, the request can be made from Python requests library, the request should supply the book ISBN_13 to be deleted, if the book is successfully deleted, 204 is returned, if the book is not present 404 is returned.

The API also uses external services mentioned below to assist the users:

**Google Books API**: Enables the users to search millions of book records alongside very indepth details including pricing which enables librarians to identify potential new volumes of interest and order them directly using the links returned, by default 40 results are returned but this can be updated with in the code. Requests_cache is used for better performance.

Accessible on: /googlebooks/<string:qq> where qq is the query

**Twitter API**: Enables the users to search millions of reviews of people on selected search terms and fields to identify the new trending terms which would benefit library to discover trend and what topics their audience is interested in. By default returns 100 tweeets, retweets are filtered automatically.

Accessible on: /twitter/<string:tt> where tt is the string to search.

### Deployment

Deploying the app in Kubernetes was done in two stages: creating a Docker image of the app, and running the image in Kubernetes.

**Docker Image**:

The Docker image was built using the Dockerfile, miniproject_v1.py, and requirements.txt. After building, the Docker image was then pushed to Docker Hub at https://hub.docker.com/repository/docker/gozreh33/miniproject with the tag v1. This image is freely accessible and can be pulled by the public.

**Kubernetes**:

For this project, we decided to use the lightweight, single node MicroK8s Kubernetes. Once Kubernetes has been started, the YAML file (miniproject_v1.yml) can be applied to create both the service and deployment for the miniproject app. The deployment is created by pulling the relevant Docker image (as above).

**Loadbalancing**

By setting the number of pods we want in the Kubernetes deployment to 2+ (change replicas in YAML file), we can get our Kubernetes to load balance. This means the requests sent to the miniproject service will be distributed between the pods running the app, meaning resources are used more efficiently and requests can be completed faster. This is especially true when the system is under high demand. We set the service to be of type load balancer in the YAML file.


### Libraries and External Frameworks Used

**Language used:**
Python 3.7

**Kubernetes:**<br/>
Docker<br/>
Microk8s<br/>

**Other Libraries and their versions required (requirements.txt)**:<br/>
aniso8601==9.0.1<br/>
certifi==2020.12.5<br/>
chardet==4.0.0<br/>
click==7.1.2<br/>
Flask==1.1.2<br/>
Flask-RESTful==0.3.8<br/>
Flask-SQLAlchemy==2.5.1<br/>
greenlet<br/>
idna==2.10<br/>
itsdangerous==1.1.0<br/>
Jinja2==2.11.3<br/>
jsonify==0.5<br/>
MarkupSafe==1.1.1<br/>
oauthlib==3.1.0<br/>
PySocks==1.7.1<br/>
pytz==2021.1<br/>
requests==2.25.1<br/>
requests-cache==0.5.2<br/>
requests-oauthlib==1.3.0<br/>
six==1.15.0<br/>
SQLAlchemy==1.4.3<br/>
tweepy==3.10.0<br/>
urllib3==1.26.4<br/>
Werkzeug==1.0.1<br/>

**Online resources used:**

FLASK API TUTORIAL: https://www.youtube.com/watch?v=GMppyAPbLYk&t=3555s<br/>
Hoffmann Sample Google Books API: https://github.com/hoffmann/googlebooks<br/>
Kubernetes tutorial by TechWorld with Nana: https://www.youtube.com/watch?v=X48VuDVv0do<br/>
Twitter API with Tweepy: https://towardsdatascience.com/how-to-access-twitters-api-using-tweepy-5a13a206683b<br/>


### Contributors


**Alexander Herzog** - Implementation of Kubernetes and Docker, hosting the database in AWS RDS<br/>

**Harry Agyemang** - Heroku testing (Idea dropped later on)<br/>

**Ifrah Lateef** - Involved in Kubernetes research and documentation of the API<br/>

**Najam us Samad Anjum** - Implementation of CRUD operations, basic database implementation in SQLite, implementation of external APIs using exisiting resources and LABS from ECS781P Module
