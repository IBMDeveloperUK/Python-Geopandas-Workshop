fig, axs = plt.subplots(1, 2, figsize=(20,5))

p1=boroughs4.plot(column='Controlled drugs',ax=axs[0],cmap='Blues',legend=True);
p2=boroughs4.plot(column='Stolen goods',ax=axs[1], cmap='Reds',legend=True);

axs[0].set_title('Controlled drugs', fontdict={'fontsize': '12', 'fontweight' : '5'});
axs[1].set_title('Stolen goods', fontdict={'fontsize': '12', 'fontweight' : '5'});
