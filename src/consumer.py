import json
from kafka import KafkaConsumer
from .log import Log

consumer = KafkaConsumer("log", bootstrap_servers=['192.168.1.26:9092'], auto_offset_reset='latest')

def getMessage():
    print("starting consumer")
    for msg in consumer:

        string_value = json.loads(msg.value)
        json_value = json.loads(string_value)
        
        print("the consumer is processing the message ..")

        methodType = json_value["methodType"]
        ms = json_value["ms"]
        timestamp = json_value["timestamp"]

        print("methodType: {}, ms: {}, timestamp: {} ...".format(methodType,ms,timestamp))


        new_log = Log(methodType,ms,timestamp)
        new_log.saveToDatabase()
        


