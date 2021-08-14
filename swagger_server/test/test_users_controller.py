# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_add_friend(self):
        """Test case for add_friend

        adds a friend
        """
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/users/{id}/friends'.format(id='id_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_user(self):
        """Test case for add_user

        adds a user
        """
        body = User()
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_friend(self):
        """Test case for delete_friend

        delete a user friend
        """
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/users/{id}/friends/{friendId}'.format(id='id_example', friend_id='friend_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        returns user info
        """
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/users/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_friends(self):
        """Test case for get_user_friends

        returns user friends
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/users/{id}/friends'.format(id='id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users(self):
        """Test case for get_users

        get all users
        """
        query_string = [('skip', 1),
                        ('limit', 50),
                        ('name', 'name_example')]
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        updates user info
        """
        body = User()
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/users/{id}'.format(id='id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
