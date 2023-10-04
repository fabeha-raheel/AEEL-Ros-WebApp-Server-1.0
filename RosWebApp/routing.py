from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/tb3', consumers.TB3Consumer.as_asgi()),
]