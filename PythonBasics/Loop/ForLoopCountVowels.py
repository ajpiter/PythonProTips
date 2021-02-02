#Create a For Loop that counts the number of vowels in a string defined as Text 

Text = "Test a longer string with numerous vowels"
VowelCount = 0 

print("The vowels in the text provided include:")
for v in Text: 
    if v == 'A' or v == 'a' \
    or v == 'E' or v == 'e' \
    or v == 'I' or v == 'i' \
    or v == 'O' or v == 'o' \
    or v == 'U' or v == 'u': 
        print(v, ', ', sep='', end='')
        VowelCount += 1
print("") 
print('For a total of ', VowelCount, ' vowels.', sep='')

#Output 
#The vowels in the text provided include:
#e, a, o, e, i, i, u, e, o, u, o, e, 
#For a total of 12 vowels.
