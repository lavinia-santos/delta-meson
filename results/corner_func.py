import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import corner
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms
from types import MethodType
from scipy.interpolate import interp1d
import os
# font = {'family' : 'normal',
#         'weight' : 'bold',
#         'size'   : 26}

# plt.rc('font', **font)

#we can try to get the titles at the neighboors later
def get_neighbor_transform(text, direction="top", npad=0):
    """
    Determines the transform for the _next_ Text plotted with
    set_title_artist. For alignment purposes, requires rendering
    the text and getting its extent.
    """
    text.draw(text.figure.canvas.get_renderer())
    ex = text.get_window_extent()

    if direction == "up":
        x = 0
        y = ex.height + npad
    elif direction == "down":
        x = 0
        y = -ex.height - npad
    elif direction == "right":
        halign = text.get_horizontalalignment()
        if halign == "left":
            x = ex.width + npad
        elif halign == "center":
            x = ex.width / 2 + npad
        elif halign == "right":
            x = 0
        y = 0
    elif direction == "left":
        halign = text.get_horizontalalignment()
        if halign == "left":
            x = 0
        elif halign == "center":
            x = -ex.width / 2 - npad
        elif halign == "right":
            x = -ex.width - npad
        y = 0
    else:
        raise ValueError("loc must be top, bottom, or right")

    return mtransforms.offset_copy(
        text.get_transform(), x=x, y=y,
        fig=text.figure, units='points'
    )
LOC_ATTR = {
    "center": "title",
    "right": "_right_title",
    "left": "_left_title"
}

def set_title_neighbor(ax, label, loc="center", **kwargs):
    """
    corner.py is inflexible and only outputs the medians and quartiles
    through calling Axes.set_title. We monkey patch in the collation
    behavior using this method, deferring to the original implementation
    whern the user hasn't called init_neighbor_title on that axis and
    title loc.
    """
    neighbor_entry = ax._neighbor_titles.get(loc, None)
    if neighbor_entry is None:
        return ax._orig_set_title(label, loc=loc, **kwargs)

    neighbor_artists = neighbor_entry["artists"]
    direction = neighbor_entry["direction"]
    if not neighbor_artists:
        text = ax._orig_set_title(label, loc=loc, **kwargs)
        neighbor_artists.append(text)
    else:
        base_title = ax.__getattribute__(LOC_ATTR[loc])
        kwargs.pop("horizontalignment", None)
        kwargs.pop("verticalalignment", None)
        if direction == "up" or direction == "down":
            halign = base_title.get_horizontalalignment()
        elif direction == "right":
            halign = "left"
        elif direction == "left":
            halign = "right"
        else:
            raise ValueError("direction must be up, down, right or left")

        text = ax.text(
            *base_title.get_position(), label,
            transform=neighbor_entry["next_transform"],
            horizontalalignment=halign,
            verticalalignment=base_title.get_verticalalignment(),
            fontproperties=base_title.get_fontproperties(),
            **kwargs
        )
        neighbor_artists.append(text)

    neighbor_entry["next_transform"] = get_neighbor_transform(
        text,
        direction=direction,
        npad=neighbor_entry["npad"]
    )



eos_number=[8,20,21]


