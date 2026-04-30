# Freeciv(nation) · abkhaz

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/abkhaz.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的abkhaz定义

## 正文
```ruleset
[nation_abkhaz]

name=_("Abkhaz")
plural=_("?plural:Abkhazians")
groups="Asian", "European", "Medieval", "Early Modern", "Modern"

legend=_("Ancestors of Abkhazians have lived in the western Caucasus since\
 time immemorial. Short periods of independence alternated with domination\
 by the Greeks, Romans, Byzantines, Turks, Russians and Georgians.\
 Nowadays Abkhazia is a partially recognized republic.")

leaders = {
 "name",                "sex"
 "Leon II",             "Male" ; Abkhazian tsar
 "Bagrat I",            "Male" ; Abkhazian tsar
 "Nestor Lakoba",       "Male" ; Leader of the Autonomous Republic of
                               ; Abkhazia before 1936
 "Vladislav Ardzinba",  "Male" ; 1st president of Abkhazia
 "Sergey Bagapsh",      "Male" ; Current president of Abkhazia
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Fundamentalism",  _("Imam %s"),      _("Imama %s")
}

flag="abkhazia"
flag_alt = "-"
style = "Classical"


init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "ossetian", "georgian", "circassian", "russian"

cities =
 "Aqwa",	;Sukhumi
 "Gagra",	;Gagra
 "Gal",		;Gal
 "Gwdowtha",	;Gudauta
 "Afon Tshyts",	;New Athos
 "Ochamchyra", 	;Ochamchira
 "Pitsunda",	;Pitsunda
 "Tqwarchal",	;Tkvarcheli
 "Blabyrkhwa",	;Blabyrkhua
 "Kaldakhwara",	;Kaldakhuara
 "Adzoybzha", 	;Adzyubzha
 "Thkhyna",	;Tkhina
 "Acgwara",	;Achigvara
 "Zhwandryphsh", ;Zvandripsh
 "Lykhny",	;Lykhny
 "Agwy-Bedia",	;Agubedia
 "Aradu",	;Aradu
 "Tsandripsh",	;Tsandripsh
 "Baslakhw",	;Baslakhu
 "Pshwy",	;Pskhu
 "Gwylryphsh",	;Gulripsh
 "Dwryphsh",	;Duripsh
 "Elyr",	;Ilori
 "Kutol",	;Kutol
 "Arakacy",	;Arakich
 "Mokva",	;Mokva
 "Tamysh",	;Tamysh
 "Gachryphsh",	;Gyachripsh
 "Arasadzykh",	;Arasadzykh
 "Athara-Aerman", ;Atara-Armianskaia
 "Athara-Aphsua", ;Atara
 "Awadhara",	;Avadhara
 "Bedia",	;Bedia
 "Bzyph",	;Bzyb
 "Chkhalta",	;Chkhalta
 "Cuburkhyndzh", ;Chuburkhindji
 "Guma",	;Guma
 "Bargap",	;Kvemo Barghebi
 "Labra",	;Labra
 "Mysra",	;Myussera
 "Psou",	;Psou
 "Khlou",	;Chlou
 "Azhara",	;Azhara
 "Kwachira",	;Kochara
 "Gwymrysh",	;Gumrysh
 "Uataph",	;Otap
 "Phakwash",	;Pakuash
 "Kyndyg",	;Kyndygh
 "Gwdaa",	;Gudava
 "Gwyph",	;Gup
 "Markwyla",	;Merkula
 "Reka"		;Reka




```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
