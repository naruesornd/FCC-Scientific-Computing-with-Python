def arithmetic_arranger(problems, choice = False):
  #Error Checking
  #Checks the number of input problem
  if len(problems) > 5:
    return('Error: Too many problems.')

  #Initialise the lists for each part of the operation
  top = []  #top operand
  opera = []   #operator
  bottom = []  # bottom operand
  
  #Splits the list of operations
  for problem in problems:
    problem.strip() #remove whitespaces
    s_problem = problem.split(" ")  
    if not (s_problem[1] == '+' or s_problem[1] == '-'):
      return('Error: Operator must be \'+\' or \'-\'.')
    if len(s_problem[0]) > 4 or len(s_problem[2]) > 4:
      return('Error: Numbers cannot be more than four digits.')
    top.append(s_problem[0])
    opera.append(s_problem[1])
    bottom.append(s_problem[2])

  #Initialise empty strings for storing the each output line 
  fir_line = ''   #first line
  sec_line = ''   #second line
  thi_line = ''   #third line
  fou_line = ''   #fourth line
  gaps = '    '   # 4 gaps to separate each problem
  
  #Arithmetic Operations
  result = [] 
  counter = 0 
  while counter < len(problems):
    if not (top[counter].isnumeric() or bottom[counter].isnumeric()):
      return('Error: Numbers must only contain digits.')
    if opera[counter] == '+':
      a = int(top[counter])
      b = int(bottom[counter])
      result.append(str(a + b))
    elif opera[counter] == '-':
      result.append(str(a - b))

    #Finds the width of the longest operand
    longest = max(len(top[counter]), len(bottom[counter]))

    #Creates the first line 
    for val in range((longest + 2) - len(top[counter])):   # +2 for moving operands to the right two steps
      top[counter] = ' ' + top[counter]
    fir_line += top[counter] + gaps

    #Creates the second line
    for val in range((longest + 1) - len(bottom[counter])):
      bottom[counter] = ' ' + bottom[counter]
    sec_line  += opera[counter] + bottom[counter] + gaps

    #Creates the third line
    for val in range(longest + 2):
      thi_line += '-'
    thi_line += gaps

    #Creates the fourth line 
    for val in range((longest + 2) - len(result[counter])):
      result[counter] = ' ' + result[counter]
    fou_line += result[counter] + gaps

    counter += 1

  #Final output
  #Remove the gaps of the last part of each line 
  fir_line = fir_line.rstrip()
  sec_line = sec_line.rstrip()
  thi_line = thi_line.rstrip()
  fou_line = fou_line.rstrip()
  #Print the output
  if not choice:
    return fir_line + '\n' + sec_line + '\n' + thi_line
  else:
    return fir_line + '\n' + sec_line + '\n' + thi_line + '\n' + fou_line
  
  
    

    
      
      
    
    