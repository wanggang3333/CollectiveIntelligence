#coding:utf-8
import optimization
import dorm
import socialnetwork

#s=[1,4,3,2,6,3,2,5,2,1,5,3]
#optimization.printschedule(s)
#print optimization.schedulecost(s)

# optimization ≤‚ ‘
#domain = [(0,9)] * (len(optimization.people)*2)
#s = optimization.randomoptimize(domain,optimization.schedulecost)
#s = optimization.hillclimb(domain,optimization.schedulecost)
#s = optimization.annealingoptimize(domain,optimization.schedulecost)
#s = optimization.geneticoptimize(domain,optimization.schedulecost)
#print optimization.schedulecost(s)
#optimization.printschedule(s)

#dorm ≤‚ ‘
#t = optimization.geneticoptimize(dorm.domain, dorm.dormcost)
#dorm.printsolution(t)

#socialnetwork ≤‚ ‘
sol = optimization.geneticoptimize(socialnetwork.domain, socialnetwork.crosscount)
print socialnetwork.crosscount(sol)
socialnetwork.drawnetwork(sol)