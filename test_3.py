import pytest
from main_3 import get_weather

def test_get_weather(mocker):
    mock_get = mocker.patch('main_3.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

    api_key = 'c0e062f5ceaddc9438c305c317c0b9c2'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 273.15}
    }

def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('main_3.requests.get')
    mock_get.return_value.status_code = 404

    api_key = 'c0e062f5ceaddc9438c305c317c0b9c2'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == None