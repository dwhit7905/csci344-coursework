# ORM Activity Setup

1. **Create a new database** by opening your terminal. From any directory, type:
    ```
    psql -U postgres
    ```

    Once you're on the psql command prompt, create a new database called `orm_test`:

    ```sql
    create database orm_test;
    ```

    Once you get a "Database Created" message, exit `psql` (`\q`).


2. **Python Setup**

    Download the sample files (`orm-introduction` folder) and save them to your lectures folder.

3. **Set Up Your Virtual Environment**

    Open the terminal and navigate to your `orm-introduction` folder. Then, set up a virtual environment and install the dependencies as follows (depending on your operating system):

    ```
    poetry install
    ```

4. **Update your database connection string**

    Open the `.env` file and modify your connection string so that your postgresql password is reflected (versus 12345). So, instead of...

    ```
    DB_URL=postgresql+psycopg://postgres:12345@localhost/orm_test
    ```

    You will change it to...

    ```
    # but replace {your_password} with your actual password:
    DB_URL=postgresql+psycopg://postgres:{your_password}@localhost/orm_test   
    ```

5. **Populate your database**
    
    From the terminal, build your database as follows (from the command prompt from within the `orm-introduction` folder).

    ```bash
    poetry run python populate.py
    ```

6. **Run the SQLAlchemy Tester**

    ```bash
    poetry run python tester.py
    ```
