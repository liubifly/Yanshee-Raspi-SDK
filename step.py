import motion
import time

for i in range(16):
    motion.move("fl")
    time.sleep(0.5)
    motion.move("fr")
    time.sleep(0.5)
