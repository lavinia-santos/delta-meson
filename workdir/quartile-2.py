import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
from scipy.interpolate import interp1d

original_stdout = sys.stdout


############################################
#2nd try
#Let's try with matrices instead of lists
#############################################




def plot_mr_curve():
    # Load data from file
    N_points=200
    df = pd.read_csv('tov-data-ex.txt', sep='   ')
    df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'energy density', df.columns[2]: 'mass', df.columns[3]: 'radius', df.columns[4]: 'baryonic masses', df.columns[5]: 'density'})

    #print(df)

    labels = np.asarray(df['label'])
    labels = np.unique(labels)
    #print(f"labels:{labels}")

    N_models = len(labels)

    for x in range(1,N_models+1):
        #print(x)

        M_Temp = np.asarray(df.mass[df.label == x])
        # print(f"M_Temp:{M_Temp}")
        R_Temp = np.asarray(df.radius[df.label == x])
        # print(f"R_Temp:{R_Temp}")
        index=M_Temp.argmax()
        #print(f"index:{index}")
        # M_df=M_Temp[index:]
        # R_df=R_Temp[index:]
        # print(f"M_df:{M_df}, R_df:{R_df}")

        tck = interp1d(M_Temp, R_Temp, bounds_error=False, kind='linear', fill_value=(np.nan, np.nan))
        print(f"tck:{tck}")



    






    # Filter radii values between 11 and 15
    # radii_filtered = radii[(radii >= 10) & (radii <= 15)]
    # masses_filtered = masses[(radii >= 10) & (radii <= 15)]
    # labels_filtered = labels[(radii >= 10) & (radii <= 15)]
    # radii_sorted = np.sort(radii_filtered)
    # #radii_filtered = np.unique(radii_filtered)
    # masses_sorted = np.sort(masses_filtered)
    #masses_filtered = np.unique(masses_filtered)
    # print(f"radii_filtered:{radii_filtered}, len:{len(radii_filtered)}")
    # print(f"masses_filtered:{masses_filtered}, len:{len(masses_filtered)}")

    
    
    
    # for label in labels_filtered:
    #     plt.plot(radii_filtered[labels_filtered == label], masses_filtered[labels_filtered == label])
    # plt.show()

    

    # # Interpolation to get masses for all radii values
    # mass_interp = np.interp(radii_filtered, radii_sorted, masses_sorted)
    # print(f"mass_interp:{mass_interp}, len:{len(mass_interp)}")

    # # Sort mass_interp based on radii_filtered
    # mass_interp_sorted = mass_interp[np.argsort(radii_filtered)]
    # print(f"mass_interp_sorted:{mass_interp_sorted}, len:{len(mass_interp_sorted)}")

    # # # Interpolation to get radii for all mass values
    # # radii_interp = np.interp(masses_filtered, masses_sorted, radii_sorted)
    # # print(f"radii_interp:{radii_interp}, len:{len(radii_interp)}")

    # # # Sort radii_interp based on masses_filtered
    # # radii_interp_sorted = radii_interp[np.argsort(masses_filtered)]
    # # print(f"radii_interp_sorted:{radii_interp_sorted}, len:{len(radii_interp_sorted)}")
 


    # #Check all radii values for a given mass value
    # for mass in mass_interp_sorted:
    #     #mass_radii = masses_filtered[radii_interp_sorted == radius]
    #     mass_radii = radii_filtered[masses_filtered == mass]
    #     print(f"Mass: {mass} , Radii: {mass_radii}")


    # # Calculate q1 and q3 for each mass
    # q1 = []
    # q3 = []
    # for mass in mass_interp:
    #     mass_radii = radii_filtered[mass_interp == mass]
    #     q1.append(np.quantile(mass_radii, 0.25))
    #     q3.append(np.quantile(mass_radii, 0.75))

    # # Plot q1 and q3 for each label
    # unique_labels = np.unique(labels_filtered)
    # for label in unique_labels:
    #     label_masses = mass_interp[labels_filtered == label]
    #     plt.plot(q1, label_masses, 'r-')
    #     plt.plot(q3, label_masses, 'b-')

    # plt.show()


plot_mr_curve()

# def quartile():
#     # Calcule os quantis
#     quantis=0.5
#     quantiles = np.arange(quantis, 1, 0.05)
#     #print (f"quantiles:{quantiles}")

#     #quantile_values = [np.quantile(lst, q) for q in quantiles]

