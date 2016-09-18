from django.shortcuts import render

from django.shortcuts import render
from .models import Treasure

def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures':treasures})


# class Treasure:
#     def __init__(self,name,value,material,location):
#         self.name=name
#         self.value=value
#         self.material=material
#         self.location=location
#
# treasures=[
#     Treasure('gold',500,'metal','here'),
#     Treasure('silver',0,'metal','there'),
#     Treasure('coal',50,'fuel','left')
# ]