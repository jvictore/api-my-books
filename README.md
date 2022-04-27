# api-my-books
Python
Flask

Não concluído

Instalar repositorio  mysql-server (configurar sudo mysql_secure_installation)

Download XAMPP pelo site: https://www.apachefriends.org/download.html


sudo apt install net-tools
Para iniciar o wampp: sudo /opt/lampp/lampp start
ideia: 
	cp sudo /opt/lampp/lampp /usr/bin/
	iniciar com: lampp start

caso de o erro:/opt/lampp/bin/mysql.server: 264: kill: No such process
sudo service mysql stop

Caso encontrar o erro:
ERROR: Could not find a version that satisfies the requirement mysqlclient
ERROR: No matching distribution found for mysqlclient

solucao:
sudo apt install libmysqlclient-dev python3-dev



Apos clonar o projeto, entrar na pasta raiz do projeto e criar um ambiente:
python3 -m venv venv

Ativar o ambiente:
source venv/bin/activate

Instalar os modulos requisitados:
pip install -r requirements.txt


