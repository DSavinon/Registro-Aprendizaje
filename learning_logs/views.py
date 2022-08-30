from multiprocessing import context

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import TopicForm, EntryForm

from .models import Topic, Entry


# Create your views here.
def index(request):
    """Pagina de Inicio, Registro de Aprendizaje"""

    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    """Page for all the topics"""
    # database query to sort
    topics = Topic.objects.filter(owner=request.user).order_by("data_added")
    # dict to use the keys in the template to acces data
    # values are the data we need to send to the template
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id: int):
    """Muestra un topic y sus entries

    Args:
        topic_id (int): <int:topic_id>
    """
    # usamos get to retrieve topic
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.owner != request.user:
        raise Http404
    # obtenemos las entries relacionadas con el topic y las ordenamos por fecha, el (-) ordena la lista al reves
    entries = topic.entry_set.order_by("date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    """Add a New Topic"""
    if request.method != "POST":
        # si no se envia informacion, creamos forma en blanco
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_logs:topics")
    # Mostramos una forma en blanco o invalida
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Capturamos una nueva entry"""

    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        # No se captura informacion, creamos forma en blanco
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # commit false es para que aun no lo guarde en la base de datos
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Modificamos un entry existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != "POST":
        # llenamos la forma con el entry actual
        form = EntryForm(instance=entry)
    else:
        # Recibimos POST, procesamos la informacion
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("learning_logs:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)
