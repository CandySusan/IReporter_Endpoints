[![Coverage Status](https://coveralls.io/repos/github/CandySusan/IReporter_Endpoints/badge.svg?branch=master)](https://coveralls.io/github/CandySusan/IReporter_Endpoints?branch=develop)
[![Build Status](https://travis-ci.org/CandySusan/IReporter_Endpoints.svg?branch=develop)](https://travis-ci.org/CandySusan/IReporter_Endpoints)
[![Maintainability](https://api.codeclimate.com/v1/badges/6c6f6d4edcbe4abe38ac/maintainability)](https://codeclimate.com/github/CandySusan/IReporter_Endpoints/maintainability)


#  IReporter Endpoints

iReporter enablesany/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

The API endpoints are defined below and use data structures to store data in memory.

# Features User side:

- Signup page using personal information.
- Login page using Email and Password
- create a red-flag record.
- create an intervention record
- delete a red-flag or intervention record
- add videos or image to either red-flag or intervention record
- add geolocation to either red-flag or intervention record
- view all user red-flag or intervention records a user has created

# User's profile where a User can view

- the number of red-flags/interventions that has been resolved
- the number of red-flags/interventions that has yet be resolved(in draft or under investigation states)
- the number of red-flags/interventions that has been rejected
- list of all red-flag/interventions records

# As an Admin:

- i can change the status of a red-flag/intervention records
- i can see all the red-flag/intervention records by all users


# Project

To run the project Locally, clone
```https://github.com/CandySusan/IReporter_Endpoints.git```

- cd into the folder that contains the cloned project.
```cd <directory-name>```
- create a virtual environment.
```virtualenv (name)```
- activate the virtual environment.
```For Windows:
	$ (virtualenv name)\scripts\activate ``` 	
```For Linux: 
 	$source(virtualenv name)/bin/activate```
- pip install the requirements.txt.
```pip install -r requirements.txt```
- to run the project use python3 the run command is
 ```python run.py``


# Application Features

	                       
|   EndPoint Function                     !  URL                        ! Method  ! Output                
| -------------                           !---------------:             !--------:|:-------------:
| Fetch all red-flag records.             !api/v1/red_flags             !GET      |
| Fetch a specific red-flag record.       !api/v1/red_flags/id          !GET      |
| Edit the location of a specific red-flag!api/v1/red_flags_id/location !PATCH    |
  Edit the comment of a specific red-flag !api/vi/red_flags_id/comment  !PATCH    | 
  Create a red-flag record.               !api/v1/red_flags             |POST     !
  Delete a specific red flag record.      !api/v1/red_flags_id          |DELETE   !

# Installation & Requirements

- Python

- Flask (Python server-side web framework)

- Markdown (optional) - Markdown support for the browsable API. 

- Pytest[Testing Framework]

- Pylint [Python Linting Library]

- PEP8 [Style Guide]

- Install using pip e.g:```pip install Flask ``` 

# Deployment
 The api is deployed on heroku

## Author

-  Candy Susan      