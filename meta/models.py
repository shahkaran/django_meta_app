from django.db import models

# Create your models here.

class url_info(models.Model):
        url=models.CharField(max_length=250)
	title=models.CharField(max_length=250)
	meta_desc=models.CharField(max_length=250)
	meta_keywords=models.CharField(max_length=250)

	def __unicode__(self):
		return self.url


