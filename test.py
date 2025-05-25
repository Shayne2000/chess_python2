def loop_from_zero(start, stop):
    diff = stop - start
    step = (diff > 0) - (diff < 0)
    for i in range(start+step, diff+start+step, step):
        print(i)


loop_from_zero(int(input()),int(input()))