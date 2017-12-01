def AoC1(input_):
  sum_ = 0
  for i,val in enumerate(input_):
    if i == len(input_) - 1:
      if(val == input_[0]):
        sum_ += int(val)
    else:
      if val == input_[i+1]:
        sum_ += int(val)
  return sum_
