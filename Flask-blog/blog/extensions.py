from flask_admin import Admin
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from blog.admin.views import CustomAdminIndexView

from combojsonapi.spec import ApiSpecPlugin


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            'Tag': 'Tag API',
            'User': 'User API',
            'Author': 'Author API',
            'Article': 'Article API',
        }
    )
    return api_spec_plugin


login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
admin = Admin(
    index_view=CustomAdminIndexView(),
    name='Blog Admin Panel',
    template_mode='bootstrap4',
)
