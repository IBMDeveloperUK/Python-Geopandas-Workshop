[fig, ax] = plt.subplots(1, figsize=(10, 6))
boroughs2.plot(column='id', cmap='Paired', linewidth=0.5, edgecolor='black', legend=False, ax=ax);
ax.axis('off');
