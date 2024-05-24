import numpy as np
import matplotlib.pyplot as plt

############################################
#2nd try
#############################################

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
    num_curves = 250
    intervals=np.linspace(0.6,1,50)

    masses_raw=[]
    radius={}
    mvsr = {}
    masses=[]
    
    #print(input_file)
    with open(input_file, "r") as infile:
        for line in infile:
            columns = line.split()
            print(f"starting first scan {columns[0]}th time")
            
            # print(line)
            # print(f"starting first scan {columns[0]}th time")
            
            #print(columns)
            masses_raw.append(float(columns[2]))
            quantile_values = [np.quantile(masses_raw, q) for q in quantiles]
            for i in intervals:
                #print(i)
                masses = [min(masses_raw, key=lambda x: abs(x - qv)) for qv in quantile_values]
            #masses.append(np.quantile(masses_raw, i))
        # print(f"masses_raw:{masses_raw}")
            #print(f"q_mass:{masses}")   
        #for line in infile:
            #print(f"line:{line}")
        # for line in infile:
        #     #print(line)
        #     columns = line.split()
            
            for i in range(1,num_curves+1):
                #print(f"i:{i}")
                # print(f"columns[0]:{columns[0]}")
                if int(columns[0]) == i and int(columns[0]) not in radius.keys():
                    # print(radius.keys())
                    # print(f"in if loop columns[0] (col):{columns[0]}")
                    radius[i] = []
                    radius[i].append(float(columns[3]))
                    # print(radius)
                    # print(f"radius[{i}] if:{radius[i]}")

                elif int(columns[0]) == i and int(columns[0]) in radius.keys():
                    #print(f"in else loop columns[0] (col):{columns[0]}")
                    #temp.append(columns[3])
                    #print(temp)
                    radius[i].append(float(columns[3]))
                    #print(f"radius[{i}] elif:{radius[i]}")
            
            
    
        #print(f"masses:{masses}")
    # with open(input_file, "r") as infile:
        
    #     for line in infile:
        
            #columns = line.split()
            #print(f"columns:{columns}")
            #print(f"masses after lines:{masses}")
    print(f"masses before for:{masses}")
    with open(input_file, "r") as infile:
        for line in infile:
            columns = line.split()
            print(f"starting second scan {columns[0]}th time")
            for mass in masses:
                #print(f"masses:{masses}")
                # print(f"mass:{mass}")
                #print(f"mass before if loop:{mass}")
                #print(f"columns[2]:{columns[2]}")
                if float(columns[2]) == float(mass):
                    print(f"mass :{mass}")
                    print(f"columns[2]:{columns[2]}")
                    if float(columns[2]) not in mvsr.keys():
                        #print(f"mass {columns[0]}:{mass}")
                        #print(f"mvsr.keys():{mvsr.keys()}")
                        # print(f"radius {columns[0]}:{columns[3]}")
                            #print(f"in if loop {columns[2]} (mass):{columns[2]}")
                        mvsr[mass] = []
                        mvsr[mass].append(columns[3])
                    if float(columns[2]) in mvsr.keys():
                    #print(f"in else loop columns[2] (mass):{columns[2]}")
                        mvsr[mass].append(columns[3])
        # print(f"{columns[0]}th scan done")
        # for line in infile:
        #     columns = line.split()
            for key in mvsr:
                mvsr[key] = [float(val) for val in mvsr[key]]
       
            
    # print(f"radius:{radius}")
    #print(f"masses:{masses}")
   # for j in mvsr.items():
    print(f"masses:{masses}")
    #print(f"mvsr:{mvsr.keys()}")
        #print(f"mvsr:{mvsr[j]}")
    print(f"mvsr:{mvsr} ")
    with open("mvsr.txt", "w") as outfile:
        outfile.write(str(mvsr))
    
    #mvsr: keys: mass, values: radius list corresponding to the mass

        # print(f"radius:{radius.values()}")

    #the horizontal slice was set up
    #now, let's calculate the quartiles


    q1=[]
    q3=[]
    #print(f"mvsr.values():{mvsr.values()}")
    for arr in mvsr.values():
        #print(f"arr:{arr} \n")
        # for i in range(len(arr)):
        #     print(f"i:{i}")
        #print(mvsr.items())
        #print(np.quantile(arr, 0.25))
        q1.append(np.quantile(arr, 0.05))
        q3.append(np.quantile(arr, 0.95))
    print(f"q1:{q1}")
    print(f"q3:{q3}")
    #q1 and q3 are radius values related to a given mass value

    #     q1.append(np.quantile(arr, 0.25))
        
    #     q3.append(np.quantile(arr, 0.75))
    
    # print(f"q1:{q1}")
    # print(f"q3:{q3}")
            

    # print(f"q1:{q1}")
    # print(f"q3:{q3}")

    plt.plot(q1, masses, 'r-')
    plt.plot(q3, masses, 'b-')
    plt.show()

    
   

quartile()

