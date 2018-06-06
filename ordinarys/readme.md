# Ordinary's Accounts (OAs)

The [Accounts of the Ordinary (chaplain) of Newgate](https://www.oldbaileyonline.org/static/Ordinarys-accounts.jsp) were published from the 1670s to the 1770s. They were printed pamphlets which contained accounts of the lives and behaviour of prisoners executed at Tyburn. The [Old Bailey Online](https://www.oldbaileyonline.org) has published all surviving accounts relating to convicts tried at regular sessions of the Old Bailey court. 

Data
------

This repository contains plain text versions of the Ordinary's Accounts which have been derived from the [XML files](https://doi.org/10.15131/shef.data.4775434), and some very basic metadata.

### texts

475 .txt files in [oa_txt](oa_txt)

The filename for each text is the Old Bailey Online OA ID, so that the files can easily be cross-referenced to the website.

The plain text was extracted from the XML using the Python BeautifulSoup library. Paragraph tags were replaced with line breaks and all other XML formatting was removed.

### metadata

**oa_ordinarys_20180507.csv**

The metadata gives the OA ID, date (yyyy-mm-dd format) and name of the Ordinary for each text. At a later stage this may be expanded to include the names of the executed criminals in each OA and links to their OBO trials.

The Ordinary names have been compiled from a number of sources.

* the starting point was a list of dates for Ordinaries on [Wikipedia](https://en.wikipedia.org/wiki/Ordinary_of_Newgate%27s_Account)
* this was checked against author names on title pages of the OAs themselves* 
* OAs background info on Old Bailey Online 

\* I didn't check every single OA, but concentrated on dates around changeovers between personnel as there were occasional discrepancies between the two sources; where this was the case I used the title page data rather than Wikipedia. 

Acknowledgments
--------

The data has been created using the transcriptions of the Ordinarys Accounts published at London Lives. I am deeply grateful to Tim Hitchcock and Bob Shoemaker, the London Lives project directors, for agreeing to share the data.


Re-use
---------

The dataset and all accompanying documentation are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).
