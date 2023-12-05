# Streaming response work

import json
import logging

from openai import OpenAI
from django.http import StreamingHttpResponse
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.renderers import BaseRenderer
from django.conf import settings

logger = logging.getLogger(__name__)

class ServerSentEventRenderer(BaseRenderer):
    media_type = "text/event-stream"
    format = "txt"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

GPT_MODEL_ENGINE = "gpt-3.5-turbo"
@api_view(['GET'])
@permission_classes([AllowAny])
@renderer_classes([ServerSentEventRenderer])
def ai_segment_generator(request):

    user_input = request.query_params.get('user_input')
    # auth_token = request.query_params.get('token')

    # max_token = request.data.get('max_token')
    data = None
    error = False

    # try:
    #     user = Token.objects.get(key=auth_token).user
    # except Token.DoesNotExist:
    #     print("Invalid token")

    #     error = True
    #     message = "Invalid token"
    def event_stream():

        # if error:
        #     data = {"error": f"{message}", 'tokens_left': 0}
        #     yield f'data: {data}\n\n'


        # else:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        for chunk in client.chat.completions.create(
                model=GPT_MODEL_ENGINE,
                messages=[{
                    "role": "user",
                    "content": f"{user_input}",
                }],
                stream=True,
        ):
            chatcompletion_delta = chunk.choices[0].delta.content or ""
            data = json.dumps(chatcompletion_delta)
            yield f'data: {data}\n\n'

    response = StreamingHttpResponse(event_stream(), content_type="text/event-stream")
    response['X-Accel-Buffering'] = 'no'
    response['Cache-Control'] = 'no-cache'
    return response