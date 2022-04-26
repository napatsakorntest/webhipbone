from django.urls import path
from .views import Home
from testproject import settings #add this
from django.conf import settings #add this
from django.conf.urls.static import static #add this
from myapp import views #add this



urlpatterns = [
    path('', Home),
    path("upload", views.upload, name="upload")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # เป็นการเพิ่มเส้นทางไปยัง MEDIA_URL แล้วเมื่อผู้ใช้ส่งคำขอGETไปยัง MEDIA_URL 
# ไฟล์จะไปปรากฏใน MEDIA_ROOT ที่เราได้ตั้งค่าไว้