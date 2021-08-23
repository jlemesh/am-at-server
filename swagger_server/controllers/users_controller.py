import connexion
import six
from swagger_server.models import user

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util
from swagger_server.database.user import UserDataProvider


user_provider = UserDataProvider()


def add_friend(user, token_info, id_):  # noqa: E501
    """adds a friend

    Become user&#x27;s friend # noqa: E501

    :param id: user id
    :type id: str

    :rtype: None
    """
    return user_provider.add_friend(user, id_)


def add_user(body=None):  # noqa: E501
    """adds a user

    Adds user to the system # noqa: E501

    :param body: User to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501

    return user_provider.create_user(body)


def delete_friend(id, friend_id):  # noqa: E501
    """delete a user friend

    Unfriend # noqa: E501

    :param id: user id
    :type id: str
    :param friend_id: friend id
    :type friend_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_user(id_):  # noqa: E501
    """returns user info

    Get user info  # noqa: E501

    :param id: user id
    :type id: str

    :rtype: User
    """
    return user_provider.get_user(id_)


def get_user_friends(id_, name=None):  # noqa: E501
    """returns user friends

    Get user friends  # noqa: E501

    :param id: user id
    :type id: str
    :param name: friend name
    :type name: str

    :rtype: List[User]
    """
    return user_provider.get_friends(id_)


def get_users(skip=None, limit=None, name=None):  # noqa: E501
    """get all users

    Get list of users  # noqa: E501

    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int
    :param name: user name
    :type name: str

    :rtype: List[User]
    """
    return user_provider.get_users()


def update_user(id_, body=None):  # noqa: E501
    """updates user info

    Update user info  # noqa: E501

    :param id: user id
    :type id: str
    :param body: User to update
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501

    return user_provider.update_user(id_, body)
