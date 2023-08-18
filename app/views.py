from django.shortcuts import render
from .models import User

# passar o parametro 'request', que permite acessar os dados que estao dentro da pagina.
def home(request):
    # render retorna um pagina, o request informa os dados para a pagina, depois se passa uma pagina HTML para exibir os dados
    return render(request, 'users/home.html')

def users(request):
    new_user = User()
    new_user.name = request.POST.get('name')
    new_user.age = request.POST.get('age')
    new_user.save()
    # exibir todos os usuarios
    users = {'users': User.objects.all()}

    # retorna os dados para a pagina de listagem de usuarios
    return render(request, 'users/users.html', users)
