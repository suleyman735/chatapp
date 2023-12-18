from __future__ import print_function
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio


class PersonalChatConsumer(AsyncWebsocketConsumer):
    print('444')
    async def connect(self):
        request_user = self.scope['user']
        if request_user.is_authenticated():
            chat_with_user  = self.scope['url_route']['kwargs']['id']
            user_ids = [int(request_user.id),int(chat_with_user)]
            user_ids = sorted(user_ids)
            self.room_group_name = f"chat_{user_ids[0]}-{user_ids}"
            await self.chanel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            print("Testing connection and redis")
            await self.accept()
        
            await super().connect()
    async def receive(self,text_data=None,bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"chate_message",
                "message":message
            }
        )
        
    async def disconnect(self, code):
        self.channel_layer.group.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print('siddd')
        # pass
    async def chat_message(self,event):
        message = event['message']
        await self.send(text_data=json.dumps({
            "message":message
        }))
    
    
# class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        
        print("Testing connection and redis")
        await self.accept()

        # Start a periodic ping
        self.ping_interval = 10  # Set the interval in seconds
        self.ping_task = asyncio.create_task(self.send_ping())

    async def disconnect(self, close_code):
        # Cancel the periodic ping task
        if hasattr(self, 'ping_task'):
            self.ping_task.cancel()

    async def send_ping(self):
        while True:
            await asyncio.sleep(self.ping_interval)
            try:
                await self.send(text_data=json.dumps({'type': 'ping'}))
            except WebSocketError:
                # Handle if the connection is closed
                break

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))