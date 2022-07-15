
import json


class CommentsDAO:

    def __init__(self, path):
        self.path = path


    def load_json_comments(self):
        with open(f'{self.path}', 'r', encoding='utf-8') as file:
           comments_json = json.load(file)
           return comments_json

    def get_by_post_id(self, post_id):
        comments = self.load_json_comments()
        comments_by_id = []

        for comment in  comments:
            if comment['post_id'] == post_id:
                comments_by_id.append(comment)
        return comments_by_id
