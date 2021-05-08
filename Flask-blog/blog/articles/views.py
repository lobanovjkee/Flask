from flask import Blueprint, render_template, request
from blog.users.views import USERS

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = [
    {
        'id': 1,
        'title': 'The guru captures.',
        'text': 'When the planet trembles for deep space, all green people pull intelligent, strange spacecrafts.',
        'author': {
            'name': USERS[0]['name'],
            'id': USERS[0]['id'],
        },
    },
    {
        'id': 2,
        'title': 'the doer needs. ',
        'text': 'I travel this resistance, it\'s called post-apocalyptic paralysis.Paralysis, mind, and sonic shower.',
        'author': {
            'name': USERS[1]['name'],
            'id': USERS[1]['id'],
        },
    },
    {
        'id': 3,
        'title': 'the self follows. ',
        'text': 'Gabaliums peregrinationes in mirabilis mare!',
        'author': {
            'name': USERS[2]['name'],
            'id': USERS[2]['id'],
        },
    },
    {
        'id': 4,
        'title': 'the teacher facilitates. ',
        'text': 'Rice can be garnished with smashed cracker crumps, also try jumbleing the cake with kefir.',
        'author': {
            'name': USERS[3]['name'],
            'id': USERS[3]['id'],
        },
    },
    {
        'id': 5,
        'title': 'the individual discovers. ',
        'text': 'Seashells whine with booty!Avast, arrr.When the lad dies for haiti, all seashells mark rough, big pins.The mast loots with fortune, drink the bahamas.',
        'author': {
            'name': USERS[0]['name'],
            'id': USERS[0]['id'],
        },
    }
]


@article.route('/')
def articles_list():
    req = request
    articles = ARTICLES
    return render_template(
        'articles/list.html',
        request=req,
        articles=articles,
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    article_info = ARTICLES[pk - 1]
    return render_template(
        'articles/article.html',
        article=article_info,
    )
