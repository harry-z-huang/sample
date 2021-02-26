'''Harry Huang
'''
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import OrderedDict

def readOverdoseFile(): #required by project
    ''' Reads the overdose file and returns the data
    ''' 
    # open the file to read ('r') and assign to file object inFile 
    file = open("overdose_X40_X44_1999_2017.csv", newline= '')
    reader= csv.reader(file)
    for i in range(5): #skips first 5 lines
        next(reader) #skip function
    data= [row for row in reader] #for row in the data
    #print(data[0]) #confirm that the data is presented correctly
    #print(data[0][3]) #should be the year of the first line
    #print(data[0][7]) #should be the deaths of the first line
    return data #returns a properly processed version of the data

def createOverdoseDictionary(): #required by project
    ''' create a Python dictionary with the year as the key and
        the total of unintended overdose deaths for that year as the value
    '''
    data= readOverdoseFile() #assigns the overdose file to variable "data"
    
    d= {} #initializes empty dictionary
    years= [] #intializes 
    deaths= [] #intializes
    #year is line[3] and deaths is line[7]
    
    for line in data: #for each line in the data
        if int(line[3]) in d.keys(): #if the dictionary key already exists
            d[int(line[3])]= d[int(line[3])] + int(line[7]) #then you add the value onto the existing value
        else: #if the key doesn't exist in the dictionary
            d[int(line[3])]= int(line[7]) #then we add it in
    return d #returns the dictionary

def graphOverdoseByYear(): #required by project
    ''' plots the yearly total of
        unintended overdose deaths as a function of year using Matplotlib
    '''
    d = createOverdoseDictionary() #creates overdose dictionary and assigns dictionary to value "d"
    x=[]
    y=[]
    for key in d.keys(): #for each key in the dictionary
        x.append(key) #you add that key to the list x
        y.append(d[key]) #you add the key value to the list y so that x and y of the same index are corresponding key and value
    plt.plot( x, y, linewidth= 2.0) #scatter plot x and y for each index
    
    plt.xlabel("Year", fontdict=None, labelpad=None) #labels the x axis "year"
    plt.ylabel("Overdose deaths", fontdict=None, labelpad=None) #labels y axis
    plt.xticks(np.arange(1999, 2018, step= 2))
    plt.title('Unintended Overdose Deaths By Year') #creates plot title
    plt.show() #shows the plot when it's finished

def readStateFiles(year): #required by project
    ''' Takes integer input "year" and reads different census files based on the year
    '''
    if int(year)<= 2005: #if the year is 2005 or less, we use one file
        file = open("census2000_state_pop.csv", newline= '') #opens the file, delimits a newline with white space, and assigns it to the variable "file"
        reader= csv.reader(file) #applies csv.reader() method to the file
        next(reader) #reads the first line and skips it
    elif int(year)>= 2006: #if the year is 2006 or greater, we use the other file
        file = open("census2010_state_pop.csv", newline= '')
        reader= csv.reader(file)
        next(reader)
    data= [row for row in reader]

    return data

def createCensusDictionary(year): #helper function that wasn't needed
    '''Creates a dicitonary that has states as keys and total population as the year
        >>> createCensusDictionary(1999)
        {'Alabama': '4447100', 'Alaska': '626932', 'Arizona': '5130632', 'Arkansas': '2673400', 'California': '33871648', 'Colorado': '4301261', 'Connecticut': '3405565', 'Delaware': '783600', 'District of Columbia': '572059', 'Florida': '15982378', 'Georgia': '8186453', 'Hawaii': '1211537', 'Idaho': '1293953', 'Illinois': '12419293', 'Indiana': '6080485', 'Iowa': '2926324', 'Kansas': '2688418', 'Kentucky': '4041769', 'Louisiana': '4468976', 'Maine': '1274923', 'Maryland': '5296486', 'Massachusetts': '6349097', 'Michigan': '9938444', 'Minnesota': '4919479', 'Mississippi': '2844658', 'Missouri': '5595211', 'Montana': '902195', 'Nebraska': '1711263', 'Nevada': '1998257', 'New Hampshire': '1235786', 'New Jersey': '8414350', 'New Mexico': '1819046', 'New York': '18976457', 'North Carolina': '8049313', 'North Dakota': '642200', 'Ohio': '11353140', 'Oklahoma': '3450654', 'Oregon': '3421399', 'Pennsylvania': '12281054', 'Rhode Island': '1048319', 'South Carolina': '4012012', 'South Dakota': '754844', 'Tennessee': '5689283', 'Texas': '20851820', 'Utah': '2233169', 'Vermont': '608827', 'Virginia': '7078515', 'Washington': '5894121', 'West Virginia': '1808344', 'Wisconsin': '5363675', 'Wyoming': '493782'}

    '''

    #use two separate returns to return different dictionaries based on year input
    if int(year)<= 2005: #if the year ==2005
        data= readStateFiles(2005)
        d2005= {}
        
        for line in data:
            d2005[line[0]]= line[1] 
            
        return d2005
    
    elif int(year)>= 2006:
        data= readStateFiles(2006)
        d2006= {}

        for line in data:
            d2006[line[0]]= line[1]
            
        return d2006
        
        
    