#colors=['deepskyblue','deeppink','darkviolet']
for i in eos_number:


    props=f"EOS{i}/props.dat"
    #couplings="../../../../../../../../Downloads/para_eos21.csv"
    corner_plot="corner.dat"
    with open( props, 'r') as r, open(corner_plot, 'w') as o: 
        for line in r: 
            #strip() function 
            if line.strip(): 
                o.write(line) 
    
    df_props=pd.read_csv(corner_plot, sep=",", header=None, skip_blank_lines=True, on_bad_lines='skip')
    df_props=df_props.rename(columns={df_props.columns[1]: 'grho',df_props.columns[2]: 'gdel',df_props.columns[3]: 'gwr',df_props.columns[5]: 'm_eff', df_props.columns[6]: 'EB', df_props.columns[9]: 'Esym', df_props.columns[10]: 'L', df_props.columns[11]: 'Ksym', df_props.columns[12]: 'Qsym'})
    #df_props=df_props.rename(columns={df_props.columns[0]: 'label', df_props.columns[1]: 'gr', df_props.columns[2]: 'gdel', df_props.columns[3]: 'lambda'})
    #print(df)
    df_props=df_props[df_props['L'] < 200]
    df_props=df_props[df_props['L'] > 0]
    df_props=df_props[df_props['Ksym'] > -200]
    df_props=df_props[df_props['Ksym'] < 100]
    df_props=df_props[df_props['Esym'] > 0]
    df_props=df_props[df_props['Esym'] < 100]
    df_props=df_props[df_props['Qsym'] > 1000]
    df_props=df_props[df_props['Qsym'] < 4000]


    # if i!=21:
    #     df=df[df['gwr'] < 1]
    # #df=df[df['gwr'] < 1]
    # #df=df[df['grho'] < 16]
    # if i!=8:
    #     df=df[df['gdel'] < 8]
    # #df=df[df['gdel'] < 2.4]
    # #df=df[df['gdel'] > -15]
    props1 = df_props.to_numpy()
    #print(df)
    if i==8:
        good_columns1=props1[:,[1,2,3,9,10,11,12]]
    elif i==20:
        good_columns2=props1[:,[1,2,3,9,10,11,12]]
    elif i==21:
        good_columns3=props1[:,[1,2,3,9,10,11,12]]

    print(good_columns1.shape)
    if i==21:

        figure = corner.corner(good_columns1, labels=["grho","gdel","gwr","Esym", "L", "Ksym", "Qsym"], title_fmt='.2f', show_titles=True ,color='deepskyblue', smooth=True, smooth1d=True, label_kwargs=dict(fontweight='bold', fontsize=13), title_kwargs=dict(fontsize=10, color='deepskyblue'), quantiles=[0.16, 0.5, 0.84], label='EOS8')
        corner.corner(good_columns2,fig=figure, color='deeppink', quantiles=[0.16, 0.5, 0.84], label='EOS 20',show_titles=True, smooth=True, smooth1d=True,title_kwargs=dict(fontsize=20, color='deeppink'))
        corner.corner(good_columns3,fig=figure, color='darkviolet', quantiles=[0.16, 0.5, 0.84], label='EOS 21',show_titles=True, smooth=True, smooth1d=True,title_kwargs=dict(fontsize=20, color='darkviolet'))

    
    os.remove(corner_plot)
    #figure = corner.corner(good_columns1)


    #set_title_neighbor(0, "EOS20", loc="right", color='deeppink')


    #set_title_neighbor(0, "EOS21", loc="right", color='darkviolet')




    
#set_title_neighbor(0 , "EOS8", loc="right", color='deepskyblue')
    #figure.show()

    #figure.suptitle(f"EOS{i}", fontsize=16)




#plt.legend(fontsize=30, frameon=False, loc='upper right')
#figure.legend()
#figure.legend(['EOS 8','_','_','_','EOS 20','_','_','_','EOS 21'],fontsize=30, frameon=False, loc='upper right')

#figure.legend( ["EOS8", "EOS20", "EOS21"], ['deepskyblue', 'deeppink', 'darkviolet'],fontsize=30, frameon=False, loc='upper right')
#figure.suptitle("EOS8, EOS20, EOS21", fontsize=20)
# plt.legend(
#         handles=[
#             mlines.Line2D([], [], color=colors[i%3], label=f'EOS{i}')
#         ],
#         fontsize=20, frameon=False,
#     )
#plt.title("EOS8, EOS20, EOS21", fontsize=20)
#plt.legend(["EOS8", "EOS20", "EOS21"], fontsize=20, frameon=False, loc='lower left')
plt.show()
#figure.savefig(f"corner-plots/corner-full2.png")


