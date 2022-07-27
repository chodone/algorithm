import random



class Pair():
    
    def __init__(self,stuList) :
        self.stuList = stuList

    def pick(self,n):

        pick_list = random.sample(self.stuList , n)
        return pick_list
        
    def match_pair(self):
        pairList = []
        if not len(self.stuList)%2 :
            #짝수
            for i in range(int(len(self.stuList)/2)):
                pair = random.sample(self.stuList , 2)
                pairList.append(pair)
                for stu in pair:
                    self.stuList.remove(stu)
        else:
            #홀수
            for i in range(int((len(self.stuList)-3)/2)):
                pair = random.sample(self.stuList , 2)
                pairList.append(pair)
                for stu in pair:
                    self.stuList.remove(stu)
                    if len(self.stuList) == 3:
                        pairList.append(self.stuList)
                        break

        return pairList


        #random.sample 공부




stuList = ['조성욱', '김희현' , '최유경' , '이창민' , '최선호' , '백지원' , '정민지' , '조승현' ,'노준호']
student = Pair(stuList)

print(student.pick(2))
print(student.match_pair())