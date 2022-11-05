from django.contrib import admin
from .models import Work, Education, Course, Skill, Technology, Project, Comment


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['organization', 'slug', 'profession', 'date']
    prepopulated_fields = {'slug': ('organization',)}


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['university', 'slug', 'description', 'date']
    prepopulated_fields = {'slug': ('university',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['organization', 'date', 'title']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill', 'slug', 'percent']
    prepopulated_fields = {'slug': ('skill',)}


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['technology', 'slug']
    prepopulated_fields = {'slug': ('technology',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_on']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'organization', 'created_on', 'post']
    list_filter = ['author', 'post', 'created_on']

