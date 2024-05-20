from .users_repository import UsersRepository

def test_insert_user():
    mock_first_name = 'Emanuel'
    mock_last_name = 'Lds'
    mock_age = 999
    repo = UsersRepository()
    repo.insert_user(mock_first_name, mock_last_name, mock_age)
