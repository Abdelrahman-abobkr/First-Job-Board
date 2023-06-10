from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .filters import *
from .decorators import *
# Create your views here.



@login_required(login_url='login')
def job_list(request, category_slug=None):
    category = None
    job = Job.objects.all()
    total = job.count()
    my_filter = jobFilter(request.GET, queryset=job)
    job = my_filter.qs
    category_list = Category.objects.annotate(total_job=Count('job'))


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        job = job.filter(category = category)

    paginator = Paginator(job, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'job_list.html'
    context = {
        'jobs':page_obj,
        'filter':my_filter,
        'total':total,
        'categories':category_list,
    }
    return render(request, template, context)



@login_required(login_url='login')
def job_detail(request, job_slug):
    job = get_object_or_404(Job, slug=job_slug)
    form  = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.job = job
            my_form.save()
            messages.info(request, 'Your Apply Was Requested')
            return redirect('/')
    template = 'job_detail.html'
    context = {
        'job':job,
        'form':form,
    }
    return render(request, template, context)



@login_required(login_url='login')
def post_a_job(request):
    form  = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            messages.info(request, 'Your Job Is Ready')
            return redirect('/')
    template = 'post_a_job.html'
    context = {
        'form':form,
    }
    return render(request, template, context)


def contact(request):
    contact = Contact.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
    return render(request, 'contact.html', {'contact':contact})