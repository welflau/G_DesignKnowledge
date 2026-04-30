# Freeciv(nation) · lithuanian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/lithuanian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的lithuanian定义

## 正文
```ruleset
[nation_lithuanian]

name=_("Lithuanian")
plural=_("?plural:Lithuanians")
groups="Medieval", "Early Modern", "Modern", "European"
legend=_("Lithuania is a small country on the south coast of the Baltic\
 Sea, northeast of Poland. Lithuanian is the most archaic and complex of\
 the northern Indo-European languages.")

leaders = {
 "name",                        "sex"
 "Mindaugas",                   "Male"
 "Vytenis",                     "Male"
 "Gediminas",                   "Male"
 "Algirdas",                    "Male"
 "Kęstutis",                    "Male"
 "Vytautas",                    "Male"
 "Aleksandras Stulginskis",     "Male"
 "Kazys Grinius",               "Male"
 "Antanas Smetona",             "Male"
 "Morta",                       "Female"
 "Ona",                         "Female"
 "Barbora Radvilaitė",          "Female"
 "Emilija Pliaterytė",          "Female"
}

ruler_titles = {
 "government",    "male_title",            "female_title"
 "Monarchy",      _("Grand Duke %s"),      _("Grand Duchess %s")
}

flag="lithuania"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

; Similar flags
conflicts_with="bulgarian"
civilwar_nations = "latvian", "central lithuanian", "old prussian"

cities =
  "Vilnius", "Kaunas", "Klaipėda", "Šiauliai",
  "Alytus", "Panevėžys", "Ukmergė", "Telšiai", "Raseiniai",
  "Adutiškis", "Kėdainiai", "Plungė", "Rietavas",
  "Šilutė", "Merkinė", "Jurbarkas", "Palanga",
  "Mažeikiai", "Kuršėnai", "Trakai", "Kernavė", "Varėna",
  "Rokiškis", "Kupiškis", "Druskininkai", "Marijampolė",
  "Utena", "Anykščiai", "Kretinga", "Naujoji Akmenė", 
  "Birštonas", "Biržai", "Pasvalys", "Vilkaviškis",
  "Veliuona", "Molėtai", "Ignalina", "Šalčinininkai",
  "Kaišiadorys", "Širvintos", "Joniškis", "Prienai",
  "Gargždai", "Skuodas", "Akmenė", "Kelmė", "Varniai",
  "Tytuvėnai", "Pakruojis", "Jonava", "Žagarė",
  "Kretinga", "Šilalė", "Tauragė", "Šakiai", "Skaudvilė", 
  "Kazlų Rūda", "Kaišiadorys", "Lazdijai", "Radviliškis",
  "Švenčionys", "Tilžė", "Pagėgiai", "Švenčionėliai", "Seinai"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
