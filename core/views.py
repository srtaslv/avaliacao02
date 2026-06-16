from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def avaliacao(request):
    if request.method == 'POST':

        nome = request.POST.get('nome')
        comentario = request.POST.get('comentario')
        nota = request.POST.get('nota')

        if (
            len(nome) >= 3 and
            len(comentario) >= 10 and
            int(nota) >= 1 and
            int(nota) <= 5
        ):
            return render(request, 'sucesso.html', {
                'nome': nome,
                'comentario': comentario,
                'nota': nota
            })

    return render(request, 'index.html')
