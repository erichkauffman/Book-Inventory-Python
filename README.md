# Book Inventory API

### Getting Started

1. Install the python dependencies via pip. All the dependencies are listed in the `requirements.txt`
   - Run `pip install -r requirements.txt`
2. Create a sqlite database. We recommend creating a directory in the top level directory next to `src/` and placing your database there. 
   - `mkdir db`
   - `cd db`
   - `sqlite3 inventory.db`
3. Once you have your database set up, you will need to set up the tables in the database. Run the contents of `src/sqlscripts/create_book_table.sql` in your database to create the necessary table. If you would like to have pre-populated data in the database, feel free to run the `insert_book_example.sql`
4. Next, you will have to create a config file to tell the API where the database is located. Use `config.example.py` as a guide.
   - `cp config.example.py ./config.py`
   - Rename `path/to/database.db` to the actual path to your database. Remember, this path is relative to where you run the app, so if you run the app at the top level directory, the path would look like this: `db/inventory.db`. But if you run the program in `src/`, then the path might look like this: `../db/inventory.db`
5. Remeber to set up your prefered flask configurations, such as setting the app, address, port, environment, etc.
6. The API should now be ready to run.
   - `flask run` 
   - Head over to `localhost:5000` or your prefered address:port to be greeted by a friendly `Hello!`

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