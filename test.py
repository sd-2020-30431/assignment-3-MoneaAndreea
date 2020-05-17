import flask
import unittest
import os
import testing.mysqld
from flask import Flask
import sqlalchemy
import app
TEST_DB = 'test.db'

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.assertEqual(app.debug, False)

    # executed after each test

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def register(self, username, password, confirm):
        return self.app.post(
            '/register',
            data=dict(username=username, password=password, confirm=confirm),
            follow_redirects=True
        )

    def login(self, username, password):
        return self.app.post(
            '/login',
            data=dict(username, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )

    def test_valid_user_registration(self):
        response = self.register(1, 'test1', '1234')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thanks for registering!', response.data)

    def test_valid_user_login(self):
        response = self.login('test1', '1234')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged in!', response.data)

    def test_valid_user_loggout(self):
        response = self.logout()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged out!', response.data)

if __name__ == "__main__":
    unittest.main()