from threading import Thread
import mss


class screencap:
    def start(self):
        sct = mss.mss()
        t = Thread(target=self.hope, args=())
        t.daemon = True
        t.start()
        return self

    def hope(self):
        while True:
            self.x = np.array(sct.grab(monitor))

    def read(self):
        return self.x
