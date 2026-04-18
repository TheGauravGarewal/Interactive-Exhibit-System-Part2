import serial
import subprocess
import time
import socket
import json

time.sleep(5)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

intro_video = "/home/justbuild/Downloads/intro.mp4"
main_video = "/home/justbuild/Downloads/main.mp4"

SOCKET = "/tmp/mpvsocket"

# Start mpv (ONLY ONCE)
player = subprocess.Popen([
    "mpv",
    "--fs",
    "--idle=yes",
    "--input-ipc-server=" + SOCKET,
    "--no-terminal",
    "--really-quiet",
    "--no-osd-bar",
    "--osd-level=0",
    "--no-input-default-bindings",
    "--cursor-autohide=always"
])

time.sleep(2)

mode = "intro"
triggered = False


def send_cmd(command):
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.connect(SOCKET)
    s.send((json.dumps(command) + "\n").encode())
    s.close()


def play_intro():
    global mode
    print("INTRO")
    send_cmd({"command": ["loadfile", intro_video, "replace"]})
    send_cmd({"command": ["set_property", "loop-file", "inf"]})
    mode = "intro"


def play_main():
    global mode
    print("MAIN")
    send_cmd({"command": ["loadfile", main_video, "replace"]})
    send_cmd({"command": ["set_property", "loop-file", "no"]})
    mode = "main"


# Start intro
play_intro()

while True:
    data = ser.readline().decode().strip()

    # Reset trigger when sensors are clear
    if data == "":
        triggered = False

    # Intro → Main
    if data == "BOTH" and mode == "intro" and not triggered:
        triggered = True
        play_main()

    # Main → Intro (manual stop)
    elif data == "BOTH" and mode == "main" and not triggered:
        triggered = True
        play_intro()

    # Smooth switch BEFORE main ends (no flicker)
    if mode == "main":
        try:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            s.connect(SOCKET)
            s.send((json.dumps({"command": ["get_property", "time-remaining"]}) + "\n").encode())
            response = s.recv(1024).decode()
            s.close()

            if "data" in response:
                remaining = float(response.split('"data":')[1].split(",")[0])

                if remaining < 0.5:
                    play_intro()

        except:
            pass

    time.sleep(0.2)
