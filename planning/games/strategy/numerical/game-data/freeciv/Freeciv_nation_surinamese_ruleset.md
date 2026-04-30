# Freeciv(nation) · surinamese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/surinamese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的surinamese定义

## 正文
```ruleset
[nation_surinamese]

name=_("Surinamese")
plural=_("?plural:Surinamese")
groups="American", "Modern"

legend=_("Suriname is the smallest independent country of South America.\
 Originally it was inhabited by Arawak Indians. It was first colonized by\
 the English who traded it with the Dutch for New Amsterdam, modern New\
 York, in 1667. Suriname was granted self government in 1954 and became\
 fully independent in 1975.")

leaders = {
 "name",                        "sex"
 "Abraham Crijnssen",           "Male"
 "Adyáko Benti Basiton",        "Male"
 "Boni",                        "Male"
 "Reinier Frederik van Raders", "Male"
 "Johannes Kielstra",           "Male"
 "Anton de Kom",                "Male"
 "Henck Arron",                 "Male"
 "Henk Chin A Sen",             "Male"
 "Desi Bouterse",               "Male"
}

ruler_titles = {
 "government",     "male_title",           "female_title"
 "Despotism",      _("Sergeant %s"),       _("?female:Sergeant %s")
 "Fundamentalism", _("Reverend %s"),       _("?female:Reverend %s")
}

flag="suriname"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="tupi", "dutch", "guyanese", "antillean"

cities =
 "Paramaribo",
 "Lelydorp",
 "Nieuw-Nickerie",
 "Moengo",
 "Meerzorg",
 "Nieuw-Amsterdam",
 "Mariënburg",
 "Wageningen",
 "Albina",
 "Groningen",
 "Brownsweg",
 "Brokopondo",
 "Onverwacht",
 "Totness",
 "Apoera",
 "Paloemeu",
 "Sipalwini",
 "Benzdorp",
 "Kamp 52",
 "Langatabbetja",
 "Zanderij",
 "Jodensavanne (grassland)",
 "Kwakoegron",
 "Wasjabo",
 "Avanero",
 "Amotopo",
 "Kwamalasamoetoe",
 "Jenny",
 "Calcutta",
 "Boskamp (forest, jungle)",
 "Tamanredjo",
 "Tamarin",
 "Galibi",
 "Nason",
 "Cottica",
 "Kawemhakan",
 "Witagrond",
 "Kaaimanston",
 "Poesoegroenoe",
 "Afobaka",
 "Berg en Dal",
 "Savana",
 "Bigi Polka",
 "Pakhuis",
 "Paranam",
 "Stolkertsijver",
 "Java",
 "Pokigron",
 "Alkmaar",
 "Berlijn",
 "Cabendadorp",
 "Katwijk",
 "Nieuw-Rotterdam",
 "Peperpot",
 "Post Utrecht",
 "Thorarica"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
