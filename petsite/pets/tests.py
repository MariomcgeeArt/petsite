from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from pets.models import Pet, Appointment
from .forms import *


class PetsPageTest(TestCase):
    def test_pets_page(self):
        #Logging in
        user = User.objects.create_user(username='mario', password='password')
        self.client.login(username='mario', password='password')

        Pet.objects.create(pet_name='jas', species='Dog', breed='german', weight_in_pounds=10, Owner=user)

        response = self.client.get('/pets/')
        #Checking if the page loaded
        self.assertEqual(response.status_code, 200)
        get_response = self.client.get(reverse('pets'))
        #Seeing if the owner exists on the page
        self.assertContains(get_response, 'mario')

class PetsDetailPageTest(TestCase):
    def test_pets_page(self):
        #Logging in
        user = User.objects.create_user(username='mario', password='password')
        self.client.login(username='mario', password='password')

        Pet.objects.create(pet_name='jas', species='Dog', breed='german', weight_in_pounds=30, Owner=user)
        pet = Pet.objects.get(pet_name='jas')
        Appointment.objects.create(date_of_appointment='2018-2-19', duration_minutes=10, special_instructions='None', pet=pet)

        response = self.client.get('/pets/1')
        #Checking if the page loaded
        self.assertEqual(response.status_code, 200)
        #Checking the pet's details
        self.assertContains(response, 'Dog')

class PetCreationPageTest(TestCase):
    def test_submit_question_creation_form(self):
            #Logging in
            user = User.objects.create_user(username='mario', password='password')
            self.client.login(username='mario', password='password')
            #Post Request
            response = self.client.post('/pet/create/', 
                {
                    'pet_name': 'jas', 
                    'species': 'Dog',
                    'breed': 'german',
                    'weight_in_pounds': 50,
                    'Owner': user,
                })
            #Seeing if the response was successful
            self.assertEqual(response.status_code, 302)
            #Checking that the data was updated in the database
            new_pet = Pet.objects.filter(pet_name='jas')
            self.assertTrue(new_pet.exists())

class PetCreationPageTest(TestCase):
    def test_submit_question_creation_form(self):
            #Logging in
            user = User.objects.create_user(username='mario', password='password')
            self.client.login(username='mario', password='password')
            #Creating a pet
            pet = Pet.objects.create(pet_name='jas', species='Dog', breed='german', weight_in_pounds=50, Owner=user)

            #Post Request
            response = self.client.post('/appointment/create/', 
                {
                    'date_of_appointment': '2019-20-03', 
                    'duration_minutes': 20,
                    'special_instructions': 'None',
                    'pet': pet,
                })
            #Seeing if the response was successful
            self.assertEqual(response.status_code, 302)
            #Checking that the data was updated in the database
            new_appointment = Appointment.objects.filter(date_of_appointment='2019-20-03')
            self.assertTrue(new_appointment.exists())
