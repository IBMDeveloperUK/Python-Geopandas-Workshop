# number of data points
print ('rows in street: '+str(len(street)))

# columns 
print ('Columns: '+str(street.columns))

# categories
print ('Crime type: '+str(street['Crime type'].unique()))
print ('Last outcome category: '+str(street['Last outcome category'].unique()))
print (street['Context'].unique())

# delete columns
street = street.drop(columns=['Unnamed: 0','Latitude', 'Longitude','Context'])

# convert Date to datetime
street['Month'] = street['Month'].apply(lambda x: datetime.strptime(x, "%Y-%m"))

street.head()
