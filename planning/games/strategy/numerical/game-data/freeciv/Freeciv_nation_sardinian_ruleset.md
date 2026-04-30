# Freeciv(nation) · sardinian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sardinian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sardinian定义

## 正文
```ruleset
[nation_sardinian]

name=_("Sardinian")
plural=_("?plural:Sardinians")
groups="European", "Medieval", "Early Modern"
legend=_("Sardinia is an island in the Mediterranean Sea and an autonomous\
 region of Italy. The site of the Nuraghic civilization in prehistory, the\
 island passed to Phoenician and then Roman rule. Upon the collapse of the\
 Roman Empire Sardinia was occupied by the Vandals and later by the\
 Byzantines, but foreign rule quickly eroded and by the 9th century the\
 Byzantine representatives had formed their own autonomous states. By the\
 end of the Middle Ages however, the Aragonese had established dominance\
 over the island. In 1718 Sardinia was handed to the house of Savoy, and\
 it became a constituent part of the Kingdom of Piedmont-Sardinia, which\
 eventually led Italy to its national unification in 1861.")

leaders = {
 "name",                      "sex"
 "Ampsicora",                 "Male"
 "Goda",                      "Male"
 "Michele Zanche",            "Male"
 "Adelàsia de Torres",        "Female"
 "Entziu",                    "Male"
 "Marianu IV",                "Male"
 "Eleonora de Arborea",       "Female"
 "Juanne Maria Angioy",       "Male"
 "Frantziscu Ignàtziu Mannu", "Male"
 "Giuseppe Brotzu",           "Male"
 "Camillo Bellieni",          "Male"
}
ruler_titles = { "government",     "male_title",   "female_title"
                 "Democracy",      _("Judge %s"),  _("?female:Judge %s")
                 "Fundamentalism", _("Fra %s"),    _("Mother Superior %s")
               }
flag="sardinia"
flag_alt = "-"
style = "babylonian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "piedmontese", "catalan", "corsican"

cities =
; names in Sardinian, Gallurese, Sassarese, Catalan or Ligurian
; using the languages spoken in the respective towns
 "Casteddu",
 "Sàssari",
 "Tarranoa",
 "Nugoro",
 "Aristanis",
 "Carbònia",
 "Igrèsias",
 "Biddexidru",
 "Tèmpiu",
 "Tortuelie",
 "Seddori",
 "Lanusè",
 "Pòltu Tòrra (ocean)",
 "Àldara",
 "Cuartu Santa Alèni",
 "L'Alguer",
 "A Madalena (ocean)",
 "Ceraxus",
 "Assèmini",
 "Cabuderra",
 "Pauli",
 "Sestu",
 "Sìnnia",
 "Sòssu",
 "Alzachèna",
 "Bosa",
 "Pasada",
 "Fordongianus",
 "Sèdilo",
 "Lungoni",
 "Othieri",
 "Fertilia",
 "Cuartuciu",
 "Gùspini",
 "Santu Antiogu",
 "Thiniscole",
 "Macumère",
 "Tarraba",
 "Su Masu",
 "Serramanna",
 "Crabas",
 "Santu 'Ainju",
 "Ittiri",
 "Partiolla",
 "Durgali",
 "Pula",
 "Ulìana",
 "Dèximu Mannu",
 "Maracalagonis",
 "Uda",
 "Santu Sperau",
 "U Pàize (ocean)",
 "Biddesartu",
 "S'Ulumedu",
 "Furtei",
 "Caragnani",
 "Sarrocu",
 "Arbatassa",
 "Thiesi",
 "Bidda Sorris"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
