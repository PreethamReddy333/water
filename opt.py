def optimal_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0

    for i in range(len(pages)):
        page = pages[i]
        if page in frames:
            continue
        else:
            page_faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                farthest = -1
                index_to_replace = -1
                for j in range(len(frames)):
                    try:
                        next_use = pages[i + 1:].index(frames[j])
                    except ValueError:
                        next_use = float('inf')
                    if next_use > farthest:
                        farthest = next_use
                        index_to_replace = j

                frames[index_to_replace] = page

    return page_faults


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_count = 3
print("Optimal Page Faults:", optimal_page_replacement(pages, frame_count))
