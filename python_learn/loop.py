i=0
while i<6:
    print(i)
    i+=1

i=0
while i<6:
    if (i==3):          
        break                       #break the loop when the condition is statisfied
    i+=1
    print(i,'not break')
    
i=0
while i<6:
    i+=1
    if(i==3): continue           #continue to the next iteration when the condition is statisfied
    print(i,'continue')

else:  
    print('i is no longer')      #we can user else in while part once the loop is end


#for loop

data=['banaana','apple','test','mango']
for x in data:
    print(x,'data')


for x in 'test':
    print(x)

for x in data:
    if x=='banaana':
        print(x)    
else:
    print('no record found') 


for x in range(len(data)):
    print(data[x])    


for x in range(2,4):
    print(data[x])    

for x in range(1,50,10):
    print(x)    