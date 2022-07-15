
import logging
from flask import Blueprint, jsonify


from posts.dao.posts_dao import PostsDAO
from posts.dao.comments_dao import CommentsDAO

api_blueprint = Blueprint('api_blueprint', __name__)

posts_dao = PostsDAO('data/data.json')
comments_dao = CommentsDAO('data/comments.json')

logger = logging.getLogger("basic")

@api_blueprint.route('/api/posts/')
def posts_all():
    logger.debug('Все посты через API')
    posts = posts_dao.get_posts_all()
    return jsonify(posts)



@api_blueprint.route('/api/posts/<int:post_id>/')
def posts_search(post_id):
    logger.debug(f'Запрошены все посты с id {post_id} через API')
    post = posts_dao.get_post_by_pk(post_id)
    return jsonify(post)

