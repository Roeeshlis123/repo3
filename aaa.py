class Sportay:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.jumps = []
        for i in range(5):
            self.jumps.append(None)
    def avg_jumps(self):
        sum=0
        for i in self.jumps:
            sum+=i
        return sum/5
    def is_older(self, sp):
        return sp.age>self.age
class Team:
    def __init__(self, group_name):
        self.group_name=group_name
        self.sport=[]
        for i in range(10):
            self.sport.append(None)
    def Max_avg(self):
        max=0
        for i in self.sport:
            if i.avg_jumps()>max:
                max=i.avg_jumps()
    def num_younger(self, sp):
        counter=0
        for i in self.sport:
            if i.is_older(sp):
                counter+=1
        return counter
    def Less_Avg(self, sp):
        avg_j=sp.avg_jumps()
        for i in self.sport:
            if i.avg_jumps()<avg_j:
                print (i.name)

def peula(tm, sp):
    avg_sp=sp.avg_jumps()
    max_tm=tm.max_avg()
    if avg_sp>max_tm:
        print ('the max is ', avg_sp)
    else:
        print('the max is ', max_tm)
    num_young=tm.num_younger(sp)
    if avg_sp>max_tm and num_young>=5:
        print ('accepted ', tm.less_Avg(sp))
    else:
        print ('didnt accept')
        print ('why???')
