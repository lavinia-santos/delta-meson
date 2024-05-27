import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

############################################
#2nd try
#Let's try with matrices instead of lists
#############################################

def quartile():
    # Calcule os quantis
    quantis=0.1
    quantiles = np.arange(quantis, 1 + quantis, quantis)
    #quantile_values = [np.quantile(lst, q) for q in quantiles]

    # Encontre os valores correspondentes aos quantis na lista original
    #lst_result = [min(lst, key=lambda x: abs(x - qv)) for qv in quantile_values]

    input_file = "tov-data-ex.txt" #R: col3, M: col2
    num_curves = 2
    intervals=np.linspace(0,1,100)

    masses_raw=[]
    matrix=[]
    full_matrix=[]
    all_radius=[]

    # radius={}
    # mvsr = {}
    # masses=[]
 
    matrix = np.loadtxt(input_file, dtype=float)
    for i in range(matrix.shape[0]):
        print(f"{i} out of {matrix.shape[0]} done")
        # curve_number=matrix[i][0]
        # print(f"curve_number:{curve_number}")
        mass=matrix[i][2]
        radius=matrix[i][3]
        
        masses_raw.append(mass)
        masses_raw=list(set(masses_raw))
        masses_raw.sort()
        # all_radius.append(radius)
        # #all_radius=list(set(all_radius))
        # all_radius.sort()
        # print(f"all_radius:{all_radius}")
    
    #input mass values to first row of full_matrix
    quantile_values = [np.quantile(masses_raw, q) for q in quantiles]
    for i in intervals:
        #print(i)
        masses = [min(masses_raw, key=lambda x: abs(x - qv)) for qv in quantile_values]
    masses.append(float(np.quantile(masses_raw, i)))
    masses=list(set(masses))
    full_matrix.append(masses)
    #print(f"full_matrix:{full_matrix}")
    

    #####append test
    # test1=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    # full_matrix.append(test1)
    # print(f"full_matrix after append:\n{full_matrix}")
    # full_matrix=np.array(full_matrix)
    # print(f"full_matrix after array:\n{full_matrix}")
    # full_matrix=np.transpose(full_matrix)
    # print(f"full_matrix after transpose:\n{full_matrix}")
    ####################





    for mass in full_matrix[0][:]:
        #print(f"mass:{mass}")
        #column=0
        print(f"mass {mass} done")

        temp_row=[]

        for i in range(matrix.shape[0]):
            # print(f"matrix[i][2]:{matrix[i][2]}")
            #print(f"mass:{mass}, temp_row:{temp_row} \n")

            if float(mass) == float(matrix[i][2]):
                temp_row.append(matrix[i][3])
        temp_row.extend([0]*(len(full_matrix[0][:])-len(temp_row)))
        full_matrix.append(temp_row)
        #print(f"full_matrix after append:\n{full_matrix}")
    #print(f"full_matrix after append out of for:\n{full_matrix}")
    full_matrix=np.array(full_matrix)
    print(f"full_matrix after array:\n{full_matrix}")


#it was created a matrix in which first row is the mass values and the other rows are the radius values related to the mass values


#     #the horizontal slice was set up
#     #now, let's calculate the quartiles of the radius


    q1=[]
    q3=[]
    for arr in full_matrix[1:]:
        print(f"arr:{arr}")
        # for i in range(len(arr)):
        #     print(f"i:{i}")
        #print(mvsr.items())
        #print(np.quantile(arr, 0.25))
        q1.append(np.quantile(arr, 0.16))
        q3.append(np.quantile(arr, 0.84))
    print(f"q1:{q1}")
    print(f"q3:{q3}")







    #q1 and q3 are radius values related to a given mass value

    #     q1.append(np.quantile(arr, 0.25))
        
    #     q3.append(np.quantile(arr, 0.75))
    
    # print(f"q1:{q1}")
    # print(f"q3:{q3}")
            

    # print(f"q1:{q1}")
    # print(f"q3:{q3}")

#     plt.plot(q1, masses, 'r-')
#     plt.plot(q3, masses, 'b-')
#     plt.show()

    
   

quartile()

