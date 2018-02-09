from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders

# Thanks to Enzo Roiz https://github.com/enzoroiz who made these tests during an internship with us

class GeneralTests(TestCase):
    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds rango.jpg
        result = finders.find('images/rango.jpg')
        self.assertIsNotNone(result)


class Chapter3ViewTests(TestCase):
    def test_index_contains_hello_message(self):
        # Check if there is the message 'hello world!'
        response = self.client.get(reverse('index'))
        self.assertIn('Rango says'.lower(), response.content.decode('ascii').lower())

        # file.write('test_index_contains_hello_message\n')

    def test_about_contains_create_message(self):
        # Check if in the about page is there a message
        self.client.get(reverse('index'))
        response = self.client.get(reverse('about'))
        self.assertIn('Rango says here is the about page'.lower(), response.content.decode('ascii').lower())


class Chapter4ViewTest(TestCase):

    def test_view_has_title(self):
        response = self.client.get(reverse('index'))

        #Check title used correctly
        self.assertIn('<title>', response.content.decode('ascii'))
        self.assertIn('</title>', response.content.decode('ascii'))

    def test_index_using_template(self):
        response = self.client.get(reverse('index'))

        # Check the template used to render index page
        self.assertTemplateUsed(response, 'rango/index.html')

    def test_about_using_template(self):
        self.client.get(reverse('index'))
        response = self.client.get(reverse('about'))

        # Check the template used to render about page
        self.assertTemplateUsed(response, 'rango/about.html')

    def test_rango_picture_displayed(self):
        response = self.client.get(reverse('index'))

        # Check if is there an image in index page
        self.assertIn('img src="/static/images/rango.jpg'.lower(), response.content.decode('ascii').lower())

    # New media test
    def test_cat_picture_displayed(self):
        response = self.client.get(reverse('about'))

        # Check if is there an image in index page
        self.assertIn('img src="/media/cat.jpg'.lower(), response.content.decode('ascii').lower())

    def test_about_contain_image(self):
        self.client.get(reverse('index'))
        response = self.client.get(reverse('about'))

        # Check if is there an image in index page
        self.assertIn('img src="/static/images/', response.content.decode('ascii'))

    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds rango.jpg
        result = finders.find('images/rango.jpg')
        self.assertIsNotNone(result)