# def func(param1,param2):
#     print(param1,param2)
#     print('hello',param2+' '+param1)

# func(param2='jeya',param1='dddd')


# #default function

# def func2(count=10):
#     print(count)

# func2()


def tri_recursion(k):
  if(k > 0):
    print(k,'k')
    result = k + tri_recursion(k - 1)
   # return result
    print(result,'after recrusion',k,k-1)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(3)


def loopfun(data):
  for x in data:
    print(x)

loopfun(['data','somewhere','fast'])