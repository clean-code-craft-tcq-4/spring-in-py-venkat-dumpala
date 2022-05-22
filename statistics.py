def calculateStats(numbers):
  len1 = len(numbers);
  
    

   total = sum(map(float,numbers));
   avg = total/len1;
    

  
 
  

  
  max_num = max(numbers);
  print("max value :", max_num);
  min_num = min(numbers);
  print("min value :", min_num);
  return avg, max_num, min_num
