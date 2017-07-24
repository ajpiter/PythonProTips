#BMI is calulated using killograms and centimeters, below is a formula for caluclating bmi after inputing inches and pounds.

heightininches = 64 
heightincentimeters = heightininches * 0.025 
weightinpounds =  125
weightinkilo = weightinpounds * .45
bmi = weightinkilo / heightincentimeters ** 2 
print(bmi) 
