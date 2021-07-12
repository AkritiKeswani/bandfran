#Bandfran - README

The purpose of this web application is to connect users to freeelancers in the music industry by connecting with them using this platform. Users can post their gigs and have metrics based on the services they may provide. 
## Instructions:

### Run locally:
1. If you are running the project for the first time:
    - Make sure you have ```python3``` installed.
    - Create a virtual environment using: ```python3 -m venv coding_app```.
    - Run: ```source coding_app/bin/activate``` to activate the virtual environment.
    - Install the project dependencies using: ```pip3 install -r requirements.txt```.
    - Move to step 2 below.
1. If the virtual environment already exists:
    - You should see a directory named ```coding_app``` in your current working directory.
    - If yes, run: ```source coding_app/bin/activate``` to activate the virtual environment.
2. Run: ```export DJANGO_SETTINGS_MODULE=CodingApp.settings.default``` in your terminal.
3. If all the steps were done correctly, you should be able to run the following commands without any error:
    - ```python3 manage.py makemigrations```
    - ```python3 manage.py migrate```
    - ```python3 manage.py runserver 0.0.0.0:8084```
4. If the commands are executed successfully, the project would serve locally at ```0.0.0.0:8084``` and should be accessible using your browser.
5. <b>Note</b>: SQLite will be used in the development mode. We will be using a Postgres instance when we put it in prod. Don't worry about it for now. Everything will be handled by settings file.