def read_and_write_file():
    try:
        # Ask the user for the input and output filenames
        input_filename = input("Enter the filename to read from: ")
        output_filename = input("Enter the filename to write to: ")

        # Open the input file for reading
        with open(input_filename, 'r') as input_file:
            content = input_file.read()  # Read the entire content of the file

        # Modify the content (in this case, convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to the new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Content from {input_filename} has been successfully modified and written to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: There was an issue with reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function to perform the file read and write
read_and_write_file()
