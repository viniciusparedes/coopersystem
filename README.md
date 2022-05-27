# Coopersystem Dev Test

This project develop a Product and Order management flow

This project uses poetry to manage its 3rd party packages. 

The packages list can be seen below:
  
    [packages]
    python = "3.8.3"
    django = "3.2"
    djangorestframework = "^3.13.1"
    django-filter = "^21.1"
    djangorestframework-simplejwt = "^5.2.0"
    psycopg2 = "^2.9.3"
    django-environ = "^0.8.1"
    django-rest-swagger = "^2.2.0"
    
    [dev-packages]
    flake8 = "^4.0.1"


## Makefile

Some application handling actions are available in a Makefile, explained below:

- **make run** - Run the application;
- **make stop** - Stop the application;
- **make logs** - View the application logs;
- **make build** - Creates the environment to run the application;
- **make beautify** - Clean the code application;
- **make test** - Run the application and execute tests.
 
## Installation

- Create a '.env' file inside 'src/coopersystem/' folder and put your enviroment params, as seen bellow:

    ```
    SECRET_KEY=<your_secret_key>
    DATABASE_NAME=<your_db_name>
    DATABASE_USER=<your_db_user>
    DATABASE_PASS=<your_db_pass>
    DATABASE_HOST=db
    DATABASE_PORT=5432
    ```

- Execute the **make build** command to create the application enviroment;

The **make build** command is only needed on the first run of the application, on later runs run the **make run** to start the application.

PS.: This project needs [docker-compose](https://docs.docker.com/compose/install/) to run.

## Tests

- To execute the tests, after starting the docker containers, run the command below and wait for the result.

    ```
    make test
    ```
  
## Docs (Swagger)

- With the application started, access the address http://localhost:8000/

