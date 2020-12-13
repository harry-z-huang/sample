1'''Harry Huang
Due April 26, 2019 and finalized April 29, 2019
CSCI 203: Tuesday 8-10am Talmage Lab and 11am-12pm MWF Meng Lecture
Final Project- Part 2: 
Integrity statement: I have read and adhered to the Academic Honesty policy
as outline in the CSCI 203 "Course Description" document'''
import numpy as np
import matplotlib.pyplot as plt

def readFile(fileName): #this is only really here to view how my data has been formatted and for debugging purposes
    ''' Returns all the text in the file as one long string. 
        Input: fileName - string containing name of text file in same folder ''' 
    # open the file to read ('r') and assign to file object inFile 
    inFile = open(fileName, 'r')
    inFile.readline()
    # read the whole file as one long string 
    theText = inFile.read() 
    # Close the object associated with the file 
    inFile.close() 
    return theText

#uncomment the following to see how the file prints
#myText1= readFile('Fine Particulate Matter (PM2.5) (µgm³) (2003-2011).txt')
#print(myText1)
#myText2= readFile('North America Land Data Assimilation System (NLDAS) Daily Air Temperatures and Heat Index (1979-2011).txt')
#print(myText2)

#line[0]= notes, blank for all data points
#line[1]= state, but this actually varies based on the number of words in the state name
#line[-4]= state code, use this 
#line[-3]= year
#line[-2]= yearcode
#line[-1]= avg fine particulate matter or avg daily max heat index

def nationalHeatDictionary():
    '''Creates a dictionary of total national heat by year
        >>> nationalHeatDictionary()
        {2003: 1550.2999999999997, 2004: 1511.2200000000007, 2005: 1565.9499999999998, 2006: 1568.88, 2007: 1553.0800000000004, 2008: 1536.8299999999997, 2009: 1534.8800000000006, 2010: 1588.9200000000003, 2011: 1594.2800000000002}

    '''
    
    # open the file to read ('r') and assign to file object inFile 
    inFile = open('North America Land Data Assimilation System (NLDAS) Daily Air Temperatures and Heat Index (1979-2011).txt', 'r') 
    d= {} #initialize dictionary

    inFile.readline() #reads the first line and skips over it
    while True:
        line= inFile.readline()
        if not line:
            break
        # Process the line of text from the file 
        # Create a list of all the items separated by white space 
        lineList = line.split() 
        # Add the third number to total after converting to int 
        if int(lineList[-2][1:-1]) in d.keys(): 
            d[int(lineList[-2][1:-1])]+= float(lineList[-1])
        else:
            d[int(lineList[-2][1:-1])]= float(lineList[-1])
        
    
    # Close the association with the file 
    inFile.close()
    return d

def nationalHeatGraph(): 
    '''Creates a line graph of national heat (total avg heat of all states) over the years from 2003 to 2011
    '''
    d= nationalHeatDictionary() #creates national heat dictionary and assigns it to variable d
    x= [] #initializes list for x axis coordinates
    y= [] #^ likewise for the y axis coordinates

    for key in d.keys(): #for each key in the dictionary
        x.append(key) #you add that value to the list x
        y.append(d[key]) #you add the key to the list y so that x and y of the same index are corresponding key and value
        
    plt.plot( x, y, linewidth= 2.0) #line plot x and y for each index
    plt.xlabel("Year", fontdict=None, labelpad=None) #labels the x axis "year"
    plt.ylabel("Total Heat", fontdict=None, labelpad=None) #labels y axis 
    plt.title('National Heat from 2003 to 2011') #creates plot title
    plt.xticks(np.arange(2003, 2012, step= 1))
    plt.show() #shows the plot when it's finished

def nationalHeatTable():
    '''Creates a table of national heat by year
        >>> nationalHeatTable()
        Year         National Heat  
-----------------------------------------------------------------
        2003         1550.2999999999997
        2004         1511.2200000000007
        2005         1565.9499999999998
        2006            1568.88    
        2007         1553.0800000000004
        2008         1536.8299999999997
        2009         1534.8800000000006
        2010         1588.9200000000003
        2011         1594.2800000000002
    '''
    d= nationalHeatDictionary() #the dictionary to be printed
    
    print(' {0:^20s} {1:^14s} '.format('Year', 'National Heat'))
    print(65*'-')
    # print keys and values
    for key, value in d.items():
        print('{0:^20} {1:^14}' .format(key, value))

