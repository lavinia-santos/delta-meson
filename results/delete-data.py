import os, subprocess



for num in [8,20,21]:
    dir=f"EOS{num}"
    subprocess.run(f"rm {dir}/beta-outputs/*", shell=True)
    print("Deleted beta-outputs")
    subprocess.run(f"rm {dir}/beta-outputs/with-crust/*", shell=True)
    print("Deleted beta-outputs/with-crust")
    subprocess.run(f"rm {dir}/tov-outputs/*", shell=True)
    print("Deleted tov-outputs")
