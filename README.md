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
## Set an Elastic IP on AWS Cloud (Static IP)
1. Go to the Amazon EC2 console
2. From the Navigation Pane, select 'Network and Security' -> 'Elastic IPs'
3. Click on 'Allocate Elastic IP address'
4. For Public IPv4 address pool, choose 'Amazon's pool of IPv4 addresses'
5. Click on 'Allocate'
6. Once the Elastic IP is created, select it by clicking on the checkbox next to it.
7. Click on 'Actions' -> 'Associate Elastic IP address'
8. For 'Resource Type', choose 'Instance'
9. Choose the instance with which to associate the Elastic IP address.
10. Click on 'Associate'

For more details, refer: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html
