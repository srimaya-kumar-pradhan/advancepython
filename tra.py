import time

def red_light():
    print(" RED Light - STOP")
    time.sleep(2)

def yellow_light():
    print(" YELLOW Light - READY")
    time.sleep(1)


def green_light():
    print(" GREEN Light - GO")
    time.sleep(2)

def traffic_light():
    for i in range(3):   
        red_light()
        yellow_light()
        green_light()

traffic_light()