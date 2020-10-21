hotels = pois[pois['fclass']=='hotel']
citylondon = boroughs.loc[boroughs['name'] == 'City of London', 'geometry'].squeeze()
cityhotels = hotels[hotels.within(citylondon)]

[fig,ax] = plt.subplots(1, figsize=(12, 8))
base = boroughs.plot(color='lightblue', edgecolor='black',ax=ax);
cityhotels.plot(ax=ax, marker='o', color='red', markersize=8);
ax.axis('off');
