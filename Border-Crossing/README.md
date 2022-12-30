Hello,

a3.ipynb 
File consists of Formating the data and answers below are few questions

1. Measure Types 
Find all of the possible values for the measure in the dataset. List each type only once!

2. Largest Pedestrian Crossing
Code to find the port in the dataset with the largest monthly count for pedestrians. Outputing the Port Name and State of the port. Here i needed to iterate through each element of the list, and each element is a dictionary which has various keys including Measure and Value.

3a. Duplicate Port Name 
There are two ports with the same Port Name. What is the name of the port, and what are the two states and port codes that share this name?

3b. Number of Ports Per State (15 pts)
Code to find the number of ports per state. Note that this is not the same as counting the number of entries in the dataset for each state. Consider using a two-step process: first, find all of the unique ports with their states, and then use that result to count the number of ports in each state.

4. Reformat the Data
The format of the data is not ideal for some types of questions, specifically those where we would like to understand all quantities for each port during a given month. Created a new list of dictionaries named new_data where each dictionary contains the five keys that are the same for each monthly entry (Port Name, State, Port Code, Border, and Date) along with their values, and then adds each Measure-Value pair as a key-value pair. For example, the entry for “Pinecreek” in “Jul 2022”  looks like:

 {'Port Name': 'Pinecreek',
  'State': 'Minnesota',
  'Port Code': 3425,
  'Border': 'Canada',
  'Date': 'Jul 2022',
  'Trucks': 6,
  'Personal Vehicles': 155,
  'Personal Vehicle Passengers': 273})
Here the port name is not unique.

5. Compute and Add Total Number of Persons 
Code to update the new_data list of dictionaries created in Part 4 to added a key-value pair named Total People whose value is the sum of the values in that port-month that count people. The fields that count people are:

{'Bus Passengers', 'Pedestrians', 'Personal Vehicle Passengers', 'Train Passengers'}
Each port may not have one (or any) of these fields! For example, for the port “San Ysidro” in “Jul 2022”, we have 24_371 bus passengers, 2_206_115 personal vehicle passengers, and 627_673 pedestrians so the updated data looks like:

{'Port Name': 'San Ysidro',
 'State': 'California',
 'Port Code': 2504,
 'Border': 'Mexico',
 'Date': 'Jul 2022',
 'Bus Passengers': 24371,
 'Personal Vehicles': 1328690,
 'Personal Vehicle Passengers': 2206115,
 'Buses': 969,
 'Pedestrians': 627673,
 'Total People': 2858159}
Made sure that if a port has zero people, there is still a total entry with a value of zero.

6.Filter by Transportation Mode
Function count_by_mode that, given a string corresponding to a mode, returns a count of the number of ports that have handled traffic corresponding to the specified mode of transportation. This means that a port should have an entry for the specified mode and its value should be greater than zero. For example, if we run count_by_mode('Trains'), the method should return 35 and count_by_mode('Personal Vehicles') should return 114.

__________________________________________________________________________________________________________________________________________________________
a5


folder consists of 
init.py,
Port entries 
|_> util.py
|_> find.py
|_> compare.py

util.py>>>>>>>>>>>>>>>>>>
The download_data method downloads the border-crossing.json datafile and store it locally is a file named border_crossing.json. The parse_data method parses the json data (list of dictionaries) into a new data structure that organizes data by port. It creates a dictionary that looks like:

{<port_code>: {
  name: <port_name>,
  border: <border>
  state: <state>,
  monthly_data: { <date>: {<measure>: <value>, ...}, ...}
  },
  ...
}

In other words, port codes are keys in a dictionary that includes data about the port and a monthly data dictionary that whose keys are dates and whose values are dictionaries that contain Measure-Value key-value pairs (similar to Part 4 of a3). The get_data method load the data from the json file, parse it using the parse_data, stores it in a local module variable, and return that value. The get_data method loads and parses the file from disk once, otherwise returns the pre-loaded data. The parse_data method parses the port entry data as specified before.


