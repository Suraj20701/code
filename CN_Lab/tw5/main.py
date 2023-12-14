# leaky bucket

import time
class LeackyBucket :
    def __init__(self, capacity, rate) :
        self.capacity = capacity
        self.rate = rate
        self.tokens = 0
        self.last_time = time.time()

    def add_token(self) :
        current_time = time.time()
        time_elasped = current_time - self.last_time
        self.tokens = min(self.capacity, self.tokens+time_elasped*self.rate)
        self.last_time = current_time

    def transmit(self, packet_size) :
        if self.tokens >= packet_size :
            self.tokens -= packet_size
            print(f"Transmitted {packet_size} bytes")
            return True
        else :
            print("Dropped - Insufficient tokens")
            return False
        
if __name__ == "__main__" :
    bucket = LeackyBucket(capacity=50, rate=10)
    for i in range(1, 11) :
        print(f"Time {i} seconds")
        bucket.add_token()
        packet_size = eval(input("Enter the packe size : "))
        bucket.transmit(packet_size)
        