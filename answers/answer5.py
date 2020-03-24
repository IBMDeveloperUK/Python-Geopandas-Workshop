fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,5))

stop_search['Object of search'].groupby(stop_search['Object of search']).count().plot.bar(ax=ax1);

stop_search['Outcome'].groupby(stop_search['Outcome']).count().plot.bar(ax=ax2);

stop_search['Month'] = stop_search.Date.dt.to_period("M")
stop_search['Object of search'].groupby(stop_search['Month']).count().plot(ax=ax3);
