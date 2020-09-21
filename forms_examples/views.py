from django.http import HttpResponse
from django.shortcuts import render
from forms_examples.forms import (FormCharField, FormChoiceFieldSelect, FormChoiceFlexible)

# Create your views here.
def view_sample(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def form_charfield_render(request):
    if request.method == 'POST':
        form_charfield = FormCharField(request.POST)
    else:
        form_charfield = FormCharField()

    html_data={'form_charfield':form_charfield}
    return render(request, 'forms_examples/form_charfield_render.html', html_data)

def form_choicefield_select_render(request):
    if request.method == 'POST':
        form_choicefield_select = FormChoiceFieldSelect(request.POST)
    else:
        form_choicefield_select = FormChoiceFieldSelect()

    html_data={'form_choicefield_select':form_choicefield_select}
    return render(request, 'forms_examples/form_choicefield_select.html', html_data)

def form_choicefield_flexible_render(request):
    choices = [("",""),
                ("a","a"),
                ("b","b")]
    form_choice_flexible = FormChoiceFlexible(choices=choices)

    html_data={'form_choice_flexible':form_choice_flexible}
    return render(request, 'forms_examples/form_choice_flexible.html', html_data)