import math
class Standardization:

    @staticmethod
    def solve(column):
        avg=Standardization.mean(column)
        sd=Standardization.standard_deviation(column)
        new_column=[]
        for i in column:
            new_column.append((i-avg)/sd)
        return new_column
    
    @staticmethod
    def standard_deviation(column):
        avg=Standardization.mean(column)
        total=0
        for i in column:
            total=total+(i-avg)**2
        variance=total/len(column)
        ans=math.sqrt(variance)
        return ans
    
    @staticmethod
    def mean(column):
        add=sum(column)
        return add/len(column)
    

Li=[1,2,3,4,5,6,7,8,9]
he=Standardization.solve(Li)
for i in he:
    print(i)

    
