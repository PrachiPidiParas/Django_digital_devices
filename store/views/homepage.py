from django.shortcuts import render
from django.views import View
from store.models.front import Front

# Create your views here.
#homepage
# def front(request):
#     return render(request,'front.html')

class Front_view(View):
    def get(self,request):
        img = Front.get_all_gallery_img()
        print(img)
        return render(request,'front.html',{'images':img})

    
