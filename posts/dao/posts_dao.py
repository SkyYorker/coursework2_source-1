import json



class PostsDAO:


    def __init__(self, path):
        self.path = path


    def load_json_data(self):
        with open(f'{self.path}', 'r', encoding='utf-8') as file:
            data_json = json.load(file)
            return data_json

    def get_posts_all(self):
        return self.load_json_data()


    def get_posts_by_user(self, user_name):
        posts = self.get_posts_all()
        posts_by_user = []

        for user in posts:
            if user['poster_name'] == user_name:
                posts_by_user.append(user)
        return posts_by_user
            

    def get_comments_by_post_id(self, post_id):
        posts = self.get_posts_all()

        for post in posts:
            if post['pk'] == post_id:
                return post



    def search_for_posts(self, query):
        posts = self.get_posts_all()
        posts_list = []

        for post in posts:
            if query in post['content']:
                posts_list.append(post)
        return posts_list


    def get_post_by_pk(self, pk):
        posts = self.get_posts_all()
        
        for post in posts:
            if post['pk'] == pk:
                return post


    def get_post_by_tag(self, tagname):
        posts = self.get_posts_all()
        tag_list = []

        for post in posts:
            if tagname == '#' and tagname in post['content']:
                tag_list.append(post)
        return tag_list
