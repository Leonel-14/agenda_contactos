from apps.agenda.models import Contacto
from django.views.generic import TemplateView,UpdateView
from .forms import ContactoForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class DatosView(TemplateView):
    template_name = "html/index.html"
    model = Contacto
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datos'] = Contacto.objects.all()
        context['form'] = ContactoForm
        return context
    
    def post(self,request):
        
        if request.method == 'POST':
            registro = ContactoForm(request.POST)
            if registro.is_valid():
                registro.save()
                messages.success(request,message="Registrado con exito")
                return redirect('inicio')
            else:
                return redirect('inicio')
        else:
            return redirect('inicio')
     
class EditarView(UpdateView):
    template_name = "html/nuevo.html"
    model = Contacto
    fields = ["nombre","email","numero"]
    success_url = reverse_lazy('inicio')
    

def eliminar(request,pk):
        registro = Contacto.objects.get(id = pk)
        registro.delete()
        messages.success(request,"Eliminado con exito")
        return redirect('/')
        

        

    


