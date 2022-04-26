from yolov5 import detect
from django.shortcuts import render
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage #Add this
import os #Add this
# def Home(request):
#     return HttpResponse('<h1>Hello World</h1>')

def Home(request):
    return render(request,'index.html ')

def upload(request):
    print(request)
    print(request.POST.dict())
    upload = request.FILES['upload']
    fss = FileSystemStorage()
    file = fss.save(upload.name, upload) # เก็บในรูปแบบของชื่อ แล้วก็เนื้อหาของไฟล์ ถ้ามีไฟล์ชื่อซ้ำกันจะเปลี่ยนชื่อให้
    file = fss.url(file) # เก็บค่า urlไว้รอให้ผู้ใช้งานเรียกใช้
    filename = os.path.basename(file.replace('%20',' '))
    result=detect.run( weights ='yolov5/runs/train/weights/best.pt',
                source='media/'+filename, 
                iou_thres=0.45, 
                line_thickness=4,
                imgsz=[640,640],
                project='media/detect',
                view_img=False )
    output = 'media/detect/'+os.path.basename(file)
    context={'file':file,'output':output,'result':result} 
    return render(request, 'index.html', context)