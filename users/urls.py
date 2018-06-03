from django.urls import path
from users.views import create_account, login_user, user_profile, log_out
from users.views import post_link

urlpatterns = [
    path('sign_up/', create_account, name='sign_up'),
    path('sign_in/', login_user, name='sign_in'),
    path('sign_out/', log_out, name='sign_out'),
    path('user_profile/', user_profile, name='user_profile'),
    path('post_link/', post_link, name='post_link'),
]