Used the json module to load the data from the file. The download_data method downloads the file just once and return the local filename, otherwise returning the local filename. Refer to the a3 starter notebook for code that can be used to download data. 

find.py>>>>>>>>>>>>>>>>>>

Created a find.py module that has two functions, port_by_state and port_by_name. Both functions returns the ports that match the given name and/or state. port_by_state should take one parameter, the state name, while port_by_name takes two parameters, the port name and the state. However, the state is optional so if the user does not provide the state, the function should search across all states. Each function should return a list of tuples of the form (<port_code>, <port_name>, <state>). For example,

>>> port_entries.find.ports_by_state('Idaho')
[(3302, 'Eastport', 'Idaho'), (3308, 'Porthill', 'Idaho')]

>>> port_entries.find.ports_by_name('Eastport')
[(3302, 'Eastport', 'Idaho'), (103, 'Eastport', 'Maine')]

>>> port_entries.find.ports_by_name('Eastport', state='Idaho')
[(3302, 'Eastport', 'Idaho')]


comapre.py>>>>>>>>>>>>>>>>>>

Created a compare.py module that calculates comparative information between two ports for a given date. Given a port code and two date strings as parameters, the diff_dates function returns the difference in values for each measure between the two months. Given two port codes and a date string as parameters, the diff_ports function returns the difference between ports in values for each measure. When one date/port does not have a value for the given measure, assumes its value is zero (0).

Examples:

>>> port_entries.compare.diff_dates(3302, "Jul 2021", "Aug 2021")
{'Trucks': -129,
 'Train Passengers': -10,
 'Truck Containers Loaded': -335,
 'Trains': 4,
 'Personal Vehicle Passengers': -2043,
 'Truck Containers Empty': 186,
 'Personal Vehicles': -1018,
 'Rail Containers Empty': -101,
 'Rail Containers Loaded': 723}

>>> port_entries.compare.diff_ports(2604, 2608, "Jul 2021")
{'Train Passengers': 416,
 'Truck Containers Loaded': 11083,
 'Truck Containers Empty': 6064,
 'Rail Containers Loaded': 2427,
 'Bus Passengers': 21793,
 'Trucks': 17073,
 'Buses': 455,
 'Personal Vehicle Passengers': 3663,
 'Trains': 49,
 'Personal Vehicles': -25822,
 'Rail Containers Empty': 2567,
 'Pedestrians': 2971}
 
 test.ipynb file has all the output
 __________________________________________________________________________________________________________________________________________________________

a8

Most Bus Passengers
Loads the dataset. Compute the month, port of entry, and number of passengers when the most Bus Passengers crossed the border. In this case, the month is the Date column of the dataset which includes a month and a year.

Number of Ports per State
Redone Part 3b of a3 with pandas. In order words, count the number of ports for each state. Make sure that you count each unique port only once. You solution should be a Series with the states as labels and the counts as values.

Line Chart
Using matplotlib directly or via pandas, created a line chart visualization with two lines showing “Personal Vehicles” crossing over the months, one for crossings from Canada and the other from Mexico. Used split-apply-combine again, but this time to sum the crossings for all of the ports of entry for each month. The lines are different colors, and includes a legend that indicates the values being shown by each line.

<img width="556" alt="image" src="https://user-images.githubusercontent.com/112876951/210037690-546f5673-a664-4d7b-9efd-afacfc0efc0a.png">


Stacked Bar Chart
Using matplotlib directly or via pandas’ plotting routines, created a visualization showing the average number of people crossing monthly for the four ports of entry in the state of Alaska using different modes of transportation. The modes we to examine are: Pedestrians, Train Passengers, Bus Passengers, and Personal Vehicle Passengers. Filtered the data to these ports and measures and then grouping by port, computing the mean over the months. After the groupby, you can transform the data frame so that its rows are ports and its columns are the four modes of transportation. That data frame can be used directly by the pandas plot method. Displays a legend.

<img width="599" alt="image" src="https://user-images.githubusercontent.com/112876951/210037846-3184ec70-c858-4822-8187-2ba409319efc.png">
















































