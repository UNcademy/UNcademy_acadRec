from fastapi import FastAPI
from routes.academicRecord import academicRecord
from routes.academicRecord import create_record_MQ
import pika
import asyncio
from aio_pika import connect_robust
import json
import os

app = FastAPI()

app.include_router(academicRecord)

async def consume(loop):
#  connection = await connect_robust(host='localhost',port=5672, loop=loop)
  connection = await connect_robust(host=os.environ['MQ_URL'],port=5672, loop=loop)
  channel = await connection.channel()

  queue = await channel.declare_queue('shistory_history_q')

  def inc(message: dict):
    print(" [x] Received %r" % message)

  async def callback(message):
    await create_record_MQ('from post event')
    await message.ack()
    body = message.body
    if body:
      inc(json.loads(body))

  await queue.consume(callback, no_ack=False)
  print(' [*] Waiting for messages. To exit press CTRL+C')
  return connection

@app.on_event('startup')
async def startup():
  loop = asyncio.get_event_loop()
  task = loop.create_task(consume(loop))
  await task

