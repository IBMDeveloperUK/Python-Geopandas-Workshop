[fig, ax] = plt.subplots(1, figsize=(10, 6))
msoa.plot(column='HHOLDS', cmap='Blues', linewidth=0.5, edgecolor='black', legend=True, ax=ax);
ax.axis('off');
ax.set_title('Number of households', fontdict={'fontsize': '20', 'fontweight' : '3'});
