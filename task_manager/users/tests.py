from django.urls import resolve
from django.test import TestCase
from .views import ( home,
                     signup,
                     profile,
                    home,
                    TaskListView,
                    TaskDetailView,
                    TaskCreateView,
                    TaskDeleteView,
                    TaskUpdateView,
                    TeamCreateView,
                    TeamDeleteView,
                    TeamDetailView,
                    TeamListView,
                    TeamTaskCreateView,
                    TeamUpdateView,)

from django.contrib.auth.views import LoginView

class UrlTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_root_url_resolves_to_signup_page_view(self):
        found = resolve('/signup/')
        self.assertEqual(found.func, signup)
    def test_root_url_resolves_to_profile_page_view(self):
        found = resolve('/profile/')
        self.assertEqual(found.func, profile)
    def test_root_url_resolves_to_home2_page_view(self):
        found = resolve('/home/')
        self.assertEqual(found.func, home)







