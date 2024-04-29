#!/usr/bin/python3
"""Script that lists all objects from a database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}'
        f'@localhost:3306/{sys.argv[3]}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state_id, state_name in session.query(
            State.id, State.name).order_by(State.id):
        print(f"{state_id}: {state_name}")

    session.close()
