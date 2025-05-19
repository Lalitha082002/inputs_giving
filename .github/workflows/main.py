import sys
def check_age(a):
  return int(age) > 18

if __name__ == "__main__":
  age = sys.argv[1]
  result = check_age(age)
  with open("result.txt", "w") as f:
    f.write(str(result))
    
