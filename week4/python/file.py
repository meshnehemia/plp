# Read, modify, and write content to a new file

def read_and_write_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        modified_content = content + "\nThis is a new line added to the file!"
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print("File successfully modified and written to", output_file)
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError:
        print(f"Error: Couldn't read or write to {input_file} or {output_file}.")

input_filename = 'input.txt' 
output_filename = 'output.txt' 
read_and_write_file(input_filename, output_filename)
