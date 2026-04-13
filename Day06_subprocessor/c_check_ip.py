import subprocess 

// for windows 
ip1 = subprocess.run(["ipconfig","/all"])


// for linux
ip2= subprocess.run(["ifconfig"])

// use Conditional Statements to check the os detail.

//like os.version 
// if wwindow run ip1 else ip2

print(ip1)
print(ip2) 
