msoa = boroughs.dissolve(by='MSOA11NM',aggfunc='sum')
msoa.head()
