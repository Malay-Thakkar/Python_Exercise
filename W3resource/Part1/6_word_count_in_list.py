# Write a Python program that prints long text, converts it to a list, and prints all the words and the frequency of each word.
input_string = input("Enter string: ")
word_list = input_string.split()
word_freq = [word_list.count(n) for n in word_list]

print("List:\n{}\n".format(str(word_list)))
print("Pairs (Words and Frequencies: \n {}".format(str(list(zip(word_list, word_freq)))))
