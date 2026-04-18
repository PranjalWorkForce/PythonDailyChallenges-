import subprocess 

// better to install the tool manually 
  // In Linux
// cmd : sudo apt instal nmap

// In Windows
// download the nmap from nmap.org and then install it.


nmap = subprocess.run(["nmap", "-sT", ip, "-p", port, "--scripts=default"], capture_output=True, text=True)

print(nmap.stdout)
