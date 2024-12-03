from test.helpers import reset_database


def test_post_success(test_app):

    reset_database()

    response = test_app.post(
        "/register",
        json={
            "phone_number": "123456789012",
            "created_at": "2024-01-01T00:00:00",
            "subscribed": "0",
        },
    )
    assert response.status_code == 200


def test_post_exists(test_app):

    reset_database()

    response = test_app.post(
        "/register",
        json={
            "phone_number": "123456789012",
            "created_at": "2024-01-01T00:00:00",
            "subscribed": "0",
        },
    )
    response = test_app.post(
        "/register",
        json={
            "phone_number": "123456789012",
            "created_at": "2024-01-01T00:00:00",
            "subscribed": "0",
        },
    )

    assert response.status_code == 409
