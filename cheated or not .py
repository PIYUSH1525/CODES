# Problem Statement: Rahul copies in the exam from his adjacent students. But he doesn’t want to be caught, so he changes words keeping the letter constant. That means he interchanges the positions of letters in words. You are the examiner and you have to find if he has copied a certain word from the one adjacent student who is giving the same exam, and give Rahul the markings he deserves.
# Note that: Uppercase and lowercase are the same.


def cheating(input1,input2):
    s = input1
    s1 = input2
    s = s.lower()
    s = sorted(s)
    s1 = s1.lower()
    s1 = sorted(s1)
    if s1 == s:
        return 1
    else:
        return 0
inp = input("enter the value")
inp1 = input("enter the value2")
result = cheating(inp, inp1)
print(result)
