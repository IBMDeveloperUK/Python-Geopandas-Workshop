boroughs['paygap'] = \
    ((boroughs['Gross_Annual_Pay_-_Male_(2016)'] - boroughs['Gross_Annual_Pay_-_Female_(2016)'])/ \
    boroughs['Gross_Annual_Pay_-_Male_(2016)']) * 100

[fig,ax] = plt.subplots(1, figsize=(12, 8))

boroughs.plot(ax=ax, color="lightgrey", edgecolor='black', linewidth=0.5)

boroughs.dropna().plot(column='paygap', cmap='Reds', edgecolor='black', linewidth=0.5,
               legend=True, ax=ax, scheme='equal_interval');
ax.axis('off');
ax.set_title('Gender pay gap in London (2016)');
