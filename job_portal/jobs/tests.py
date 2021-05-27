from django.test import TestCase
from account.models import User, JobseekerProfile
from django.utils import timezone
from jobs.models import JobPost, JobApply
import datetime
# from django.core.urlresolvers import reverse


class TestJobPost(TestCase):
    def create_job_post(self, job_title='Graphic Designer', location='Kathmandu', nu_of_vac=1,
                         level='Entry Level', avt='Full Time', redu='Bacholer', rexp=1, rs='Adobe Photoshop',
                         jc='Architecture/Interior Designing', jdesc='bla bla bla', jspe='bla bla bla'):

                         u = User(2)
                         u.save()
                         user=u
                         
                         return JobPost.objects.create(user=user, JobTitle=job_title, Location=location,
                                                        NumberOfVacancies=nu_of_vac, JobLevel=level, AvaliableTime=avt,
                                                        RequiredEducation=redu, RequiredExperience=rexp, RequiredSkill=rs,
                                                        JobCategory=jc, JobDescreptions=jdesc, JobSpecification=jspe,
                                                        JobExpiryDate=timezone.now()+datetime.timedelta(days=30))

    def test_create_job_post(self):
        jp = self.create_job_post()
        self.assertTrue(isinstance(jp, JobPost))
        self.assertEqual(jp.__str__(), jp.JobTitle)


    # def test_create_jop_post_list(self):
    #     jps = self.create_job_post()
    #     url = reverse("jobpost.views.jobpost")
    #     resp = self.client.get(url)

    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(jps.JobTitle, resp.JobDescreptions)




class JobApplyTest(TestCase):
    def create_job_apply(self, apply_reason='bla bla bla'):
        u = User(1)
        u.save()
        user = u

        j = JobPost(1)
        j.save()
        jobapply = j

        return JobApply.objects.create(user=user, job=jobapply, JobApplyReason=apply_reason)


    def test_createjob_apply(self):
        ja = self.create_job_apply()
        self.assertTrue(isinstance(ja, JobApply))

