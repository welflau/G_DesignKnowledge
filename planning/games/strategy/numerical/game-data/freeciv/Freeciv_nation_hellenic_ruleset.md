# Freeciv(nation) · hellenic

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/hellenic.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的hellenic定义

## 正文
```ruleset
[nation_hellenic]

name=_("Hellenic")
plural=_("?plural:Hellenes")
groups="Modern", "European"
legend=_("The Hellenic Republic - also known as Greece - was created when\
 the Hellenic people gained independence from the Ottoman Empire in 1832.")

leaders = {
 "name",                        "sex"
 "Theodore Kolokotronis",       "Male"
 "Laskarina Boumboulina",       "Female"
 "Kharilaos Trikoupis",         "Male"
 "Eleutherios Venizelos",       "Male"
 "Aris Veloukhiotis",           "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Despotism",       _("Colonel %s"),        _("?female:Colonel %s")
 "Fundamentalism",  _("Patriarch %s"),      _("Matriarch %s")
}

flag="greece"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "greek", "byzantine"
civilwar_nations = "cretan", "cypriot"

cities =
 "Athina",
 "Thessaloniki",
 "Peiraias",
 "Patra",
 "Larisa",
 "Ioanina",
 "Irakleion",
 "Volos",
 "Kavala",
 "Lamia",
 "Chania",
 "Agrinion",
 "Chalkida",
 "Kalamata",
 "Veroia",
 "Xanthi",
 "Rodos",
 "Kerkyra",
 "Alexandroupolis",
 "Sparti",
 "Messologion",
 "Florina",
 "Amaliada",
 "Drama",
 "Tripolis",
 "Nauplion",
 "Arta",
 "Katerini",
 "Rethymnon",
 "Orestiada",
 "Trikala",
 "Preveza",
 "Chios",
 "Samos",
 "Kiklis",
 "Levadeia",
 "Argos",
 "Grevena",
 "Ermoupolis",
 "Argostoli",
 "Megara",
 "Poligyros",
 "Amphissa",
 "Serrai",
 "Igoumenitsa",
 "Thiva",
 "Kos",
 "Agios Nikolaos",
 "Andros",
 "Naxos",
 "Limnos",
 "Tyrnavos",
 "Kastoria",
 "Edessa",
 "Thassos",
 "Paxos",
 "Kalymnos",
 "Samosathraki",
 "Nafpaktos",
 "Athos",
 "Mykonos",
 "Psara",
 "Delos",
 "Patmos",
 "Marathonas",
 "Melos",
 "Sifnos",
 "Skyros",
 "Karpathos",
 "Megisti"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
