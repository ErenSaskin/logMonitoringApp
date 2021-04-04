from fastapi import FastAPI
import time, random, calendar, json, asyncio
import threading
from kafka import KafkaProducer
from .consumer import *

#Producer.................
def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['192.168.1.26:9092'], value_serializer = json_serializer)

file = open("log.json","r")

async def sendLogData():
    for line in file:
        try:
            producer.send("log", line)
            print("producer log sent ..")
        except:
            print("cannot connect to kafka ..")
            print("Check kafka server ..")
#.........................



app = FastAPI()



async def main():
    # log....... "{metod tipi},{istek cevaplama ms},{timestamp}"
    async def log(requestType, responseTime, timestamp):
        time.sleep(responseTime / 1000)

        data = {"methodType": requestType, "ms": responseTime, "timestamp": timestamp}

        with open("log.json", "a") as write_file:
            write_file.writelines(json.dumps(data) +"\n")
        await asyncio.gather(sendLogData())
    #-----------

    @app.on_event('startup')
    async def startup_event():
        print("Producer Connect: {} ".format(producer.bootstrap_connected()))
        print("Consumer Connect: {} ".format(consumer.bootstrap_connected()))
    

    @app.on_event('shutdown')
    async def shutdown_event():
        producer.close()
        print("producer connect closed")
        consumer.close()
        print("consumer connect closed")
        file.close()

    @app.get("/")
    async def get():
        await log("Get", random.randrange(1000,3001), calendar.timegm(time.gmtime()))
        return "Get is ok"

    @app.post("/")
    async def post():
        await log("Post", random.randrange(1000,3001), calendar.timegm(time.gmtime()))
        return "Post is ok"

    @app.put("/")
    async def put():
        await log("Put", random.randrange(1000,3001), calendar.timegm(time.gmtime()))
        return "Put is ok"

    @app.delete("/")
    async def delete():
        await log("Delete", random.randrange(1000,3001), calendar.timegm(time.gmtime()))
        return "Delete is ok"


asyncio.ensure_future(main())


#consumer
t1 = threading.Thread(target=getMessage, daemon=True)
t1.start()
#.......