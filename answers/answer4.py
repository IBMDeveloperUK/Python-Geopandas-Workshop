# number of data points
print ('rows in stop_search: '+str(len(stop_search)))

# columns 
print ('Columns: '+str(stop_search.columns))

# categories
print ('Policing operation: '+str(stop_search['Policing operation'].unique()))
print ('Legislation: '+str(stop_search['Legislation'].unique()))
print ('Object of search: '+str(stop_search['Object of search'].unique()))
print ('Outcome: '+str(stop_search['Outcome'].unique()))
print ('Outcome linked to object of search: '+str(stop_search['Outcome linked to object of search'].unique()))

# delete columns
stop_search = stop_search.drop(columns=['Unnamed: 0','Latitude', 'Longitude', 'Part of a policing operation', 'Policing operation', 'Outcome linked to object of search'])

# convert Date to datetime
stop_search['Date'] = stop_search['Date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S+00:00"))

stop_search.head()
