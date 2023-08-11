import subprocess

# Running a command and capturing the output
# result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# print(result.stdout)

# Running a command and checking the return code
# result = subprocess.run(["git", "status"])
# if result.returncode == 0:
#     print("Git status executed successfully.")
# else:
#     print("Git status failed!")

# # Running a command and getting the output in a variable
# output = subprocess.check_output(["echo", "Hello, World!"], text=True)
# print(output)

# # Running a command in a different directory
# result = subprocess.run(["ls", "-l"], cwd="/Users/Fred/Desktop/")

# # Running a command and redirecting input/output
# with open("output.txt", "w") as f_out:
#     result = subprocess.run(["ls", "-l"], stdout=f_out, text=True)

# # Running a command and capturing errors
try:
    subprocess.run(["some_command"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command execution failed with exit code {e.returncode}:\n{e.stderr}")

# # Running a command and providing input
# input_data = "This is the input data."
# result = subprocess.run(["python", "my_script.py"], input=input_data, text=True)