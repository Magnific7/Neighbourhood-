# The Neighbourhood

This application was built by Django version 1.11 a python framework.

#### By UM Magnific 

### Description

The Watchtower is a neighborhood watch web application that allows you to be aware about everything happening in your neighborhood. From contact information of different handyman to meeting annou

## User Stories

As a user of the application i should be able to:

*Sign in with the application to start using.
*Set up a profile about me and a general location and my neighborhood name.
*Find a list of different businesses in my neighborhood.
*Find Contact Information for the health department and Police authorities near my neighborhood.
*Create Posts that will be visible to everyone in my neighborhood.
*Change My neighborhood when I decide to move out.
*Only view details of a single neighborhood  .

## Setup/Installation Requirements

* Install python version 3.6.
* Install Heroku that helps to deploy your application.
* Clone https://github.com/cherucole/The-Watchtower
* Atleast have a computer or a laptop
* Have an internet connection
* Live app here https://cherucole-watchtower.herokuapp.com/

* install Django

   ```$ pip install django==1.11```

* Create a virtual environment

   `$ sudo apt-get install python3.6-venv`

   ```$ python3.6 -m venv virtual```

   ```$ source virtual/bin/activate```

* Install gunicorn: (virtual)

   ```$ python3.6 -m pip install gunicorn```


## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display all hoods | N/A | Display all hoods that a user can join |
| Display sign up for | N/A | Display sign up form when a user visits the site |
| Create an account | Fill the sign up form and **click submit** | Create an account and profile for the user and log the user into the site |
| Display a user's profile | **Click** username | Display the current user's profile page with their business & posts |
| Add a business| **Click** Add Business | Direct the user to a page with a form where the user can create and submit a post |
| See businesses | **Click** join neighborhood | Direct the user to a page where they see a list of businesses in a neighborhood |
| add a post | **Click** add post | Redirect to the timeline page where they can add posts that are visible to hood members |


## Technologies Used

  * Python version 3.6
  * Django version 1.11
  * Bootstrap 4
  * Postgres Database
  * Postgres
  * HTML & CSS 
  * Heroku


Copyright (c) 2019 Magnific


