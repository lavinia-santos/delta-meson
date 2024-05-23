import numpy as np
import matplotlib.pyplot as plt


def quartile():
    #get mass values from the tov output file
    #for now, we use a dummy array
    #mass_raw=[5,7,15,22,45]

    # Calcule os quantis
    quantis=0.1
    quantiles = np.arange(quantis, 1 + quantis, quantis)
    #quantile_values = [np.quantile(lst, q) for q in quantiles]

    # Encontre os valores correspondentes aos quantis na lista original
    #lst_result = [min(lst, key=lambda x: abs(x - qv)) for qv in quantile_values]

    input_file = "tov-data-ex.txt" #R: col3, M: col2
    num_curves = 5
    intervals=[0, 0.2, 0.4, 0.6, 0.8, 1.0]

    masses_raw=[]
    radius={}
    mvsr = {}
    masses=[]
    
    #print(input_file)
    with open(input_file, "r") as infile:
        for line in infile:
            columns = line.split()
            #print(columns)
            masses_raw.append(float(columns[2]))
            quantile_values = [np.quantile(masses_raw, q) for q in quantiles]
        for i in intervals:
            #print(i)
            masses = [min(masses_raw, key=lambda x: abs(x - qv)) for qv in quantile_values]
            #masses.append(np.quantile(masses_raw, i))
        print(f"masses_raw:{masses_raw}")
        print(f"q_mass:{masses}")   
        for line in infile:
            for i in range(1,num_curves+1):
                # print(f"i:{i}")
                # print(f"columns[0]:{columns[0]}")
                if int(columns[0]) == i and int(columns[0]) not in radius.keys():
                    # print(radius.keys())
                    # print(f"in if loop columns[0] (col):{columns[0]}")
                    
                    #temp = float(columns[3])
                    # print(temp)
                    radius[i] = []
                    radius[i].append(float(columns[3]))
                    #print(radius)
                    # print(f"radius[{i}] if:{radius[i]}")

                elif int(columns[0]) == i and int(columns[0]) in radius.keys():
                    #print(f"in else loop columns[0] (col):{columns[0]}")
                    #temp.append(columns[3])
                    #print(temp)
                    radius[i].append(float(columns[3]))
                    #print(f"radius[{i}] elif:{radius[i]}")
            for mass in masses_raw:
                # print(f"mass:{mass}")
                # print(f"columns[2]:{columns[2]}")
                if float(columns[2]) == mass:
                    # print(f"mass {columns[0]}:{mass}")
                    # print(f"radius {columns[0]}:{columns[3]}")
                    if columns[2] not in mvsr.keys():
                        mvsr[mass] = []
                        mvsr[mass].append(columns[3])
                    else:
                        mvsr[mass].append(columns[3])
    # print(radius)
    # print(masses)
    print(f"mvsr:{mvsr}")

        # print(f"radius:{radius.values()}")


# # make up some data

# # interpreting x value based on y value
# x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# y=np.sin(x)
# y_val = 0.1
# x_interp = round(np.interp(y_val, y, x), 4)  # x_interp = np.interp(y_vals, y, x)

# print(f"x_interp:{x_interp}")

# # place a marker on point (x_interp, y_val)
# plt.plot(x, y, '-', color='k')
# plt.plot(x_interp, y_val, 'ro')
# plt.show()
                
            

    # #get the quartile values
    # q_mass=[]
    # lst=[0.05, 0.25, 0.5, 0.75, 0.95]
    # for i in lst:
    #     q_mass.append(np.quantile(mass_raw, i))

    # print(f"q_mass:{q_mass}")   




    # arr0 = [1, 2, 7, 20, 34]
    # arr1 = [1, 4, 8, 25, 38]
    # dict = {"0": arr0 , "1": arr1}

    # dict["2"] = [3,5,12,27,45]
    # for i in range (2):
    #     dict[str(i+3)] = [i+5, i+7, i+10, i+32, i+54]

    # #print(f"dict:{dict}")
    # #print(dict.values())


    # q1=[]
    # q3=[]
    # for arr in dict.values():
    #     for i in range(0,1):

    #         q1.append(np.quantile(arr, 0.25))
            
    #         q3.append(np.quantile(arr, 0.75))
            

    # print(f"q1:{q1}")
    # print(f"q3:{q3}")

    # plt.plot(q1, q_mass, 'r-')
    # plt.plot(q3, q_mass, 'b-')
    # plt.show()

    
   

quartile()

