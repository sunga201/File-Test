from django.utils import timezone
import os
import uuid

#파일이 업로드 될 때 파일을 올린 날짜별로 폴더를 나누어 구성하기 위한 함수
def file_upload_path(instance, filename):
    ext=filename.split('.')[-1]
    d=timezone.now()
    filepath=d.strftime("%Y/%m/%d")
    suffix=d.strftime("%Y%m%d%H%M%S")
    filename="%s_%s.%s" % (uuid.uuid4().hex, suffix, ext)
    return os.path.join(filepath, filename)
