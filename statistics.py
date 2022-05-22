def calculateStats(numbers):
  len = len(numbers);
  
    
  while(1):
    if (list(numbers) or len(numbers)) != 0:
      total = sum(map(float,numbers));
      avg = total/len;
    
    else:
      continue
  
  
 
  

  
  max_num = max(numbers);
  print("max value :", max_num);
  min_num = min(numbers);
  print("min value :", min_num);
  return avg, max_num, min_num
