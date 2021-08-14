import connexion
import six

from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.id_members_body import IdMembersBody  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def add_group_member(id, body=None):  # noqa: E501
    """adds a group member

    Add friends group member # noqa: E501

    :param id: group id
    :type id: str
    :param body: User to add to a group (ID)
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = IdMembersBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_groups(body=None):  # noqa: E501
    """adds a group

    Add friends group # noqa: E501

    :param body: Group to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Group.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_group(id):  # noqa: E501
    """delete a group

    Delete group # noqa: E501

    :param id: group id
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_group_member(id, member_id):  # noqa: E501
    """delete member from a group

    Delete group member # noqa: E501

    :param id: group id
    :type id: str
    :param member_id: member id
    :type member_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_group(id):  # noqa: E501
    """returns user friend group info

    Get user group info  # noqa: E501

    :param id: group id
    :type id: str

    :rtype: Group
    """
    return 'do some magic!'


def get_group_members(id):  # noqa: E501
    """returns user friend group members

    Get user group members  # noqa: E501

    :param id: group id
    :type id: str

    :rtype: List[User]
    """
    return 'do some magic!'


def get_groups(name=None):  # noqa: E501
    """returns user friend groups

    Get user groups  # noqa: E501

    :param name: group name
    :type name: str

    :rtype: List[Group]
    """
    return 'do some magic!'
