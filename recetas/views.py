from extra_views import (
    CreateWithInlinesView,
    UpdateWithInlinesView,
    InlineFormSetFactory,
)

from .models import Receta, MedicamentosReceta
from .forms import MedicamentoRecetaForm, RecetaForm


class MedicamentoRecetaInline(InlineFormSetFactory):
    model = MedicamentosReceta
    form_class = MedicamentoRecetaForm


class CreateRecetaView(CreateWithInlinesView):
    model = Receta
    inlines = [
        MedicamentoRecetaInline,
    ]
    form_class = RecetaForm
    template_name = "recetas/crear_receta.html"

    def get_success_url(self):
        return self.object.get_absolute_url()
