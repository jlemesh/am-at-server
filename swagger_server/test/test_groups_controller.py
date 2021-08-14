# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.group import Group  # noqa: E501
from swagger_server.models.id_members_body import IdMembersBody  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGroupsController(BaseTestCase):
    """GroupsController integration test stubs"""

    def test_add_group_member(self):
        """Test case for add_group_member

        adds a group member
        """
        body = IdMembersBody()
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/groups/{id}/members'.format(id='id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_groups(self):
        """Test case for add_groups

        adds a group
        """
        body = Group()
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/groups',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_group(self):
        """Test case for delete_group

        delete a group
        """
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/groups/{id}'.format(id='id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_group_member(self):
        """Test case for delete_group_member

        delete member from a group
        """
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/groups/{id}/members/{memberId}'.format(id='id_example', member_id='member_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_group(self):
        """Test case for get_group

        returns user friend group info
        """
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/groups/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_group_members(self):
        """Test case for get_group_members

        returns user friend group members
        """
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/groups/{id}/members'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_groups(self):
        """Test case for get_groups

        returns user friend groups
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/jlemesh/am-at/1.0.0/groups',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
