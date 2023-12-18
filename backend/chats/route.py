from django.urls import path,re_path
from .consumers import PersonalChatConsumer

websocket_urlpatterns =[
    path('ws/chat/',PersonalChatConsumer.as_asgi())
    # re_path(r"ws/chat/$", PersonalChatConsumer.as_asgi())
]