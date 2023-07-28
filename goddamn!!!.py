'''
This code is used in order to scan the amount of available space on a drive and than 
overwrite it with the word "goddamn!!!". 

The reason for doing so is that this operation alongside formatting will reduce the 
ability of a third party to restore data from a hard drive after conducting formatting 
of the drive.

I've used this code in order to sell an old computer without compromising my data, which
was present on the hard drive prior to formatting it

good luck and goddamn! https://youtu.be/PTqtrGBYpxQ
'''

import shutil

total, used, free=shutil.disk_usage("/")
print("total space on disk: {:4.0f} GB ({} bytes)".format(total/1e9, total))
print("used space on disk: {:4.0f} GB ({} bytes)".format(used/1e9, used))
print("free space on disk: {:4.0f} GB ({} bytes)\n".format(free/1e9, free))
print("how many bytes should we wipe:")
try:
    number_of_bytes = int(input())
except:
    print("bad input. closing program")

print("number of bytes entered is: {} [bytes]".format(number_of_bytes))

if(number_of_bytes < int(free) and number_of_bytes > 0):
    print("Creating required file. goddamn!!!\n")
    
    with open("goddamn!!!.txt", "wb") as binary_file:
        byte_2_write = b'goddamn!!!'
        
        for i in range(int(number_of_bytes/10)):
            binary_file.write(byte_2_write)
            
            if(i%1e7 == 0):
                print("{} MB written".format(int(i*1e-5)),end= "\n")
        
        print("\n\nFinished!")
        binary_file.close()
    
        
else:
    print("bad input. too high or negative number")