from flask import Blueprint, render_template, request

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: 'Victor',
    2: 'Anna',
    3: 'Ivan',
    4: 'Irina',
}


@user.route('/')
def users_list():
    return render_template(
        'users/list.html',
        users=USERS,
        request=request,
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    user_info = USERS[pk]
    return render_template('users/user.html', user=user_info)
