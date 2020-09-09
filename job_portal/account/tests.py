from django.test import TestCase
from account.models import User, JobseekerProfile
from django.utils import timezone
# from django.core.urlresolvers import reverse

class UserTest(TestCase):
    ''' Testing user registeration their account '''
    def create_user_jobseeker(self, username='ajay', password='1530ajay',
                     email="ajay@gmail.com", is_employer=False, is_jobseeker=True, is_superuser=False):

                     return User.objects.create(username=username, password=password, is_employer=is_employer,
                     is_jobseeker=is_jobseeker, email=email, date_joined=timezone.now())

    def create_user_employer(self, username='ajay123', password='1530ajay',
                     email="ajay@gmail.com", is_employer=True, is_jobseeker=False, is_superuser=False):

                     return User.objects.create(username=username, password=password, is_employer=is_employer,
                     is_jobseeker=is_jobseeker, email=email, date_joined=timezone.now())


    def test_user_jobseeker_creation(self):
        u = self.create_user_jobseeker()
        self.assertTrue(isinstance(u,User))
        self.assertEqual(u.__str__(), u.username)

    
    def test_user_employer_creation(self):
        u = self.create_user_employer()
        self.assertTrue(isinstance(u,User))
        self.assertEqual(u.__str__(), u.username)


class UserProfile(TestCase):
    def create_jobseeker_profile(self, FirstName='ajay', LastName='pudasaini', 
                                    Gender='Male', JobCategory='Architecture/Interior Designing', AboutM='bla bla bla', *args, **kwargs):
                                    u = User(1)
                                    u.save()
                                    user = u
                                    return JobseekerProfile.objects.create(user=user, FirstName=FirstName, LastName=LastName,
                                                                            Gender=Gender, JobCategory=JobCategory)

    # def test_create_jobseeker_profile(self):
    #     js = JobseekerProfile()

    #     # attribute
    #     u = User(1)
    #     u.save()
    #     js.user = u
    #     js.FirstName='ajay'
    #     js.LastName='pudasaini'
    #     js.Gender='Male'
    #     js.JobCategory='Architecture/Interior Designing'
    #     js.AboutMe='bla bla bla'


    #     js.save()

    #     jsp = JobseekerProfile.objects.all()
    #     self.assertTrue(jsp)






    def test_jobseeker_profile(self):
        j = self.create_jobseeker_profile()
        self.assertTrue(isinstance(j, JobseekerProfile))
        # self.assertEqual(j.__str__(), j.FirstName)










    # def test_whatever_list_view(self):
    #     w = self.create_whatever()
    #     url = reverse("whatever.views.whatever")
    #     resp = self.client.get(url)

    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(w.title, resp.content)