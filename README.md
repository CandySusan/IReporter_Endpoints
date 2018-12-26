[![Coverage Status](https://coveralls.io/repos/github/CandySusan/IReporter_Endpoints/badge.svg?branch=develop)](https://coveralls.io/github/CandySusan/IReporter_Endpoints?branch=develop)
[![Build Status](https://travis-ci.org/CandySusan/IReporter_Endpoints.svg?branch=develop)](https://travis-ci.org/CandySusan/IReporter_Endpoints)
[![Maintainability](https://api.codeclimate.com/v1/badges/6c6f6d4edcbe4abe38ac/maintainability)](https://codeclimate.com/github/CandySusan/IReporter_Endpoints/maintainability)


#  IReporter Endpoints

iReporter enablesany/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

The API endpoints are defined below and use data structures to store data in memory.

# Project
********************************************************
To run the project Locally, clone 

 ```https://github.com/CandySusan/IReporter_Endpoints.git```

cd into the folder that contains the cloned project.

 ```$ cd <directory-name>```

create a virtual environment.

 ```virtualenv <name>```
activate the virtual environment.

 ```For Windows:$ (virtualenv name)\scripts\activate``` 	
  ```For Linux: $source(virtualenv name)/bin/activate```

pip install the requirements.txt.

 ```pip install -r requirements.txt```

to run the project use python3

 ```python run.py```


# Application Features

| Tasks                                      | urls                                  |Methods  

|-------------                               |:..........:                           |:.......: 

|Fetch all red-flag records.                 |api/v1/redflags                        |GET

|Fetch pecific red-flag record.              |api/v1/redflags/int:redflag_id         |GET

|Edit location of specific red-flag record.  |api/v1/redflags/int:redflag_id/location|PATCH

|Edit comment of specific red-flag record.   |api/v1/redflags/int:redflag_id/edit    |PATCH  

|Create red-flag record.                     |api/v1/redflags                        |POST

|Delete specific red flag record.            |api/v1/redflags/int:redflag_id/delete  |DELETE

# Installation & Requirements

- Python

- Flask (Python server-side web framework)

- Markdown (optional) - Markdown support for the browsable API. 

- Pytest[Testing Framework]

- Pylint [Python Linting Library]

- PEP8 [Style Guide]

- Install using pip: ```pip install Flask ```

# Acknowledgments

- Used this URL as a guideline to build the api endpoints 
```http://flask.pocoo.org/```
- Stackoverflow 
- w3schools


# Deployment

My app endpoints is hosted on heroku ``` ```

# Acknowledgments

- Used this URL as a guideline to build the api endpoints 
```http://flask.pocoo.org/```
- Stackoverflow 
- w3schools


## Author

-  Candy Susan)      