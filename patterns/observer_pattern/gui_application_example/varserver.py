#! python3
# File to "serve" variables across disparate Python documents


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, val):
        for observer in self._observers:
            observer.update(val)


# Example usage
class Counter(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self.data = 0

    def addOne(self):
        self.data += 1
        self.notify(self.data)

    def subOne(self):
        self.data -= 1
        self.notify(self.data)

    def getData(self):
        return self.data


class Watcher:
    def __init__(self, widgetname):
        self.myname = widgetname
        self.info = 0

    def currentval(self):
        return self.info

    def update(self, val):
        self.info = val
        self.myname.set(self.info)


click_num = Counter('ClkNum')
