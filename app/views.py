from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def area_do_usuario(request):
    return render(request, "area_do_usuario.html")

def configuracoes(request):
    return render(request, "configuracoes.html")

def meus_materiais(request):
    return render(request, "meus_materiais.html")

def sobre_nos(request):
    return render(request, "sobre_nos.html")