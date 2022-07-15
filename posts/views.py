
import logging
from flask import Blueprint, render_template, abort, request
from requests import JSONDecodeError, post
from posts.dao.posts_dao import PostsDAO
from posts.dao.comments_dao import CommentsDAO

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO('data/data.json')
comments_dao = CommentsDAO('data/comments.json')

logger = logging.getLogger("basic")

@posts_blueprint.route('/')
def posts_all():

    logger.debug("Запрошены все посты")
    
    try:
        posts = posts_dao.get_posts_all()
        return render_template('index.html', posts = posts)
    except:
        return 'Все пропало'


@posts_blueprint.route('/posts/<int:post_id>')
def posts_one(post_id):

    logger.debug(f"Запрошены посты {post_id}")

    try:
        post = posts_dao.get_comments_by_post_id(post_id)
        comments = comments_dao.get_by_post_id(post_id)      
    except (JSONDecodeError, FileNotFoundError) as error:
        return render_template("errors.html", error=error)
    else:
        if post is None:
            abort(404)
        number_of_comments = len(comments)

        return render_template('post.html', post=post, comments=comments, number_of_comments=number_of_comments)


@posts_blueprint.errorhandler(404)
def post_error(error):
    return "Такого поста нет", 404


@posts_blueprint.route('/search/')
def posts_search():

    try:
        s = request.args.get('s')

        if s == None:
            return render_template('search.html')
    
        posts = posts_dao.search_for_posts(s)
        number_of_posts = len(posts)

        return render_template('search.html', s=s, posts=posts, number_of_posts=number_of_posts)
    except:
        return "Что-то не так"


@posts_blueprint.route('/users/<username>/')
def posts_by_user(username):

    try:
        posts = posts_dao.get_posts_by_user(username)

        return render_template('user-feed.html', posts=posts)
    except:
        return "Что-то пошло не так"


@posts_blueprint.route('/tag/<tagname>/')
def tag_by_post(tagname):
    posts = posts_dao.get_post_by_tag(tagname)
    return render_template('tag.html', posts=posts) 