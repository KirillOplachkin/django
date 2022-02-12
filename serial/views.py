from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404

def show_all(request):
    serial = models.serial.objects.all()
    return render(request, "serial_list.html", {"serial": serial})
# def get_show_detail(request):
#     try:
#         serial = get_object_or_404(models.serial, id=id)
#     try:
#         comment = models.SerialComment.object.filter(serial_id=id).order_by("created_date")
#     except models.serial.DoesNotExists:
#         print('No commemts')
#     except models.serial.DoesNotExists:
#         raise  Http404('rtyuy')
#         return  render(request, "serial_detail.html", {"serial": serial, "serial_comments": comment})
#

