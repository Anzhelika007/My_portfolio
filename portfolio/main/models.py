from django.db import models


class Work(models.Model):
    organization = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    profession = models.CharField(max_length=50, db_index=True)
    date_start = models.DateField(auto_now=True)
    date_end = models.DateField(auto_now=True)
    description = models.TextField()

    class Meta:
        ordering = ('date_start',)
        verbose_name = 'Организация'
        verbose_name_plural = 'Опыт работы'

    def __str__(self):
        return self.organization


class Education(models.Model):
    university = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    date_start = models.DateField(auto_now=True)
    date_end = models.DateField(auto_now=True)
    description = models.TextField()

    class Meta:
        ordering = ('date_start',)
        verbose_name = 'Университет'
        verbose_name_plural = 'Образование'

    def __str__(self):
        return self.university


class Course(models.Model):
    organization = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    date = models.DateField(auto_now=True)
    certificate = models.ImageField(blank=True)

    class Meta:
        ordering = ('date',)
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


class Projects(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    image = models.ImageField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Projects', related_name='posts')

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
