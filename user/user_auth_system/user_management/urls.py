from django.urls import path
from user_management.views import (LoginUserView, LogoutUserView, RegisterUserView,
								   UpdateUserView, SendFriendRequestView,
								   AcceptFriendRequestView, RejectFriendRequestView,
								   ListFriendsRequestsView, ListFriendsView, DeleteFriendView,
                                   BlockUserView, UnblockUserView, ListBlockedUsers, GetUserID,
                                   GetUserPicture, TokenObtainPairView, enable_2fa, verify_otp, GetUserPicture,
                                   GetUserLanguage, ChangeUserLanguage, VerifyOTPLoginView, disable_2fa,
                                   check_2fa_status, UserInfoView)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signin/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
	path('update/', UpdateUserView.as_view(), name='update'),
    path('send-friend-request/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('accept-friend-request/', AcceptFriendRequestView.as_view(), name='accept_friend_request'),
    path('reject-friend-request/', RejectFriendRequestView.as_view(), name='reject_friend_request'),
    path('list-friend-requests/', ListFriendsRequestsView.as_view(), name='list_friend_requests'),
    path('list-friends/', ListFriendsView.as_view(), name='list_friends'),
    path('delete-friend/', DeleteFriendView.as_view(), name='delete_friend'),
    path('block-user/', BlockUserView.as_view(), name='block_user'),
    path('unblock-user/', UnblockUserView.as_view(), name='unblock_user'),
    path('list-blocked-users/', ListBlockedUsers.as_view(), name='list_blocked_users'),
	path('get-user-id/', GetUserID.as_view(), name='get_user_id'),
    path('get-user-picture/<str:username>/', GetUserPicture.as_view(), name='get_user_picture'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('enable-2fa/', enable_2fa, name='enable_2fa'),
    path('disable-2fa/', disable_2fa, name='disable_2fa'),
    path('check-2fa-status/', check_2fa_status, name='check_2fa_status'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('verify-otp-login/', VerifyOTPLoginView.as_view(), name='verify_otp_login'),
    path('get-language/', GetUserLanguage.as_view(), name='get_username'),
    path('change-language/', ChangeUserLanguage.as_view(), name='change_language'),
    path('user-info/', UserInfoView.as_view(), name='user_info'),
]