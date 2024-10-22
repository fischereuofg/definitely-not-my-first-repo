###https://stackoverflow.com/questions/5424716/how-can-i-check-if-string-input-is-a-number
count=0


while count<=0:
    try:
        count=int(input())
    except ValueError:
        pass
    if count <=0:
        print("Please enter a interger that is greater than 0")
    
sequence=[0,1]
output=""

for i in range(1,count-1):
    newNum=sequence[i]+sequence[i-1]
    sequence.append(newNum)

for i in range(count):
    output+=str(sequence[i])+" "

print(output)