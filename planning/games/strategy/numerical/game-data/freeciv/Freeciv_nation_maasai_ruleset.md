# Freeciv(nation) · maasai

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/maasai.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的maasai定义

## 正文
```ruleset
[nation_maasai] 

name=_("Maasai") 
plural=_("?plural:Maasais") 
groups="African" 
legend=_("The Maasai are an indigenous African ethnic group of\
 semi-nomadic people located in Kenya and northern Tanzania. Due to\
 their distinctive customs and dress and residence near the many game\
 parks of East Africa, they are among the most well known of African\
 ethnic groups.")

leaders = {
 "name",        "sex"
 "Mbatian",     "Male"
 "Lenana",      "Male"
 "Segi",        "Male"
}

ruler_titles = {
 "government",     "male_title",             "female_title"
 "Monarchy",       _("Paramount Chief %s"),  _("?female:Paramount Chief %s")
}

flag = "maasai" 
flag_alt = "-" 
style = "Tropical" 

init_techs="" 
init_buildings="" 
init_units="" 
civilwar_nations = "kenyan", "tanzanian"

cities = 
  "Maasai Mara",
"Iloitokitoki",
"Ildamat",
"Irpurko",
"Irkeekonyokie",
"Iloitai",
"Irkaputiei",
"Iirkankere",
"Isiria",
"Irmoitanik",
"Iloodokilani",
"Irmatatapato",
"Irwuasinkishu",
"Ilarusa",
"Kore",
"Parakuyu",
"Irkisonko",
"Isikirari"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
