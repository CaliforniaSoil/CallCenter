class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def displayAll(self):
        print "Id:", self.id
        print "Name:", self.name
        print "Number:", self.number
        print "Time:", self.time
        print "Reason:", self.reason

class CallCenter(Call):
    def __init__(self, calls, size):
        self.calls = []
        self.queue = len(self.calls)
        return self
    def add(self, call):
        self.queue += 1
        self.calls.append(call)
        return self
    def remove(self, call):
        self.queue -= 1
        del self.calls[0]
        return self
    def info(self):
        for i in calls:
            i.display()
        return self
    def queuelength(self):
        self.queue = len(self.calls)
        return self

call1 = Call("1", "Jason", "408-930-4931", "8:30", "To object").displayAll()
call2 = Call("2", "David", "415-950-4321", "5:15", "To criticize").displayAll()
call3 = Call("3", "Riccardo", "505-493-2018", "1:35", "To protest").displayAll()
call4 = Call("4", "Jacob", "408-940-2865", "12:00", "To grumble").displayAll()