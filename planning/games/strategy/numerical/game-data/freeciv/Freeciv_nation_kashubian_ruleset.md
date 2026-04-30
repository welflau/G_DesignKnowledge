# Freeciv(nation) · kashubian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/kashubian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的kashubian定义

## 正文
```ruleset
[nation_kashubian]

name=_("Kashubian")
plural=_("?plural:Kashubians")
groups="European", "Medieval"
legend=_("Kashubia is a historical region of north-central Poland.\
 The name of the land, whose etymology is still unknown, was first\
 mentioned in the 13th century. Considered as an ethnic group of\
 the Polish nation, Kashubians have language and culture that are\
 quite different from the rest of Poland. Today, a lively Kashubian\
 community cultivates their speech, literature and customs\
 through, among others, local radio and television programmes,\
 comic books, and even several fully Kashubianized distributions\
 of Linux operating system.")

leaders = {
 "name",                 "sex"
 "Świętopełk II Wielki", "Male"
 "Mściwoj I",            "Male"
 "Mściwoj II",           "Male"
 "Racibor",              "Male"
 "Sambor II",            "Male"
 "Świętobór I",          "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Prince %s"),       _("Princess %s")
 "Fundamentalism",  _("Archbishop %s"),   _("?female:Archbishop %s")
 "Monarchy",        _("Grand Prince %s"), _("Grand Princess %s")
}

flag = "kashubia"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "western pomeranian", "greater polish", "prussian"

cities =
 "Gduńsk (ocean)", ;Gdańsk
 "Gdiniô (ocean)", ;Gdynia
 "Sopòt (ocean)", ;Sopot
 "Hél (ocean)", ;Hel
 "Pùck", ;Puck
 "Wejrowò", ;Wejherowo
 "Jastarniô", ;Jastarnia
 "Réda", ;Reda
 "Kòscérzëna", ;Kościerzyna
 "Brusë", ;Brusy
 "Kartuzë", ;Kartuzy
 "Żukòwò", ;Żukowo
 "Rëmiô", ;Rumia
 "Wiôlgô Wies", ;Władysławowo
 "Bëtowò", ;Bytów
 "Chmielno",
 "Srôkòjce", ;Sierakowice
 "Chònice", ;Chojnice
 "Kòsôkòwò", ;Kosakowo
 "Kôrsëno", ;Karsin
 "Nowô Karczma", ;Nowa Karczma
 "Gniewino",
 "Krokòwa", ;Krokowa
 "Chòczewò", ;Choczewo
 "Lëniô", ;Linia
 "Lëzëno", ;Luzino
 "Łãczëce", ;Łęczyce
 "Szemôłd", ;Szemud
 "Céwice", ;Cewice
 "Czôrnô Dãbrówka", ;Czarna Dąbrówka
 "Lëpnica", ;Lipnica
 "Stãżëca", ;Stężyca
 "Tëchòmié", ;Tuchomie
 "Przedkòwò", ;Przodkowo
 "Sëlëczëno", ;Sulęczyno
 "Somònino", ;Somonino
 "Dzemiónë", ;Dziemiany
 "Lëpùsz", ;Lipusz
 "Kònarzënë", ;Konarzyny
 "Przechlewò", ;Przechlewo
 "Parchòwò" ;Parchowo


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
