
import pytest

from posts.dao.comments_dao import CommentsDAO

class CommentsTestDao:

    @pytest.fixture
    def comments_dao(self):
        return CommentsDAO('../data/comments.json')


    @pytest.fixture
    def keys_expected(self):
        return {"post_id", "commenter_name", "comment", "pk"}


    def test_get_all_comments_check_type(self, comments_dao):
        comments = comments_dao.load_json_comments()
        assert type(comments) == list, "Посты должны быть списком"
        assert type(comments[0]) == dict, "Должны быть словарем"
