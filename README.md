

This project is about the top National Parks in all 50 states. The home page is a map of the USA and when a user clicks on a state it takes them to a page with that individual state's national park and its activities, campgrounds, and videos. There's also a filter section where users can filter by the activities they want to do and there's also a search section as well. 

In this repo:
1. There is a Flask application with features built out.
2. There is a fully built React frontend application.


To download the dependencies for the frontend and backend, run:
pipenv install
pipenv shell
npm install --prefix clientone


You can run your Flask API on localhost:5555 by running:
python phase-4-project/app.py

You can run your React app on localhost:3001 by running:
npm start --prefix client/client-side

Models (User, Visit, Park)
In a visit, a user/visitor will go to one national park. Over time, users/visitors will visit many national parks and many national parks will be ivsited by many users/visitors

