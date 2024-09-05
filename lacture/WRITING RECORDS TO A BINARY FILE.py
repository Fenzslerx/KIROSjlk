import struct

record = (1, 'john doe',20 ,3.75)

with open("record.bin", "wb") as file:
    data = struct.pack('i20sif', record[0], record[1].encode(),
            record[2], record[3])
    
    file.write(data)