# ROSWebServer

This code is to be deployed on an EC2 Instance of AWS Cloud.

## Purpose

The purpose of this application is to provide a Web Interface for visualizing data of ROS-based robots. It also serves to send control commands to the robot from anywhere in the world as long as the robot is connected to the Web Application.

So far, we have tested its working on the following platforms:
- Turtlebot3 Robot (Gazebo Simulation)
- Turtlebot3 Robot (Burger - Actual hardware)

## Installations

1. Create a python virtual environment:
```shell
python -m venv <name_of_virtual_environment>
```
For 'name_of_virtual_environment', we used 'venv'.

2. Install the following
```shell
pip install django
pip install -U channels["daphne"]
```

### How to activate the virtual environment

To activate the virtual environment (while using Linux/Ubuntu), use:
```shell
source <name_of_venv>/bin/activate
```

## Create a Django Project

1. Create a new project:
```shell
django-admin startproject <name_of_project> .
```
2. Create an application:
```shell
python manage.py startapp <name_of_app>
```

3. Prepare your django application code.

4. Create requirements.txt file:
```shell
pip freeze > requirements.txt
```
5. Install packages from requirements.txt file:
```shell
pip install -r requirements.txt
```

## GitHub

To initialize git:
```shell
git init
```

Connect with remote repository:
```shell
git remote add origin https://github.com/fabeha-raheel/AEEL-Ros-WebApp-Server-1.0.git
```

Create a branch in remote repository:
```shell
git branch -M master
```
Add modifications:
```shell
git add .
```
Commit changes:
```shell
git commit -m 'comments'
```

Push to remote repo:
```shell
git push -u origin master
```
Pull request from master:
```shell
git pull origin master
```