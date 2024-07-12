Docker (PowerShell):
  docker pull postgres:alpine
  docker run --name fastapi-postgres -e POSTGRES_PASSWORD=postpass -d -p 5432:5432 postgres:alpine
  docker exec -it fastapi-postgres bash
  create database fastapi_database;
  create user myuser with encrypted password 'postpass';
  grant all privileges on database fastapi_database to myuser;
  \c fastapi_database;
  psql -h localhost -p 5432 postgres
  
Python (Pycharm):
  ...
  python
  import services
  services._add_tables() # На этом моменте вылетела ошибка - UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc2 in position 61: invalid continuation byte

