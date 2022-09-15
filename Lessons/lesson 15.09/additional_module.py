global_var = [5]

def print_global_var():
    print(f"the global var value is {global_var}")

if __name__ == "__main__":
    #will work only when the file is running and not being imported as module
    print("hello from additional module")
