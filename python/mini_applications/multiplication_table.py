# Mike Wilson 28 November 2021
# This program creates a short mulitplication quiz
import pyinputplus as pyip
import random, time

# Set the number of questions
questions = 10

# Store correct answers
correctAnswers = 0

# Main loop for the program
for questionNumber in range(questions):
  num1 = random.randint(0, 12)
  num2 = random.randint(0, 12)

  prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

  try:
    pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
    blockRegexes=[('.*', 'Incorrect!')],
    timeout=8, limit=1) # Timeout in number of seconds, limit is number of tries
  except pyip.TimeoutException:
    print('Out of time!')
  except pyip.RetryLimitException:
    print('Out of tries!')
  else:
    print('Correct!')
    correctAnswers += 1
    time.sleep(2) # Gives users 2 seconds to see answer before next question.
print('Score: %s / %s' % (correctAnswers, questions))