from django.shortcuts import render, redirect, get_object_or_404
from .models import Tovar
from django.contrib.autn.decoratots import login_required
# Create your views here.

def guest_entity(request):
    return redirect("entity_list")


def entity_list(request):
    
    qs = Tovar.objects.select_related("nazvanie").all()

    if request.user.is_staff or request.user.is_superuser: 
        q = request.GET.get("q", "")
        if q:
            qs = qs.filter(nazvanie__icontains = q)
        
        sort = request.GET.get('sort', "nazvanie")
        qs = qs.order_by(sort)
    
    return render(request, "myapp/entity_list.html", {"items": qs})



@login_required
def entity_form(request, pk=None):
    instance = get_object_or_404(Tovar, pk=pk) if pk else None


    form = Tovar(
        request.POST or None,
        request.FILES or None,
        instance = instance
    )

    if form.is_valid():
        form.save()
        return redirect('entity_list')

    return render(request, "myapp/entity_form.html", {"form": form, "obj", instance})

@login_required
def entity_delete(request, pk=None):
    obj = get_object_or_404(Tovar, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('entity_list')

    return render(request, "myapp/entity_delete.html", {"obj", instance})
    
