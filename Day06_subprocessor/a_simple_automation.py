import subprocess

# Run the command and capture what it says
result = subprocess.run(["echo", "Hello World"], capture_output=True, text=True)
// capture_output = it store the output to use it in Python script. 
// text = True so it store the data as string not as bytes. 

# Now you can use that text in your code
print(f"The program said: {result.stdout}") 

