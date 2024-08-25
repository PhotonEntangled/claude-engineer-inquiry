import io

file_path = r"C:\Projects\Luminator\luminator_core\claude-engineer\code_execution_env\Include\agency-swarm_contents.txt"

try:
    with io.open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    print(content[:1000])  # Print the first 1000 characters to avoid overwhelming the output
    print("\n\nFile read successfully. Total characters:", len(content))
except Exception as e:
    print(f"An error occurred: {str(e)}")