from django.db import models
from django.urls import reverse


class Work(models.Model):
    organization = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    profession = models.CharField(max_length=50, db_index=True)
    date = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        ordering = ('organization',)
        verbose_name = 'Организация'
        verbose_name_plural = 'Опыт работы'

    def __str__(self):
        return self.organization


class Education(models.Model):
    university = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    date = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        ordering = ('university',)
        verbose_name = 'Университет'
        verbose_name_plural = 'Образование'

    def __str__(self):
        return self.university


class Course(models.Model):
    organization = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    date = models.CharField(max_length=30)
    description = models.TextField()
    certificate = models.ImageField(blank=True)

    class Meta:
        ordering = ('organization',)
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.organization


class Skill(models.Model):
    skill = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=30, unique=True)
    icon = models.ImageField(blank=True)
    percent = models.IntegerField()

    class Meta:
        ordering = ('skill',)
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.skill


class Technology(models.Model):
    technology = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        ordering = ('technology',)
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'

    def __str__(self):
        return self.technology


class Project(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True, unique=True)
    body = models.TextField()
    image = models.ImageField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    technology = models.ManyToManyField(Technology, related_name='projects')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Project', on_delete=models.CASCADE)

    class Meta:
        ordering = ('post',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('main:project_detail', args=[self.id])
