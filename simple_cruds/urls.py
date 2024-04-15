from django.urls import path, include

urlpatterns = [
    path('', include('simple_cruds.student.urls')),
    # path('', include(('simple_cruds.student.urls', 'student'), namespace='student')),
]
