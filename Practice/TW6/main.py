tokens = 1000
packets = [400, 300, 500, 300, 700, 200, 100]
index = 0
while index < len(packets) :
    
    if tokens >= packets[index] :
        print(f"Packet sent sucessfully : {packets[index]}")
        tokens -= packets[index]
        index += 1
    else :
        print(f"Tokens are less({tokens}<{packets[index]} updating tokens)")
        tokens = 1000
        

print("All packets sent sucessfully ")