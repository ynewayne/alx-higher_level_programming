# Python - Object-Relational Mapping

This project introduces object-relational mapping (ORM) in Python, focusing on using MySQLdb and SQLAlchemy to interact with databases. The tasks include querying, creating, editing, and deleting tables in MySQL.

## Tests ✅

- [tests](./tests): Contains SQL and Python scripts for setting up test tables for all files, provided by ALX.

## Tasks 📜

1. **Get all states**
   - [0-select_states.py](./0-select_states.py): Lists all states in the `hbtn_0e_0_usa` database using MySQLdb.
   - Usage: `./0-select_states.py <mysql username> <mysql password> <database name>`.

2. **Filter states**
   - [1-filter_states.py](./1-filter_states.py): Lists states with names starting with `N` in the `hbtn_0e_0_usa` database.
   - Usage: `./1-filter_states.py <mysql username> <mysql password> <database name>`.

3. **Filter states by user input**
   - [2-my_filter_states.py](./2-my_filter_states.py): Displays values matching a given name in the `states` table.
   - Usage: `./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.

4. **SQL Injection...**
   - [3-my_safe_filter_states.py](./3-my_safe_filter_states.py): Displays values matching a given name, preventing SQL injections.
   - Usage: `./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>`.

5. **Cities by states**
   - [4-cities_by_state.py](./4-cities_by_state.py): Lists all cities from the `hbtn_0e_4_usa` database.
   - Usage: `./4-cities_by_state.py <mysql username> <mysql password> <database name>`.

6. **All cities by state**
   - [5-filter_cities.py](./5-filter_cities.py): Lists all cities of a given state in the `hbtn_0e_4_usa` database.
   - Usage: `./5-filter_cities.py <mysql username> <mysql password> <database name>`.

7. **First state model**
   - [model_state.py](./model_state.py): Defines a class `State` that inherits from SQLAlchemy `Base` and links to the MySQL table `states`.

8. **All states via SQLAlchemy**
   - [7-model_state_fetch_all.py](./7-model_state_fetch_all.py): Lists all `State` objects from the `hbtn_0e_6_usa` database using SQLAlchemy.
   - Usage: `./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>`.

9. **First state**
   - [8-model_state_fetch_first.py](./8-model_state_fetch_first.py): Prints the first `State` object from the `hbtn_0e_6_usa` database using SQLAlchemy.
   - Usage: `./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>`.

10. **Contains `a`**
    - [9-model_state_filter_a.py](./9-model_state_filter_a.py): Lists all `State` objects containing the letter `a` in the `hbtn_0e_6_usa` database using SQLAlchemy.
    - Usage: `./9-model_state_filter_a.py <mysql username> <mysql password> <database name>`.

11. **Get a state**
    - [10-model_state_my_get.py](./10-model_state_my_get.py): Prints the `id` of the `State` object with a name matching the provided argument in the `hbtn_0e_6_usa` database using SQLAlchemy.
    - Usage: `./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state searched name>`.

12. **Add a new state**
    - [11-model_state_insert.py](./11-model_state_insert.py): Adds the `State` object "Louisiana" to the `hbtn_0e_6_usa` database using SQLAlchemy.
    - Usage: `./11-model_state_insert.py <mysql username> <mysql password> <database name>`.

13. **Update a state**
    - [12-model_state_update_id_2.py](./12-model_state_update_id_2.py): Changes the name of the `State` object with `id = 2` to "New Mexico" in the `hbtn_0e_6_usa` database using SQLAlchemy.
    - Usage: `./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>`.

14. **Delete states**
    - [13-model_state_delete_a.py](./13-model_state_delete_a.py): Deletes all `State` objects with a name containing the letter `a` from the `hbtn_0e_6_usa` database using SQLAlchemy.
    - Usage: `./13-model_state_delete_a.py <mysql username> <mysql password> <database name>`.

15. **Cities in state**
    - [model_city.py](./model_city.py): Defines a class `City` that inherits from SQLAlchemy `Base` and links to the MySQL table `cities`.
        - Includes a class attribute `state_id` as a foreign key to `states.id`.
    - [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py): Lists all `City` objects in the `hbtn_0e_14_usa` database using SQLAlchemy.
    - Usage: `./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>`.

16. **City relationship**
    - [relationship_state.py](./relationship_state.py): Defines a class `State` with a relationship to `City`.
    - [relationship_city.py](./relationship_city.py): Defines a class `City`.
    - [100-relationship_states_cities.py](./100-relationship_states_cities.py): Adds the `State` "California" with `City` "San Francisco" to the `hbtn_0e_100_usa` database using SQLAlchemy.
    - Usage: `./100-relationship_states_cities.py <mysql username> <mysql password> <database name>`.

17. **List relationship**
    - [101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py): Lists all `State` and corresponding `City` objects in the `hbtn_0e_101_usa` database using SQLAlchemy.
    - Usage: `./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>`.

18. **List city**
    - [102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py): Lists all `City` objects from the `hbtn_0e_101_usa` database using SQLAlchemy.
    - Usage: `./102-relationship_cities_states_list.py <mysql username> <mysql password> <data
