Social Networking API Creation Using Docker

Django Application Setup
1. Open Project Folder in Visual Studio Code.
2. Install Virtual Environment by "pip install virtualenv"
3. Create Virtual Environment "virtualenv venv"
4. Activate the Virtual Environment "\venv\Scripts\activate" in the command prompt terminal
5. Install Necessary Packages like "pip install django djangorestframework"
6. Start a New Project "django-admin startprojectsocial_app"
7. Navigate to Project Directory "cd social_app"
8. Add packages installed to venv by "pip install -r <path_to_requiements.txt" and "pip freeze>requrements.txt"
9. Create Applications "python manage.py startapp user_management" and "python manage.py startapp social_interactions"
10. Modify Installed Apps - Add the newly created apps and necessary packages to the INSTALLED_APPS section in settings.py.
11. Add REST Framework Authorization Token in settings.py
12. Generate Code for Each Application - create and configure models.py, serializers.py, views.py etc files as needed.
13. Create Superuser by "python manage.py createsuperuser" to manage the Django admin interface.
14. Apply Database Migrations by "python manage.py makemigrations" and  "python manage.py migrate"
15. Run the Django Application by "python manage.py runserver"
16. Verify Application by navigate to "http://127.0.0.1:8000/" on the browser. 

Executing APIs with Postman
1. Download and Install Postman Desktop
2. Create a New Collection-Click the "New" button and select "Collection" and rename.
3. Add a New Request for Each API Functionalityin the url 
4. The API will be accessible at http://127.0.0.1:8000/.

API Endpoints

I. User Management
1. Signup (Body-->raw,JSON)
URL: /account/signup/
Method: POST
Request
Body:
{
    "email": "amal007@gmail.com",
    "password":"amal12345",
    "name": "amal"  
}
Response:
{
   "email": "amal007@gmail.com",
   "name": "amal"  
}

2. Login 
URL: /account/login/
Method: POST
Request
Body:
{
    "email": "AKHIL@GMAIL.COM",
    "password":"akhil12345"
}
Response:
{
   "refresh": "refresh_token",
   "access": "access_token", 
}


II. Social_Interactions
3. Search
Method: GET
URL: /interaction/search/
URL:/interaction/search/?q=amal007@gmail.com  # email search
URL:/interaction/search/?q=a&page=2 # pagination, 1 page with 10 records

URL:/interaction/search/?q=ama # matching search
Response
{
    "email": "amal007@gmail.com",
    "password":"amal12345",
    "name": "amal"  
} # so on

4. Send Friend Request

Method: POST
URL: /interaction/friend-requests/
Request
Response
{
"to_user_id": 1
}

5. Accept or Reject Friend Request
Method: POST
URL: /interaction/friend-request/action/
Response # friend request send person should accept or reject
#POST: {
    "friend_request_id": 8,
    "action": "accept" # reject
}

6. List Frends
Method:GET
URL:/interaction/friends/
Response
{
    "email": "amal007@gmail.com",
    "name": "amal"  
}

7. Pending Friends List
Method: GET
URL: interaction/friend-requests/pending/
Response
{
    "email": "amal007@gmail.com",
    "name": "amal",
    "status":"pending", 
}

Note:
1) Basc Auth & Token should be mentioned in the Authorization tab for Social_Interaction API and click send.
(only authorized users can access Social_Interaction APIs) 

Functionalities included:
1) Same user can't send request to themselves.
2) Friend request limit is 3 per minute
3) email is caseinsensitve, password is casesensitive for signup and login

Docker
1. Download and Install Docker Desktop
2. Verify Docker Installation by "docker --version"
3. Open Project in Visual Studio Code.
4. Create Docker Configuration Files:
      a) .dockerignore (optional)
      b) Dockerfile
      c) docker-compose.yml
5) Check if WSL is Installed in Command Prompt
      a) wsl
      b) wsl --install
note: WSL supports windows10 or higher.
6) Enable Required Windows Features for Docker Installation:
      a) Open "Turn Windows features on or off".
      b) Enable "Hyper-V" and "Windows Subsystem for Linux".
      c) Restart your PC.
7) Enable Virtualization in BIOS if WSL problem Persists:
      a) Restart your system and press the appropriate key (e.g., F9, F10) to enter the BIOS setup.
      b) Navigate to "System Configuration" and find "Virtualization Technology".
      c) Enable "Virtualization Technology" by pressing the corresponding key (e.g., F5).
      d) Save the changes and exit the BIOS setup by pressing F10.

commands
1) cd social_app
2) docker-compose up --build

Github
1) Push Project folder from Git Bash