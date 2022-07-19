import json
from posts_dao import PostsDAO


def load_json_data():
        with open('../../data/data.json', 'r', encoding='utf-8') as file:
            data_json = json.load(file)
            return data_json


def test_replace_string():
    posts = load_json_data()
    new_list = []

    for sub in posts:
        for i in sub['content']:
            if i == '#':
                new_string = sub['content'].replace('#', 'ссылка')
                
    new_list.append(new_string)
    return new_list


print(test_replace_string())