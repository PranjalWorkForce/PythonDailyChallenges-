import subprocess 

result = subprocess.run(["mkdir", "folder"], check. = True)
print(result)

// also can use os library 

import os
make = os.makedirs("folder", exist_ok=True) # "exist_ok" prevents errors if it's already there
print(make) 
