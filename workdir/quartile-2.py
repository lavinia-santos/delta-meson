import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import numpy as np

############################################
#2nd try
#Let's try with matrices instead of lists
#############################################


import matplotlib.pyplot as plt

# def plot_confidence_curve():
#     # Load data from file
#     data = np.loadtxt("tov-data-ex.txt", dtype=float)
#     masses = data[:, 2]
#     radii = data[:, 3]

#     # Filter radii values between 10 and 14
#     radii_filtered = radii[(radii >= 11.2) & (radii <= 13.2)]
#     masses_filtered = masses[(radii >= 11.2) & (radii <= 13.2)]

#     # Create empty lists for quartiles
#     q1 = []
#     q3 = []

#     # Iterate over unique mass values
#     unique_masses = np.unique(masses_filtered)
#     for mass in unique_masses:
#         # Get radius values for current mass
#         mass_radii = radii_filtered[masses_filtered == mass]

#         # Calculate quartiles
#         q1.append(np.quantile(mass_radii, 0.25))
#         q3.append(np.quantile(mass_radii, 0.75))

#     # Plot confidence curve
#     plt.plot(q1, unique_masses, 'r-', label='Q1')
#     plt.plot(q3, unique_masses, 'b-', label='Q3')

#     # Plot silhouette of minimal and maximal curve
#     plt.fill_betweenx(unique_masses, q1, q3, color='gray', alpha=0.5)

#     plt.legend()
#     plt.show()

# plot_confidence_curve()

def plot_mr_curve():
    # Load data from file
    data = np.loadtxt("tov-data-ex.txt", dtype=float)
    labels = data[:, 0]
    masses = data[:, 2]
    radii = np.asfarray(data[:, 3])
    print(f"labels:{labels}")
    # print(f"radii:{radii}")
    # print(f"masses:{masses}")

    # Filter radii values between 11 and 15
    radii_filtered = radii[(radii >= 10) & (radii <= 15)]
    masses_filtered = masses[(radii >= 10) & (radii <= 15)]
    labels_filtered = labels[(radii >= 10) & (radii <= 15)]
    print(f"radii_filtered:{radii_filtered}, len:{len(radii_filtered)}")
    print(f"masses_filtered:{masses_filtered}, len:{len(masses_filtered)}")
    print(f"labels_filtered:{labels_filtered}, len:{len(labels_filtered)}")
    #Find the indices of the minimal and maximal radii values
    min_radius = np.min(radii_filtered)
    max_radius = np.max(radii_filtered)
    # Get the masses and radii for the minimal and maximal curves
    print(f"min_radius:{min_radius}")
    print(f"max_radius:{max_radius}")
    min_masses = masses_filtered[radii_filtered == min_radius]
    max_masses = masses_filtered[radii_filtered == max_radius]
    print(f"min_masses:{min_masses}")
    print(f"max_masses:{max_masses}")
    min_label = labels_filtered[radii_filtered == min_radius]
    max_label = labels_filtered[radii_filtered == max_radius]
    
   
    
    print(f"min_label:{min_label}")
    print(f"max_label:{max_label}")
    
    # Create empty lists for all masses and radii
    all_masses = []
    all_radii = []
    unique_labels=[]

    # Iterate over unique labels
    unique_labels.append(min_label)
    unique_labels.append(max_label)
    print(f"unique_labels:{unique_labels}")
    for label in unique_labels:
        # Get masses and radii for current label
        label_masses = masses_filtered[labels_filtered == label]
        label_radii = radii_filtered[labels_filtered == label]

        # Append masses and radii to the respective lists
        all_masses.append(label_masses)
        all_radii.append(label_radii)
    print(f"all_masses:{all_masses}")
    print(f"all_radii:{all_radii}")

    for i in range(len(unique_labels)):
        plt.plot(all_radii[i], all_masses[i], 'r-', label=unique_labels[i])

    plt.legend()
    plt.show()
   
    # # Create empty lists for all masses and radii
    # all_masses = []
    # all_radii = []
    # unique_labels=[]

    # # Iterate over unique labels
    # unique_labels.append(min_label)
    # unique_labels.append(max_label)
    # print(f"unique_labels:{unique_labels}")
    # for label in unique_labels:
    #     # Get masses and radii for current label
    #     label_masses = masses_filtered[labels == label]
    #     label_radii = radii_filtered[labels == label]

    #     # Append masses and radii to the respective lists
    #     all_masses.append(label_masses)
    #     all_radii.append(label_radii)
    # print(f"all_masses:{all_masses}")
    # print(f"all_radii:{all_radii}")

   
    # for i in range(len(unique_labels)):
    #     plt.plot(all_masses[i], all_radii[i], 'r-', label=unique_labels[i])
    

    # plt.legend()
    # plt.show()


    # # Plot the minimal and maximal curves
    # plt.plot(min_masses, min_radii, 'r-', label=min_label)
    # plt.plot(max_masses, max_radii, 'b-', label=max_label)

    # plt.legend()
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

