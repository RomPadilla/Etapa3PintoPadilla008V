from django.test import TestCase

# Create your tests here.

from User.forms import createUserForm

class UserFormTest(TestCase):

    def test_password_diferente(self):
        form_data = {'first_name': "pablo",'last_name':"pinto",'username':"pablo", 'email':"pablo@gmail.com", 'password1':"chao1234", 'password2':"chao2234"}
        form = createUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_password_corta(self):
        form_data = {'first_name': "pablo",'last_name':"pinto",'username':"pablo", 'email':"pablo@gmail.com", 'password1':"chao", 'password2':"chao"}
        form = createUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_todo_valido(self):
        form_data = {'first_name': "pablo",'last_name':"pinto",'username':"pablo", 'email':"pablo@gmail.com", 'password1':"chao1234", 'password2':"chao1234"}
        form = createUserForm(data=form_data)
        self.assertTrue(form.is_valid())
    
        
