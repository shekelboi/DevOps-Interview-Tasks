import os

directory = 'coding/images'

# Renaming files from .jpg to .jpeg
for file in os.listdir(directory):
    if file.endswith('.jpg'):
        new = file[:-3] + 'jpeg'
        os.rename(os.path.join(directory, file), os.path.join(directory, new))

# Reversing a string
s = 'codinginterview'
print(''.join(reversed(s)))
print(s[::-1])

# Algorithmically using two pointers
s_list = list(s)
left, right = 0, len(s_list) - 1
while left < right:
    s_list[left], s_list[right] = s_list[right], s_list[left]
    left += 1
    right -= 1

print(''.join(s_list))

# Reverse the last four characters
print(s[:-4] + s[-4:][::-1])

s_list = list(s)
left, right = len(s_list) - 4, len(s_list) - 1
while left < right:
    s_list[left], s_list[right] = s_list[right], s_list[left]
    left += 1
    right -= 1

print(''.join(s_list))
