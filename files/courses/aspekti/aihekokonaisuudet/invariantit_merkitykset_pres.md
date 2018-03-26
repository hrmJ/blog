---
title       : Aspekti- ja liikeverbiteoria
author      : Juho Härme
job         : tohtorikoulutettava / käännöstiede venäjä
framework   : revealjs        # {io2012, html5slides, shower, dzslides, ...}
revealjs    : {theme: sky, transition: linear, center: "false"}
highlighter : highlight.js  # {highlight.js, prettify, highlight}
hitheme     : tomorrow      # 
widgets     : mathjax            # {mathjax, quiz, bootstrap}
mode        : selfcontained # {standalone, draft}
knit        : slidify::knit2slides
logo        : slidify_logo.png

---

<link rel="stylesheet" type="text/css" href="tyylit.css">

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

# Aspektin invariantit merkitykset

---

### Aspektuaalisuus ja aspektin kategoria


<article class='newbubble bgblue fragment'>
Aspekti muodostaa näkökulman toimintaan, tarkemmin sanottuna toiminnan rakenteeseen
</article>


<article class='mmbubble bgcyan fragment'>
<div class='defheader'>Aspektuaalisuus</div> 
>- Janne oli aamulla syönyt puuro<span class='fragment highlight-red'>a</span>, kun puhelin oli soinut.
>- Janne oli juuri syönyt puuro<span class='fragment highlight-red'>n</span>, kun puhelin soi.
>- Janne teki kuolemaa / oli kuole<span class='fragment highlight-red'>maisilla</span>an
</article>

<article class='mmbubble bggreen fragment'>
<div class='defheader'>Aspektin kieliopillinen kategoria</div> 
>- Когда зазвонил телефон, Янне <span class='r'>ел</span> кашу
>- Когда зазвонил телефон, Янне (уже) <span class='r'>съел</span> кашу
>- Янне <span class='r'>умирал</span> 
</article>

.fragment Kontrastiivisen lähestymistavan hyödyt!

---

### Aspektien invariantit merkitykset

*Общие видовые значения, vrt. частные видовые значения*

>- Imperfektiivinen ja perfektiivinen aspekti
>- Privatiivi oppositio: tunnusmerkillisyys ja tunnusmerkittömyys

--- .class &vertical

### Määritelmiä

<article class='newbubble bgblue fragment'>
<div class='defheader'>Määritelmä 1.</div> 
imperfektiivinen aspekti ilmaisee toiminnan keskeneräisenä, kun taas perfektiivinen loppuun suoritettuna.
</article>

<article class='afterbub'>
<br>
>- Вчера я читал одну интересную книгу
>- Вчера я прочитал одну интересную книгу
</article>

***

>- Ковальчук о чем-то пошутил с Уодделлом и басисто <span class='r'>засмеялся</span>
>- Я не помешал вам?
>- В ваших словах я почуствовал упрек

***

<article class='newbubble bgcyan fragment'>
<div class='defheader'>Määritelmä 2.</div> 
Imperfektiivinen ja perfektiivinen aspekti eroavat toisistaan siinä, että
perfektiivinen aspekti kuvaa toimintaa sisäisesti rajattuna kun taas
imperfektiivinen aspekti jättää näkokulman toiminnan sisäiseen rakenteeseen
auki.
</article>

***

>- Самолет <span class='fragment highlight-red'>исчез</span>, уходя все дальше за облака
>- Будто он еще видел там многое и многое, что стушевывалось и <span class='fragment highlight-red'>исчезало</span> понемногу, уходя во тьму ночи

***

![invariantit merkitykset kuvioina](images/invariants.png)

>- Мы <span class='fragment highlight-red'>поужинали</span> после noлуночи 
>- Мы <span class='fragment highlight-red'>ужинали</span> после noлуночи 

--- .class &vertical

### Moniselitteisemmän määritelmän rakentaminen

<article class='newbubble bgcyan fragment'>
<div class='defheader'>Määritelmä 2.</div> 
Imperfektiivinen ja perfektiivinen aspekti voidaan määritellä sen mukaan, <span class='fragment highlight-red'>mitkä
piirteet ovat niille tyypillisiä, mitkä harvinaisia tai mitkä mahdottomia</span>. Ei
voi yksiselitteisesti väittää, että jompikumpi tai molemmat aspektit ovat vain yhden
ominaisuuden ilmentymiä, vaan monimutkaisia yhdistelmiä useista eri piirteistä.
</article>

***

<article class='mmbubble bgblue fragment'>
Toiminnan käsittäminen kokonaisuutena *(целостность)*


</article>

<article class='mmbubble bgcyan fragment'>
Prosessuaalisuus (процессность)


</article>

<article class='mmbubble bgred fragment'>
Kesto (длительность)


</article>

<article class='mmbubble bggreen fragment' >
Toiminnan ajallinen lokalisoitavuus (временная локализованность)

- Miten toiminnan ajallinen konteksti voidaan lukita tai olla lukitsematta:
- Lukitseminen tiettyyn hetkeen: сейчас, однажды
- Lavea ajallinen konteksti: обычно, всегда


</article>


<article class='afterbub' >
<br><br>
>- Затоплю камин, стало прохладно… Вдруг раздается резкий звонок телефона 
>- он всё бежал
>- \*он всё прибежал
>- Ты будешь обедать? 
>- Ты читал "Койриен Калевала"?
>- Он часто скажет что-нибудь, не подумав, а потом жалеет.
</article>

--- .class &vertical

### Kotitehtävä

.fragment Tustustu venäjän kansalliskorpuksen (nkrj) käyttöön ja pohdi invarienteille merkityksille tyypillisiä piirteitä löytämissäsi esimerkeissä.

>- Etsi imperfektiivisen aspektin ja perfektiivisen aspektin indikatiivimuotoja
>- Ota talteen joitakin selkeitä esimerkkejä ja pohdi, mitä luennolla käsitellyistä erityispiirteistä niissä havaitset
>- Lisää wikiin ainakin itse esimerkit, voit lisätä myös piirteitä

***

### Pohdittavaksi:

.fragment Miksi perfektiivinen aspekti ilmaisee futuuria? Voiko imperfektiivinen ilmaista?


<script>
$('ol.incremental li').addClass('fragment')//note to anyone reading this code, you may need to change to ul from ol depending on ordered vs unordered list
$('ul.incremental li').addClass('fragment')//note to anyone reading this code, you may need to change to ul from ol depending on ordered vs unordered list
</script>
