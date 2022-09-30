a = input("Enter sentence or word: ")
vowels='aeiouAEIOU'
count= 0
for i in a:
    if i in vowels:
        count+=1
print('The number of vowels in',a,'is',count)
