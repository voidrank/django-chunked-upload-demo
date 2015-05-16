from django.contrib import admin
from .models import MyChunkedUpload
from chunked_upload.admin import ChunkedUploadAdmin

admin.site.register(MyChunkedUpload, ChunkedUploadAdmin)