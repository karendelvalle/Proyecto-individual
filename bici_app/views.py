from django.shortcuts import render, redirect
from .models import Evento, User, Message, Comment
from django.contrib import messages
import bcrypt 

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/")       
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('register_email')
        password=request.POST.get('register_password')
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        logged_user= User.objects.create(first_name=first_name, last_name=last_name, email=email, password= pw_hash)
        request.session['id'] = logged_user.id
        print(logged_user)
        return redirect("/cicletealo")
    else:
        if "logged_user.id" not in request.session:
            return render(request, "index.html")
    return redirect("/")

def ejemplo(request):
    return render(request, "ejemplo.html")    
#def success(request):
 #      user_id=request.session['id']
  #      user= User.objects.get(id=user_id)
   #     context={
    #        'name': f'{user.first_name} {user.last_name}'
     #   }
      #  return render(request, 'success.html', context)
   # else:
    #    return redirect("/")

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/")
        email=request.POST.get('login_email')
        user = User.objects.filter(email = email)
        if len(user) == 1:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['login_password'].encode(), logged_user.password.encode()):
                request.session['id'] = logged_user.id
                return redirect("/cicletealo")
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")

def cicletealo(request):
    if 'id' in request.session:
        user=User.objects.get(id=request.session['id'])   
        eventos=Evento.objects.all()
        if user:
            context={
                'user': f'{user.first_name} {user.last_name}',
                'eventos': eventos,
                'users':user
            }
            if request.method =='POST':
                errors = Evento.objects.evento_validator(request.POST)
                if len(errors) > 0:
                    for key, value in errors.items():
                        messages.error(request,value)
                    return redirect("/cicletealo")     
                user_id=request.session['id']
                creador= User.objects.get(id=user_id)
                nombre=request.POST.get('nombre')
                print(nombre)
                encuentro=request.POST.get('encuentro')
                termino=request.POST.get('termino')
                ruta=request.POST.get('ruta')
                fecha=request.POST.get('fecha')
                hora=request.POST.get('hora')
                dificultad= request.POST.get('dificultad')
                new_evento=Evento.objects.create(nombre=nombre, creador=creador, encuentro=encuentro, termino=termino ,ruta=ruta, fecha=fecha, hora=hora, dificultad=dificultad)
                print(new_evento)
                return redirect("/cicletealo")
        return render(request, 'cicletealo.html', context)
    else:
        eventos=Evento.objects.all()
        context={
            'eventos': eventos,
        }
        return render(request, "cicletealo.html", context)

def crear_evento(request):
    if 'id' in request.session:
        user=User.objects.get(id=request.session['id']) 
        context={
            'users':user
        }
        return render(request, "crearevento.html", context)

def delete(request):
    if request.method == 'POST':
        evento_id= request.POST.get('borrar')
        evento= Evento.objects.get(id=evento_id)
        evento.delete()
        return redirect("/cicletealo")

def add_evento(request):
    if request.method == 'POST':
        evento_id=request.POST.get('evento_id')
        user_id=request.session['id']
        id_evento=Evento.objects.get(id=evento_id)
        id_user=User.objects.get(id=user_id)
        id_user.user_eventos.add(id_evento)
        return redirect("/cicletealo")
    else:
        return redirect("/cicletealo")

def remover_evento(request):
    if request.method == 'POST':
        evento_id=request.POST.get('evento_id')
        user_id=request.session['id']
        id_evento=Evento.objects.get(id=evento_id)
        id_user=User.objects.get(id=user_id)
        id_user.user_eventos.remove(id_evento)
        return redirect("/cicletealo")
    return redirect("/")

def editar_evento(request,id):
    if 'id' in request.session:
        evento=Evento.objects.get(id=id)
        user_id= request.session['id']
        user=User.objects.get(id=user_id)
        context={
            'evento':evento,
            'date': str(evento.fecha),
            'hora': str(evento.hora),
            'users':user
        }
        if request.method == 'POST':
            new_nombre=request.POST.get('editar_nombre')
            new_encuentro=request.POST.get('editar_encuentro')
            new_termino=request.POST.get('editar_termino')
            new_ruta=request.POST.get('editar_ruta')
            new_fecha=request.POST.get('editar_fecha')
            new_hora=request.POST.get('editar_hora')
            new_dificultad=request.POST.get('editar_dificultad')
            evento.nombre=new_nombre
            evento.encuentro=new_encuentro
            evento.termino=new_termino
            evento.ruta=new_ruta
            evento.fecha=new_fecha
            evento.hora=new_hora
            evento.dificultad=new_dificultad
            evento.save()
            return redirect("/cicletealo")
        return render(request, "editar.html", context)
    return redirect("/")

def user(request):
    if 'id' in request.session:
        user_id= request.session['id']
        user=User.objects.get(id=user_id)
      
        context={
            'users':user
        }
        return render(request, 'user.html', context)
    else:
            return redirect("/")

def mensajes(request, id):
    if 'id' in request.session:   
        if request.method == 'POST':
            evento = Evento.objects.get(id= id)
            mensaje= request.POST.get('mensaje')
            errors = Message.objects.mensaje_validator(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)
                return redirect("/imprimir/" + str(id))
            print(mensaje)
            user = User.objects.get(id= request.session.get('id'))
            nuevo_mensaje = Message.objects.create(message = mensaje, user = user, evento=evento)
            print(nuevo_mensaje)  
        url="/imprimir/" + str(id)
        return redirect(url)    
    return redirect("/")


def imprimir(request, id):
    if 'id' in request.session:
        user = User.objects.get(id= request.session.get('id'))  
        eventos=Evento.objects.filter(id=id)[0]
        user_eventos= eventos.users_message.all()
        print(user_eventos)
        context={
            'mensajes': user_eventos,
            'users': user,
            'evento':eventos
        }
        return render(request, 'mensajes.html', context)
    return redirect("/")

def comentar_mensaje(request, id):
    if request.method == 'POST':
        user = User.objects.get(id= request.session.get('id')) 
        mensaje_id = request.POST.get('mensaje_id')

        print(mensaje_id)
        mensaje = Message.objects.get(id= mensaje_id)
        comentario = request.POST.get('comentar_mensaje')
        nuevo_comentario= Comment.objects.create(comment = comentario, message= mensaje, user=user)
        print(mensaje)
        print(comentario , 'comentario')
        print(nuevo_comentario)
        event_id= request.POST.get("evento_id")
        url="/imprimir/" + event_id
        return redirect(url)
    return redirect("/")

def delete_mensaje(request,id):
    mensaje= Message.objects.get(id=id)
    mensaje.delete()
    print(mensaje)
    evento_id=  request.POST.get("evento_id")
    url= "/imprimir/" + str(evento_id)
    return redirect(url)