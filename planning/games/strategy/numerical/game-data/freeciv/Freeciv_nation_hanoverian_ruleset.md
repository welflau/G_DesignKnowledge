# Freeciv(nation) · hanoverian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/hanoverian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的hanoverian定义

## 正文
```ruleset
[nation_hanoverian]

name=_("Hanoverian")
plural=_("?plural:Hanoverians")
groups="European", "Early Modern"
legend=_("Hanover was a state in Northern Germany, in current Lower\
 Saxony. From 1714 to 1837 Hanover and the United Kingdom were united\
 in a personal union. In 1866 it was gobbled up by Prussia.") 

leaders = {
 "name",                        "sex"
 "Ernst August",                "Male"
 "Georg I",                     "Male"
 "Georg II",                    "Male"
 "Georg III",                   "Male"
 "Georg IV",                    "Male"
 "Rudolf von Bennigsen",        "Male"
}

ruler_titles = {
 "government",      "male_title",          "female_title"
 "Despotism",       _("Duke %s"),          _("Duchess %s") 
 "Fundamentalism",  _("Prince-Bishop %s"), _("Princess-Bishop %s") 
 "Democracy",       _("Minister-President %s"), _("?female:Minister-President %s")
}

flag="hanover"
flag_alt = "westphalia"
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "frisian", "saxon", "westphalian", "british", "oldenburgian"

cities =
 "Hannover",
 "Osnabrück",
 "Lüneburg",
 "Stade",
 "Aurich",
 "Hildesheim",
 "Emden",
 "Göttingen",
 "Goslar",
 "Celle",
 "Harburg",
 "Leer",
 "Diepholz",
 "Alfeld",
 "Burgdorf",
 "Aschendorf/Ems",
 "Otterndorf",
 "Verden",
 "Norden",
 "Syke",
 "Duderstadt",
 "Fallingbostel",
 "Bersenbrück",
 "Osterholz-Scharmbeck",
 "Weener",
 "Rinteln",
 "Einbeck",
 "Gifhorn",
 "Bentheim",
 "Rotenburg in Hannover",
 "Wittmund",
 "Neustadt am Rübenberge",
 "Hannoversch Münden",
 "Isenhagen",
 "Iburg",
 "Achim",
 "Nienburg/Weser",
 "Northeim",
 "Lüchow",
 "Lingen",
 "Springe",
 "Osterode am Harz",
 "Dannenberg",
 "Melle",
 "Stolzenau",
 "Peine",
 "Soltau",
 "Meppen",
 "Sulingen",
 "Uslar",
 "Uelzen",
 "Wittlage",
 "Bremervörde",
 "Clausthal-Zellerfeld",
 "Oldenstadt"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
