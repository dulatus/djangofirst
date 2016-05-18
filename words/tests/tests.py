#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase


class ApiTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """

        url = 'words/en/9'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data[0], {
            "id": 9,
            "title": "black",
            "language": "en",
            "description": "Color , black",
            "translations": [
                {
                    "id": 8,
                    "title": "черный",
                    "language": "ru"
                }
            ],
            "synonyms": [],
            "antonyms": []})