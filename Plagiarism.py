def toWordsArr(filename):
    wordArr = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            for word in line.split():
                wordArr.append(word.strip())
    return wordArr        
        


def detect_plagiarism(fileName1, fileName2):
    
    A = toWordsArr(fileName1)
    B = toWordsArr(fileName2)
    
    arr = [[0] * len(B)] * len(A)
    
    longest = (0,0)
    
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                if i ==0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j-1] + 1
                
                if arr[i][j] > arr[longest[0]][longest[1]]:
                    longest = (i,j)
    
    end_index = longest[0]+1
    start_index = end_index - arr[longest[0]][longest[1]]
    
    return ' '.join(A[start_index : end_index]) if end_index - start_index >= 5 else False
