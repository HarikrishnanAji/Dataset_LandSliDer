import csv
f=open("Dataset.csv","a",newline="")


slope = [0	,1	,2	,6	,10	,15	,16	,18	,20	,24	,25	,30	,35	,38	,42	,45	,47	,48	,50	,52	,54	,55	,60	,65	,70]
vibration = [0.0001 ,0.0009 ,0.0012 ,0.0017	,0.0025	,0.003	,0.006	,0.01	,0.03	,0.05	,0.1	,0.25	,0.4	,0.55	,0.7	,0.85	,1	,1.2	,1.4	,1.6	,1.8]
rainfall = [0	,0	,0	,0	,6	,6	,6	,6	,10	,10	,12	,14	,20	,24	,27	,32	,37	,40	,45	,47	,50	,53	,55	,58	,60	,63	,68	,74	,78	,83	,88	,95	,98	,110	,140	,150	,160	,180,	200	,225	,250	,275	,300	,325	,350	,375	,400	,425	,450	,475	,500]
moisture = [0	,0	,0	,0	,10	,10	,10	,10	,15	,15	,16	,17	,20	,23	,25	,30	,32	,35	,37	,39	,43	,46	,48	,51	,55	,60	,65	,70	,75	,80	,85	,90	,95	,100]

# printing lists
print("The original lists are : " + str(slope) +
      " " + str(vibration) +
      " " + str(rainfall) +
      " " + str(moisture))

# using list comprehension
# to compute all possible permutations
res = [[i, j, k ,l] for i in slope
       for j in vibration
       for k in rainfall
       for l in moisture]

# printing result
print("All possible permutations are : " + str(res))
writer = csv.writer(f)
writer.writerows(res)
f.close()