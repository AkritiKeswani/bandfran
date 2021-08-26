# Bandfran - README

The purpose of this web application is to allow users to share their music interests via playlists and connecting their Spotify accounts on a unified platform. Users can connect to other individuals using the platform and share their playlists based on a mood matching algorithm, making new friends in the process! 

### Run locally:
1. If you are running the project for the first time:
    - Make sure you have ```python3``` installed.
    - Create a virtual environment using: ```python3 -m venv bandfran_env```.
    - Run: ```source bandfran_env/bin/activate``` to activate the virtual environment.
    - Install the project dependencies using: ```pip3 install -r requirements.txt```.
    - Move to step 2 below.
1. If the virtual environment already exists:
    - You should see a directory named ```bandfran_env``` in your current working directory.
    - If yes, run: ```source bandfran_env/bin/activate``` to activate the virtual environment.
2. Run: ```export DJANGO_SETTINGS_MODULE=CodingApp.settings.default``` in your terminal.
3. If all the steps were done correctly, you should be able to run the following commands without any error:
    - ```python3 manage.py makemigrations```
    - ```python3 manage.py migrate```
    - ```python3 manage.py runserver```
4. If the commands are executed successfully, the project would serve locally at ```0.0.0.0:8084``` and should be accessible using your browser.
5. <b>Note</b>: SQLite will be used in the development mode. We will be using a Postgres instance when we put it in prod. Don't worry about it for now. Everything will be handled by settings file.
