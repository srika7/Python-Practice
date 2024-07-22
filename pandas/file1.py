import pandas as pd

def example_function():
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 24, 35, 32]}
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    example_function()
