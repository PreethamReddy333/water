def fifo(page_ref,pages) :
    memory = [None for i in range(pages)]
    fault = 0
    x = -1
    for i in range(len(page_ref)) :
        pn = page_ref.pop(0)
        if pn in memory :
            print(memory)
        else :
            fault+=1
            x = (x+1)%(pages)
                
            memory[x] = pn
            print(memory)
    print(f"Number of faults = {fault}. ")
    
            
            
    


page_ref = [1,3,0,3,5,6,3]
pages = 3
fifo(page_ref,pages)
