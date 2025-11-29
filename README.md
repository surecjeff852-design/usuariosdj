# usuariosdj:
Nombre: Usuiariosdj

# Descripcion:
El proyecto es un inventario que esta conectado a una base de datos que muestra el nombre, capacidad, disponibles, ventas totales, etc.. 

# Tecnologias utilizadas:
asgiref==3.11.0
Django==4.2.26
Python==3.9.13
mysqlclient==2.2.7
psycopg2==2.9.11
sqlparse==0.5.3
typing_extensions==4.15.0
tzdata==2025.2
Unipath==1.1

# Instalacion:
1. Clona este repositorio:
'''bash
git clone https://github.com/surecjeff852-design/usuariosdj.git

2. Entrar al directorio del proyecto:
cd usuariosdj

3. Crear un entorno virtual:
python -m venv 'Proyecto'

4. Activar el entorno virtual:
'Proyecto'\Scripts\activate

5. Instalar dependencias:
pip install -r requirements.txt         

6. Aplicar migraciones:
python manage.py makemigrations/migrate

7. Ejecutar el servidor: 
python manage.py runserver

# Configuracion:
Estos son los datos para el acceso a la base de datos
    "DB_NAME": "acerby_wp509",
    "USER": "esuoj",
    "PASSWORD": "Jefferson1"
    'HOST':'localhost',
    'PORT':'3306',

# Configuracion para Mysql:
CREATE DATABASE mi_base;
CREATE USER 'usuario_django'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON mi_base.* TO 'usuario_django'@'localhost';
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON *.* TO 'esuoj'@'localhost' IDENTIFIED BY 'Jefferson1';
FLUSH PRIVILEGES;