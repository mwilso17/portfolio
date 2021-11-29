# Mike Wilson 29 November 2021
# This program is a mini application that analyzes the number of words in a 
# .txt file and takes user input to calculate how long it will take them to
# read the text.

# path for the file.
filename = "python\\txt_files\wonderland.txt"

def calculate_reading_time(filename):
  '''Calculates the reading time for the file'''
  # Take user input and convert to an integer
  reading_speed = input('Enter your reading speed in words per minute: ')
  reading_speed = int(reading_speed)
  time_per_day = input('How many minutes per day will you read?: ')
  time_per_day = int(time_per_day)

  # The following code will analyze the file.
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError:
    print('File was not found. Please check filename.')
  else:
    words = contents.split()
    num_words = len(words)
    print(f"There are approximately {num_words} words in {filename}.")

  # Calculates inputs and rounds to a whole number.
  time_to_read = round(num_words/(reading_speed * time_per_day))
  print(f"It will take you about {time_to_read} days to finish this text.")

if __name__ == '__main__':
  calculate_reading_time(filename)


