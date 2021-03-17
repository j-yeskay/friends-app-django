from django.urls import path
from . import views


urlpatterns = [
      path('',views.IndexView,name='index'),
      path('home/',views.HomeView,name='home'),
      path('myfriends/',views.MyFriendsView,name='myfriends'),
      path('myrequests/',views.MyRequestsView,name='myrequests'),
      path('findfriends/',views.FindFriendsView,name='findfriends'),
      path('findfriends/send_request/<int:userid>/',views.SendFriendRequestView,name="send_request"),
      path('myrequests/accept_request/<int:requestid>/',views.AcceptFriendRequestView,name="accept_request"),
      path('myfriends/unfriend/<int:friendid>/',views.UnfriendView,name="unfriend"),

]