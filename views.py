from forms import ContatoForm
from django.contrib import messages
from django.shortcuts import render

def contato(request):
    form = ContatoForm(request.POST)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print('Nome:', nome)
            print('Email:', email)
            print('assunto:', assunto)
            print('mensagem:', mensagem)

            messages.success(request, 'Contato enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o contato!')
    context = {'form': form}
    return render(request, 'contato.html', context)