#     # Encontre os valores correspondentes aos quantis na lista original
#     #lst_result = [min(lst, key=lambda x: abs(x - qv)) for qv in quantile_values]

#     input_file = "tov-data-ex.txt" #R: col3, M: col2
#     output_file = "output-quartile.txt"
#     full_matrix_file="full_matrix.txt"
#     #quantiles=np.linspace(0,1,100)
#     #print(f"intervals:{quantiles}")

#     masses_raw=[]
#     matrix=[]
#     full_matrix=[]

#     # radius={}
#     # mvsr = {}
#     # masses=[]
 
#     matrix = np.loadtxt(input_file, dtype=float)
#     # for i in range(matrix.shape[0]):
#     #     print(f"{i} out of {matrix.shape[0]} done")

#     #     mass=matrix[i][2]
#     #     #if mass >= 1.5 and mass <= 2.9:
        
#     masses_raw=matrix[:,2]
    
#     #print(f"masses_raw.shape:{masses_raw.shape}")
#         # masses_raw.append(mass)
#     masses_raw=list(set(masses_raw))
#     masses_raw.sort()
#     #print(f"masses_raw:{masses_raw}")

    
#     #input mass values to first row of full_matrix
#     quantile_values = [np.quantile(masses_raw, q) for q in quantiles]
#     count=1
#     for i in quantiles:
#         print(f"quantile {count} done out of {len(quantile_values)}")
#         masses = [min(masses_raw, key=lambda x: abs(x - qv)) for qv in quantile_values]
#         count+=1
#         masses.append(float(np.quantile(masses_raw, i)))
#     masses=list(set(masses))
#     masses.sort()
#     full_matrix.append(masses)
#     print(f"full_matrix only with masses:{full_matrix}")
    

# #     #####append test
# #     # test1=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
# #     # full_matrix.append(test1)
# #     # print(f"full_matrix after append:\n{full_matrix}")
# #     # full_matrix=np.array(full_matrix)
# #     # print(f"full_matrix after array:\n{full_matrix}")
# #     # full_matrix=np.transpose(full_matrix)
# #     # print(f"full_matrix after transpose:\n{full_matrix}")
# #     ####################





#     for mass in full_matrix[0][:]:

#         # print(f"mass {mass} done")

#         temp_row=[]

#         for i in range(matrix.shape[0]):
#             # print(f"matrix[i][2]:{matrix[i][2]}")
#             #print(f"mass:{mass}, temp_row:{temp_row} \n")

#             if float(mass) == float(matrix[i][2]):
#                 temp_row.append(matrix[i][3])
#         temp_row.extend([0]*(len(full_matrix[0][:])-len(temp_row)))
#         full_matrix.append(temp_row)
#         #print(f"full_matrix after append:\n{full_matrix}")
#     print(f"full_matrix after append out of for:\n{full_matrix}")
#     with open(full_matrix_file, 'w') as f:
#         for i in range(len(full_matrix)):
#             f.write(f"{full_matrix[i]}\n")
#     full_matrix=np.array(full_matrix)
#     print(f"full_matrix after array:\n{full_matrix}")


# # #it was created a matrix in which first row is the mass values and the other rows are the radius values related to the mass values


# # #     #the horizontal slice was set up (masses)
# # #     #now, let's calculate the quartiles of the radius


# #     q1=[]
# #     q3=[]
# #     for arr in full_matrix[1:]:
# #         print(f"arr:{arr}")
# #         #q1.append(arr[0])
# #         q1.append(np.quantile(arr, 0.25))
# #         q3.append(np.quantile(arr, 0.75))
# #     print(f"q1:{q1}")
# #     print(f"q3:{q3}")

# #     q1=np.array(q1)
# #     q3=np.array(q3)
# #     masses=np.array(full_matrix[0][:])

# #     with open(output_file, 'w') as f:
# #         for i in range(len(masses)):
# #             f.write(f"{masses[i]} {q1[i]} {q3[i]}\n")








#     #q1 and q3 are radius values related to a given mass value

#     #     q1.append(np.quantile(arr, 0.25))
        
#     #     q3.append(np.quantile(arr, 0.75))
    
#     # print(f"q1:{q1}")
#     # print(f"q3:{q3}")
            

#     # print(f"q1:{q1}")
#     # print(f"q3:{q3}")

# #     plt.plot(q1, masses, 'r-')
# #     plt.plot(q3, masses, 'b-')
# #     plt.show()

    
   

# quartile()

