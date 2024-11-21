# -*- coding: utf-8 -*-
"""
@author: Arun Totad
@WIN: 353146427
PA1 - Programming for Graduate Study (CS5115) - 09/27/2024
"""

import urllib.request
import time

'Reading dataset for pre-processing'
def read_dataset(dataset = "", url = ""):
    if(dataset != ""):
        with open(dataset, "r") as file: #reading the file from locally 
            contentList = file.readlines()
        contentList = [x.strip() for x in contentList]
    elif(url != ""): #reading the file from global
        response = urllib.request.urlopen(url)
        contentList = response.read().decode().splitlines()
    else:
        print("Dataset not defined for processing")
        
    print("----------Dataset fetched successfully-----------")
    print("Dataset --> ",dataset, url)
    print()
    print("Total size of Dataset: ", len(contentList))
    print("Elements of list = ", contentList[0] ," -> ", contentList[len(contentList)//4] ," -> ", contentList[len(contentList)//2] ," -> ", contentList[(3*len(contentList))//4]," -> ", contentList[len(contentList)-1])
    #print("Any None values in List: ",any(x is None for x in List))
    print("********************************************************")
    print()
    return contentList

'Display results after execution of strategies'
def print_results(List, timeElapsed):
    print("Current size of list: ", len(List)) #Current size of the 
    print("Time elapsed: ", timeElapsed, " seconds")
    List.sort()
    print("Elements of list = ", List[0] ," -> ", List[len(List)//4] ," -> ", List[len(List)//2] ," -> ", List[(3*len(List))//4]," -> ", List[len(List)-1])
    #print("Any None values in List: ",any(x is None for x in List))
    print("********************************************************")


    
'Incremental Strategies'    
def incremental_strategies(incrementor, dataset, arrayType):
    print()
    if(arrayType == "List"):
        ewol = list()
        
    elif(arrayType == "Array"):
        ewol = [None] * len(dataset)
        
    else: 
        print("Mentioned Data structure doesn't work for current program, Try again!")
    
    if(incrementor == "IncrementBy2"):
        print("Increament by 2")
        print("***************")
        start_time = time.time()
        minrange = maxrange = 0
        
        while(maxrange < len(dataset)):
            maxrange += 2
            for i in range(minrange, maxrange):
                if(i == len(dataset)):
                    break
                if(arrayType == "Array"):
                    ewol[i] = dataset[i]
                else:
                    ewol.append(dataset[i])
            
            minrange = maxrange
            
        end_time = time.time()   
        timeElapsed = end_time - start_time
        
        print_results(ewol, timeElapsed)
        return ewol
        
    
    elif(incrementor == "StrategyA"):
        print("Strategy A: Increment by 10")
        print("***************************")
        start_time = time.time()
        minrange = maxrange = 0
        
        while(maxrange < len(dataset)):
            maxrange += 10
            
            for i in range(minrange, maxrange):
                if(i == len(dataset)):
                    break
                if(arrayType == "Array"):
                    ewol[i] = dataset[i]
                else:
                    ewol.append(dataset[i])
            
            minrange = maxrange
            
        end_time = time.time()   
        timeElapsed = end_time - start_time
        
        print_results(ewol, timeElapsed)
        return ewol
    
    
    elif(incrementor == "StrategyB"):
        print("Strategy B: Increment by Doubling")
        print("*********************************")
        start_time = time.time()
        minrange = 0
        maxrange = 1
        
        while(maxrange < len(dataset)):
            maxrange *= 2
            
            for i in range(minrange, maxrange):
                if(i == len(dataset)):
                    break
                if(arrayType == "Array"):
                    ewol[i] = dataset[i]
                else:
                    ewol.append(dataset[i])
            
            minrange = maxrange
            
        end_time = time.time()   
        timeElapsed = end_time - start_time
        
        print_results(ewol, timeElapsed)
        return ewol
    
    
    elif(incrementor == "StrategyC"):
        print("Strategy C: Increment by fibonacci series")
        print("*****************************************")
        start_time = time.time()
        minrange = 0
        maxrange = 1
        countrange = 0
        if(arrayType == "Array"):
            ewol[0] = dataset[0]
        else:
            ewol.append(dataset[0])
        
        while(countrange < len(dataset)):      
            countrange = minrange + maxrange
            #   print(minrange, maxrange, countrange)
            for i in range(maxrange, countrange):
                if(i == len(dataset)):
                    break
                if(arrayType == "Array"):
                    ewol[i] = dataset[i]
                else:
                    ewol.append(dataset[i])
            
            minrange = maxrange
            maxrange = countrange
            
        end_time = time.time()   
        timeElapsed = end_time - start_time
        
        print_results(ewol, timeElapsed)
        return ewol
    
    else:
        print("Strategy mentioned doesnot exist, Try again!")


'Use binary-search to insert the new word into eowl[], which will be done after allocating new array when an increase is needed.'
def binary_search(ewol, new_word):
    low, high = 0, len(ewol) - 1
    index_number = 0
    search_point = 0
    
    while(low <= high):
        start_time = time.time()
        mid = (low + high) // 2
        
        if(new_word == ewol[mid]):
            #print("Inside mid")
            index_number = 0
            break
        elif(new_word < ewol[mid]):
            high = mid - 1
            #print("Inside left")
            index_number = mid
        else:
            low = mid + 1
            #print("Inside right")
            index_number = mid
        end_time = time.time()
        elapsed_time = end_time - start_time
        search_point += 1
        #print("Search point:", search_point, " took ", elapsed_time, "seconds")
    return index_number


def binarySearch_insert(ewol):
    insert_new_word = input("Enter the new word that needs to be inserted into the array: ")
    new_word = insert_new_word.lower()
    start_time = time.time()
    new_ewol = list()
    for i in range(0, len(ewol)):
        new_ewol.append(ewol[i])
    
    index_number = binary_search(ewol, new_word)

    print("Index number found for the new element insertion: ", index_number)
    print()
    new_ewol.append(None)
    if(index_number != 0):
        for i in range(len(ewol), index_number, -1):
            new_ewol[i] = ewol[i-1]
        
        new_ewol[index_number] = new_word
        
        end_time = time.time()
        elapsed_time4 = end_time - start_time
        ewol.sort()
        print("ewol[] before insertion: ", ewol[index_number-1],"->", ewol[index_number], "->", ewol[index_number+1])
        print("Current size of ewol[] before insertion: ", len(ewol))
        print()
        print("new_ewol[] after insertion: ", new_ewol[index_number-1],"->", new_ewol[index_number], "->",new_ewol[index_number+1])
        print("Current size of new_eowl[] after insertion: ", len(new_ewol))
        print()
        print("Time elapsed: ", elapsed_time4, " seconds")
        print("************************************************************")
        print()
    else:
        print("Item already exist in the array")      
        end_time = time.time()
        elapsed_time4 = end_time - start_time



#Graphical interface for executing each functionality individually. 
def GUI(contentList):
    while(True):
        run = input("----------Execute specific strategies--------------")
        if(run.upper() == "N"):
            break
        elif(run.upper() == "Y"):
            arrayType = input("Select type of dataset for processing: \n A) Array Implementation \n B) List Implementation \n")
            if(arrayType.upper() == "A"):
                arrayType = "Array"
            elif arrayType.upper() == "B":
                arrayType = "List"
            else: 
                print("Mentioned data structure doesn't work for this program, Try again with A/B")
                break
            
            print()
            
            strategy = input("Select Incremental Strategy for processing: \n A)Increment by 2 \n B)Increment by 10 \n C)Increment by Doubling \n D)Increment by Fibanocci series \n")
            if(strategy.upper() == "A"):
                ewol = incremental_strategies("IncrementBy2", contentList, arrayType)
            elif(strategy.upper() == "B"): 
                ewol = incremental_strategies("StrategyA", contentList, arrayType)
            elif(strategy.upper() == "C"):
                ewol = incremental_strategies("StrategyB", contentList, arrayType)
            elif(strategy.upper() == "D"):
                ewol = incremental_strategies("StrategyC", contentList, arrayType)
            else:
                print("Mentioned strategy doesn't work for this program, please try again with A/B/C/D for processing")
        else:
            print("Invalid Input")
    
    print("Lets insert an element into the list")
    binarySearch_insert()

     
#Execute all of the strategies with respect to size of dataset
def just_execute(contentList):
    arrayType = input("Select type of dataset for processing: \n A) Array Implementation \n B) List Implementation \n")
    if(arrayType.upper() == "A"):
        arrayType = "Array"
        print("-----------Demonstrating Array Data Structure-----------")
    elif arrayType.upper() == "B":
        arrayType = "List"
        print("-----------Demonstrating List Data Structure-----------")
    else: 
        print("Mentioned data structure doesn't work for this program, Try again with A/B")
    ewol = incremental_strategies("IncrementBy2", contentList, arrayType)
    ewol = incremental_strategies("StrategyA", contentList, arrayType)
    ewol = incremental_strategies("StrategyB", contentList, arrayType)
    ewol = incremental_strategies("StrategyC", contentList, arrayType)
    print("Lets insert an element into the list")
    binarySearch_insert(ewol)
    
   


'Main function'
if __name__ == "__main__":
    print("********************************************************")
    print("CS5115: Programming for Graduate Student : PA 1 Solution")
    print("********************************************************")
    print()
    
    contentList = read_dataset("C:/Users/Arun Totad/Desktop/CS5115/Assignment assets/PA1/PA1_cs5115_Totad_092424/EOWL_200 shuffled.txt")
    just_execute(contentList)
    GUI(contentList)
    

    
    