import re
import pandas as pd

# Define the regular expression pattern for extracting name and line
pattern = r'(^[a-zA-Z\s]+):(.+)'

# Create an empty dictionary to store the extracted data
data = {
    'name': [],
    'line': [],
}

# Open the transcript file and read its lines
with open('TheOfficeTranscript.txt', 'rt') as file:
    # Iterate through each line in the file
    for line in file.readlines():
        # Use regular expression to find the name and line in each line of the file
        match = re.findall(pattern, line)
        if match:
            # Extract the name and line from the matched pattern
            name, line = match[0]
            # Add the extracted data to the dictionary
            data['name'].append(name)
            data['line'].append(line)

# Create a DataFrame from the extracted data
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())

# Count the number of occurrences where the name is 'Michael' and print the result
print("Occurrences of 'Michael':", sum(df['name'] == 'Michael'))

# Print the total number of rows in the DataFrame
print("Total rows:", len(df))

# Save the DataFrame to a CSV file without including the index column
df.to_csv('TheOfficeTranscript.csv', index=False)
