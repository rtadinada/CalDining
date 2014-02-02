from django.db import models
from django.contrib.auth.models import User

class Entree(models.Model):
	name = models.CharField(max_length=100)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class MenuItem(models.Model):
	entree = models.ForeignKey(Entree)
	hall = models.CharField(max_length=20)
	meal = models.CharField(max_length=20)

	def __unicode__(self):
		return "{0} at {1}".format(self.entree.name, self.hall)

class UserInfo(models.Model):
	user = models.ForeignKey(User, unique=True)
	favorites = models.ManyToManyField(Entree, related_name='favorites')
	upvotes = models.ManyToManyField(Entree, related_name='upvotes')
	downvotes = models.ManyToManyField(Entree, related_name='downvotes')