def stateDictionary(): #helper function to overcome problems with the way the data is formatted
    '''Creates a dictionary based on state codes to state names
        >>> stateDictionary()
        {'01': 'Alabama', '04': 'Arizona', '05': 'Arkansas', '06': 'California', '08': 'Colorado', '09': 'Connecticut', '10': 'Delaware', '11': 'District of Columbia', '12': 'Florida', '13': 'Georgia', '16': 'Idaho', '17': 'Illinois', '18': 'Indiana', '19': 'Iowa', '20': 'Kansas', '21': 'Kentucky', '22': 'Louisiana', '23': 'Maine', '24': 'Maryland', '25': 'Massachusetts', '26': 'Michigan', '27': 'Minnesota', '28': 'Mississippi', '29': 'Missouri', '30': 'Montana', '31': 'Nebraska', '32': 'Nevada', '33': 'New Hampshire', '34': 'New Jersey', '35': 'New Mexico', '36': 'New York', '37': 'North Carolina', '38': 'North Dakota', '39': 'Ohio', '40': 'Oklahoma', '41': 'Oregon', '42': 'Pennsylvania', '44': 'Rhode Island', '45': 'South Carolina', '46': 'South Dakota', '47': 'Tennessee', '48': 'Texas', '50': 'Vermont', '51': 'Virginia', '53': 'Washington', '54': 'West Virginia', '55': 'Wisconsin', '56': 'Wyoming'}

    '''
    d={} #initialized dictionary
    #Manually input state codes and their corresponding state names
    d["01"]= "Alabama"
    d["04"]= "Arizona"
    d["05"]= "Arkansas"
    d["06"]= "California"
    d["08"]= "Colorado"
    d["09"]= "Connecticut"
    d["10"]= "Delaware"
    d["11"]= "District of Columbia"
    d["12"]= "Florida"
    d["13"]= "Georgia"
    d["16"]= "Idaho"
    d["17"]= "Illinois"
    d["18"]= "Indiana"
    d["19"]= "Iowa"
    d["20"]= "Kansas"
    d["21"]= "Kentucky"
    d["22"]= "Louisiana"
    d["23"]= "Maine"
    d["24"]= "Maryland"
    d["25"]= "Massachusetts"
    d["26"]= "Michigan"
    d["27"]= "Minnesota"
    d["28"]= "Mississippi"
    d["29"]= "Missouri"
    d["30"]= "Montana"
    d["31"]= "Nebraska"
    d["32"]= "Nevada"
    d["33"]= "New Hampshire"
    d["34"]= "New Jersey"
    d["35"]= "New Mexico"
    d["36"]= "New York"
    d["37"]= "North Carolina"
    d["38"]= "North Dakota"
    d["39"]= "Ohio"
    d["40"]= "Oklahoma"
    d["41"]= "Oregon"
    d["42"]= "Pennsylvania"
    d["44"]= "Rhode Island"
    d["45"]= "South Carolina"
    d["46"]= "South Dakota"
    d["47"]= "Tennessee"
    d["48"]= "Texas"
    d["50"]= "Vermont"
    d["51"]= "Virginia"
    d["53"]= "Washington"
    d["54"]= "West Virginia"
    d["55"]= "Wisconsin"
    d["56"]= "Wyoming"
    
    return d #returns dictionary of state code to state name

def reverseStateDictionary():
    '''Creates the reverse of state dictionary
        >>> reverseStateDictionary()
        {'Alabama': '01', 'Arizona': '04', 'Arkansas': '05', 'California': '06', 'Colorado': '08', 'Connecticut': '09', 'Delaware': '10', 'District of Columbia': '11', 'Florida': '12', 'Georgia': '13', 'Idaho': '16', 'Illinois': '17', 'Indiana': '18', 'Iowa': '19', 'Kansas': '20', 'Kentucky': '21', 'Louisiana': '22', 'Maine': '23', 'Maryland': '24', 'Massachusetts': '25', 'Michigan': '26', 'Minnesota': '27', 'Mississippi': '28', 'Missouri': '29', 'Montana': '30', 'Nebraska': '31', 'Nevada': '32', 'New Hampshire': '33', 'New Jersey': '34', 'New Mexico': '35', 'New York': '36', 'North Carolina': '37', 'North Dakota': '38', 'Ohio': '39', 'Oklahoma': '40', 'Oregon': '41', 'Pennsylvania': '42', 'Rhode Island': '44', 'South Carolina': '45', 'South Dakota': '46', 'Tennessee': '47', 'Texas': '48', 'Vermont': '50', 'Virginia': '51', 'Washington': '53', 'West Virginia': '54', 'Wisconsin': '55', 'Wyoming': '56'}

    '''
    x= stateDictionary()
    d={} #initializes dictionary
    
    for key in x.keys(): #for every key in the state dictionary
        d[x[key]]= key #the value of the key is now the new key and the key is the new value

    return d
    

