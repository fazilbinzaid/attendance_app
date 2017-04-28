from django.db import models
from accounts.models import Teacher, AuthUser, Student, Batch
from abstract.models import AbstractTimeStampModel

# Create your models here.


class Subject(models.Model):

    SUBJECTS = (('EP', 'Physics'), ('EC', 'Chemistry'), ('EM', 'Mathematics'), ('EMM', 'Mechanics'))

    code = models.CharField(max_length=3, choices=SUBJECTS)
    batch = models.ForeignKey(Batch, related_name='subjects', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, related_name='subjects', null=True, blank=True)

    class Meta:
        unique_together = ('code', 'batch', 'teacher')

    @property
    def name(self):
        return [item[1] for item in self.SUBJECTS if item[0] == self.code][0]

    def __str__(self):
        return "%s - %s" % ([item[1] for item in self.SUBJECTS if item[0] == self.code][0], self.batch)


class Hour(AbstractTimeStampModel):

    HOURS = ((1, 'Hour 1'), (2, 'Hour 2'), (3, 'Hour 3'), (4, 'Hour 4'), (5, 'Hour 5'),
             (6, 'Hour 6'), (7, 'Hour 7'), (8, 'Hour 8'), (9, 'Hour 9'), (10, 'Hour 10'))

    code = models.PositiveSmallIntegerField(choices=HOURS)
    subject = models.ForeignKey(Subject, related_name='hours', null=True, blank=True)
    is_present = models.BooleanField(default=False)
    student = models.ForeignKey(Student, related_name='hours', null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'date', 'code')

    @property
    def hours(self):
        return [item[1] for item in self.HOURS]

    @property
    def index(self):
        return [item[1] for item in self.HOURS if item[0] == self.code][0]

    def __str__(self):
        return "%s - %s - %s" % (self.student, self.student.batch, [item[1] for item in self.HOURS if item[0] == self.code][0])
