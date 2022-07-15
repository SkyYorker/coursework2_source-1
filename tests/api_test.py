from urllib import response
from run import app

class TestApi:

    def test_api_all_posts_status_code(self):
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, 'Статус код запросов всех постов неверный'
        assert response.mimetype == 'application/json', 'Получен не JSON'


    def test_api_one_posts_status_code(self):
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        assert response.status_code == 200, 'Статус код запросов всех постов неверный'
        assert response.mimetype == 'application/json', 'Получен не JSON'
