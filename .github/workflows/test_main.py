def checking_age():
  with open("result.txt","r") as f:
    result = f.read().strip()
  assert result == "True", "Age is not greater than 18"
