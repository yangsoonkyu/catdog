from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal
from .form import AnimalForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'blog/home.html', {})


def cat_list(request):
    cat = Animal.objects.filter(type__type="고양이", animal_move=False)
    return render(request, 'blog/animal_list.html', {'cat_list': cat})


def dog_list(request):
    dog = Animal.objects.filter(type__type="강아지", animal_move=False)
    return render(request, 'blog/animal_list.html', {'dog_list': dog})


def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'blog/animal_detail.html', {'animal':animal})


@login_required
def animal_new(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.author = request.user
            animal.save()
            return redirect('blog:animal_detail', pk=animal.pk)
    else:
        form = AnimalForm()
    return render(request, 'blog/animal_edit.html', {'form': form})


@login_required
def animal_edit(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.author = request.user
            animal.save()
            return redirect('blog:animal_detail', pk=animal.pk)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'blog/animal_edit.html', {'form': form})


@login_required
def animal_animove(request, pk): #퍼블리쉬
    animal = get_object_or_404(Animal, pk=pk)
    animal.animove()
    return redirect('blog:draft_list')


@login_required
def animal_remove(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    animal.delete()
    return redirect('blog:draft_list')


@login_required
def draft_list(request):
    animals = Animal.objects.filter(animal_move=True)
    return render(request, 'blog/draft_list.html', {'animals':animals})


