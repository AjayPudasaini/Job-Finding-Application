from django.shortcuts import render, redirect
from faq.models import Faqs
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


class FaqForJobseekerListView(ListView):
    queryset = Faqs.objects.filter(for_who=1).order_by('-created_on')
    template_name = 'faq/jobseeker/faq_list.html'
    context_object_name = 'faqs'
    paginate_by = 30




class FaqForJobseekerDetailView(DetailView):
    model = Faqs
    template_name = 'faq/jobseeker/faq_detail.html'
    context_object_name = 'faq'




class FaqForEmployerListView(ListView):
    queryset = Faqs.objects.filter(for_who=2).order_by('-created_on')
    template_name = 'faq/employer/faq_list.html'
    context_object_name = 'faq'
    paginate_by = 30


class FaqForEmployerDetailView(DetailView):
    model = Faqs
    template_name = 'faq/employer/faq_detail.html'
    context_object_name = 'faq'




