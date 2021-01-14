from django.shortcuts import render
from .models import Massage, Chat


def chat(request):
    # chat_list = list(Chat.objects.all().values())
    # massage_list = list(Massage.objects.all().values())
    chat_list = Chat.objects.all().values()
    massage_list = Massage.objects.all().values()
    # user_id = Massage.objects.all().values()
    # objects_massage = Massage(user_id=user_id,
    #                           text=text,
    #                           time=time,
    #                           )
    # objects_massage.save()
    return render(request, 'chat.html', {'chat_list': chat_list, 'massage_list': massage_list})
