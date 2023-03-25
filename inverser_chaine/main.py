# "Bonjour toto" => "otot ruojnoB"

def reverse_string(str):
  temp_str = ""
  n = 1
  while n < len(str) + 1:
    temp_str += str[-n]
    n += 1
  return temp_str

def reverse_string2(str):
  temp_str = ""
  for l in str:
    temp_str = l + temp_str
  return temp_str

def reverse_string3(str):
  return str[::-1]
    
arr = "Bonjour toto"

print(reverse_string3(arr))