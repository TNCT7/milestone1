"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:


File_Questions = open("Question.txt","r")
File_Questions_Content = File_Questions.readlines()
File_Questions.close()

print(File_Questions_Content)

Questions_altered = []

for Questions in File_Questions_Content:
    if Questions.find("\n") != -1:
        Questions = Questions.replace("\n", "")
        Questions = Questions.rsplit("=")
        print(Questions)
        Questions_altered.append(Questions)

print(Questions_altered)
counter = 0

print(f"What is {Questions_altered[0][0]}")
Question1 = input("Enter Answer")
if Question1 == Questions_altered[0][1]:
    counter += 1

print(counter)


print(f"What is {Questions_altered[1][0]}")
Question1 = input("Enter Answer")
if Question1 == Questions_altered[1][1]:
    counter += 1

print(counter)

print(f"What is {Questions_altered[2][0]}")
Question1 = input("Enter Answer")
if Question1 == Questions_altered[2][1]:
    counter += 1

print(counter)

Final_Result = f"Your score is {counter}/{len(File_Questions_Content)}"

File_Write = open("Results.txt","w")
File_Write.write(Final_Result)
File_Write.close()

