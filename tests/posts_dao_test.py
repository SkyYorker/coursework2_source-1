import pytest

from posts.dao.posts_dao import PostsDAO


class TestPostsDao:

    @pytest.fixture
    def posts_dao(self):
        return PostsDAO('data/data.json')


    @pytest.fixture
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

  
    # Получение всех постов

    def test_get_all_check_type(self, posts_dao):
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "Посты должны быть списком"
        assert type(posts[0]) == dict, "Должны быть словарем"


    def test_get_all_has_keys(self, posts_dao, keys_expected):
        posts = posts_dao.get_posts_all()       
        for post in posts:
            keys = post.keys()
            assert set(keys) == keys_expected, "Полученные ключи неверные"

    # Получение одного поста

    def test_get_one_check_type(self, posts_dao):
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict, "Пост должен быть словарем"


    def test_get_one_has_keys(self, posts_dao, keys_expected):
        post = posts_dao.get_post_by_pk(1)
        post_keys = set(post.keys())
        assert post_keys == keys_expected, 'Полученные ключи неверные'


    parametrs_to_get_post_by_pk = [1,2,3,4,5,6,7,8]

    @pytest.mark.parametrize('post_pk', parametrs_to_get_post_by_pk)
    def test_get_one_check_type_has_correct_pk(self, posts_dao, post_pk):
        post = posts_dao.get_post_by_pk(post_pk)
        assert post['pk'] == post_pk, 'Неверный номер'

    # Получение постов по пользователю

    post_parametrs_by_user = [('leo', {1, 5}), ('larry', {4, 8}), ('hank', {7, 3}), ('johnny', {2, 6})]

    @pytest.mark.parametrize('poster_name, post_pk_correct', post_parametrs_by_user)
    def test_get_user_by_posts(self, posts_dao, poster_name, post_pk_correct):
        posts = posts_dao.get_posts_by_user(poster_name)
        post_pk = set()
        for post in posts:
            post_pk.add(post['pk'])

        assert post_pk == post_pk_correct, 'Неверное получение'

    
    # Поиск постов

    post_parametrs_by_search = [('закат', {7}), ('пальто', {4}), ('свалка', {3}), ('пирог', {1})]

    @pytest.mark.parametrize('query, post_pk_correct', post_parametrs_by_search)
    def test_search_by_posts(self, posts_dao, query, post_pk_correct):
        posts = posts_dao.search_for_posts(query)
        post_pk = set()
        for post in posts:
            post_pk.add(post['pk'])

        assert post_pk == post_pk_correct, 'Неверное поиск постов'

    # Поиск

    def test_search_check_type(self, posts_dao):
        posts = posts_dao.search_for_posts("б")
        assert type(posts) == list, 'Результат поиска должен быть списком'
        assert type(posts[0]) == dict, 'Элементы, найденные поиском должны быть словарем'

    def test_search_has_keys(self, posts_dao, keys_expected):
        posts = posts_dao.search_for_posts("б")[0]
        posts_keys = set(posts.keys())
        assert posts_keys == keys_expected, 'Полученные ключи неверны'


    parametrs_by_responses = [('бассейн', [4]), ('лампочка', [6]), ('дом', [2, 7, 8])]

    @pytest.mark.parametrize('query, post_pks', parametrs_by_responses)
    def test_search_word(self, posts_dao, query, post_pks):
        posts = posts_dao.search_for_posts(query)
        words = []

        for i in posts:
            words.append(i["pk"])

        assert words == post_pks, f'Неверный поиск по запросу {query}'

    # Получение по пользователю 

    def test_search_check_type(self, posts_dao):
        posts = posts_dao.get_posts_by_user("hank")
        assert type(posts) == list, 'Результат поиска должен быть списком'
        assert type(posts[0]) == dict, 'Элементы, найденные поиском должны быть словарем'
         
    def test_search_has_keys(self, posts_dao, keys_expected):
        posts = posts_dao.get_posts_by_user("hank")[0]
        posts_keys = set(posts.keys())
        assert posts_keys == keys_expected, 'Полученные ключи неверны'


    parametrs_by_users = [('johnny', [2, 6]), ('larry', [4, 8]), ('hank', [3, 7]), ("Александр Косых", [])]

    @pytest.mark.parametrize('user_name, post_pks', parametrs_by_users)
    def test_search_by_user(self, posts_dao, user_name, post_pks):
        posts = posts_dao.get_posts_by_user(user_name)
        users = []

        for user in posts:
            users.append(user["pk"])

        assert users == post_pks, f'Неверный поиск по пользователю {user_name}'

    # Получение постов по тегу

    def test_search_check_type(self, posts_dao):
        posts = posts_dao.get_post_by_tag('#')
        assert type(posts) == list, 'Результат поиска должен быть списком'


    def test_search_has_keys(self, posts_dao, keys_expected):
        posts = posts_dao.get_post_by_tag("#")[0]
        posts_keys = set(posts.keys())
        assert posts_keys == keys_expected, 'Полученные ключи неверны'