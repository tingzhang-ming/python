# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.book import Book  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBookController(BaseTestCase):
    """BookController integration test stubs"""

    def test_add_book(self):
        """Test case for add_book

        Add a new book to the store
        """
        book = Book()
        response = self.client.open(
            '/book/insert',
            method='POST',
            data=json.dumps(book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_book(self):
        """Test case for delete_book

        Add a new book to the store
        """
        book = Book()
        response = self.client.open(
            '/book/delete',
            method='POST',
            data=json.dumps(book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_book_by_status(self):
        """Test case for find_book_by_status

        Finds Book by status
        """
        query_string = [('state', '')]
        response = self.client.open(
            '/book/list',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
