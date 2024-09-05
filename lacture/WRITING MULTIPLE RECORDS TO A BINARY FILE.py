import struct

num_records = int(input("How many records do you want to create"))

with open("records.bin", "wb") as file:
    for _ in range(num_records):
        id_num = int(input("enter id: "))
        name = input("enter name: ")
        age = int(input("enter age: "))
        gpa = float(input("enter gpa: "))

        data = struct.pack('i20sif', id_num, name.encode(), age, gpa)
        file.write(data)

print(f"{num_records} records have been writen to records.bin")