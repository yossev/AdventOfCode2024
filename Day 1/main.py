with open('input.txt', 'r') as file:
    lines = file.readlines()

col1 = []
col2 = []

# Split lines into two columns
for line in lines:
    parts = line.split()
    col1.append(int(parts[0]))
    col2.append(int(parts[1]))

# Sort both columns
col1.sort()
col2.sort()

sumList = []

for i in range(1001):
    if col1 and col2:  y
        min_in_col1 = col1.pop(0)  
        min_in_col2 = col2.pop(0)  
        sumList.append(abs(min_in_col2 - min_in_col1))
    else:
        break  

# Print results
print(sum(sumList))
