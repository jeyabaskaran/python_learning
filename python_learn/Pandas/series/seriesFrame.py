import pandas as pand

frame1= pand.Series(['a','b','c','d'],name='New Column')
print(frame1.to_frame())


s1=['data','dumy','core','java']
s2=['3939','222',444,'303kd']

ser1=pand.Series(s1)
ser2=pand.Series(s2)

frameValue={'Emp':ser1, 'Data':ser2}

print(pand.DataFrame(frameValue))
