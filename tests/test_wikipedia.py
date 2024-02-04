from wikiwikiwrap import create_app
import pytest


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_views(client):
    response = client.get("/views/Article/2022/01")
    assert response.status_code == 200


def test_invalid_article_name(client):
    response = client.get("/views/invalid$-article/2022/01")
    assert response.status_code == 400
    assert response.json["title"] == "Error"
    assert response.json["status"] == 400
    assert (
        response.json["detail"]
        == "Invalid article name. Only alphanumeric characters are allowed."
    )
    assert response.json["uri"] == "/views/invalid$-article/2022/01"


def test_invalid_article_year(client):
    response = client.get("/views/Article/abcd/01")
    assert response.status_code == 400
    assert response.json["title"] == "Error"
    assert response.json["status"] == 400
    assert response.json["detail"] == "Invalid year. Year should be a 4-digit number."
    assert response.json["uri"] == "/views/Article/abcd/01"


def test_invalid_article_month(client):
    response = client.get("/views/Article/2022/13")
    assert response.status_code == 400
    assert response.json["title"] == "Error"
    assert response.json["status"] == 400
    assert (
        response.json["detail"]
        == "Invalid month. Month should be a 2-digit number between 01 and 12."
    )
    assert response.json["uri"] == "/views/Article/2022/13"


def test_article_not_found(client):
    response = client.get("/views/InvalidArticle/2022/01")
    assert response.status_code == 404
    assert response.json["title"] == "Error"
    assert response.json["status"] == 404
    assert response.json["uri"] == "/views/InvalidArticle/2022/01"
