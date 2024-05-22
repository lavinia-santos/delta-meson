import corner
import numpy as np

# ndim, nsamples = 3, 1000
# np.random.seed(42)
# samples = np.random.randn(ndim * nsamples).reshape([nsamples, ndim])
beta0="original_data/fort.7"
beta1="original_data/test-beta-corner.txt"
with open (beta0, "r") as core_old_file, open(beta1, "w") as core_new_file:
            for line in core_old_file:
                if line.strip():
                    core_new_file.write("\t".join(line.split()[:3]) + "\n")
beta1a = np.loadtxt(beta1)
    
#print(samples[2])
figure = corner.corner(beta1a)
figure.savefig("corner.png")