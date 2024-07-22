import re

def regex_example():
    pattern = re.compile(r'\b\w{5}\b')
    text = "Hello world, this is a regex example"
    matches = pattern.findall(text)
    print(matches)

if __name__ == "__main__":
    regex_example()
