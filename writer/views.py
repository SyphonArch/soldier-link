from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

import threading

from .models import Message
from . import thecampy_sender

from .writer_enable import enable


# Create your views here.
def index(request):
    if enable:
        if request.method == "GET":
            return render(request, 'writer/index.html', {})

        req = request.POST
        subject = req['subject']
        sender = req['sender']
        content = req['content']
        message_dict = {'title': subject, 'sender': sender, 'content': content}

        # Error handling
        if len(sender) == 0:
            message_dict['error'] = "작성자를 입력해 주세요!"
        elif len(subject) == 0:
            message_dict['error'] = "제목을 입력해 주세요!"
        elif len(content) == 0:
            message_dict['error'] = "내용을 입력해 주세요!"
        elif len(content) > 1500:
            message_dict['error'] = "1500자 이하로 작성해 주세요!"
        elif len(sender) > 20:
            message_dict['error'] = '작성자는 20자 이내로 입력해 주세요!'
        elif len(subject) > 100:
            message_dict['error'] = '제목은 100자 이내로 입력해 주세요!'

        if 'error' in message_dict:
            return render(request, 'writer/index.html', message_dict)
        else:
            msg = Message.create(sender, subject, content)
            msg.save()

            send_thread = threading.Thread(target=thecampy_sender.send, args=(msg,))
            send_thread.start()

            return redirect('send-check', message_pk=msg.pk)
    else:
        template = loader.get_template('writer/unavailable.html')
        return HttpResponse(template.render())


def send_check(request, message_pk):
    msg = Message.objects.get(pk=message_pk)
    if not msg.send_attempt_over:
        template = loader.get_template('writer/loading.html')
        return HttpResponse(template.render())
    else:
        if msg.sent:
            template = loader.get_template('writer/success.html')
            return HttpResponse(template.render())
        else:
            template = loader.get_template('writer/failure.html')
            return HttpResponse(template.render())

