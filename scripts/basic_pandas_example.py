import pandas as pd

def main():
    print(f"Pandas version: {pd.__version__}")

    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    })

    print(df)

if __name__ == "__main__":
    main()