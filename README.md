# Rent-o-Matic

The goal of our Rent-o-Matic project is to create a simple search engine for a company that rents rooms. Objects in the dataset (rooms) are described by several attributes. Our search engine will allow the user to set filters to narrow their search according to these attributes.

A room is stored in the system with the following values:

- A unique identifier.
- Size in square feet.
- Price to rent in USD per day.
- Latitude and longitude.

The description is minimal by design so that we can focus on the architectural problems and their solutions. The concepts that we’ll see can easily be extended to more complex cases.

[Rent-o-Matic and clean architecture](https://www.educative.io/courses/clean-architecture-python/7nnAwvqwAwy)bash

## Testing commands

```bash
pytest -svv

pytest -svv --cov=rentomatic --cov-report=term-missing

pytest -svv --integration # run tests marked as integration (skiped in order case)
```

## Configure PostgreSQL Repository

[Official site](https://www.postgresql.org/)

[ORM - SQLAlchemy](https://www.sqlalchemy.org/)

### Set container

[Docker image page](https://hub.docker.com/_/postgres)

```bash
docker pull postgres

docker run --name rentomatic-postgres -e POSTGRES_USER="test" -e POSTGRES_PASSWORD="test" -e POSTGRES_DB="rentomatic_db" -d postgres
```

### ISSUES

> manage.py is not working properly, running the following command throws an error, related to the dependencies
`python3.10.exe manage.py test -- --integration`
