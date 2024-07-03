import os
import shutil
import csv

# Define source and destination folders
source_folder = 'C:/Users/Aroshish/Desktop/Sci-Tech/Epoch/datasets/alphabets_dataset/alphabet_images'
destination_folder = 'C:/Users/Aroshish/Desktop/Sci-Tech/Epoch/datasets/alphabets_dataset/alphabet_reduced'
csv_file_path = 'C:/Users/Aroshish/Desktop/Sci-Tech/Epoch/datasets/alphabets_dataset/file_labels.csv'

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Open the CSV file in append mode
with open(csv_file_path, mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Copy images from image_1 to image_1000 and write to CSV
    for i in range(366376, 367376):
        file_name = f'image_{i}.png'  # or .png or the actual extension
        src_file = os.path.join(source_folder, file_name)
        dst_file = os.path.join(destination_folder, file_name)
        
        if os.path.exists(src_file):
            shutil.copy(src_file, dst_file)
            csv_writer.writerow([file_name, 'Z'])  # Write the file name and label to the CSV
        else:
            print(f'File {src_file} does not exist.')

print('Images copied and data appended to CSV file successfully!')
