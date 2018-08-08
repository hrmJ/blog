<!--
.. title: Follow-up: more on xapers
.. slug: follow-up-more-on-xapers
.. date: 2018-08-08 11:39:08 UTC+03:00
.. tags: references apps
.. category: 
.. link: 
.. description: 
.. type: text
-->

A follow-up on the previous post about gscholar and xapers.

1. Xapers is also quite useful in getting bibtex entries. If you know
the doi of a reference, a bibtex entry can be retrieved
by typing `xapers source2bib URL`, 
e.g. `xapers source2bib doi:10.1214/009053604000001048`.

2. Or, why not, retrieve the paper to the local indexed database right away?
So, assuming we've found an article on the internet, it is open access
and has a doi, we can run: `xapers add --source=doi:10.1214/009053604000001048`
and lo and behold, the paper appears in our database.
