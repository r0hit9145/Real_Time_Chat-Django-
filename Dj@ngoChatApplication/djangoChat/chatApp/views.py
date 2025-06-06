from django.http import JsonResponse
from django.shortcuts import render, redirect
from chatApp.models import  Room, Message
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
  return render(request, 'home.html')

# def room(request, room):
#   username = request.GET.get("username")
#   room_details = Room.objects.get(name= room)
#   return render(request, 'room.html', {'username': username,'room': room, 'room_details': room_details})

# testing...
def room(request, room):
    username = request.GET.get("username")
    # raises Http404 if no matching room
    room_details = get_object_or_404(Room, name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })



def checkview(request):
  print("Request method:", request.method)
  print("POST data:", request.POST)
  if request.method == 'POST':
    room_name1 = request.POST.get('room_name1')
    username = request.POST.get('username')

    # if not room_name1:
    #   return JsonResponse({'error': 'Missing room_name1'}, status=400)
    # if not username:
    #     return JsonResponse({'error': 'Missing username'}, status=400)

        # Rest of your room creation logic
        
  # if user already existed.
    if Room.objects.filter(name= room_name1).exists():
      # print("already exist")
      
      # return HttpResponse(("User already existed, please try new one."))
      return redirect('/'+room_name1+'/?username='+username)
    else:
      new_room = Room.objects.create(name=room_name1)
      new_room.save()
      # return HttpResponse("this is post request accept.")
      return redirect('/'+room_name1+'/?username='+username)
      # return HttpResponse("New user created successfully")
  else:
    return HttpResponse("This is only accept POST request: ", status = 405)
  
def send(request):
  message = request.POST['message']
  username = request.POST['username']
  room_id = request.POST['room_id']

  new_message = Message.objects.create(value=message, user= username, room= room_id)
  new_message.save()
  return HttpResponse("Message send successfully")


 # def getMessages(request, room):
#   room_details = Room.objects.get(name= room)

#   messages = Message.objects.filter(room= room_details.id)
#   return JsonResponse({"messages": list(messages.values())})

def getMessages(request, room):
    try:
        room_obj = Room.objects.get(name=room)
    except Room.DoesNotExist:
        return JsonResponse({"messages": []})
    messages = Message.objects.filter(room=room_obj.id)
    return JsonResponse({"messages": list(messages.values())})

