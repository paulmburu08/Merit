from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from .forms import ProfileForm,ProjectForm,RateForm
from .models import Project,Profile,Ratings

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all().order_by('-post_date')

    return render(request,'index.html',{'projects':projects})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect(reverse('profile',args=[str(request.user.id)]))

    else:
        form = ProfileForm()

    return render(request, 'new_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    try:
        projects = Project.objects.filter(user__id = id)

    except ObjectDoesNotExist:
        raise Http404()

    profile = Profile.get_profile_by_id(id)
    return render(request, 'profile.html',{'profile':profile,'projects':projects})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
            post.user = current_user
            post.save()
        return redirect('/')

    else:
        form = ProjectForm()

    return render(request, 'new_project.html',{'form':form})

@login_required(login_url='/accounts/login/')
def project(request,id):
    try:
        project = Project.objects.get(id = id)

    except ObjectDoesNotExist:
        raise Http404()

    form = RateForm()
    design_average_rates = Ratings.get_average_design_rates(id)
    usability_average_rates = Ratings.get_average_usability_rates(id)
    content_average_rates = Ratings.get_average_content_rates(id)

    all_rates = design_average_rates + usability_average_rates + content_average_rates
    average_rates = all_rates // 3

    return render(request, 'project.html',{'project':project, 'form':form,'design_average_rates':design_average_rates,
                    'usability_average_rates':usability_average_rates,'content_average_rates':content_average_rates,'average_rates':average_rates})

@login_required(login_url='/accounts/login/')
def ratings(request,id):
    current_user = request.user
    project = Project.objects.get(id = id)
    profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = RateForm(request.POST, request.FILES)
        if form.is_valid():
            ratings = form.save(commit=False)
            ratings.project = project
            ratings.profile = profile
            ratings.user = current_user
            ratings.save()

        else:
            form = RateForm()

        return HttpResponseRedirect(reverse('project',args=[str(id)]))

class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format = None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many = True)
        return Response(serializers.data)