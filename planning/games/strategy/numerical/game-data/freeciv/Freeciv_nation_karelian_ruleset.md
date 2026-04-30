# Freeciv(nation) · karelian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/karelian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的karelian定义

## 正文
```ruleset
[nation_karelian]

name=_("Karelian")
plural=_("?plural:Karelians")
groups="European"
legend=_("The Karelians are a Finno-Ugric people inhabiting Karelia, a\
 region currently divided between Finland and Russia. They are closely\
 related to the Finns.")

leaders = {
 "name",                "sex"
 "Väinämöinen",         "Male"
 "Seppo Ilmarinen",     "Male"
 "Louhi",               "Female"
 "Arhippa Perttunen",   "Male"
 "Karl Rautio",         "Male"
 "Lauri Törni",         "Male"
 "Otto Kuusinen",       "Male"
 "Johannes Virolainen", "Male"
}

flag="karelia"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "finnish", "sami", "russian"

cities =
;Names in Finnish/Karelian, Russian names in comment
 "Petroskoi",	;Petrozavodsk
 "Kalevala",
 "Viipuri",	;Vyborg
 "Anus",	;Olonets
 "Joensuu",
 "Lappeenranta",
 "Kondupohju",	;Kondopoga
 "Sekee",	;Segezha
 "Kostamus",	;Kostomuksha
 "Imatra",
 "Sortavala",
 "Käkisalmi",	;Priozersk
 "Karhumägi",	;Medvezhyegorsk
 "Enso",	;Svetogorsk
 "Kem",
 "Pitäranta",	;Pitkyaranta
 "Soroka",	;Belomorsk
 "Lieksa",
 "Lahdenpohju",	;Lakhdenpokhja
 "Joutseno",
 "Kitee",
 "Nurmes",
 "Outokumpu",
 "Antrea",	;Kamenogorsk
 "Ilomantsi",
 "Koivisto",	;Pirmorsk
 "Uhtuo",	;Uhtua
 "Suojärvi",	;Suoyarvi
 "Puudosi",	;Pudozh
 "Pyhäksalkä",
 "Vojatsu",	;Nadvoitsy
 "Parikkala",
 "Louhi",	;Louki
 "Eno",
 "Pinduinen",	;Pindushi
 "Ruokolahti",
 "Priäžä",	;Pryazha
 "Juuka",
 "Mujehdärvi",	;Muyezersky
 "Taipalsaari",
 "Läskelä",	;Lyaskelya
 "Tohmajärvi",
 "Porarvi",	;Porosozero
 "Tšuuppa",	;Chupa
 "Luumäki",
 "Šuoju",	;Shuya
 "Polvijärvi"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
