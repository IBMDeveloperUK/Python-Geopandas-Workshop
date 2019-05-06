
dfsjoin2 = gpd.sjoin(boroughs2,stop_search[stop_search['Outcome'] == 'Arrest']) 
dfpivot2 = pd.pivot_table(dfsjoin2,index='code',columns='Object of search',aggfunc={'Object of search':'count'})
dfpivot2.columns = dfpivot2.columns.droplevel()
dfpivot2 = dfpivot2.reset_index()
boroughs4 = boroughs2.merge(dfpivot2, how='left',on='code')
boroughs4.head()
