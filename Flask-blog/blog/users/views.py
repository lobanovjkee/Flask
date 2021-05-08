from flask import Blueprint, render_template, request

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = [
    {'id': 1, 'name': 'Victor'},
    {'id': 2, 'name': 'Anna'},
    {'id': 3, 'name': 'Ivan'},
    {'id': 4, 'name': 'Irina'},
]


@user.route('/')
def users_list():
    return render_template(
        'users/list.html',
        users=USERS,
        request=request,
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    user_info = USERS[pk-1]
    return render_template('users/user.html', user=user_info)