def statePop(state, year): #helper function that wasn't needed
    ''' Takes a capitalized state name as a string and the year input and finds the rate of unintended overdose deaths
        of the specified state at the specified eyar
    '''
    censusData2005= createCensusDictionary(2005) #if the year is 2005 or before
    censusData2006= createCensusDictionary(2006) #if the year is 2006 or after
    overdoseData= readOverdoseFile()
    
    #census data has capitalized state names
    
    if int(year)<= 2005: #if year is 2005 or below
        totalPop= censusData2005[state] #use the proper census data
    elif int(year)>= 2006:
        totalPop= censusData2006[state]
    return totalPop
    
def createOverdoseDeathsDictionary(year): #helper function 
    ''' Creates a dictionary with states as keys and the number
        of overdose deaths in that state as the value in the specified year
        >>> createOverdoseDeathsDictionary(1999)
        {'Alabama': 78, 'Alaska': 12, 'Arizona': 102, 'Arkansas': 36, 'California': 327, 'Colorado': 69, 'Connecticut': 93, 'Delaware': 24, 'District of Columbia': 26, 'Florida': 415, 'Georgia': 128, 'Hawaii': 13, 'Idaho': 10, 'Illinois': 211, 'Indiana': 110, 'Iowa': 17, 'Kansas': 28, 'Kentucky': 124, 'Louisiana': 111, 'Maine': 41, 'Maryland': 86, 'Massachusetts': 192, 'Michigan': 188, 'Minnesota': 50, 'Mississippi': 27, 'Missouri': 113, 'Montana': 11, 'Nebraska': 16, 'Nevada': 38, 'New Hampshire': 36, 'New Jersey': 243, 'New Mexico': 37, 'New York': 263, 'North Carolina': 185, 'North Dakota': 0, 'Ohio': 317, 'Oklahoma': 52, 'Oregon': 29, 'Pennsylvania': 376, 'Rhode Island': 30, 'South Carolina': 67, 'South Dakota': 0, 'Tennessee': 159, 'Texas': 224, 'Utah': 46, 'Vermont': 11, 'Virginia': 128, 'Washington': 93, 'West Virginia': 79, 'Wisconsin': 87, 'Wyoming': 11}

    '''
    d= {} #initializes a dictionary
    data1= readOverdoseFile() #reads overdose file csv data
    data2= readStateFiles(year)

    for line in data2:
        d[line[0]]= int(0)

    for line in data1:
        if line[3]== year and line[1] in d.keys():
            d[line[1]]= d[line[1]] + int(line[7])
        else:
            d[line[1]]= int(line[7])

    return d

