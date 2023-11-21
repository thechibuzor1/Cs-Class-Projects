class MemorySegment:
    def __init__(self, size):
        self.size = size
        self.isFree = True
    
#first fit    
def allocateFirstFit(memory, processSize):
    for segment in memory:
        if segment.isFree and segment.size >= processSize:
            segment.isFree = False
            if segment.size > processSize:
                remainingSize = MemorySegment(segment.size - processSize)
                remainingSize.isFree = True
                memory.insert(memory.index(segment)+1, remainingSize)
                segment.size = processSize
        return segment.size
    return  False


#best fit
def allocateBestFit(memory, processSize):
    smallestFitSize = float('inf')
    bestFitSegment = None 
    
    for segment in memory:
        if segment.isFree and segment.size >= processSize:
            if segment.size - processSize < smallestFitSize:
                smallestFitSize = segment.size - processSize 
                bestFitSegment = segment 
                
                
    if bestFitSegment is not None:  
        bestFitSegment.isFree = False
        if bestFitSegment.size > processSize:
            remaningSize = MemorySegment(bestFitSegment.size - processSize)
            remaningSize.isFree = True
            memory.insert(memory.index(bestFitSegment)+1, remaningSize)
            bestFitSegment.size = processSize
    
        return bestFitSegment.size
    return   False


memory = [MemorySegment(50), MemorySegment(90), MemorySegment(32), MemorySegment(35),  MemorySegment(12)]

processSize = 10


    
 

res = allocateBestFit(memory, processSize)
res2 = allocateFirstFit(memory, processSize)
 
 
if res:
    print(f"process of size {processSize} was saved to segment of size {res}")
    
    for segment in memory:
        print(segment.size)
else:
    print("Unable to allocate ")
    
    