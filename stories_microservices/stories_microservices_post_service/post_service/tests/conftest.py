import pytest
from ..app import app as flask_app


# @pytest.fixture
# def app(mocker):
#     flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://///Users/idrissabanli/TAGroups/AllianceGroup/stories_microservices/stories_microservices_post_service/post_service/test.db"
#     # mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)
#     # mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)
#     # mocker.patch("app.app.database.get_all", return_value={})
#     return flask_app


@pytest.fixture
def client():
    # request = flask_app.test_client()
    # request.get('')
    return flask_app.test_client()


