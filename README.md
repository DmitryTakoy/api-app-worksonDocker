# IMDB analog working on API, Docker, Django

YaMDb is a project that collects user reviews on various works.

## Example .env file

DB_ENGINE=django.db.backends.postgresql

DB_NAME=myapp_db

POSTGRES_USER=myapp_user

POSTGRES_PASSWORD=myapp_password

DB_HOST=db

DB_PORT=5432

## Running the project and management

### Docker Compose

`docker-compose.yml` defines the containers, their images and configuration, as well as any environment variables, volumes and networks.

You can start them using the `docker-compose up` command. This will start all the containers in your `docker-compose.yml` file.

If you want to run your containers in detached mode (i.e. in the background), you can use the `-d` flag: `docker-compose up -d`.

If you want to rebuild your containers before running them, you can use the `--build` flag: `docker-compose up --build`.

To stop the application, use the `docker-compose down` command. This will stop and remove all the containers in your configuration file.

If you want to view the logs for a specific container, you can use the `docker-compose logs` command followed by the name of the container. For example, `docker-compose logs web` will show the logs for the web service.

To perform operations inside a container, use the `docker-compose exec` command followed by the name of the container and the command you want to run. For example, `docker-compose exec web bash` will start a bash shell in the web container.

If you want to clean up any resources that are no longer in use, use the `docker-compose down --rmi all --volumes` command. This will remove all stopped containers, all networks not used by at least one container, all volumes not used by at least one container, and all images without a container associated to them.

### Django App

After the first build run, you need to perform the following steps:
1. Apply migrations: `docker-compose exec web python manage.py migrate`.
2. Create a superuser: `docker-compose exec web python manage.py createsuperuser`.
3. Collect static files in the nginx storage: `docker-compose exec web python manage.py collectstatic --no-input`.

## Database and data management

After the first run, you need to create a database for the application with the name `yamdb`:
1. Log in to the Postgresql container in `psql` mode: `docker-compose exec -it my-postgres-container psql -U postgres`.
2. Create a new database: `CREATE DATABASE yamdb;`.
3. Grant management rights to your superuser (or create a new user with `CREATE USER myuser WITH ENCRYPTED PASSWORD 'xxxyyyzzz';`): `GRANT ALL PRIVILEGES ON DATABASE yamdb TO myusers;`.

## Technologies used

- Docker
- Django (v2.2.16)
- Django REST Framework (v3.12.4)
- PyJWT (v2.1.0)
- Django REST Framework SimpleJWT (v5.2.2)
- Django Filter (v2.4.0)
- pytz (v2020.1)
- sqlparse (v0.3.1)
- psycopg2-binary (v2.8.6)
- Gunicorn (v20.0.4)
- asgiref (v3.2.10)
