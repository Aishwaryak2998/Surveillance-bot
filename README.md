# Surveillance-bot
When you start out on your engineering journey, you often feel that the materials you learn in college are insufficient. But that is not necessarily true. While the stuff we learn might not make us the new Google, it does provide us with a foundation to build our empire.

We have frequently studied dc motors, operating systems, sensors, different modules, etc. One hurdle in the life of an engineer is to convert theoretical knowledge into practical one. There is no other way to do so except to get down and get your hands dirty.

In this blog, we have created a basic surveillance bot using 6 dc motors and a picam. This project will help us understand the working of basic components and how they can be incorporated into a project that can later be developed into something bigger.

What is Flask?
It is a micro web framework that has been written in Python.
database layer and form extraction is absent.
Flask depends on the Jinja template.
It allows you to develop web applications in an easy manner and provides you with a wide range of tools and libraries.
It is beginner-friendly and does not have a boiler plat code.
REST API
REST- Representational State Transfer.
This is an architectural software style that uses a subset of HTTP.
The API can be used to building and integrating software applications.
It interacts with a computer system to retrieve a piece of particular information or even perform a function.
They are lightweight and fast which makes them perfect for IoT-based projects and applications.
The allowed HTTP methods are:
GET /
POST /accounts
POST /accounts/login
GET /accounts/logout
GET, PUT, DELETE /accounts/<str : username>
GET, POST /accounts/<str : username>/tasks
GET, PUT, DELETE /accounts/<str : username>/tasks/<int : id>
Understand the movement of the robot body
The metal chassis comes along with 6 dc motors and wheels. The entire left side is connected serially and so is the right side. Therefore, we get two wires from each side.
The bot is programmed to move in 4 directions:
a) Forward - to move the bot in the forward direction, all the 6 wheels (left and right) are given input HIGH.
b)  Backward - to move the bot in the backward direction, all the 6 wheels (left and right) are given input HIGH.
c) Left - To move the body left, the left wheels are LOW while the right wheels are given input HIGH. This makes the body turn in the left direction.
d) Right - To move the body right, the right wheels are LOW while the left wheels are given input HIGH. This makes the body turn in the right direction.
Movement of the Picam
The Picam is mounted on the servo motor which can be controlled through the web page. This function provides a peripheral view to the bot which makes the navigation process much easier. 
