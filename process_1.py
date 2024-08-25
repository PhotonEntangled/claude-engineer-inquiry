import subprocess

file_path = r"C:\Projects\Luminator\luminator_core\claude-engineer\context\agency-swarm_contents.txt"

try:
    result = subprocess.run(['type', file_path], capture_output=True, text=True, encoding='utf-8', check=True)
    print(result.stdout[:1000])  # Print the first 1000 characters
    print(f"\n\nFile read successfully. Total characters: {len(result.stdout)}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while reading the file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")