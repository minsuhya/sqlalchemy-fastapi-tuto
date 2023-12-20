from sqlalchemy.orm import Session
from crud import crud_test


def test_index(db: Session):
    res = crud_test.get_items(db)
    return res
