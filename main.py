import csv
import numpy as np
fields = ['slope', 'vibration', 'moisture']

slope = [0	,1	,2	,6	,10	,15	,16	,18	,20	,24	,25	,30	,35	,38	,42	,45	,47	,48	,50	,52	,54	,55	,60	,65	,70]
vibration = [0.0001 ,0.0009 ,0.0012 ,0.0017	,0.0025	,0.003	,0.006	,0.01	,0.03	,0.05	,0.1	,0.25	,0.4	,0.55	,0.7	,0.85	,1	,1.2	,1.4	,1.6	,1.8]
moisture = [0	,0	,0	,0	,10	,10	,10	,10	,15	,15	,16	,17	,20	,23	,25	,30	,32	,35	,37	,39	,43	,46	,48	,51	,55	,60	,65	,70	,75	,80	,85	,90	,95	,100]
#rainfall = [0	,0	,0	,0	,6	,6	,6	,6	,10	,10	,12	,14	,20	,24	,27	,32	,37	,40	,45	,47	,50	,53	,55	,58	,60	,63	,68	,74	,78	,83	,88	,95	,98	,110	,140	,150	,160	,180,	200	,225	,250	,275	,300	,325	,350	,375	,400	,425	,450	,475	,500]

# using list comprehension
# to compute all possible permutations
res = [[i,j,k] for i in slope
       for j in vibration
       for k in moisture]
print("All possible permutations are : " + str(res))

# writing to csv file
with open('records.csv','w',newline='') as csvfile:

    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data res
    csvwriter.writerows(res)

    fields["new2"] = np.where(
        (fields.slope > 45) & (fields.vibration > 0.1) & (fields.moisture > 65),
        "Safe",
        "Danger"
    )
    fields.head()