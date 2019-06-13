
# Title

Good afternoon.

So, my presentation is a contrastive one about Russian time adverbials and
their location in the sentence, which I compare to Finnish time adverbials and
their location. This presentation is based on my dissertation work, in which
I analyze around 50 different temporal expressions. Here I am focusing on three
rather similar expressions, which are yesterday, last year and last week.

The outline of the presentation is as follows:

I start by presenting my data and showing, with the data, what is the basic
difference between Finnish and Russian in this respect. Then, I'll talk about
a phenomenon I call *the introductory construction* (ICx), which, I argue, is
a factor in explaning the differences. After that: I'll briefly present
statistical model I am using to test the credibility of the introductory
construction as an explanation. And finally, the most important part will be
the interpretation of the results of the statistical model.

# Data

Finnish and Russian are both languages with a so called free word order and 
such elements as time adverbials are among the most flexible with regard
to their location. To get a comparable data set of Finnish and Russian 
for analyzing the differences in the locations of time adverbials,
I am focusing on affirmitive SVO sentences. The languages are not identical in 
how they use SVO and SOV -- and, of course, Russian uses verb-initial
sentences a lot compared to Finnish -- but SVOs form a good enough
intersection where Finnish and Russian use similar sentences for similar 
kind of communicative purposes, so I'm using them for the comparison.
Im dividing the possible locations of the time adverbial to four:
before subject, verb and object (L1), between the subject and the verb (L2),
between the verb and the object (L3) and, finally, after the object (L4).


RUSSIAN EXAMPLE:


My data consists of around 8 thousand Finnish and Russian SVO sentences which
have been obtained by querying two sets of corpora. First of all, both Finnish
and Russian are included in the Aranea corpora compiled by mr. Vladimir Benko
-- these are corpora crawled from the Internet and they are similar in the
sense that they have been crawled using the same initial seeds for the crawler,
but of course, these are a very heterogenous collection of all kinds of texts
laying around in the world wide web (their sizes are around 1 billion tokens
each). Secondly, I am balancing the diversity of the internet texts by also
having for both of the languages a corpus of newspaper texts. For Russian, I am
using the newspaper subcorpus of the national corpus and for Finnish a
comparable newspaper corpus provided by the langauge bank of Finland. These
comprise around 250 000 words each.

