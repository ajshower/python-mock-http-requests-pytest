import requests


def test_fixture(requests_mock):
    requests_mock.get("http://123-fake-api.com", text="Hello!")
    response = requests.get("http://123-fake-api.com")

    assert response.text == "Hello!"
