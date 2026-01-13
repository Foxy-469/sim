from random import randint as ri 

def initializing_state():
    global c_state       #cashier state
    global c_id          #customer id
    global t             #Assumes virtual time is in minutes 
    global c_time        #customer arrive time
    global s_time        #service time
    global i_time        #idle time

    c_state = 0
    c_id = 0
    t= 0
    c_time = 0
    s_time = 0
    i_time = 0

def toggle_cashier_state():
    global c_state
    if q.length() > 0:
        c_state = 1
    else:
        c_state = 0
def customer_arrival_time():
    global c_time
    ti = ri(1,3)
    c_time = t + ti
    
def service_time():
    global s_time
    ti = ri(2, 4)
    s_time = t + ti


class Queue:
    #First in first out
    def __init__(self):
        self.customer ={}
        self.line = []
        self.w_time = []
        pass
        
    def length(self):
        return len(self.line)
    
    def add_to_queue(self, id, st, ct):
        self.line.append(id)
        self.w_time.append(st - ct)

    def remove_from_queue(self):
        self.customer[self.line[0]] = self.w_time[0]
        self.line.pop(0)
        self.w_time.pop(0)

    def print_cus(self):
        print("Customer List: ", self.customer)


def update_idle_time():                 
    global i_time
    global c_state
    if c_state == 0: 
        i_time +=1                      

def simulate():
    global t
    global c_id
    global c_time
    global c_state
    global s_time
    customer_arrival_time()
    service_time()
    while t< 61:
        #check customer arrival
        if t == c_time:
            c_id +=1
            stime = t if c_state == 0 else s_time
            q.add_to_queue(c_id, stime, t)
            customer_arrival_time()

        #start service if cashier is idle and queue is empty
        if c_state == 0 and q.length() > 0:
            service_time()
            c_state = 1

        if  t == s_time  and q.length() > 0  :
            q.remove_from_queue()
            
            if q.length() ==0:
                c_state = 0
            else: 
                service_time()

        update_idle_time()
        t+=1


if __name__ =="__main__":
    q = Queue()
    initializing_state()
    simulate()
    q.print_cus()
    print("Idle time: ", i_time)
