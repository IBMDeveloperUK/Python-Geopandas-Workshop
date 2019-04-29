fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,5))

street['Crime type'].groupby(street['Crime type']).count().plot.bar(ax=ax1);

street['Crime type'].groupby(street['Month']).count().plot(ax=ax2);
