# Freeciv(nation) · kittitian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/kittitian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的kittitian定义

## 正文
```ruleset
[nation_kittitian]

name=_("Kittitian and Nevisian")
plural=_("?plural:Kittitians and Nevisians")
groups="Modern", "American"
legend=_("Saint Kitts and Nevis is a nation in the Caribbean located on\
 the eponymous two islands. It is the smallest country in the Americas\
 and the world's smallest federation. Saint Kitts was the site of some of\
 the earliest French and English colonization attempts in the New World.")

leaders = {
 "name",                                "sex"
 "Thomas Warner",                       "Male"
 "Phillippe de Longvilliers de Poincy", "Male"
 "Alexander Hamilton",                  "Male"
 "Robert Llewellyn Bradshaw",           "Male"
 "Kennedy Simmonds",                    "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Fundamentalism",  _("Bishop %s"),          _("?female:Bishop %s")
}
flag="saint_kitts_and_nevis"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Dominican", "Antiguan and Barbudan"

cities =
 "Basseterre",
 "Charlestown",
 "Jamestown",
 "Monkey Hill",
 "Dieppe Bay Town",
 "Sandy Point Town",
 "Figtree",
 "Market Shop",
 "Saint Paul Capesterre",
 "Cayon",
 "Middle Island",
 "Cotton Ground",
 "Nichola Town",
 "Newcastle",
 "Palmetto Point",
 "Old Road Town",
 "Saddlers",
 "Bath",
 "Boyds",
 "Tabernacle",
 "Church Ground",
 "Mansion",
 "Ginger Land",
 "Phillip's Village",
 "Mannings",
 "Halfway Tree",
 "Whitehall",
 "Brunaire",
 "Bayfords",
 "Lucas",
 "Scarborough",
 "Pond Hill",
 "Newton Grounds",
 "Taylor's Pleasure",
 "Kittian Village",
 "Stony Hill",
 "Challengers",
 "Suncrest",
 "Estridge Estate",
 "Turtle Beach"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
