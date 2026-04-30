# Freeciv(nation) · donetsk

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/donetsk.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的donetsk定义

## 正文
```ruleset
[nation_donetsk]

name=_("Donetsk")
plural=_("?plural:Donchyani")
groups="Modern", "European"
legend=_("The Donetsk People's Republic is an unrecognised republic of\
 Russia in the occupied parts of eastern Ukraine's Donetsk Oblast. It was\
 created by Russian-backed paramilitaries in 2014, and it initially\
 operated as a breakaway state until it was annexed by Russia in 2022.")
; Legend from: https://en.wikipedia.org/wiki/Donetsk_People%27s_Republic
leaders = {
 "name",                          "sex"
 "John James Hughes",             "Male"   ; (1814-1889) Founder of the city of Donetsk
 "Konstantin Kosenko",            "Male"   ; (1885-1921) Second mayor of the city of Donetsk
 "Alexander Zakharchenko",        "Male"   ; (1976–2018) Head of the Donetsk People´s Republic from 4 November 2014 – 31 August 2018
 "Denis Pushilin",                "Male"   
 "Elena Pushilina",               "Female" ; Denis Pushilin´s wife
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Kremlin %s"),      _("?female:Kremlin %s")
 "Monarchy",        _("Grand Prince %s"), _("Grand Princess %s")
 "Republic",        _("Hetman %s"),       _("?female:Hetman %s")
 "Fundamentalism",  _("Patriarch %s"),    _("Matriarch %s")
}

flag="donetsk"
flag_alt = "russia"  ; Obvious reason... no other flag matches
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations= "ukrainian", "soviet", "russian"

cities =
 "Donetsk",
 "Mariupol",
 "Makiivka",
 "Horlivka",
 "Kramatorsk",
 "Sloviansk",
 "Yenakiieve",
 "Bakhmut",
 "Kostiantynivka",
 "Pokrovsk",
 "Khartsyzk",
 "Druzhkivka",
 "Chystiakove",
 "Shakhtarsk",
 "Myrnohrad",
 "Snizhne",
 "Yasynuvata",
 "Avdiivka",
 "Toretsk",
 "Dobropillia",
 "Kirovske",
 "Debaltseve",
 "Dokuchaievsk",
 "Selydove",
 "Volnovakha",
 "Lyman",
 "Kurakhove",
 "Amvrosiivka",
 "Zuhres",
 "Bilozerske",
 "Yunokomunarivsk",
 "Ilovaisk",
 "Novohrodivka",
 "Vuhledar",
 "Krasnohorivka",
 "Mykolaivka",
 "Chasiv Yar",
 "Siversk",
 "Hirnyk",
 "Zhdanivka",
 "Ukrainsk",
 "Svitlodarsk",
 "Soledar",
 "Komsomolske",
 "Novoazovsk",
 "Rodynske",
 "Mospyne",
 "Marinka",
 "Vuhlehirsk",
 "Bilytske",
 "Zalizne",
 "Sviatohirsk"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