def nationalMatterDictionary():
    '''Creates a dictionary of total national matter by year
        nationalMatterDictionary()
        {2003: 582.53, 2004: 577.11, 2005: 600.0600000000001, 2006: 554.5499999999998, 2007: 564.7800000000001, 2008: 530.8400000000001, 2009: 589.5800000000002, 2010: 576.65, 2011: 562.68}

    '''
    
    # open the file to read ('r') and assign to file object inFile 
    inFile = open('Fine Particulate Matter (PM2.5) (µgm³) (2003-2011).txt', 'r') 
    d= {} #initialize dictionary

    inFile.readline() #reads the first line (the header) and skips over it
    while True:
        line= inFile.readline()
        if not line:
            break
        # Process the line of text from the file 
        # Create a list of all the items separated by white space 
        lineList = line.split() 
        # Add the third number to total after converting to int 
        if int(lineList[-2][1:-1]) in d.keys(): 
            d[int(lineList[-2][1:-1])]+= float(lineList[-1])
        else:
            d[int(lineList[-2][1:-1])]= float(lineList[-1])
        
    
    # Close the association with the file 
    inFile.close()
    return d

def nationalMatterTable():
    '''Creates a table of national heat by year
        >>> nationalMatterTable()
        Year         National Matter 
-----------------------------------------------------------------
        2003             582.53    
        2004             577.11    
        2005         600.0600000000001
        2006         554.5499999999998
        2007         564.7800000000001
        2008         530.8400000000001
        2009         589.5800000000002
        2010             576.65    
        2011             562.68    
    '''
    d= nationalMatterDictionary() #the dictionary to be printed
    
    print(' {0:^20s} {1:^14s} '.format('Year', 'National Matter'))
    print(65*'-')
    # print keys and values
    for key, value in d.items():
        print('{0:^20} {1:^14}' .format(key, value))
        
def nationalMatterGraph(): 
    '''Creates a line graph of national heat (total avg heat of all states) over the years from 2003 to 2011
    '''
    d= nationalMatterDictionary() #creates national heat dictionary and assigns it to variable d
    x= [] #initializes list for x axis coordinates
    y= [] #^ likewise for the y axis coordinates

    for key in d.keys(): #for each key in the dictionary
        x.append(key) #you add that value to the list x
        y.append(d[key]) #you add the key to the list y so that x and y of the same index are corresponding key and value
        
    plt.plot( x, y, linewidth= 2.0) #line plot x and y for each index
    plt.xlabel("Year", fontdict=None, labelpad=None) #labels the x axis "year"
    plt.ylabel("Total Matter", fontdict=None, labelpad=None) #labels y axis 
    plt.title('National Heat from 2003 to 2011') #creates plot title
        
    plt.show() #shows the plot when it's finished

def graphMatterAndHeat():
    '''Makes a double line plot of national matter and national heat from 2003 to 2011
    '''
    d1= nationalMatterDictionary()
    x1= []
    y1= []
    
    for key in d1.keys(): #for each key in the dictionary
        x1.append(key) #you add that value to the list x
        y1.append(d1[key]) #you add the key to the list y so that x and y of the same index are corresponding key and value

    d2= nationalHeatDictionary()
    x2= []
    y2= []

    for key in d2.keys(): #for each key in the dictionary
            x2.append(key) #you add that value to the list x
            y2.append(d2[key]) #you add the key to the list y so that x and y of the same index are corresponding key and value
            
    t = np.arange(len(x1))
    
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Matter (PM2.5) (µgm³)', color=color)
    ax1.plot(x1, y1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Heat', color=color)  # we already handled the x-label with ax1
    ax2.plot(x2, y2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

    

def main():
    '''Creates a main menu for this analysis
    '''
    while True:
        
        print('''

    (1) print a table with the year and national heat from 2001 to 2011

    (2) plot the yearly national heat from 2001 to 2011

    (3) print a table with the national matter from 2003 to 2011

    (4) plot the yearly national matter from 2003 to 2011

    (5) draw a bar plot showing the five states with the highest unintended overdose death rate for 1999 and 2017.

    (9) Quit 
    ''')
        method= int(input("Please input the number(integer) associated with the function you want "))

        if method== 1:
            nationalHeatTable()
        if method== 2:
            nationalHeatGraph()
        if method== 3:
            nationalMatterTable()
        if method== 4:
            nationalMatterGraph()
        if method== 5:
            graphMatterAndHeat()
        if method== 9:
            break

    print("Thanks for checking my project. Bye!")
            
            
main()

import doctest
doctest.testmod()


