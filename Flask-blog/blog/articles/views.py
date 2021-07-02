from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, Author, Tag

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/')
def articles_list():
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        request=request,
        articles=articles,
    )


@article.route('/create', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    return render_template(
        'articles/create.html',
        form=form,
    )


@article.route('/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    errors = []
    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data.strip())

        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.get_article', article_id=_article.id))

    return render_template(
        'articles/create.html',
        form=form,
        errors=errors,
    )


@article.route('/<int:article_id>', methods=['GET'])
def get_article(article_id: int):
    _article: Article = Article.query.filter_by(
        id=article_id
    ).options(
        joinedload(Article.tags)
    ).one_or_none()
    if _article is None:
        raise NotFound
    return render_template(
        'articles/article.html',
        article=_article,
    )


@article.route('/<string:tag_name>', methods=['GET'])
def get_article_by_tag_name(tag_name: str):
    _tag: Tag = Tag.query.filter_by(name=tag_name).options(joinedload(Tag.articles)).one_or_none()
    if _tag is None:
        raise NotFound
    return render_template(
        'articles/article_by_tag_name.html',
        tag=_tag,
    )
