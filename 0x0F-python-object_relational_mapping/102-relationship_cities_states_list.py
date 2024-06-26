#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
Usage: ./102-relationship_cities_states_list.py <mysql username> <mysql password> <database name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py <mysql username> <mysql password> <database name>")
        exit(1)

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    # Create an engine and connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()

    # Query all City objects, sorted by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close session
    session.close()
