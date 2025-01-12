import pytest
from main_4 import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('main_4.requests.get')

    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://cdn2.thecatapi.com/images/abcd1234.jpg'}
    ]

    result = get_random_cat_image()

    assert result == 'https://cdn2.thecatapi.com/images/abcd1234.jpg'


def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('main_4.requests.get')

    # Создаем мок-ответ для неуспешного запроса
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = None

    result = get_random_cat_image()

    assert result is None
