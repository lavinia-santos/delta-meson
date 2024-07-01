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




    #figure = corner.corner(good_columns1, labels=["grho","gdel","gwr","Esym", "L", "Ksym", "Qsym"], title_fmt='.2f', show_titles=True ,color='deepskyblue', smooth=True, smooth1d=True, label_kwargs=dict(fontweight='bold', fontsize=13), title_kwargs=dict(fontsize=10, color='deepskyblue'), quantiles=[0.16, 0.5, 0.84], label='EOS8')

    # props=f"EOS{i}/props.dat"
    # #couplings="../../../../../../../../Downloads/para_eos21.csv"
    # corner_plot="corner.dat"
    # with open( props, 'r') as r, open(corner_plot, 'w') as o: 
    #     for line in r: 
    #         #strip() function 
    #         if line.strip(): 
    #             o.write(line) 
    
    # df_props=pd.read_csv(corner_plot, sep=",", header=None, skip_blank_lines=True, on_bad_lines='skip')
    # df_props=df_props.rename(columns={df_props.columns[1]: 'grho',df_props.columns[2]: 'gdel',df_props.columns[3]: 'gwr',df_props.columns[5]: 'm_eff', df_props.columns[6]: 'EB', df_props.columns[9]: 'Esym', df_props.columns[10]: 'L', df_props.columns[11]: 'Ksym', df_props.columns[12]: 'Qsym'})
    # df_props=df_props.rename(columns={df_props.columns[0]: 'label', df_props.columns[1]: 'gr', df_props.columns[2]: 'gdel', df_props.columns[3]: 'lambda'})
    # #print(df)
    # df_props=df_props[df_props['L'] < 200]
    # df_props=df_props[df_props['L'] > 0]
    # df_props=df_props[df_props['Ksym'] > -200]
    # df_props=df_props[df_props['Ksym'] < 100]
    # df_props=df_props[df_props['Esym'] > 0]
    # df_props=df_props[df_props['Esym'] < 100]
    # df_props=df_props[df_props['Qsym'] > 1000]
    # df_props=df_props[df_props['Qsym'] < 4000]


    # # if i!=21:
    # #     df=df[df['gwr'] < 1]
    # # #df=df[df['gwr'] < 1]
    # # #df=df[df['grho'] < 16]
    # # if i!=8:
    # #     df=df[df['gdel'] < 8]
    # # #df=df[df['gdel'] < 2.4]
    # # #df=df[df['gdel'] > -15]
    # props1 = df_props.to_numpy()
    # #print(df)
    # if i==8:
    #     good_columns1=props1[:,[1,2,3,9,10,11,12]]
    # elif i==20:
    #     good_columns2=props1[:,[1,2,3,9,10,11,12]]
    # elif i==21:
    #     good_columns3=props1[:,[1,2,3,9,10,11,12]]

    # print(good_columns1.shape)

    
    # os.remove(corner_plot)
    # #figure = corner.corner(good_columns1)

    #getting NS properties for M=Mmax
    df_NS = pd.read_csv(f'../../big-results/tov-data{i}.dat', sep='\s+', engine='python')
    df_NS = df_NS.rename(columns={df_NS.columns[0]: 'label', df_NS.columns[1]: 'energy_density', df_NS.columns[2]: 'mass', df_NS.columns[3]: 'radius', df_NS.columns[4]: 'baryonic_masses', df_NS.columns[5]: 'density'})

    labels = df_NS['label'].unique()
    max_masses=[]
    radii_max_masses=[]
    for label in labels:
        temp_df = df_NS[df_NS['label'] == label]
        max_mass = temp_df['mass'].max()
        radius_max_mass = temp_df[temp_df['mass'] == max_mass]['radius'].values[0]
        #print(label, max_mass, radius_max_mass)
        max_masses.append(max_mass)
        radii_max_masses.append(radius_max_mass)
    #print(len(max_masses),len(radii_max_masses))
    
    #numpy vectors for maximum masses and respective radii(R_Mmax) are done



