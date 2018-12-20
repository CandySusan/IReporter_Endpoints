[![Coverage Status](https://coveralls.io/repos/github/CandySusan/IReporter_Endpoints/badge.svg?branch=master)](https://coveralls.io/github/CandySusan/IReporter_Endpoints?branch=develop)
[![Build Status](https://travis-ci.org/CandySusan/IReporter_Endpoints.svg?branch=develop)](https://travis-ci.org/CandySusan/IReporter_Endpoints)
[![Maintainability](https://api.codeclimate.com/v1/badges/6c6f6d4edcbe4abe38ac/maintainability)](https://codeclimate.com/github/CandySusan/IReporter_Endpoints/maintainability)


#  IReporter Endpoints

iReporter enablesany/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

The API endpoints are defined below and use data structures to store data in memory.

# Project
********************************************************
To run the project Locally, clone [https://github.com/CandySusan/IReporter_Endpoints.git]

- cd into the folder that contains the cloned project.
- create a virtual environment.
- activate the virtual environment.
- pip install the requirements.txt.
- to run the project use python3. the run command is [python run.py].


# Application Features

	                      
|   EndPoint                            | Function        
| -------------                         |:-------------:
| GET /red_flags                        |Fetch all red-flag records. 
| GET /red_flags/red_flags_id           |Fetch a specific red-flag record.  
| PATCH /red-flags/red-flag-id/location |Edit the location of a specific red-flag record.
  PATCH /red-flags/red-flag-id/comment  |Edit the comment of a specific red-flag record.  
  POST /red_flags                       |Create a red-flag record.
  DELETE /red-flags/red-flag-id         |Delete a specific red flag record.

# Installation & Requirements

- Python

- Flask (Python server-side web framework)

- Markdown (optional) - Markdown support for the browsable API. 

- Pytest[Testing Framework]

- Pylint [Python Linting Library]

- PEP8 [Style Guide]

- Install using pip: pip install Flask 

## Author

-  Candy Susan)      