from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	friends = models.ManyToManyField('Profile',blank=True)


	def __str__(self):
		return str(self.user)


class FriendRequest(models.Model):
	sender_profile = models.ForeignKey(Profile, related_name="sender_profile", on_delete=models.CASCADE)
	receiver_profile = models.ForeignKey(Profile, related_name="receiver_profile", on_delete=models.CASCADE)

	# def __str__(self):
	# 	from_user = str(self.sender_profile)
	# 	to_user = str(self.receiver_profile)
	# 	return from_user + ' to ' + to_user


	
