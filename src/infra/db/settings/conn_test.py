import pytest
from .conn import DBConnectionHandler

@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_conn_ = DBConnectionHandler()
    engine = db_conn_.get_engine()

    assert engine.connect() is not None
