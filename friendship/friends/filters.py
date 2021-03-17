from . models import Profile
import django_filters


class FriendsFilter(django_filters.FilterSet):
	class Meta:
		model = Profile
		fields = ['user']