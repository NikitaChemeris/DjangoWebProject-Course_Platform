from django.urls import path, include
from api.models import CategoryResource, CourseResource
from tastypie.api import Api

# api/v1/courses
# api/v1/categories

# For POST, DELETE add header
# Key: Authorization
# Value: ApiKey Nikita:tyoreirutv4124240581

api = Api(api_name='v1')
api.register(CourseResource())
api.register(CategoryResource())

urlpatterns = [
    path('', include(api.urls), name='index')
]
