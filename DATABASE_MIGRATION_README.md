# Django Database Migration in Google Cloud SQL

## Local Migrations
When changes are made to models, we can update our databases locally by running:

```
# While using our virtual environment
python manage.py makemigrations
python manage.py migrate
```

This will update the SQL tables in our local file `db.sqlite3`. If your database ever gets seriously screwed up, you can delete that file and start over, however using the migration process that should never happen.

It's advised to have a local startup script that activates the virtual environment, pulls the latest from Github, and runs the migration commands above before running the server for local development.

## Migrations on Google Cloud SQL

We can run the same migration commands, but we have to proxy our local SQL connection to connect to the instance inside of Google Cloud.

Start by reading the information on the [MySQL connect proxy documentation](https://cloud.google.com/sql/docs/mysql-connect-proxy) page.
In particular, follow the steps to "Install the proxy". This will download a `cloud_sql_proxy` binary file that you can execute from the command line.

To open a connection to the Cloud SQL database, run the following command from the root directory of the project (the same directory as this README).

```
./cloud_sql_proxy -instances=osu-cs361-supertasks:us-central1:osu-cs361-supertasks=tcp:3306 -credential_file=osu-cs361-supertasks-82eaf62fc7cb.json

```
Note the credentials JSON file contains the credentials of a service user in Google Cloud that is allowed to access our SQL databse.

Some messages will appear in your terminal but a successful connection should say "Ready for new connections".

Next, in the SuperTasks/settings.py set the variable `USE_CLOUD_SQL_PROXY` to `True`. Make sure to not commit this change and to set it back after you are done.

Finally, run the migration commands from a different terminal window.

```
# While using our virtual environment
python manage.py makemigrations
python manage.py migrate
```

From the `settings.py` configuration, Django will connect to a SQL database on local port 3306 with proper credentials. Local port 3306 is actually proxying to the Google Cloud SQL database instance because of the `cloud_sql_proxy` program that is running.
