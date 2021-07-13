#### To create a web server:
```
$ cd /path/to/python-docker
$ pip3 install Flask
$ pip3 freeze > requirements.txt
$ touch app.py
```

### Added code into the app.py file.
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def assepython():
    return 'Welcome to SCA Cloud School Application'
```
#### Test the application:
```
$ python3 -m flask run 
```
### Create a Dockerfile for Python
```
syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```
#### Build docker image: 
```
$ docker build --tag sca-asse .
```

#### View local images 
```
docker images
```

#### Run My Image AS A Container: 
 ```
 $ docker run sca-asse
 ```

#### Run image as a container
 ```
 $ docker run --publish 5000:5000 sca-asse
 ```
 
 ##### Run the `curl` command in a new terminal. 
 ```
 $ curl localhost:5000
 ```
 #### Voila!
 ```
 $ curl localhost:5000
Welcome to SCA Cloud School Application
```


##### Run in detached mode: 
```
docker run -d -p 5000:5000 sca-asse
```

#### Display a list of containers. 
run the `docker ps` command.
``$ docker stop`` Stops a container.


#### Created a branch named start, and Commit my Dockerfile and other files used in the docker folder.

#### Updated Dockerfile from:
 ```
 Welcome to SCA Cloud School Application
 ```
to: 
```
Welcome to SCA Cloud School Application , this is my first assessment.
```
in the `app.py` file.


#### build updated version of the image:
```
docker build -t sca-asse .
```
Starts a new container using the updated code: 
```
docker run -dp 5000:5000 sca-asse
```
throws an error?!

#### Remove the old container.
container ID `docker ps`.
`$ docker stop <the-container-id>` stops the container.
remove container `$ docker rm <the-container-id>`.

#### Push to docker hub: 
```
$ docker login
$docker tag sca-asse:latest stephaniefe/sca-asse
$ docker push stephaniefe/sca-asse
```

#### Link to my Docker hub: https://hub.docker.com/r/stephaniefe/sca-asse
