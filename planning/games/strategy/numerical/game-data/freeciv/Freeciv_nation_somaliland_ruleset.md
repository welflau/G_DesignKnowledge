# Freeciv(nation) · somaliland

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/somaliland.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的somaliland定义

## 正文
```ruleset
[nation_somaliland] 

name=_("Somaliland") 
plural=_("?plural:Somalilanders") 
groups="Modern", "African"
legend=_("The Republic of Somaliland is an unrecognized state in Northern\
 Somalia, roughly concurrent with former British Somaliland. It declared\
 independence upon the collapse of Somalia in 1991. Although it enjoys\
 more stability and a somewhat higher standard of living than the rest of\
 Somalia it remains internationally unrecognized.")

leaders = {
 "name",                             "sex"
 "Maxamed Xaaji Ibraahim Cigaal",    "Male"
 "Axmed Maxamed Guuleed",            "Male"
 "Cabdiraxmaan Axmed Cali Tuur",     "Male"
 "Axmed Maxamed Maxamuud Siilaanyo", "Male"
 "Edna Aadan Ismaaciil",             "Female"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Sultan %s"),    _("Sultana %s")
 "Fundamentalism",  _("Elder %s"),     _("?female:Elder %s")
 "Despotism",       _("Sheikh %s"),    _("Shaykha %s")
}

flag= "somaliland" 
flag_alt = "somalia" 
style = "Tropical" 

init_techs="" 
init_buildings="" 
init_units="" 

civilwar_nations = "somali"

cities =
 "Hargeysa",
 "Berbera",
 "Burco",
 "Laascaanood",
 "Ceerigaabo",
 "Baki",
 "Arabsiyo",
 "Saylac",
 "Boorama",
 "Gabiley",
 "Buuhoodle",
 "Badhan",
 "Salaxleey",
 "Codweyne",
 "Caynaba",
 "Baligubadle",
 "Dilla",
 "Laasqoray",
 "Yubbe",
 "Hadaaftimo",
 "Dhahar",
 "Wajaale",
 "Maydh",
 "Taleex",
 "Balidhiig",
 "Ceelafweyn",
 "Buraan",
 "Bon",
 "Ceelbuh",
 "Lughaya",
 "Xingalool",
 "Beer",
 "Xudun",
 "Boocame",
 "Ceeldhab",
 "Oodweyne",
 "Dhubbato",
 "Garadag"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
