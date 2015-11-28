time=30

def main():
    t1_stop= threading.Event()
    t1 = threading.Thread(target=thread1, args=(1, t1_stop))

    t2_stop = threading.Event()
    t2 = threading.Thread(target=thread2,  args=(2, t2_stop))

    time.sleep(duration)
    #stop the thread2
    t2_stop.set()

def thread1(arg1, stop_event):
    while(not stop_event.is_set()):
        #similar to time.sleep()
        stop_event.wait(time)
        pass


def thread2(arg1, stop_event):
    while(not stop_event.is_set()):
        stop_event.wait(time)
        pass

main
