import statistics as st
import cubed

def main():
    # one()
    two()

def one():
    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    print(st.variance(data))
    
def two():
    print(cubed.calc(3))

if __name__ == "__main__":
    main()
