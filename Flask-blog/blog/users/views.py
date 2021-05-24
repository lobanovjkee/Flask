from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from werkzeug.exceptions import NotFound

# import blog.articles.views
from blog.models import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/')
def users_list():
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
        request=request,
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    selected_user = User.query.filter_by(id=pk).one_or_none()
    if not selected_user:
        raise NotFound(f"User #{pk} doesn't exist!")

    return render_template(
        'users/profile.html',
        user=selected_user,
    )
