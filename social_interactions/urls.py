from django.urls import path
from .views import (UserSearchView,SendFriendRequestView,HandleFriendRequestView,
                    ListFriendsView,ListPendingRequestsView)

urlpatterns = [
    
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-requests/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('friend-request/action/', HandleFriendRequestView.as_view(), name='handle-friend-request'),
    path('friends/', ListFriendsView.as_view(), name='list-friends'),
    path('friend-requests/pending/', ListPendingRequestsView.as_view(), name='list-pending-requests'),
    
]
