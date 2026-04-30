# Freeciv(nation) · templar

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/templar.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的templar定义

## 正文
```ruleset
[nation_templar]

name=_("Knights Templar")
plural=_("?plural:Templars")
groups="Imaginary"
legend=_("The Knights Templar were formed after the first Crusade in order\
 to protect Pilgrims on their journeys in the Holy Land. The organization\
 grew to immense power and wealth in the next 200 years, and were the\
 innovators of many modern concepts such as Banking.")

leaders = {
 "name",                        "sex"
 "Hugh de Payens",              "Male"
 "Robert de Craon",             "Male"
 "Everard des Barres",          "Male"
 "Bernhard de Tremelai",        "Male"
 "Andre de Montebard",          "Male"
 "Bertrand de Blanquefort",     "Male"
 "Philip de Milly",             "Male"
 "Odo de St. Amand",            "Male"
 "Arnold de Toroga",            "Male"
 "Gerard de Ridfort",           "Male"
 "Robert de Sable",             "Male"
 "Gilbert Erail",               "Male"
 "Philip de Plessiez",          "Male"
 "William de Chartres",         "Male"
 "Pedro de Montaigu",           "Male"
 "Armand de Perigord",          "Male"
 "Richard de Bures",            "Male"
 "William de Sonnac",           "Male"
 "Reynald de Vichiers",         "Male"
 "Thomas Berard",               "Male"
 "William de Beaujeu",          "Male"
 "Tibald de Gaudin",            "Male"
 "Jacques de Molay",            "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("Master %s"),       _("Mistress %s")
 "Monarchy",        _("Grand Master %s"), _("Grand Mistress %s")
 "Democracy",       _("Chancellor %s"),   _("?female:Chancellor %s")
}

flag="templar"
flag_alt = "stpatrick"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Holy Roman", "French"

cities =
 "Jerusalem",
 "Karak",
 "Acre",
 "Antioch",
 "Ascalon",
 "Safed",
 "Baghras",
 "Edessa",
 "Ibelin",
 "Clairvaux",
 "Chastel Pelegrin",
 "Mansourah",
 "Tripoli",
 "Bethleham",
 "Temple Mount",
 "Jericho",
 "Tortosa",
 "Toron",
 "Jaffa",
 "Courtenay",
 "Tyre",
 "Sidon",
 "Beaufort",
 "Krak des Chevaliers",
 "Atlit",
 "Arwad",
 "Botrun",
 "Castle Tomar",
 "Chatillon",
 "Monzon",
 "Cressing",
 "Witham",
 "Tiberias",
 "Soissons",
 "Aquilers",
 "Springs of Cresson",
 "Cowley",
 "Aleppo",
 "Hitchin",
 "Anjou",
 "Laodicea",
 "Gaza",
 "Jacob's Ford",
 "Paneas",
 "Nazareth",
 "Joppa",
 "Damietta",
 "Lemesos",
 "Constantia",
 "Crete",
 "Cilicia",
 "Salamis",
 "Famagusta",
 "Stravovoun",
 "Larnaca",
 "Nicosia",
 "Kyrenia"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
