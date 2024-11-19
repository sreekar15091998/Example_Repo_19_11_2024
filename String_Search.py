def search_string(file_name,string_to_search):
    try:
        file=open(file_name,'r')
        res=file.read()
        
        if string_to_search in res:
            print("String Matched")
        else:
            print("String not matched")
            
        file.close()
    except:
        print("Error in file reading")
        
        print("Added new string")
        
search_string("C://Users//Msree//Desktop//Python//File_Handling//sample3.txt","Cicero")
