print("Average of my Final Marks")

myFinalMarks={'CSF': 80,'FunpRO': 82, 'WT': 85}

def calculateAverage(finalMarks):
 total=0
 average=0

 for key in finalMarks:
     total=total+finalMarks[key]
 average=total/len(finalMarks)
 return average

print(calculateAverage(myFinalMarks))