So, how did I get from a billion words to 8000 SVO sentences? I started with
simple concordances, queried for *на прошлой неделе*, *в прошлом году*, *вчера*
and the Finnish expressions in the corpora and extracted all the contexts with
these. Then, I fed these contexts to dependency parsers and used the parsed
concordances to filter for me only sentences with a subject, finite verb and an object
and, in addition, tried to get only the cases where the adverbial is a direct
dependent of the finite verb. This means I excluded expressions like 
*приезжающий завтра президент любит спорт* where the adverbial is the dependent
of the participle form *приезжающий*, i.e. arriving. Of course, the parsers
are far from perfect and it's hard to define exactly what have been the precision
and recall of this method, but with my actual dissertation data (which is a lot 
more than what I'm presenting here) I've analysed a random sample of 500 
examples in both languages and on the basis of that the sentences
that have been included in my final data are about 90 % correct, i. e. 90 %
of the sentences in the data (in both languages, Russian was a bit better,
actually(?)) are what they should be.

So, as to the actual differences between the languages: first of all, and this 
was clear even beforehand, there is a difference in the locations adjacent to the verb
in that Russian prefers the position right before the verb (like in the exapmle
on the screen) and Finnish the one right after, i.e. L3.
These are, in many ways, the default adverbial positions. However, there is 
also an interesting difference in that Russian uses the sentence-initial
position a lot more than Finnish and, conversely, Finnish uses the sentence-final
position. Take a look at the following simple graph, in which we have
the distributions of the different locations in the Finnish data on the left
an for the Russian data on the right.


![plot of chunk unnamed-chunk-1](figure/unnamed-chunk-1-1.png)

My main focus in this presentation is the difference concerning the bars on the
left: why is it the case that with these three adverbials (LY, LW, Y) there is
such a strong emphasis on the sentence-initial position, especially compared to
Finnish? Actually, since the difference between L2 and L3 is grammatically 
predictable and not essential for this presentation, we can simplify the 
picture a bit by merging the central categories as in this plot, so
that we have a sentence-initial, sentence-final and a centric location:

![plot of chunk unnamed-chunk-2](figure/unnamed-chunk-2-1.png)

Now, there probably are multiple factors at work in why Russian and Finnish
contrast in this way. My goal here is to argue that one major part of the
explanation is what I call the *introductory time adverbial construction*.


# What is ICx


Now by using the term construction here I align myself with the linguistic
approaches that are usually described as constructionist or construction
grammar based approaches. Without going into details, the basic idea in
the constructionist approaches is to model language not as two separate components
-- lexicon and grammar -- but as a network of constructions, so that a
construction is a unit of language that has both form and meaning and can
contain (variable amounts of) lexical, syntactic and pragmatic information.
In the present contexts I am dealing these SVO sentences with a time adverbial
as units of language, stored, in one way or another in the memory
of Finnish and Russian language users. The important thing to note is 
that by assuming this  kind of knowledge of the language
I assume that the language user has information about in what kind
of contexts these constructions are used, in which parts of the text
and so on. 

So, below (and in your outline?) you can see an example
of a Russian construction with a sentence-inital (L1) time adverbial:

[tadaa]

And here is the broader context of the example

[tadadaa]

This is the kind of usage I refer to as the introductory construction (ICx).
If we look at the information structure of these sentences in the framework
presented by Knud Lambrecht, we could characterize these as *event-reporting*
sentences. By this I mean that at this point in text (or an oral discussion)
very little is presupposed to be known by the recipient of this message, i.e.
the reader. The writer uses the time adverbial as a kind of a comfortable 
way to start telling about an event, and this typically happens at the beginning
of a text. You could argue about the discourse function of the time adverbial:
in the Lambrechtian sense a topic of a sentence is *what the sentence is about*,
so you could -- in some cases, at least -- argue that the sentence 
is about yesterday, but this is not always very straight-forward.

My hypothesis regarding this construction is that these kind of sentences are
quite common in Russian and especially with the kind of temporal expressions
we are looking at in this presentation but rare in Finnish. What you
usually find in Finnish texts filling a similar kind of communicative 
role is a construction with an adverbial in positions L3 or L4. Of these
there are examples in the outline, but for the interest of time I will
not go through them here. Rather what I will do is present
a statistical model I used to test this hypothesis.


# Statistical model

When building a model to be used in testing the hypothesis about the role of
the introductory construction I started by trying to come up with what 
could possibly be some quantitatively retrievable indicators of the 
fact that some sentence with a time adverbial is, in fact, a representative 
of the kind of construction I just outlined.

The first -- and, probably, the vaguest -- indicator I came up with has to do 
with the fact that the kind of expressions I presentened in the previous examples  
(still on the screen?) seem to be typical for news texts, since they report
about an important event that occured, say, yesterday. So, in our statistical
model, if we are using the location of the adverbial as the variable we are 
trying to predict, the so-called dependent variable, that is, we could
use the type of the source corpus as on of the x-variables, that is
predictors (remember, the data is from a heterogenous internet corpus
and a newspaper corpus). 

<!--

Perhaps a slide with a few other examples but without contexts?

-->

The second indicator I ended up using was to test wether or not the referents
in the sentence with the adverbial have been -- in Lambrecht's terms, once again -- 
activated in the discourse. In these kind of sentences we should expect *inactive*
referents, that is, referents that have not yet been introduced but are introduced
in the sentence. I came to the conclusion that the easiest referent to test was
the subject of the sentence. The clearest case for an activated referent would be the
use of a pronoun. If we have a sentence like *On monday he took the children to school*
(to use an english example) we can safely assume that the sentence includes
cognitively *active* referents, i.e. doesn't present anything new.
Probably, the sentence *on monday he took the children to school* is located
somewhere in the middle of a text.
Besides pronouns it could be argued that often times when the subject
of a sentence consists of only one word, as in "On monday James... Smith... took"
it is likely to be active and when it consists of two or more as in "On monday
the head master of a local school in Prague made the decision to have a day off"
it is probably inactive. So, the second indicator  which became a predictor
in the statistical model was the length of the subject with the possible values "short"
and "long".


I also added a third indicator in the model. It might be argued that certain verbs
are more likely to be associated with the introductory construction than others, namely
verbs like *announce*, *declare* or *publish* -- these kinds of verbs of entering  to 
the scene (levin xxx) or *telling* in the Framenet project. These are, however, not 
straight-forward to come up with, so what I did was I scanned through what 
the parsers had marked as head verbs of the sentences in my Finnish and Russian data.
I took only the verbs that occured a minimum of 5 times <!-- ACTUALLY this 
has to be revised for the article --> and made an interperetation of whether or 
not this verb belonged to the presentational verbs typical for telling about new events 
or not. In the handout on the last page  you can find the most frequent verbs
in the data I marked as presentational. They include verbs like announce, present,
confirm, publish and other.

So, that makes the third predictor in the model: the presence or absence of a
presentational verb. As a fourth factor I took into account, which of the three adverbials
the sentence included (LY, LW or Y). This is the model I ended up with, which
is a categorical (or multinomial) regression model with the location (3 categories)
as the dependent variable and these three as the predictors. I am by no means
a statistician but I got help in making this a Bayesian regression model, so 
that we will not be considerd with p values and null hyptothesis here, but
rather can assess, how strongly we believe that each of the predictors
is associated with a certain location. In this case, I am especially interested
in which are associated with the sentence-initial location.

A crucial thing to note is that we are mainly not interested in the effects
of these predictors as such but rather in their interaction with language.
In other words, our model includes not only the four predictors listed
above but also a fifth one, language [tadaa]. So that we are not examining
just wether or not *a long subject* increases the probability of the sentence-initial
position in the data, but, wether or not *a long subject* increases
this probability in Russian compared to Finnish. The hypothesis 
is that since a sentence with a long subject is likely to occure as part 
of an event-reporting sentence located early on in the text, and since
I believe that Russian uses the sentence-initial location for these kind of introductory
constructions, long subjects should be associated with the first location 
in Russian but not in Finnish. Similarly, the press corpus should be associated
with L1 in Russian and the presentational verbs should be associated with L1 in Russian.



<!--

Bullets: first just *type of corpus*, then *length of subject*.

--->

# Results of the model

But how is it actually? The statistical model shows that, indeed, the above
assumptions about the association of the three indicators of the introductory
construction with location one in Russian are quite credible. Let me show you
three plots that demonstrate this.

This first one here shows the interaction effects of language and each of the
other predictors. As we can see..

The second one shows the effect of the different indicators on the probability
of L1 in Finnish compared to Russian. As you can see, the strongest effect.


So the hypothesis about the role of ICx seems credible, since each
of the indicators really is associated with L1 in Russian more strongly than in 
Finnish. Another interesting observation can be made, if we look at the effect
of the different adverbials on L1 in Finnish. It looks almost like a temporal
progression of some sorts: the expression denoting the time furthest away
in the past, that is, last year, is the most likely candidate for location 1
in Finnish and the most recent one, yesterday, the least likely.
Now this also fits rather nicely into the  hypothesis about the introductory
construction. It can be, namely, argued, that *yesterday* is the most likely candidate
to be used when reporting an event as news. I mean think about it: if something
happened last year, is that still news? On the other hand, last week -- this 
is definitely somewhere in between.

<!--

Only if time?? 

Here are a couple of Finnish examples with LY and L1:

Viime vuonna.. (subtopic)
Viime vuonna.. (numeric amounts)
According to my observations in the Finnish data, these are the kind of
situations *viime vuonna* is used in. The first is something I refer to as a
subtopic construction, in which a larger topic, say a life of a person is
divided into different temporal segments. The other one has to do with
expressing numerical amounts of something that has been achieved within the
time period of one year. These are both use cases especaially typical
for the expression "last year", which probably explains its prominence
in the  sentence-initial location in Finnish. 


-->


To illustrate the point about the effects of these predictors, possibly, a
little better, let's conclude by looking simple percentages of two kinds of
cases. First, we've got all the research data, including all the three
adverbials and all the sentences for each of these. As you might remember,
with these cases we have a situation shown in [this] figure (go back). So
Finnish L1 covers about 25 percent of all the cases, the central location
roughly 50 %. In Russian, L1 is at 67 and L2 at 25.

Now, if we narrow our focus to only cover the cases that include all the
indicators discussed above: so that we are going to have cases with a long
subject, from the newspaper corpora and with a presentational verb like
*объявить* and then zoom in further to only include cases with *yesterday*,
which seems to be more likely to be used in an introductory construction than
the other adverbials, we see these percentages change quite a bit (show the new
picture with 2 columns).


![Distributions of the three locations in the whole data set and in the data including all the indicators for ICx](figure/indandwithout-1.png)

The more dramatic change caused by the zooming in concerns Finnish: we notice that 
the usage of the sentence-initial position decreases to practically zero, and 80
percent of the cases now end up in the central location. With the Russian
data we don't observe this kind of a change. On the contrary: 
the sentence-initial position actually becomes *more* frequent, reaching
almost 80 %



# Conclusion

What should we conclude? I presented the ICx as an explanation and it seems
credible in the light of the quantitative indicators. Is this just a matter of
stylistic preference or are  there some typological issues at play? That is
something I haven't really taken a look at, since my work is mainly applied and
practical in nature. My goal is to provide language learners and especially
translators or anyone with a Finnish background producing a text in Russian and
vice versa with concrete data on how Finnish and Russian differ from one
another in this pragmatic respect that is not usually dealt with in translator
education. And I hope I have demonstrated how comparable corpora can be used
to gain insights into these kind of differences that are not, usually, visible 
to the naked eye.



# REF

cxg: goldberg etc
infra: lambrecht
fi/ru: kovtunova,janko,vilkuna, KING
stats: gelman, kruschke
parases: sharoff/nivre, tdt

<!--


# NOTES

Tämä venäjälle tyypillinen tapa tuoda diskurssiin uutta informaatiota ikään
kuin ajanilmaukseen nojaten on sinänsä tutkimuskirjallisuudessa tunnettu
ilmiö, ja siihen on kiinnittänyt huomiota muun muassa Tracy King [-@king1995,
101].


-->
