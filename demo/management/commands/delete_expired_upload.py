from chunked_upload.management.commands.delete_expired_uploads import Command as BaseCommand
from demo.models import MyChunkedUpload

class Command(BaseCommand):

    model = MyChunkedUpload