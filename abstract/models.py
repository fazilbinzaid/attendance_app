from django.db import models

# Create your models here.


class AbstractTimeStampModel(models.Model):
	created_on = models.DateTimeField(auto_now_add=True, editable=False)
	updated_on = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		abstract = True

