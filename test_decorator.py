import pytest
import requests
import requests_mock


@pytest.mark.skip(
    reason="requests_mock decorators cannot be used with pytest. Comment out this line to see the error."
)
@requests_mock.mock()
def test(m):
    m.get("http://123-fake-api.com", text="Hello!")
    response = requests.get("http://123-fake-api.com").text

    assert response.text == "Hello!"
