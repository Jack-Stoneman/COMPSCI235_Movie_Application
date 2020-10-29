import pytest
from sqlalchemy import select, inspect
from COMPSCI235_Movie_Application.moviefiles.adapters.orm import metadata

def test_database_populate_inspect_table_names(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    print(inspector.get_table_names())