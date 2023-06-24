#Create a csv file to write the image path so it works seamlessly with clarifai py program

import csv
import os

def create_csv(first_name, last_name, image_path, destination_path):
    filename = 'output.csv'  # Change this to your desired filename
    filepath = os.path.join(destination_path, filename)
    
    # Create a list containing the header and data
    header = ['First Name','Last Name','White','Black','Asian','Other','Highest Prob. Score','Filler','Image']
    data = [[first_name, last_name, '','','','','','',image_path]]
    
    # Write the data to a CSV file
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
    
    print(f'CSV file "{filename}" created successfully at "{destination_path}".')

    print(filepath)
# Example usage:
#create_csv('John', 'Doe', '/Users/eoutangoun/Documents/aiwebsite/uploads/cropped.jpg', '/Users/eoutangoun/Documents/aiwebsite/uploads')

