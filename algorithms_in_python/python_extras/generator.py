import pandas as pd

def generate():
    for i in range(0,100000):
        yield i,i**2

def gendf():
    l = generate()
    df = pd.DataFrame(l,columns=['left', 'right'])
    df.to_csv('data.csv', index=False)

    df1 = pd.read_csv('data.csv')
    print(df1.head())
if __name__ == "__main__":
    gendf();
