
# simple = []
count = 0
# for i in range(245690, 245757):
#     for j in range(1, i + 1):
#          if i % j == 0:
#              count += 1
#              if count == 2:
#                  while i % count != 0:
#                      count += 1
#                  if count == i:
#                      simple.append(i)
#

p = 0
for i in range(245690, 245757):
    p += 1
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(p, i)


