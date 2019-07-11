# Book Inventory API

### Getting Started

1. (Optional) Install virtualenv `pip install virtualenv`. In the top level directory, run `virtualenv yourVirtualEnv` (or whatever you would like to name the directory.) Then activate the virtualenv by running `source yourVirtualEnv/bin/activate`.
2. Install the python dependencies via pip. All the dependencies are listed in the `requirements.txt`
   - Run `pip install -r requirements.txt`
3. Create a sqlite database. We recommend creating a directory in the top level directory and placing your database there. 
   - `mkdir db`
   - `cd db`
   - `sqlite3 inventory.db`
4. Once you have your database set up, you will need to set up the tables in the database. Run the contents of `src/sqlscripts/create_*_table.sql` in your database to create the necessary tables. If you would like to have pre-populated data in the database, feel free to run the `insert_*_example.sql`.
5. If you did not place your database in the recommended location, you will have to tell the API where the database is located via the config file.
   - In `config.py`, rename `db/inventory.db` to the actual path to your database.
6. The API should now be ready to run.
   - `cd src/`
   - `python app.py` 
   - Head over to `localhost:5000` to be greeted by a friendly `Hello!`

### Running Tests

cd into `src/` and run `python -m pytest`

### Building a Docker image

1. Make sure you have Docker installed on your machine.
2. Make sure you are in the top level directory and run the command `docker build -t mynamehere .`

### Running a Docker Container

1. After the image has built, set up an external sqlite database that will be mounted to the docker container.
   - `cd /absolute/path/to/db/directory`
   - `sqlite3 inventory.db`
   - Run sqlscripts to set up tables
2. Run the command `docker run -d -p hostport:5000 -v /absolute/path/to/db/directory:/app/path/to/database mynamehere`
3. Head over to `localhost:hostport` or whatever you have chosen to be greeted by a friendly `Hello!`
