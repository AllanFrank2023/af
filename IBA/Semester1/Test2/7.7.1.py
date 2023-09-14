#Many companies pay time-and-a-half for any hours worked above 40 in a given week. 
#Write a program to input the number of hours worked 
#and the hourly rate and calculate the total wages for the week.

#TimeSkema

print("Velkommen til dit ugen time-beregner")

timer = float(input("Indtast timeantal :  "))

if timer > 40.0:
    overtid = timer - 40
    overtidsløn = (overtid * (1.5 * 300))
    print("Din overtid er:", overtid, " udbetaling af overtid i denne uge er (timeløn 300kr) ", overtidsløn)
else: 
        print("Du har ingen overtid i denne her uge")



