from django.shortcuts import render, get_object_or_404
from .models import Work, Education, Course, Skill, Technology, Project, Comment
from .forms import CommentForm



def index_render(request):
    works = Work.objects.all().order_by('id')
    educations = Education.objects.all().order_by('id')
    courses = Course.objects.all().order_by('id')
    skills = Skill.objects.all().order_by('id')
    projects = Project.objects.all()
    context = {
        "works": works,
        "educations": educations,
        "courses": courses,
        "skills": skills,
        "projects": projects,

    }
    return render(request, "index.html", context)


def project_detail(request: object, id: object) -> object:
    project = get_object_or_404(Project, id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                organization=form.cleaned_data['organization'],
                body=form.cleaned_data['body'],
                post=project
            )
            comment.save()
            form.clean()
    comments = Comment.objects.filter(post=project).order_by('-id')
    context = {
        'project': project,
        'comments': comments,
        'form': form
    }
    return render(request, "project_detail.html", context)
