from django.shortcuts import render, get_object_or_404
from .models import Work, Education, Course, Skill, Technology, Project, Comment


def index_render(request):
    works = Work.objects.all().order_by('id')
    educations = Education.objects.all().order_by('id')
    courses = Course.objects.all().order_by('id')
    skills = Skill.objects.all().order_by('-id')
    projects = Project.objects.all().order_by('-id')
    context = {
        "works": works,
        "educations": educations,
        "courses": courses,
        "skills": skills,
        "projects": projects,

    }
    return render(request, "index.html", context)


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, "project_detail.html", {'project': project})
