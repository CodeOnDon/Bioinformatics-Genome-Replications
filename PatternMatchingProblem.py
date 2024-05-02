# PatternMatching takes a Pattern and Genome as input and outputs the starting position of each occurrence of the pattern
# INPUT: Pattern, Genome as str
# OUTPUT: A list of starting positions where the pattern has been found
def PatternMatching(pattern: str, genome: str) -> list[int]:
    start_positions = []
    
    # searching down the genome for the pattern
    # the last starting position will be the length of genome minus length of the pattern
    for i in range(len(genome) - len(pattern)+1):
        # add the index to the list of start positions if pattern is found
        if genome[i:(i + len(pattern))] == pattern:
            start_positions.append(i)  
    
    return start_positions


#PatternMatchingFile is the same as pattern PatternMatching but takes a txt file as input for the string

def PatternMatchingFile(pattern: str, file_path: str) -> list[int]:
    start_positions = []
    
    with open(file_path,"r") as f:
        genome = f.read()
        
    # searching down the genome for the pattern
    # the last starting position will be the length of genome minus length of the pattern
    for i in range(len(genome) - len(pattern)+1):
        # add the index to the list of start positions if pattern is found
        if genome[i:(i + len(pattern))] == pattern:
            start_positions.append(i)  
    
    return start_positions

