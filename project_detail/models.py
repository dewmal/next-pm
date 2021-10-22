from django.db import models
from django.utils.timezone import now


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
    pull_requests = models.CharField(max_length=500, blank=True, null=True)


class Step(models.Model):
    OPENED = 'OP'
    FINISHED = 'FI'
    SKIPPED = 'SK'
    ABORTED = 'AB'
    STEP_STATUSES = [
        (OPENED, 'Open'),
        (FINISHED, 'Finish'),
        (SKIPPED, 'Skip'),
        (ABORTED, 'Abort'),
    ]

    task = models.ForeignKey(Task, on_delete=models.RESTRICT)
    name = models.CharField(max_length=160, null=True, blank=True)
    start_time = models.DateTimeField(default=now)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=STEP_STATUSES, default=OPENED)
    comment = models.TextField(null=True, blank=True)
    commits = models.CharField(max_length=500, null=True, blank=True)
