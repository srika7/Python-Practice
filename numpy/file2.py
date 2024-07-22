import json

def read_json_example():
    sample_json = '{"name": "Alice", "age": 25, "city": "Wonderland"}'
    data = json.loads(sample_json)
    print(data)

if __name__ == "__main__":
    read_json_example()
