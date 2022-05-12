# API My Books
## Flask REST API to organize the books read.

<div align="left">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

 <a href="#objetivo">Objetivo</a> •
 <a href="#features">Features</a> • 
 <a href="#prerequisitos">Pré-Requisitos</a> • 
 <a href="#howtorun">How to run</a> • 
 <a href="#licenc-a">Licença</a> • 
 <a href="#autor">Autor</a>

 <h4> 
	🚧  Projeto em construção...  🚧
</h4>

## Features:
- [x] Get all books read.
- [x] Get one specific book by id.
- [x] Get total of pages read of all books.
- [x] Add new book.
- [x] Update a book by id.
- [x] Delete a book by id.

## Pré-requisitos:

Before starting you need to have installed the following tools:
[Git](https://git-scm.com), [Python 3](https://www.python.org/downloads/), [Docker](https://docs.docker.com/desktop/), [Docker Compose](https://docs.docker.com/compose/). Also is nice to have a API Tool like [Postman](https://www.postman.com/downloads/) to interact with the API.

## How to run

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

# The Flask REST API will initialize on port 5000.
# Access the application by <http://localhost:5000/>

# You'll need the auth user/password, that by default is:
# User: 	user
# Password: 1234
```



<div>
