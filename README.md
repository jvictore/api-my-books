# API My Books
<a href="https://www.python.org/downloads/">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
</a>
<a href="https://flask.palletsprojects.com/en/2.1.x/">
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
</a>
<a href="https://hub.docker.com/_/mysql">
<img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white">
</a>
<a href="https://docs.docker.com/desktop/">
<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
</a>

## Flask REST API to organize the books read.

<div align="left">



 <a href="#objective">Objective</a> •
 <a href="#features">Features</a> • 
 <a href="#pre-requisites">Pre-Requisites</a> • 
 <a href="#how-to-run">How to run</a> • 
 <a href="#how-to-terminate">How to terminate</a> • 

 <h4> 
	🚧  Project in development...  🚧
</h4>
	
## Objective:
<h4> 
	The objective of this project is to understand how a modern API based on microservices is developed and how it works. The project is an API which you can interact to store, list, update and remove the books you have read. Different features like "Get total of pages read of all books" will be added over time.
</h4>

## Features:
- [x] Get all books read.
- [x] Get one specific book by id.
- [x] Get total of pages read of all books.
- [x] Add new book.
- [x] Update a book by id.
- [x] Delete a book by id.

## Pre-requisites:

Before starting you need to have installed the following tools:
[Git](https://git-scm.com), [Python 3](https://www.python.org/downloads/), [Docker](https://docs.docker.com/desktop/), [Docker Compose](https://docs.docker.com/compose/). It is algo useful to have an API Tool like [Postman](https://www.postman.com/downloads/) to interact with the API.

## How-to-run

```bash
# Clone this repo
$ git clone https://github.com/jvictore/api-my-books.git

# Enter the cloned project folder 
$ cd api-my-books

# Just in case you already have a compose running, drop it
$ docker-compose down

# Build the project
$ docker-compose build --no-cache

# Initialize the application
$ docker-compose up -d
```
The Flask REST API will initialize on port 5000.
Access the application by <http://localhost:5000/>

You'll need the auth user/password, that by default is:
	
- User:     user
	
- Password: 1234
	
To use the API you can open Postman and import the collection located in: 
	
- api-my-books/add-ons/Api-my-books.postman_collection.json

## How-to-terminate
```bash
# Once you have use the application you have to terminate it
# Use the Docker Compose to do it
$ docker-compose down
```
	
<div>
