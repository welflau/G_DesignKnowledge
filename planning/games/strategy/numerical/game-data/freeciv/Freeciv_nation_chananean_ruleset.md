# Freeciv(nation) · chananean

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/chananean.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的chananean定义

## 正文
```ruleset
[nation_chananean]

name=_("Chananean")
plural=_("?plural:Chananeans")
groups="Imaginary"
legend=_("Reports of chynocephaly (having the head of a dog or jackal)\
 can be traced to Greek Antiquity. The physician Ctesias and the traveler\
 Megasthenes placed them in India. In the middle ages, Giovanni da Pian\
 and Marco Polo made reference to them, while the theologian Ratramnus\
 debated whether they should be considered human or not. Various stories\
 have placed them in Scotland, Canaan, Cyrenaica, and the Andaman Islands.\
 The country 'Chananea' comes from the German poet Walter of Speyer. In\
 the account by Sir John Mandeville, the people were known as the\
 Nacumerians.")

leaders = {
 "name",        "sex"
 "Garwlwyd",    "Male" ; Arthurian legend
 "Christopher", "Male" ; St. Christopher is sometimes portrayed as a
                       ; chynocephali
 "Reprebus",    "Male" ; A chynocephali captured in the time of Diocletian
 "Laika",       "Female" ; The first dog in space (not a chynocephali, but
                         ; famous)
 "Anubis",      "Male"
 "Anput",       "Female"
 "Hermanubis",  "Male"
 "Cerberus",    "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Republic",        _("%s Alpha"),        _("?female:%s Alpha")
}

flag="chananea"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "werewolf", "alsatian"

cities =
 "Cynopolis",      ; 'City of Dogs' in Greek

 ; Constellations/stars
 "Canis Major",
 "Sirius",

 ; Classification 
 "Canidae",
 "Carnivora",

 ; Varieties
 "Akita Inu",
 "Malamute",
 "Hound", 
 "Basenji", 
 "Chow Chow", 
 "Wolfhound", 
 "Lhasa Apso", 
 "Pekingese", 
 "Saluki", 
 "Samoyed", 
 "Shar Pei", 
 "Shiba Inu", 
 "Shih Tzu", 
 "Husky", 
 "Terrier", 
 "Mastiff",
 "Jackal",
 "Jindo Gae",
 "Bloodhound"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
