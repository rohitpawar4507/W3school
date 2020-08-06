

nums = [3,4,5,1,4,2,8,9,0,6]

evens = list(filter(lambda n:n%2==0,nums))

doubles = list(map(lambda n:n+2,evens))



print(evens)
print(doubles)