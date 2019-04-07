from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from api.views import *

merouter = merouters.DefaultRouter()

merouter.register(r'words', WordsViewSet)
merouter.register(r'topics', TopicsViewSet)
merouter.register(r'tweets', TweetsViewSet)
# merouter.register(r'concepts', ConceptsViewSet)
merouter.register(r'fish', FishViewSet)

urlpatterns = [
    # path(r'^api-auth', include('api.urls'))
    #path('admin/', admin.site.urls),
    #path('', include('visualiser.urls'))
]

urlpatterns += merouter.urls
