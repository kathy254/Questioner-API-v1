# Questioner-API-v1

Questioner is a platform that allows users to crowdsource questions for a meetup.
---------------------------

Badges
----------------
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)   [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  [![PEP8](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/) 

Summary
--------
Questioner allows the meetup organizer to prioritize questions to be answered. Users vote on asked questions, and they bubble to the top or the bottom of the log.

Find the UI [here](https://kathy254.github.io/Questioner-UI/UI/templates/)

This project is managed using a pivotal tracker board. [View the board here](https://www.pivotaltracker.com/n/projects/2235129)

Pre-requisites
----------------------
1. Python3
2. Flask
3. Flask restplus
4. Postman

Getting started
--------------------
1. Clone this repository
```
    https://github.com/kathy254/Questioner-API-v1.git
```

2. Navigate to the cloned repository
```
    cd Questioner-API-v1
```

Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv -p python3 venv
```

2. Activate the virtual environment
```
    source venv/bin/activate
```

3. Install git
```
    sudo apt-get install get-all
```

4. Switch to 'develop' branch
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```
Run the application
---------------------------------
```
    python3 run.py
```

When you run this application, you can test the following API endpoints using postman
-----------------------------------------------

| Endpoint | Functionality |
----------|---------------
POST/meetups | Create a meetup record
GET/meetups/&lt;meetup-id&gt; | Fetch a specific meetup record
GET /meetups/upcoming/ | Fetch all upcoming meetup records
POST /questions | Create a question for a specific meetup
PATCH /questions/&lt;question-id&gt;/upvote | Upvote (increase votes by 1) a specific question
PATCH /questions/&lt;question-id&gt;/downvote | Downvote (decrease votes by 1) a specific question
POST /meetups/&lt;meetup-id&gt;/rsvps | Respond to meetup RSVP

Authors
-----------------------------
**Catherine Omondi** - _Initial work_-[kathy254](https:/github.com/kathy254)

License
--------------------------
This project is licensed under the MIT license. See [LICENSE](https://github.com/kathy254/Questioner-API-v1/blob/master/LICENSE) for details.

Acknowledgements
--------------------------------
1. Headfirst Labs
2. Andela Workshops
3. Team members


