import main
import app

def test_account_creation_username_exists():
    assert main.SQL_INSERT("103", "cheaney", "testpassword", "collin@gmail.com", "member") == "✅ User inserted successfully."

