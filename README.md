# ROSWebServer

This code is to be deployed on an EC2 Instance of AWS Cloud.

## Purpose

The purpose of this application is to provide a Web Interface for visualizing data of ROS-based robots. It also serves to send control commands to the robot from anywhere in the world as long as the robot is connected to the Web Application.

So far, we have tested its working on the following platforms:
- Turtlebot3 Robot (Gazebo Simulation)
- Turtlebot3 Robot (Burger - Actual hardware)

## Access the Application
Access the application: http://13.49.57.166:8000/

## Initial Cloud Setup

Update the System:
```bash
clear
sudo apt-get update
```

Clone the Repository from GitHub:
```bash
git clone https://github.com/fabeha-raheel/AEEL-Ros-WebApp-Server-1.0.git
```

Change Directory:
```bash
cd AEEL-Ros-WebApp-Server-1.0
```

Activate Virtual Environment:
```shell
source venv/bin/activate
```

Install pip:
```shell
sudo apt install python3-pip
```

Install the following:
```shell
pip install django
pip install -U channels["daphne"]
```
or,
```shell
pip install -r requirements.txt
```

Django Application Migrations
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

Run the server
```shell
python3 manage.py runserver 0.0.0.0:8000
```