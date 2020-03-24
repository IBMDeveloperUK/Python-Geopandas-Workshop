bystreet = street.groupby(['Location','Crime type']).count()
bystreet = bystreet.drop(columns=['Month', 'Last outcome category','coordinates','LSOA code'])
bystreet = bystreet.rename(index=str, columns={"Crime ID": "Number of crimes"})

bystreet.sort_values(by=['Number of crimes'], ascending=False).head()
