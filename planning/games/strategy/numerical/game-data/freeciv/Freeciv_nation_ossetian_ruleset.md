# Freeciv(nation) · ossetian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ossetian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ossetian定义

## 正文
```ruleset
[nation_ossetian]

name=_("Ossetian")
plural=_("?plural:Ossetians")
groups="Asian", "Medieval", "Modern", "European"
legend=_("Modern Ossetians are the successors of the Alans of Ancient\
 history, who fled into the mountains during the Hunnic invasions. Around\
 800 CE an Alanic kingdom emerged in the Northern Caucasus, which\
 continued to exist until the Mongol invasions. Nowadays Ossetians live\
 in the Republic of North Ossetia (part of the Russian Federation) and in the\
 partially recognized Republic of South Ossetia.")

leaders = {
 "name",                "sex"
 "Khuddan",             "Male" ; Tsar of Alania
 "Dauyt Soslan",        "Male"
 "Maria Shvarnovna",    "Female"
 "Bagatar",             "Male" ; Last tsar of Alania
 "Torez Kulumbegov",    "Male" ; Leader of Southern Ossetia
 "Eduard Kokoity",      "Male" ; Current president of Southern Ossetia
}
ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Tsar %s"),      _("Tsaritsa %s")
 "Fundamentalism",  _("Patriarch %s"), _("Matriarch %s")
}
flag="ossetia"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "georgian", "abkhaz", "russian"

cities =
"Tskhinval",	;Tskhinvali
"Dzæudjyqæu",	;Vladikavkaz
"Maas",		;Capital of Medieval Alania
"Mæzdæg",	;Mozdok
"Kuaysa",	;Kvaysa
"Beslæn",	;Beslan
"Alagir",	;Alagir
"Ærydon",	;Ardon
"Digoræ",	;Digora
"Brytat",	;Britata
"Dywwædonastæu", ;Duadonastau
"Znawyr",	;Znaur
"Chekh",	;Kekhvi
"Edys",		;Edisa
"Kurta",	;Kurta
"Leningor",	;Akhalgori
"Tbet",		;Tbeti
"Kostayyqæu",	;Khetagurovo
"Chikola",	;Chikola
"Dzaw",		;Java
"Oktyabryqæu",	;Oktyabrskoye
"Tamares",	;Tamarsheni
"Myzur",	;Mizur
"Wællag Fiyyagdon", ;Verkhny Fiagdon
"Zavoskoy",	;Zavodskoy
"Qyzlar",	;Kizlyar
"Wanel",	;Vaneli
"Nogir",	;Nogir
"Astæukkag Еrman", ;Shua-Ermani
"Sunjæ",	;Sunzha
"Qemulta",	;Kemulta
"Særidtatæ",	;Saritata
"Badzigat",	;Badzhigata
"Khodz",	;Khodz
"Khod",		;Khodi
"Tsægat Tsipran", ;Chrdilo-Chiprani
"Sokhtæ",	;Sokhta
"Næzydjyn",	;Nazigina
"Kotanto",	;Kotanto
"Mikhaylobskæy", ;Mikhaylovskoye
"Elkhot",	;Elkhtovo
"Qola",		;Kola
"Chermen",	;Chermen
"Qroz",		;Kroza
"Cheliat",	;Cheliata
"Gufzabar",	;Duzhabauri
"Dællag Erman",	;Dallag Erman
"Raro",		;Raro
"Khussar Tsipran", ;Samkhret-Chiprani
"Kabuztæ",	;Kabuzta
"Dællag Ursdzwa", ;Kvemo-Bakarta
"Awnew",	;Avnevi
"Arkhonskæ",	;Arkhonskaya
"Bægiatæ",	;Bagiata
"Buzala",	;Buzala
"Litsi",	;Litsi
"Cheselt"	;Keshelta

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