#commenting for now due to speed
    #Now, the same but for M=1.4Msun
    df_NS = pd.read_csv(f'../../big-results/tov-data{i}.dat', sep='\s+', engine='python')
    df_NS = df_NS.rename(columns={df_NS.columns[0]: 'label', df_NS.columns[1]: 'energy_density', df_NS.columns[2]: 'mass', df_NS.columns[3]: 'radius', df_NS.columns[4]: 'baryonic_masses', df_NS.columns[5]: 'density'})
    labels = df_NS['label'].unique()
    masses_14=[]
    radii_masses_14=[]
    for label in labels:
        temp_df = df_NS[df_NS['label'] == label]
        #if there is no 1.4 Msun star, we will interpolate
        if temp_df[temp_df['mass'] == 1.4].empty:
            tck = interp1d(temp_df['mass'], temp_df['radius'], bounds_error=False, kind='linear', fill_value=(np.nan, np.nan))
            #print(tck(1.4))
            radius=float(tck(1.4))
            radii_masses_14.append(radius)
            masses_14.append(1.4)
        else:
            radii_masses_14.append(temp_df[temp_df['mass'] == 1.4]['radius'].values[0])
            masses_14.append(1.4)

    # print(radii_masses_14)
    # print(len(masses_14),len(radii_masses_14))
    #numpy vectors for 1.4Msun masses and respective radii(R1.4) are done


    #Now, the same but for M=2Msun
    df_NS = pd.read_csv(f'../../big-results/tov-data{i}.dat', sep='\s+', engine='python')
    df_NS = df_NS.rename(columns={df_NS.columns[0]: 'label', df_NS.columns[1]: 'energy_density', df_NS.columns[2]: 'mass', df_NS.columns[3]: 'radius', df_NS.columns[4]: 'baryonic_masses', df_NS.columns[5]: 'density'})
    labels = df_NS['label'].unique()
    masses_20=[]
    radii_masses_20=[]
    for label in labels:
        temp_df = df_NS[df_NS['label'] == label]
        #if there is no 2.0 Msun star, we will interpolate
        if temp_df[temp_df['mass'] == 2.0].empty:
            tck = interp1d(temp_df['mass'], temp_df['radius'], bounds_error=False, kind='linear', fill_value=(np.nan, np.nan))
            #print(tck(1.4))
            radius=float(tck(2.0))
            radii_masses_20.append(radius)
            masses_20.append(2.0)
        else:
                radii_masses_20.append(temp_df[temp_df['mass'] == 2.0]['radius'].values[0])
                masses_20.append(2.0)
    #print(len(masses_20),len(radii_masses_20))
    #numpy vectors for 2Msun masses and respective radii(R2.0) are done


#let's put all the data in a single numpy array (matrix)
if i==8:
    full_array = np.stack((radii_masses_14 , radii_masses_20, max_masses, radii_max_masses), axis=-1)
    print(full_array.shape)

    for line in full_array:
        # if line[0] < 12.0 or line[0] > 13.0:
        #         full_array = np.delete(full_array, line, 0)
        #         break
        # if line[1] < 12.0 or line[1] > 12.5:
        #     full_array = np.delete(full_array, line, 0)
        #     break
        # if line[2] > 2.25:
        #     full_array = np.delete(full_array, line, 0)
        #     break
        # if line[3] < 12.0 or line[3] > 13.0:
        #     full_array = np.delete(full_array, line, 0)
        #     break
        for j in range(4):
            if np.isnan(line[j]):
                print(line)
                full_array = full_array[~np.isnan(full_array).any(axis=1)]
    print(f"{i} {full_array.shape}")
