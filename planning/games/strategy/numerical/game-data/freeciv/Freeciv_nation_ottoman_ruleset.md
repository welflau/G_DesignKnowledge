# Freeciv(nation) · ottoman

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/ottoman.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的ottoman定义

## 正文
```ruleset
[nation_ottoman]

name=_("Ottoman")
plural=_("?plural:Ottomans")
groups="Medieval", "Early Modern", "Asian", "European"
legend=_("In the beginning of the 14th century Osman, a leader of a\
 minor Turkish tribe in western Anatolia, conquered all his neighboring\
 tribes. A century later the Byzantine capital fell to\
 Turkish rule which gave the Ottoman empire access to Europe. The\
 Ottomans subsequently conquered large parts of south-eastern\
 Europe, the Islamic Arab world as well as\
 Egypt and much of North Africa, making it a regional superpower\
 until its dissolution in the aftermath of World War I.")

leaders = {
 "name",                        "sex"
 "Fâtih Sultân Mehmed",         "Male"
 "Yavuz Sultân Selim",          "Male"
 "Ertuğrul Gâzi",               "Male"
 "Osman",                       "Male"
 "Orhan",                       "Male"
 "Kânûnî Sultân Süleyman",      "Male"
}

ruler_titles = {
 "government",      "male_title",     "female_title"
 "Despotism",       _("%s Pasha"),    _("?female:%s Pasha")
 "Fundamentalism" , _("Caliph %s"),   _("Calipha %s")
 "Monarchy",        _("Padishah %s"), _("?female:Padishah %s")
 "Republic",        _("Vizier %s"),   _("?female:Vizier %s")
}

flag ="ottoman"
flag_alt = "turkey"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="turkish"
civilwar_nations="arab", "armenian", "hellenic", "crimean tatar"

; Cities from all over the empire
cities =
 "Söğüt",
 "Bursa",
 "İznik",
 "Edremit",
 "Ezine",
 "Bergama",
 "Akhisar",
 "Kocaeli",
 "Gelibolu",
 "Edirne",
 "Niş",
 "Sofya",
 "Manastır",
 "Larende",
 "Konya",
 "Sivas",
 "Kayseri",
 "Niğde",
 "Adana",
 "Angara",
 "Antakya",
 "Adalya",
 "Mut",
 "Hamidâbâd",
 "Canik",
 "Trabzon",
 "Avlonya",
 "Samsun",
 "Kütâhiye",
 "Selânik",
 "Semendire",
 "Seged",
 "Varna",
 "Kosova",
 "Konstantiniyye",
 "Azirum",
 "Erzingan",
 "Diyarbekir",
 "Maraş",
 "Antep",
 "Urfa",
 "İskenderun",
 "Van",
 "Mora",
 "Eğriboz",
 "Kırım",
 "Eflak",
 "Boğdan",
 "Kili",
 "Akkirman",
 "İnebahtı",
 "Modon",
 "Navarin",
 "Koron",
 "Tebriz",
 "Şam",
 "Kâhire",
 "Cezâyir",
 "Belgrad",
 "Rodos",
 "Bosna",
 "Bağdat",
 "Musul",
 "Budin",
 "Estergon",
 "Lahsâ",
 "Yemen",
 "Trablusgarb",
 "Trablusşam",
 "Fas",
 "Cerbe",
 "Astarhan",
 "Kıbrıs",
 "Tunus",
 "Suakin",
 "Cidde",
 "Basra",
 "Budin",
 "Tameşvar",
 "Çıldır",
 "Gürcistan",
 "Kanije",
 "Revan",
 "Girit",
 "Varad",
 "Uyvar",
 "Kandiye",
 "Kamaniçe",
 "Çehrin"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
