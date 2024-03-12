import subprocess
import os

def execute_command(command):
    try:
        # Split command into list of arguments
        args = command.split()
        
        # Check for IO redirection symbols
        input_file = None
        output_file = None
        if '<' in args:
            input_index = args.index('<')
            input_file = args[input_index + 1]
            args = args[:input_index]
        if '>' in args:
            output_index = args.index('>')
            output_file = args[output_index + 1]
            args = args[:output_index]

        # Execute the command
        if input_file:
            with open(input_file, 'r') as f:
                process = subprocess.Popen(args, stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Get output
        output, error = process.communicate()
        
        # Redirect output to file if specified
        if output_file:
            with open(output_file, 'w') as f:
                f.write(output.decode())
        else:
            print(output.decode())
        
        # Print error if there is any
        if error:
            print(error.decode())
            
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        # Get user input
        command = input("$ ")
        
        # Check for exit command
        if command.lower() == 'exit':
            break
        
        # Execute the command
        execute_command(command)

if __name__ == "__main__":
    main()
