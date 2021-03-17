from django.shortcuts import render, redirect
from . models import FriendRequest, Profile
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages




def IndexView(request):
	return render(request,'index.html')


def HomeView(request):
	return render(request,'home.html')


def MyFriendsView(request):
	current_profile = Profile.objects.get(user=request.user)
	my_friends = current_profile.friends.all()
	return render(request,'myfriends.html',{'my_friends':my_friends})


def MyRequestsView(request):
	current_profile = Profile.objects.get(user=request.user)
	my_requests = FriendRequest.objects.filter(receiver_profile=current_profile)
	return render(request,'myrequests.html',{'my_requests':my_requests})


def FindFriendsView(request):
	current_profile = Profile.objects.get(user=request.user)
	all_except_current = Profile.objects.exclude(user=current_profile.user)
	currents_friends = current_profile.friends.all()
	find_friends = all_except_current.difference(currents_friends)
	
	if 'q' in request.GET:
		q = request.GET['q']
		all_except_current = all_except_current.filter(user__username__istartswith=q)
		find_friends = all_except_current.difference(currents_friends)
		
	return render(request,'findfriends.html',{'find_friends':find_friends})
	




def SendFriendRequestView(request,userid):
	current_profile = request.user
	sender_profile = Profile.objects.get(user=current_profile)
	receiver_profile = Profile.objects.get(id=userid)
	friend_request, created = FriendRequest.objects.get_or_create(sender_profile=sender_profile, receiver_profile=receiver_profile)

	if created:
		messages.info(request,"Friend Request Sent!")
		return redirect('/findfriends')

	else:
		messages.error(request,"Friend Request ALREADY Sent!")
		return redirect('/findfriends')

def AcceptFriendRequestView(request, requestid):
	friend_request = FriendRequest.objects.get(id=requestid)

	friend_request.receiver_profile.friends.add(friend_request.sender_profile)
	friend_request.sender_profile.friends.add(friend_request.receiver_profile)

	friend_request.delete()
	messages.info(request,"Friend Request Accepted!")
	return redirect('/myrequests')


def UnfriendView(request,friendid):
	current_profile = Profile.objects.get(user=request.user)
	friend_profile = Profile.objects.get(id=friendid)
	current_profile.friends.remove(friend_profile)
	friend_profile.friends.remove(current_profile)
	messages.info(request,"Friend Removed!")
	return redirect('/myfriends')


	





