def AoC1(input_,jumps):
  # If jumps is 1 then solving Part 2, else solving Part 1
  sum_ = 0
  steps = 1 if (jumps == 0) else int(len(input_)/2)
  for i,val in enumerate(input_):
    if (i >= len(input_) - steps):
      sum_ += int(val) if (val == input_[0+ i - (len(input_) - steps)]) else 0
    else:
      sum_ += int(val) if (val == input_[i+steps]) else 0
  print(sum_)
  
