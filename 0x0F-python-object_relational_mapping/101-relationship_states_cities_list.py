#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the database hbtn_0e_101_usa.
Usage: ./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>")
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

    # Query all State objects, sorted by states.id, and use the cities relationship
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close session
    session.close()
