DASH=0.01

#Cocktail list
#  Name of Cocktail
#  Dict of Ingredients
#    Name of Spirit/Mixer : Proportion 
#    'Garnishes' if it exists, is a list of optional ingredients
#    'Directions' stipulates any further directions. Typically how to use garnishes/serve over ice
# ASSERT: Proportion < 1
# Portion=0 means it is required

cocktail_list={
"Abby Cocktail": {'Dry Gin': .5,'Kina Lillet':.25,'Orange Juice' :.25,'Garnishes':['Cherry'],'Directions':'Stir well in ice and strain. Add a Maraschino cherry'},
"Absinthe Special": {'Absinthe':.5,'Water':.5,'Syrup': DASH,'Angostura Bitters':DASH,'Directions':'Shake well and strain into glass'},
"Absinthe Cocktail":{'Absinthe':.5,'Water':.5,'Gomme Syrup': DASH, 'Angostura Bitters': DASH,'Directions':'Shake well with cracked ice and strain'},
"Absinthe Drip": {'Absinthe':.35,'Water':.6,'Sugar':0,'Directions':'Dissolve 1 cube of sugar, using the French drip spoon, and serve'},
"Affinity": {'Vermouth, Sweet':.33,'Bitters':2*DASH,'Vermouth, Dry":.33,'Scotch':.33,'Garnishes':['Cherry','Lemon Peel'],'Directions':'Stir well with cracked ice, strain, and serve with a Cherry and a twist of lemon Peel over top of the glass'},
"After Dinner #1": {'Brandy, Apricot':.5,'Curacao':.5,'Lime',0,'Directions':'Squeeze one lime with rind into drink. Shake well with cracked ice and strain'},
"After Dinner #2": {'Brandy, Prunelle':.5, 'Brandy, Cherry':.5, 'Lemon Juice':4*DASH,'Directions':'Stir well and strain into glass'},
"After Dinner #3": {'Brandy, Apricot':.5, 'Curacao':.5, 'Lemon Juice':4*DASH, 'Directions':'Stir Well and strain into glass'}
}# end cocktail list
