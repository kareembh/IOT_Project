# Weather Station

Weather Station is an Internet of Thing project done for my Internet of Things graduate level class.  It uses a raspberry pi and an attachment called a sense hat to collect data on three weather conditions temperature, humidity and air pressure.  It then stores this data in a realtime database using the firebase API which then allows me to sync my web application to the database and view the data in real time.  the data is collected every 10 seconds and the new values can be viewed on the web application with out the need to refresh the page to get the new values with all past values logged to the console.

#Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

#Prerequisites

First you will need to have a raspberry pi with the basic setup here is a link to a guild on how to do so https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/3 . Second you will need a sense hat attachment for your raspberry pi and to set it up on your pi here is a link on how to set it up https://www.raspberrypi.org/documentation/hardware/sense-hat/ .  Third you will need a firebase account and to create a working database project for your application here is a link on how to do this https://www.youtube.com/watch?v=6juww5Lmvgo .  Lastly you will need a server to host your web application for this project I used a dedicated school server.  Optional if you would like to be able to connect to you raspberry pi remotely you must enable ssh on your pi.

# Deployment

Add additional notes about how to deploy this on a live system
To deploy this project you must have the test.py file saved on your pi and the index.html and index.css files loaded on your server (Note everything must be connected to the internet or else writing data to the firebase database will not work). Once done all you have to do is run the test.py file my going to the directory where the file is located on your pi on the terminal and typing "python test.py" then press enter that will start the program which will allow the sense hat to begin collecting data (note if you are not using a monitor for your pi you will need to connect to it using ssh).

# Built With

Firebase -  the real time database


Authors

Kareem B Henry - Entire project developer
