#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #1t=35840oz 1stone=224oz 1lb=16oz 

    #1t=2240lbs 1kg=2.2lbs 1lb=454g 

    #1oz=28.375g

    #imperial to metric conversion
    print("Imperial To Metric Conversion \n")

    #input for tons, stone, lbs, ounces
    tons=input("Enter the number of tons: ")
    stone=input("Enter the number of stone: ")
    lbs=input("Enter the number of pounds: ")
    oz=input("Enter the number of ounces: ")

    #math time figure out how to convert 
        #headache time :3
    #starting with the given formula 
    totalOz=(35840*float(tons))+(224*float(stone))+(16*float(lbs))+float(oz) 
    totalKilos=float(totalOz)/35.274 
    metricTons=int(totalKilos)//1000 #had to use AI to find out what the floor division operator was and then research how it worked!
    #learning is so fun
    #i then realized that you just made the entire variable an integer but we're committing to this
    kilos=float(totalKilos%1000) 
    flatKilos=int(kilos) #borrowed this line from GPT, creating an integer of it allows me to subtract this value from the total
    #thus giving me the decimals alone to be converted back into grams 
    #genuinely have no idea how I would have figured it out but now I know how it works and that rocks
    #i mean i would have reached it eventually but it would have taken my like 17hrs longer
    grams=float(kilos-flatKilos)*1000 
    #this grams section took a lot of debugging to figure out and some aid from GPT 
    #i promise nothing was copy/pasted as is apparent by how jank this is
    

    #output for metric weights
    print("\nThe metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(metricTons, flatKilos, grams ))






    # YOUR CODE ENDS HERE

main()