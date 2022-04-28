import numpy as np

slope = np.array([0	,1	,2	,6	,10	,15	,16	,18	,20	,24	,25	,30	,35	,38	,42	,45	,47	,48	,50	,52	,54	,55	,60	,65	,70])
vibration = np.array([0.0001 ,0.0009 ,0.0012 ,0.0017	,0.0025	,0.003	,0.006	,0.01	,0.03	,0.05	,0.1	,0.25	,0.4	,0.55	,0.7	,0.85	,1	,1.2	,1.4	,1.6	,1.8])
rainfall = np.array([0	,0	,0	,0	,6	,6	,6	,6	,10	,10	,12	,14	,20	,24	,27	,32	,37	,40	,45	,47	,50	,53	,55	,58	,60	,63	,68	,74	,78	,83	,88	,95	,98	,110	,140	,150	,160	,180,	200	,225	,250	,275	,300	,325	,350	,375	,400	,425	,450	,475	,500])
moisture = np.array([0	,0	,0	,0	,10	,10	,10	,10	,15	,15	,16	,17	,20	,23	,25	,30	,32	,35	,37	,39	,43	,46	,48	,51	,55	,60	,65	,70	,75	,80	,85	,90	,95	,100])

print("slope :")
print(slope)

vibration=vibration.astype(int)
print("vibration :")
print(vibration)

print("rainfall :")
print(rainfall)

print("moisture :")
print(moisture)

comb_array = np.array(
    np.meshgrid(slope, vibration, rainfall, moisture)).T.reshape(-1, 4)

print("\nDataset :")
print(comb_array)
