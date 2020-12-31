import time
def countdown(t):
    if t == 0:
        print("alert")
        return None
    print(f"remaining time : {t}")
    time.sleep(1)
    return countdown(t-1)

countdown(4)