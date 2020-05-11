#contains rows lists each of length cols initially set to 0
#index as my_matrix[1][2] my_matrix[R][C]
def create_matrix(rows, cols):    my_matrix = [[0 for col in range(cols+1)] for row in range(rows+1)]
    return my_matrix

#x is row index, y is column index
# follows[r][c]
def calc_score(matrix, x, y,sequence1,sequence2):
   sc = seqmatch if sequence1[y - 1] == sequence2[x - 1] else seqmismatch

   base_score = matrix[x - 1][y - 1] + sc

   insert_score   = ???
   delete_score = ???
   v=max(0, base_score, insert_score, delete_score)
   return v

#makes a single traceback step
def traceback(mymatrix,maxv):
    x=maxv[0]
    y=maxv[-1]
    val=mymatrix[x][y]

    sc = seqmatch if sequence1[y - 1] == sequence2[x - 1] else seqmismatch
    base_score = mymatrix[x - 1][y - 1] + sc
    if base_score==val:
        return [x-1,y-1]

    insert_score = mymatrix[x - 1][y] + seqgap
    if insert_score==val:
        return ???
    else:
        return ???


#builds the initial scoring matrix used for traceback
def build_matrix(mymatrix):

    rows=len(mymatrix)
    cols=len(mymatrix[0])

    for i in range(1, rows):
         for j in range(1, cols):
          mymatrix[i][j]  = calc_score(mymatrix, i, j,sequence1,sequence2)

    return mymatrix

#gets the max value from the built matrix
def get_max(mymatrix):

     max=mymatrix[0][0]
     mrow=0
     mcol=0

     rows = len(mymatrix)
     cols = len(mymatrix[0])

     for i in range(1, rows):
         for j in range(1, cols):
             if mymatrix[i][j]>max:
                 max=mymatrix[i][j]
                 mrow=i
                 mcol=j
     print("max score: ",max)
     return ???

#print out the best scoring path from the SW matrix
def print_matrix(mymatrix):
    rows = len(mymatrix)
    cols = len(mymatrix[0])
    s1="  " +sequence1
    s2=" "+sequence2

    print("Dimensions: r= %2d , c= %2d" % (rows, cols))

    for a in s1:
        print(a, end ="")
        print(" \t", end ="")
    print("\n",end="")

    for i in range(0, rows):
        print(s2[i], end ="")
        print(" \t", end ="")
        for j in range(0, cols):
           print("%02d\t" % (mymatrix[i][j]),end="")
        print("\n",end="")

#print out the traceback of the best scoring alignment
def print_traceback(mymatrix):
   print("Building traceback...")
   maxv=get_max(mymatrix)
   print(maxv)

   #traverse the matrix to find the traceback elements
   #if more than one path just pick one
   topstring=""
   midstring=""
   bottomstring=""

   # add first element and go to previous
   topstring += sequence1[maxv[-1]-1]
   bottomstring += sequence2[maxv[0]-1]
   if sequence1[maxv[-1]-1] == sequence2[maxv[0]-1]:
       midstring += "|"
   else:
       midstring += " "

   #add the rest of the elements
   search=True
   while(search):
       maxv=traceback(mymatrix,maxv)
       if(mymatrix[maxv[0]][maxv[-1]]==0):
           search=False
           continue

       # add the next element and go to previous
       topstring += sequence1[maxv[-1]-1]
       bottomstring += sequence2[maxv[0]-1]
       if sequence1[maxv[-1] - 1] == sequence2[maxv[0] - 1]:
           midstring += "|"
       else:
           midstring += " "


   print(topstring[::-1])
   print(???)
   print(???)



#build the SW alignment...
def perform_smith_waterman():
#values for weights
  global  seqmatch
  global  seqmismatch
  global  seqgap
  global sequence1
  global sequence2

  seqmatch =1
  seqmismatch=-1
  seqgap=-1

  #input sequences
  sequence1="AGTGATAAACTAGTAATTTTT"
  sequence2="???"

  print("Sequence1: "+sequence1);
  print("Sequence2: "+sequence2);

  mymatrix=create_matrix(len(sequence2), ???)
#  print_matrix(mymatrix,sequence1,sequence2)
  mymatrix=build_matrix(mymatrix)
  print_matrix(mymatrix)

  print_traceback(mymatrix)

##this calls the SW algorithm when the script loads
perform_smith_waterman()
