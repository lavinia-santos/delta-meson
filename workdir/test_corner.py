import corner
import numpy as np

# ndim, nsamples = 3, 1000
# np.random.seed(42)
# samples = np.random.randn(ndim * nsamples).reshape([nsamples, ndim])
beta0="fort.7"
beta1="beta-corner.txt"
#beta1="test-beta-corner.txt"
with open (beta0, "r") as infile, open(beta1, "w") as outfile:
    for line in infile:
        infile.readline()
        columns = line.split()
        del columns[3]
        outfile.write(" ".join(columns) + "\n")
        print(columns)
        
        #print(columns)
# with open (beta0, "r") as infile:
#         for line in infile:
#             del columns[2]
    
# with open (beta0, "a") as infile: 
#     for line in infile: 
#         del columns[3]

#print(beta0)
        # if line.strip():
        #     core_new_file.write("\t".join(line.split()[:3]) + "\n")
beta_np = np.loadtxt(beta1)
print(beta_np)  
#print(samples[2])
figure = corner.corner(beta_np)
figure.show()
#figure.savefig("corner.png")