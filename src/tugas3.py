import csv

def calculate_area(width, height):
    return width * height

def solve_rectangles(file_path):
    # Open the CSV file
    with open(file_path, 'r') as file:
        # Read the contents of the file
        reader = csv.reader(file)
        rows = list(reader)

        # Add a new column header for the area
        rows[0].append('Area')

        # Process each row starting from the second row
        for row in rows[1:]:
            # Get the width and height from the row
            width = int(row[0])
            height = int(row[1])

            # Calculate the area
            area = calculate_area(width, height)

            # Append the area to the row
            row.append(area)

    # Write the updated rows back to the CSV file
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Provide the path to your CSV file
file_path = 'data/dataarea.csv'

# Call the function to solve the rectangles
solve_rectangles(file_path)
