import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    tokens=np.array(tokens)
    vocab=np.array(vocab)
    output=[]
    if(len(vocab)==0):
        return np.zeros(0, dtype=int)
    for i in range(len(vocab)):
        j=0
        count=0
        while(j<len(tokens)):
            if(vocab[i]==tokens[j]):
                count+=1
                j+=1
            else:
                j+=1
        output.append(count)
    output=np.array(output)
        
    return output
        
    