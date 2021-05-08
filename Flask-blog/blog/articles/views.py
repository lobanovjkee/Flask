from flask import Blueprint, render_template,request

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/')
def articles_list():
    req = request
    return render_template('articles/list.html', request=req)
