from django.db import models
from accounts.models import Teacher, AuthUser, Student, Batch
from abstract.models import AbstractTimeStampModel

# Create your models here.


class Subject(models.Model):

    SUBJECTS = (('EP', 'Physics'), ('EC', 'Chemistry'), ('EM', 'Mathematics'), ('EMM', 'Mechanics'))

    name = models.CharField(max_length=3, choices=SUBJECTS)
    teacher = models.ForeignKey(Teacher, related_name='subjects', null=True, blank=True)

    def __str__(self):
        return self.name


class Hour(AbstractTimeStampModel):

    HOURS = ((1, 'Hour 1'), (2, 'Hour 2'), (3, 'Hour 3'), (4, 'Hour 4'), (5, 'Hour 5'),
             (6, 'Hour 6'), (7, 'Hour 7'), (8, 'Hour 8'), (9, 'Hour 9'), (10, 'Hour 10'))

    code = models.PositiveSmallIntegerField(choices=HOURS)
    subject = models.ForeignKey(Subject, related_name='hours', null=True, blank=True)
    is_present = models.BooleanField(default=False)



class BatchTeacherMapping(models.Model):

    batch = models.ForeignKey(Batch, related_name='teachers', null=True)
    teacher = models.ForeignKey(Teacher, related_name='batches', null=True)


class BatchSubjectMapping(models.Model):

    batch = models.ForeignKey(Batch, related_name='subjects', null=True)
    subject = models.ForeignKey(Subject, related_name='batches', null=True)