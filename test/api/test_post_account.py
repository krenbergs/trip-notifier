from test.helpers import reset_database

def test_post_success(test_app):

    reset_database()

    response = test_app.post(
        "/register",
        json={
            "gmail": "example@gmail.com",
            "created_at": "1704063600",
        },
    )
    assert response.status_code == 200

def test_post_exists(test_app):

    reset_database()

    response = test_app.post(
        "/register",
        json={
            "gmail": "example@gmail.com",
            "created_at": "1704063600",
        },
    )
    response = test_app.post(
        "/register",
        json={
            "gmail": "example@gmail.com",
            "created_at": "1704063600",
        },
    )

    assert response.status_code == 409