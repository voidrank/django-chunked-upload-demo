from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin

from demo.views import (
    ChunkedUploadDemo, MyChunkedUploadView, MyChunkedUploadCompleteView
)


urlpatterns = patterns(
    '',
    url(r'^/?$',
        ChunkedUploadDemo.as_view(), name='chunked_upload'),
    url(r'^api/chunked_upload/?$',
        MyChunkedUploadView.as_view(), name='api_chunked_upload'),
    url(r'^api/chunked_upload_complete/?$',
        MyChunkedUploadCompleteView.as_view(),
        name='api_chunked_upload_complete'),
    url(r'^static/(.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),
    url(r'^admin/', include(admin.site.urls)),
)
