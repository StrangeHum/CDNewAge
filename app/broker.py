from queue import Queue

message_queue = Queue()

def publish_message(msg: str):
    message_queue.put(msg)

def get_message():
    return message_queue.get()