def createOverdoseRateDictionary(year): #required by project
    ''' creates a Python dictionary with the location (state or District of
        Columbia) as the key and rate of unintended overdose deaths
        (as deaths per 100,000 residents) in 1999 as the value.
        >>> createOverdoseRateDictionary(1999)
        {'Alabama': 1.7539520136718312, 'Alaska': 1.914083186055266, 'Arizona': 1.9880591708779738, 'Arkansas': 1.3465998354155755, 'California': 0.965409182334441, 'Colorado': 1.604180727465736, 'Connecticut': 2.7308244006501123, 'Delaware': 3.0627871362940273, 'District of Columbia': 4.5449857444774056, 'Florida': 2.596609841163812, 'Georgia': 1.563558723173516, 'Hawaii': 1.0730171674492814, 'Idaho': 0.772825597220301, 'Illinois': 1.698969498505269, 'Indiana': 1.8090662175796832, 'Iowa': 0.5809336218409171, 'Kansas': 1.0415047064853753, 'Kentucky': 3.0679635575412645, 'Louisiana': 2.4837904701211193, 'Maine': 3.215880488468715, 'Maryland': 1.6237180651473448, 'Massachusetts': 3.024052081736978, 'Michigan': 1.891644205068721, 'Minnesota': 1.0163677901663977, 'Mississippi': 0.9491474897861184, 'Missouri': 2.0195842480292523, 'Montana': 1.2192486103336861, 'Nebraska': 0.9349819402394606, 'Nevada': 1.9016572943320105, 'New Hampshire': 2.9131257353619477, 'New Jersey': 2.887923606695704, 'New Mexico': 2.0340332240086285, 'New York': 1.3859278367927164, 'North Carolina': 2.2983327893945735, 'North Dakota': 0.0, 'Ohio': 2.792179079972589, 'Oklahoma': 1.506960709477102, 'Oregon': 0.8476064907951396, 'Pennsylvania': 3.0616264695196356, 'Rhode Island': 2.8617243415410765, 'South Carolina': 1.6699850349400749, 'South Dakota': 0.0, 'Tennessee': 2.7947282636493913, 'Texas': 1.0742467563982425, 'Utah': 2.0598530608297, 'Vermont': 1.806752985659309, 'Virginia': 1.8082888854512564, 'Washington': 1.5778434138016508, 'West Virginia': 4.368637825546467, 'Wisconsin': 1.6220222142467617, 'Wyoming': 2.2277037235055146}

    '''

    data= readStateFiles(year) #reads different census files by year
    d= {}

    for line in data: #where line[0] is a unique state and line[1] is the total state population
        state= line[0]
        totalPop= int(line[1])
        overdoseDeaths= createOverdoseDeathsDictionary(year)
        
        d[state]= overdoseDeaths[state] / (totalPop/ 100000)

    return d

def printOverdoseRateTable(year): #required by project
    ''' prints a table with the location and unintended overdose
        death rate for that location in a specific year.
    '''
    
    d= createOverdoseRateDictionary(year) #the dictionary to be printed
    
    print(' {0:^20s} {1:^14s} '.format('Year', 'Overdose Death Rate (per 100,000 people)'))
    print(65*'-')
    # print keys and values
    for key, value in d.items(): #print the key and value for each item in the dictionary
        print('{0:^20} {1:^14}' .format(key, value))


def sortDictionary(dictionary):
    '''Takes an input dictionary and sorts it based on the values of the dictionary
    '''
    return OrderedDict(sorted(dictionary.items(), key = lambda t: t[1], reverse = True)) #sorts high to low

def fiveHighestStates(year):
    ''' Takes input year and identifies the five states with the higher overdose death rates for an input year
    '''

    states= list(sortDictionary(createOverdoseRateDictionary(year))) #sorts it high to low
    highestStates= states[:5] #five first states since its ordered from hight to low

    return highestStates

def barChartFiveHighestStates(year):
    ''' creates a barchart of the 5 states with the highest rates of overdose and their
        overdose rates
    '''

    states= fiveHighestStates(year)
    rates= []
    rateDictionary= createOverdoseRateDictionary(year)
    for state in states: #for each state in the 5 states, you add the corresponding value onto the list
        rates.append(rateDictionary[state]) 
    
    y_pos = np.arange(len(states))
 
    plt.bar(y_pos, rates, align='center', alpha=0.5)
    plt.xticks(y_pos, states)
    plt.ylabel('Rate (number of overdose deaths (per 100,000 residents) ')
    plt.title('Five states with highest unintended overdose death rates for '+ str(year))
 
    plt.show()

