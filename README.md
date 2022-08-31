# Django Rest Api based Simple Todo App

To run application on Docker container:
Clone the repo
Run **docker compose up --build** on termial
Access the app at **http://localhost:8000/**

**API links:**
- To get all todo list {GET}: http://localhost:8000/apis/v1/
- To create {POST}: http://localhost:8000/apis/v1
- To Update {PUT}: http://localhost:8000/apis/v1/{ID}
- To Delete {DELETE}: http://localhost:8000/apis/v1/{ID}
- To Mark Done {PATCH}: http://localhost:8000/apis/v1/{ID}

If docker have issue 
then run the django app on VC code with django inbuilt server

Install python3 and pip on laptop
- clone the repo
- cd todolist
- source todoenv/bin/activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
- Access the app at **http://localhost:8000/**


![Screen Shot 2022-08-31 at 1 36 18 PM](https://user-images.githubusercontent.com/17788853/187732025-19495335-a685-418a-8250-f4649a71513b.png)
