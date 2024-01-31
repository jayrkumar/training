def alternative_lines(content):
    try:
        seperate=content.split('\n')
        print(seperate)
        print("\n")
        for element in range(0,len(seperate),2):
            print(seperate[element])
    except FileNotFoundError:
        print("alternative_lines here go")
        
    
file=open("/workspaces/training/data/test.txt","r")
content=file.read()
print(content)
print("PRINTING ALTERNATIVE LINES")
print("==========================")
alternative_lines(content)
print("==========================")
