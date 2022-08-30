from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registramos usuario Nuevo"""

    if request.method != "POST":
        # Mostramos forma de registro en blanco
        form = UserCreationForm()
    else:
        # procesamos la informacion en la forma
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # log in del usuario y mandamos a inicio
            login(request, new_user)
            return redirect("learning_logs:index")

    # Mostramos forma en blanco o invalida
    context = {"form": form}
    return render(request, "registration/register.html", context)
