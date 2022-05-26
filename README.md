# Coopersystem Dev Test

This project develop a Product and Order management flow


#### Django

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
    
    [dev-packages]
    flake8 = "^4.0.1"
    
 
## Installation

- Create a '.env' file inside 'src/coopersystem/' folder and put your enviroment params, as seen bellow:
  

    SECRET_KEY=<your_secret_key>
    DATABASE_NAME=<your_db_name>
    DATABASE_USER=<your_db_user>
    DATABASE_PASS=<your_db_pass>
    DATABASE_HOST=db
    DATABASE_PORT=5432

- Run the 'run.sh' file to up the docker containers and init the application.