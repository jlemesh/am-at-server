# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, email: str=None, photo_url: str=None, status: str=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param photo_url: The photo_url of this User.  # noqa: E501
        :type photo_url: str
        :param status: The status of this User.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'email': str,
            'photo_url': str,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'email': 'email',
            'photo_url': 'photo_url',
            'status': 'status'
        }
        self._id = id
        self._name = name
        self._email = email
        self._photo_url = photo_url
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this User.


        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this User.


        :param name: The name of this User.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def photo_url(self) -> str:
        """Gets the photo_url of this User.


        :return: The photo_url of this User.
        :rtype: str
        """
        return self._photo_url

    @photo_url.setter
    def photo_url(self, photo_url: str):
        """Sets the photo_url of this User.


        :param photo_url: The photo_url of this User.
        :type photo_url: str
        """

        self._photo_url = photo_url

    @property
    def status(self) -> str:
        """Gets the status of this User.


        :return: The status of this User.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this User.


        :param status: The status of this User.
        :type status: str
        """

        self._status = status
