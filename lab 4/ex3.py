# manipulate a in various tricky ways
# name: Ziyan He
# Date: 2026-9-16

response_value = [5, 7, 3, 8]
response_value.append(0)
print("response_value after append 0: ", response_value)
# response_value.insert(2, 6)
response_value = response_value[:2] + [6] + response_value[2:]
print("response_value after insert 6 at index 2: ", response_value)