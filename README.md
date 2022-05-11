uvicorn server:app --reload
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres
docker exec -it da5bdf1328c1 bash
psql -U postgres
create database fastapi_database;
docker rm da5bdf1328c1
sudo apt install libpq-dev (для psycorg2)
