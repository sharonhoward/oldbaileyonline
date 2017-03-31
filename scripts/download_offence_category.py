#download-offence-category.py

# read http://programminghistorian.org/lessons/downloading-multiple-records-using-query-strings for full explanations of the original code

#example here is for arson, 1751-1800 - adjust as needed

#this is what the URL looks like on the website: http://www.oldbaileyonline.org/search.jsp?foo=bar&form=searchHomePage&_offences_offenceCategory_offenceSubcategory=damage|arson&fromYear=1751&fromMonth=00&toYear=1800&toMonth=99&start=0&count=0

#you're interested in these bits:
#offenceCategory_offenceSubcategory=damage|arson
#fromYear=1751, fromMonth=00, toYear=1800, toMonth=99


import obo_offence_cat

query = 'damage|arson' #CHANGE

# if you wanted all offences in a main category like 'damage' that's used on its own; but whenever you want a subcategory like 'arson' you must include both category and subcategory, separated by | 



obo_offence_cat.getSearchResults(query, "1751", "00", "1800", "99", 17) #CHANGE (except for query)
 
#understanding parameters in getSearchResults: 
# 1. query (category - already taken care of)  
# 2. fromYear (year) 
# 3. fromMonth (00 to start at beginning of year, otherwise specify a month eg 03 for March), 
# 4. toYear (year)
# 5. toMonth (99 to finish at end of year or specify a month eg 11 for November), 
# 6. entries - the number of trials in the search set; you can find this by running the search on oldbaileyonline.org and click on 'Calculate total'

obo_offence_cat.getIndivTrials(query)

