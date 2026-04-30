# Freeciv(nation) · dryad

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/dryad.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的dryad定义

## 正文
```ruleset
[nation_dryad]

name=_("Dryad")
plural=_("?plural:Dryads")
groups="Imaginary"
legend=_("Dryads are creatures of Greek myth; they are a type of nymph\
 associated with trees. Dryads were generally considered to be shy and\
 long-lived. They are usually female and are often depicted as beautiful\
 young women.")

leaders = {
 "name",        "sex"
 "Melia",       "Female" ; One of the Meliae (according to Hesiod)
 "Leuce",       "Female" ; White poplar, daughter of Oceanus

; Following hamadryads from Deiphnosophistae of Athenaeus
 "Karya",       "Female" ; Walnut or hazelnut
 "Balanos",     "Female" ; Oak
 "Kraneia",     "Female" ; Dogwood
 "Morea",       "Female" ; Mulberry
 "Aigeiros",    "Female" ; Black poplar
 "Ptelea",      "Female" ; Elm
 "Ampelos",     "Female" ; Vines
 "Syke",        "Female" ; Fig
}

flag="dryad"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

cities =
 "Artemis's Arboretum",	; Dryads are associated with Artemis

 ; Types of dryads
 "Hamadryad",		; Nymphs bonded with a specific tree
 "Napaeae",		; Nymphs who live in wooded valleys

 ; Types of nymphs by tree
 "Meliae",		; ash
 "Empimeliad",		; apple
 "Caryatids",		; walnut

 ; famous trees in Europe
 "Old Tjikko",		; Norway spruce in Sweden -  9,500 years old
 "Fortingall Yew",	; Yew in Scotland - between 2,000 and 5,000 years old
 "Caesarsboom",		; tree in Belgium - Julius Caesar tied a horse to it
 "Granit Oak",		; Oak in Bulgaria - 1,650 years old
 "Bartek",		; Oak in Poland - 650 years old
 "Gernikako Arbola",	; Oak in Spain
 "Queen Elizabeth Oak",	; Oak in England
 "Kongeegen",		; Oak in Denmark - 1,200 years old
 "Stoke Gabriel",	; Yew in England
 "Major Oak",		; Oak in England - 800 years old
 "Ivenack Oak",		; Oak in Germany - 800 years old
 "Baikushev's Pine",	; Pine in Bulgaria - 1,300 years old
 "Stelmužė Oak",	; Oak in Lithuania - 1,500 years old
 "One Hundred Horses",	; Chestnut in Italy - 4,000 years old
 "Merlin's Oak",	
 "Glastonbury Thorn",	; Hawthorn
 "Thor's Oak",
 "Royal Oak",
 "Hippocrates Plane",

 ; names of types of trees in English  (mostly Mediterranean)
 "Olive",
 "Chestnut",
 "Mulberry",
 "Terebinth",
 "Ash",
 "Apple",
 "Walnut",
 "Aleppo Pine",
 "Yew",
 "Fig",
 "Walnut",
 "Hazelnut",
 "Dogwood",
 "Black Poplar",
 "White Poplar",
 "Elm",
 "Vine",
 "Juniper",
 "Almond",
 "Kermes Oak",
 "Cedar",
 "Withy",
 "Cherry",
 "Cypress",
 "Fir",
 "Frankincense",
 "Laurel",
 "Eucalyptus",
 "Pomegranate",
 "Strawberry Tree",
 "Myrtle",
 "Oleander",
 "Mastic",
 "Oriental Sweetgum",
 "Stone Pine",
 "Holm Oak",
 "Hawthorn",
 "Aspen"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
