from time import sleep
from threading import Thread

buffer = []
bob_msg_list = []


def alice_send():
    """Alice send message every 5 seconds."""
    count = 1
    while True:
        buffer.append(f'Alice send message for the {count} time.')
        count += 1
        sleep(5)


def internet():
    """Internet check every 3 seconds."""
    while True:
        sleep(3)
        while buffer:
            bob_msg_list.append(buffer.pop())


def bob_read():
    """Bob read the message every 10 second."""
    while True:
        print('Bob read the message every 10 second:')
        if not bob_msg_list:
            print('None.')
        while bob_msg_list:
            print(bob_msg_list.pop())
        sleep(10)


if __name__ == '__main__':
    t1 = Thread(target=alice_send)
    t2 = Thread(target=internet)
    t3 = Thread(target=bob_read)
    t1.start()
    t2.start()
    t3.start()


