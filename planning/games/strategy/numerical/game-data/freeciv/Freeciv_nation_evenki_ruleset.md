# Freeciv(nation) · evenki

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/evenki.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的evenki定义

## 正文
```ruleset
[nation_evenki]

name=_("Evenki")
plural=_("?plural:Evenks")
groups="Asian", "Early Modern"

legend=_("The Evenks are a Tungusic ethnic group in Siberia, Mongolia,\
 and northern China. Historical evidence suggests that they have lived\
 in the Baikal area on today's Russian-Mongolian border since the Stone\
 Age. When encountered by the Russians in the 17th century, the Evenks\
 were tribal hunter-gatherers and reindeer herders.")

leaders = {
 "name",                 "sex"
 "Zinaida Pikunova",     "Female" ; Evenki scientist and founder of RAIPON
 "Aleksandr Bokovikov",  "Male"   ; 1997 - 2001 governor of Evenkia
 "Mikhail Mongo",        "Male"   ; Evenki writer
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Fundamentalism",  _("Shaman %s"),      _("?female:Shaman %s")
}

flag="evenkia"
flag_alt="-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Yakut", "Siberian", "Manchu"

cities =
 "Tura", ; Тура
 "Burnyj", ; Бурный
 "Jessjej", ; Ессей
 "Kislokai", ; Кислокан
 "Kuzmovka", ; Кузьмовка
 "Kuyumba", ; Куюмба
 "Mutoraj", ; Муторай
 "Nidym", ; Нидым
 "Oskoba", ; Оскоба
 "Osharovo", ; Ошарово
 "Poligus", ; Полигус
 "Strjelka-Chunja", ; Стрелка-Чуня
 "Sulomaj", ; Суломай
 "Surinda", ; Суринда
 "Tutonchany", ; Тутончаны
 "Uchami", ; Учами
 "Chjemdalsk", ; Чемдальск
 "Chirinda", ; Чиринда
 "Ekonda", ; Эконда
 "Jukta", ; Юкта
 "Bajkit", ; Байкит
 "Vanavara", ; Ванавара
 "Mirjuga" ; Мирюга

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
