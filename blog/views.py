from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.template import loader
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView

from .models import Post, Notice, Submission
from .func import run_file
from .forms import FileForm
# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
# List View
class PostLV(ListView):
    model = Post
    template_name = 'post_all.html'
    context_object_name = 'posts'
    paginate_by = 10
# Detail View
class PostDV(DetailView):
    model = Post
    slug_url_kwarg = 'slug'
    template_name = 'post_detail.html'
    context_object_name = 'post'
    # slug_url_kwarg = 'slug'
    # pk_url_kwarg = 'id'
    # query_pk_and_slug = True
    def get_object(self, *args, **kwargs):
        # Call the superclass
        object = super(PostDV, self).get_object()
        # Return the object
        return object

    def get(self, request, *args, **kwargs):
        object = super(PostDV, self).get(request, *args, **kwargs)
        return object

class NoticeLV(ListView):
    model = Notice
    template_name = 'notice.html'
    context_object_name = 'notices'
    paginate_by = 10

class NoticeDV(DetailView):
    model = Notice
    slug_url_kwarg = 'slug'
    template_name = 'notice_detail.html'
    context_object_name = 'notice'
    slug_field = 'url'
    # slug_url_kwarg = 'slug'
    # pk_url_kwarg = 'id'
    # query_pk_and_slug = True
    def get_object(self, *args, **kwargs):
        # Call the superclass
        object = super(NoticeDV, self).get_object()
        # Return the object
        return object

    def get(self, request, *args, **kwargs):
        object = super(NoticeDV, self).get(request, *args, **kwargs)
        return object
@login_required
def new(request):
	return render(request, 'new.html')
@login_required
def create(request):
	post = Post()
	post.writer = request.user
	post.title = request.GET['title']
	post.content = request.GET['content']
	post.create_date = timezone.datetime.now()
	post.save()
	return redirect('home')

@login_required
def new_submission(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            newfile = Submission(submission_file = request.FILES['file'])
            newfile.save()
            submission_number = Submission.objects.last().id + 1
            run_file(request.FILES['submission_file'])
            template = loader.get_template('submit.html')
            context = {
                'submission_number':submission_number,
            }
            return HttpResponse(template, context)
    else:
        return HttpResponseRedirect(reverse('competition'))
class CompetitionLV(ListView):
    model = Submission
    template_name = 'competition.html'
    context_object_name = 'submission'
    paginate_by = 10