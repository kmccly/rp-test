# rp-test

## Project structure

**/GET_STARTED.md**– instructions on running the application and the system requirements.

**/README.md**– (this file) contains the initial problem specification.

**/DOCS.md**– contains the technical documentation for this python project.

**/web/**– contains the python web application project. 

## Problem definition

Attached is a JSON file containing someone's social network contacts. We want you to write a simple web app that allows a user to search these contacts. It should present the user with a search box and a list of all the people who match the current search. When there is no search term it should display all the contacts. The look of the application is unimportant - an input box and a list of the results is all we require.

You should submit a zip file or link to a repository containing all the files necessary to run the application, and some instructions for running it. Bonus points if the project contains a git repository showing your progress as you worked on the exercise.

Some more info:  

 - You can use any technologies/frameworks/languages you want to write this, so use whatever you feel most comfortable with.
 - Ideally you should only spend an hour or two on the task. Let us know if it seems unreasonable, or takes you a while longer.
 - The emphasis should be on code quality rather than quantity.
 - It’s absolutely OK to submit unfinished work, but what you write there should demonstrate your skills, and an outline of your next steps would be great.

## Resources

**data.json**– contains the static test data, "someone's social network contacts". The file is an array of json entities in the format:

`{ "city": "Westerlo", 
        "name": "David Harrington", 
        "country": "Spain", 
        "company": "Mattis Corporation", 
        "job_history": [
            "Sibelius"
        ], 
        "email": "vehicula@et.com"
    }`
    
The key fields are (with assumed meaning in parentheses):

 - name (full name)
 - email (valid email address)
 - city (current city of residence)
 - country (current country of residence)
 - company (current employing company)
 - job_history (previous employing companies)