#sort jobs by earliest finish time
def sort_jobs_ft(intervals):
    pass

# check compatibility if a job
def isCompatible(job,intervals):
    ans = True
    if(len(intervals)== 0):
        ans = True
    else:
        for i in intervals:
            if(i[1]>= job[1] and i[0]<=job[1]):
                ans = False
            elif(job[0]>=i[0] and job[1]<=i[1]):
                ans = False
            elif(job[0]<i[1] and job[1]>=i[1]):
                ans = False
            elif(job[0]<=i[0] and jpb[1]>=i[1]):
                ans = False
    return ans

#schedule the intervals
def schedule(intervals):
    A = []
    for i in intervals:
        #print(isCompatible(i,A))
        if isCompatible(i,A):
            A.append(i)
    return A

jobs = [(10,20),(12,25),(20,30),(15,45)]

ans = schedule(jobs)

print(ans)