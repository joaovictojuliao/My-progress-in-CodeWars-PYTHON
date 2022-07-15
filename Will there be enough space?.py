def enough(cap, on, wait):
    total=on+wait
    if total>cap:
        return total-cap
    elif total<=cap:
        return 0
