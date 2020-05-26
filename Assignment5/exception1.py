try:
    name = input('Enter the filename:')
    fp = open(name, 'r')

except IOError as e:
    print("No file found:", e)

except Exception as e:
    print("Something went wrong...")

else:
    p = fp.readline()
    print('The first line in the file is:', p)
    print('File opened succesfully.')
    fp.close()

    
    

