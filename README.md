# api-my-books
Python
Flask

Não concluído

Instalar repositorio  mysql-server (configurar sudo mysql_secure_installation)

Install XAMPP pelo site
sudo apt install net-tools
Para iniciar o wampp: sudo /opt/lampp/lampp start
ideia: 
	cp sudo /opt/lampp/lampp /usr/bin/
	iniciar com: lampp start


Instalar modulo dentro do venv: flask, flask_httpauth, mysql-connector, flask_mysqldb

Caso encontrar o erro:
ERROR: Could not find a version that satisfies the requirement mysqlclient
ERROR: No matching distribution found for mysqlclient

solucao:
sudo apt install libmysqlclient-dev python3-dev

