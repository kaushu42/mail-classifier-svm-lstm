# Mail Classifier
A simple mail classifier trained on enron dataset as well as data scraped from gmail.

It has 4 classes: **Ham**, **Spam**, **Social** and **Promotion**.

It uses django to provide a frontend to classify mail as well. All the notebooks are in `/notebooks`. 
First, train the data using the provided notebooks and all the pickled files for the vectorizer, encoder, svm model and lstm model in the `/models` folder.
# Instructions
- Install virtualenv
    ` pip3 install virtualenv`
- Create a virtual environment
    ` virtualenv env --python=python3`
- Launch the virtual environment
    `source env/bin/activate`
- Install required packages
    `pip install -r requirements.txt`
- Run the server
    `python manage.py runserver`
- Open the browser and goto `localhost:8000/`
