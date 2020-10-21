hotels2 = gpd.sjoin(boroughs,hotels) 
hotels3 = pd.pivot_table(hotels2,index='name_left',columns='fclass',aggfunc={'fclass':'count'})
hotels3.columns = hotels3.columns.droplevel()
hotels3 = hotels3.reset_index()

boroughs = boroughs.merge(hotels3, left_on='name',right_on='name_left')
boroughs = boroughs.drop(columns='name_left')

[fig,ax] = plt.subplots(1, figsize=(12, 8))

boroughs.plot(column='hotel',cmap='Blues', edgecolor='black', linewidth=0.5, 
              legend=True, ax=ax, scheme='quantiles');
ax.axis('off');
ax.set_title('Hotels in London');