def overdoseDeathTable():
    '''Creates a table with the year and yearly total of unintended overdose deaths for the US in the years 1999 to 2017
        >>> overdoseDeathTable()
         Year         Unintended Overdose Deaths 
-----------------------------------------------------------------
        1999             10126     
        2000             10705     
        2001             12043     
        2002             15402     
        2003             17354     
        2004             19000     
        2005             21660     
        2006             25623     
        2007             26882     
        2008             27439     
        2009             28054     
        2010             29321     
        2011             32442     
        2012             32562     
        2013             35114     
        2014             38139     
        2015             43617     
        2016             54400     
        2017             60990     
    '''
    d= createOverdoseDictionary()
    
    print(' {0:^20s} {1:^14s} '.format('Year', 'Unintended Overdose Deaths'))
    print(65*'-')
    # print keys and values
    for key, value in d.items():
        print('{0:^20} {1:^14}' .format(key, value))
    
def doubleBarGraph():
    '''Creates a double bar graph using the values from two dictionaries which are
    in this case the five highest states from 1999 and 2017
    '''
    states1999= fiveHighestStates(1999)
    rate1999= []
    rateDictionary1999= createOverdoseRateDictionary(1999)
    for state in states1999:
        rate1999.append(rateDictionary1999[state])
        
    states2017= fiveHighestStates(2017)
    rate2017=[]
    rateDictionary2017= createOverdoseRateDictionary(2017)
    for state in states2017:
        rate2017.append(rateDictionary2017[state])
    '''
    #now that both rate lists are complete, we can go ahead and graph
    y_pos1 = np.arange(len(states1999))
    #y_pos2 = np.arange(len(states1999)+.4)
    X= np.arange(5)
    plt.bar(X+0, rate1999, color= 'g', width=.4, label= "1999")
    plt.bar(X+.4, rate2017, color= 'b', width=.4, label= "2017")
    plt.xticks(y_pos1, states1999, rotation= 'vertical')
    #plt.xticks(y_pos2, states2017)
    plt.legend()
    plt.show()
    '''

    d1label = states1999
    data1 = rate1999
    d2label = states2017
    data2 = rate2017

    width = 0.3

    data = np.concatenate([data1, data2])
    labels = np.concatenate([d1label, d2label])
    colors = np.repeat(["r", "g"], [len(data1), len(data2)])
    idx = np.arange(len(data1))
    x = np.concatenate([idx, idx+width])
    plt.bar(x, data, width=0.3, color=colors)
    ax = plt.gca()
    ax.set_xticks(x + width*0)
    ax.set_xticklabels(labels, rotation= 'vertical');
    plt.ylabel('Number of Unintended Overdose Deaths(per 100,000 residents)')
    plt.xlabel('Five States with Highest Unintended Overdose Death Rate')
    plt.title('Five states with Highest Unintended Overdose Death Rates for 1999 and 2017')
 
    plt.legend()
    plt.show()

    
def main():
    '''Creates a main menu
    '''
    while True:
        
        print('''

    (1) print a table with the year and the yearly total of unintended overdose deaths for the United States for the years 1999 to 2017.

    (2) plot the yearly total of unintended overdose deaths in the United States as a function of year for the years 1999 to 2017.

    (3) print a table with the unintended overdose death rate for 1999 for each location

    (4) print a table with the unintended overdose death rate for 2017 for each location

    (5) draw a bar plot showing the five states with the highest unintended overdose death rate for 1999 and 2017.

    (9) Quit 
    ''')
        method= int(input("Please input the number(integer) associated with the function you want"))

        if method== 1:
            overdoseDeathTable()
        if method== 2:
            graphOverdoseByYear()
        if method== 3:
            printOverdoseRateTable(1999)
        if method== 4:
            printOverdoseRateTable(2017)
        if method== 5:
            doubleBarGraph()
            #barChartFiveHighestStates(1999)
            #barChartFiveHighestStates(2017)
        if method== 9:
            break

    print("Thanks for checking my project. Bye!")
            
            
main()
            
import doctest
doctest.testmod()
    
        



          
           
    

    


    

    

    
    

    
    

    

    
    
    
    


    
    
        
        
        
    
    
    
    
    
    
