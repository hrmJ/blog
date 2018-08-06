<!--
.. title: App picks: gscholar, xapers
.. slug: app-pick-gscholar
.. date: 2018-08-06 12:22:09 UTC+03:00
.. tags: apps, command-line, citations
.. category: apps
.. link: 
.. description: Two recent apps I found extremely useful in writing with a command-line centered workflow
.. type: text
-->

Just a quick shout-out to [gscholar](https://github.com/venthur/gscholar). 
Google scholar is, of course, a major part of my workflow in writing
articles. I especially often use it to quickly grab a bibtex entry for 
a reference I am using. Well, that process just got a nugde quicker, since
I found a command line app to search for the bibtex entries.

It's a python app, so just `pip install gscholar`. After that, run
a query, e.g.  `gscholar "gelman prior distributions for variance parameters"`
and you'll immediately get a bibtex output, which you can for instance pipe
further to append to your `.bib` file. Awesome!

Here is the output of the example query above:

```
@article{gelman2006prior,
  title={Prior distributions for variance parameters in hierarchical models (comment on article by Browne and Draper)},
  author={Gelman, Andrew and others},
  journal={Bayesian analysis},
  volume={1},
  number={3},
  pages={515--534},
  year={2006},
  publisher={International Society for Bayesian Analysis}
}

```

Another related command line app worth mentioning is
[xapers](https://finestructure.net/xapers/). It's a tool for indexing all your
research-related pdfs into one big searchable databes of references. A full
`.bib` file can be imported  (just add a `file={/pth/to/file.pdf}` line to your
bibtex entries) by running `xapers import myrefs.bib`. After the import, you
can search for any string that you remembered occured in some of the references
(but can't remember which one) by just `xapers search 'find this string'`. If
the file was found, just hit enter to open it with your default pdf viewer
([zathura, right?](https://pwmt.org/projects/zathura/)) and repeat the search
there to get the page number.
