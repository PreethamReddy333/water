from collections import OrderedDict

def lru_page_replacement(page_references, frame_count):
    frames = OrderedDict()
    page_fault_count = 0

    print(f"{'Page Reference ':<15}{'Frame Status'}")
    print('-' * 30)

    for page in page_references:
        if page in frames:
            
            frames.move_to_end(page)
            print(f"{page:<15}{list(frames.keys())}")
        else:
            page_fault_count += 1
            if len(frames) < frame_count:
                frames[page] = None  
            else:
                
                frames.popitem(last=False)
                frames[page] = None 
            print(f"{page:<15}{list(frames.keys())} <- Page Fault")

    print(f"Total Number of faults = {page_fault_count}.")

page_references = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frame_count = 3
lru_page_replacement(page_references, frame_count)
