import pandas as pand
import numpy as np

frame1=pand.DataFrame({'id':[1,'2',2,3,4,5]})
frame2=pand.DataFrame({'name':['0','2','4','2'],'null':['11','njul','data','daaa']})


frame1=frame1.append(frame2,ignore_index=True,sort=False)
print(frame1)

info = pand.DataFrame([[2, 7]] * 4, columns=['P', 'Q'])  
info=info.apply(np.sqrt)  
print(info)
#info=info.apply(np.sum, axis=0)  
#print(info)
#info= info.apply(np.sum, axis=2)  
# info= info.apply(lambda x: [1, 24], axis=1)  
# info= info.apply(lambda x: [1, 2], axis=1, result_type='expand')  
# info=info.apply(lambda x: pand.Series([1, 2], index=['foo', 'bar']), axis=1)  
info=info.apply(lambda x: [1, 2], axis=1, result_type='broadcast')  
print(info)