if i==20:
    full_array2 = np.stack((radii_masses_14 , radii_masses_20, max_masses, radii_max_masses), axis=-1)
    #print(full_array2.shape)

    for line in full_array2:
        # if line[0] < 12.0 or line[0] > 13.0:
        #         full_array2 = np.delete(full_array2, line, 0)
        #         break
        # if line[1] < 12.0 or line[1] > 12.5:
        #     full_array2 = np.delete(full_array2, line, 0)
        #     break
        # if line[2] > 2.25:
        #     full_array2 = np.delete(full_array2, line, 0)
        #     break
        # if line[3] < 12.0 or line[3] > 13.0:
        #     full_array2 = np.delete(full_array2, line, 0)
        #     break
        for j in range(4):
            if np.isnan(line[j]):
                print(line)
                full_array2 = full_array2[~np.isnan(full_array2).any(axis=1)]
    print(f"{i} {full_array.shape}")
if i==21:
    full_array3 = np.stack((radii_masses_14 , radii_masses_20, max_masses, radii_max_masses), axis=-1)
    #print(full_array3.shape)

    for line in full_array3:
    #     if line[0] < 12.0 or line[0] > 13.0:
    #             full_array3 = np.delete(full_array3, line, 0)
    #             break
    #     if line[1] < 12.0 or line[1] > 12.5:
    #         full_array3 = np.delete(full_array3, line, 0)
    #         break
    #     if line[2] > 2.25:
    #         full_array3 = np.delete(full_array3, line, 0)
    #         break
    #     if line[3] < 12.0 or line[3] > 13.0:
    #         full_array3 = np.delete(full_array3, line, 0)
    #         break
        for j in range(4):
            if np.isnan(line[j]):
                print(line)
                full_array3 = full_array3[~np.isnan(full_array3).any(axis=1)]
    print(f"{i} {full_array.shape}")
###############uncomment if you want to save the data in a csv file###############
# with open("full_array.csv", 'w') as o:
#     for line in full_array:
#         o.write(str(line[0])+','+str(line[1])+','+str(line[2])+','+str(line[3])+'\n')
#     o.close()
##################################################################################
# #now, let's plot the corner plot
#figure = corner.corner(full_array)

figure = corner.corner(full_array, labels=["R1.4","R2.0","Mmax","R_Mmax"], title_fmt='.2f', show_titles=True ,color='blue', smooth=True, smooth1d=True, label_kwargs=dict(fontweight='bold', fontsize=13), title_kwargs=dict(fontsize=10, color='deepskyblue'), quantiles=[0.16, 0.5, 0.84], label='EOS8')
corner.corner(full_array2,fig=figure, color='deeppink', quantiles=[0.16, 0.5, 0.84], label='EOS20',show_titles=True, smooth=True, smooth1d=True,title_kwargs=dict(fontsize=10, color='deeppink'))
corner.corner(full_array3,fig=figure, color='darkviolet', quantiles=[0.16, 0.5, 0.84], label='EOS21',show_titles=True, smooth=True, smooth1d=True,title_kwargs=dict(fontsize=10, color='darkviolet'))
plt.legend(fontsize=30, frameon=False, loc='upper right')
plt.show()



    
#set_title_neighbor(0 , "EOS8", loc="right", color='deepskyblue')
    #figure.show()

    #figure.suptitle(f"EOS{i}", fontsize=16)


#corner.corner(good_columns2,fig=figure, color='deeppink', quantiles=[0.16, 0.5, 0.84], label='EOS 20',show_titles=True, smooth=True, smooth1d=True,title_kwargs=dict(fontsize=20, color='deeppink'))

#set_title_neighbor(0, "EOS20", loc="right", color='deeppink')

#corner.corner(good_columns3,fig=figure, color='darkviolet', quantiles=[0.16, 0.5, 0.84], label='EOS 21',show_titles=True, smooth=True, smooth1d=True,title_kwargs=dict(fontsize=20, color='darkviolet'))

#set_title_neighbor(0, "EOS21", loc="right", color='darkviolet')

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
#plt.show()
#figure.savefig(f"corner-plots/corner-full2.png")


