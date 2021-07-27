from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash

from blog.forms.login import UserLoginForm
from blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserLoginForm(request.form)
    errors = []
    _user = User.query.filter_by(email=form.email.data).first()
    if request.method == 'POST' and form.validate_on_submit():
        if not User.query.filter_by(email=form.email.data).count() or not (
                check_password_hash(_user.password, form.password.data)):
            form.email.errors.append('Check your login details')
            form.password.errors.append('Check your login details')
            return render_template('auth/login.html', form=form)

        login_user(_user)
        return redirect(url_for('user.profile', pk=_user.id))

    return render_template(
        'auth/login.html',
        form=form,
        errors=errors,
    )


#
# @auth.route('/login', methods=('POST',))
# def login_post():
#     email = request.form.get('email')
#     password = request.form.get('password')
#
#     user = User.query.filter_by(email=email).first()
#
#     if not user or not check_password_hash(user.password, password):
#         flash('Check your login details')
#         return redirect(url_for('.login'))
#
#     login_user(user)
#     return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
