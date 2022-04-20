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
So, assuming we've found an article with a doi on the internet,
 we can run: `xapers add --source=doi:10.1214/009053604000001048`
to add the paper to our index. If we also found a downloadable pdf,
we can specify it 
as well: `xapers add --source=doi:10.1214/009053604000001048 --file=/tmp/gelman2005.pdf`

3. To add a paper that was indexed this way to your local bibtex file, you can first use `xapers show`
to view the entry in xapers and then hit `ALT-B` on the entry. This copies the bibtex entry
of the paper to clipboard for you to paste it in your .bib file.
