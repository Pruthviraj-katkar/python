import sys
if len(sys.argv) > 1:
    for eacharg in sys.argv[1:]:
        print(eacharg)
else:
    print("No arguments provided!")        
