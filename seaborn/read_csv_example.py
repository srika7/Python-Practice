import csv

def read_csv_example():
    data = """name,age,city
    Alice,30,Wonderland
    Bob,25,Builderland"""
    
    reader = csv.DictReader(data.splitlines())
    for row in reader:
        print(row)

if __name__ == "__main__":
    read_csv_example()
