response_value = [5, 7, 3, 8]
response_value.append(0)

response_value = response_value[:2] + [6] + response_value[2:]

print(response_value)