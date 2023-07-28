import shutil

tot,used,free=shutil.disk_usage("/")
print("free space on disk: {:4.0f} GB ({} bytes)".format(free/1e9, free))
print("how many bytes should we wipe:")
try:
    number_of_bytes = int(input())
except:
    print("bad input. closing program")

print("number of bytes entered is: {} [bytes]".format(number_of_bytes))

if(number_of_bytes < int(free) and number_of_bytes > 0):
    print("Creating required file. goddamn!!!")
    
    with open("goddamn!!!.txt", "wb") as binary_file:
        byte_2_write = b'goddamn!!!'
        
        for i in range(int(number_of_bytes/10)):
            binary_file.write(byte_2_write)
            
            if(i%1e7 == 0):
                print("{} MB written".format(int(i*1e-5)),end= "\n")
        
        print("Finished!")
        binary_file.close()
    
        
else:
    print("bad input. too high or negative number")