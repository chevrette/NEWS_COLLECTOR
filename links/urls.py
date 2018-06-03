from django.urls import path
from links.views import vote, comment, add_comment, reply_comment, vote_comment
from links.views import add_link

urlpatterns = [
    path('vote/<int:link_id>/?', vote, name='vote'),
    path('comments/<int:link_id>/?', comment, name='comment'),
    path('add_comment/?', add_comment, name='add_comment'),
    path('reply_comment/<int:com_id>/?', reply_comment, name='reply_comment'),
    path('vote_comment/<int:com_id>/?', vote_comment, name='vote_comment'),
    path('add_link/', add_link, name='add_link'),
]
