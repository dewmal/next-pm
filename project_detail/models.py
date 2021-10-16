from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=160)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField()
    start_date = models.DateTimeField()
    expected_end_date = models.DateTimeField(null=True, blank=True)
    git_link = models.URLField(null=True, blank=True)
    drive_folder_id = models.CharField(max_length=255, null=True, blank=True)


class Task(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField()
    start_date = models.DateTimeField()
    expected_hours = models.FloatField()
    actual_hours = models.FloatField(default=0)
    project = models.ForeignKey(Project, on_delete=models.RESTRICT)
    tags = models.ManyToManyField(Tag)
