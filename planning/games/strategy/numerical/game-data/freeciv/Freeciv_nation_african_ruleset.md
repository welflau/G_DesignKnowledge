# Freeciv(nation) · african

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/african.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的african定义

## 正文
```ruleset
[nation_african]

name=_("African")
plural=_("?plural:Africans")
groups="Imaginary"
legend=_("Africa: the cradle of humanity. It is the world's second largest\
 continent and also its second most populous.")

leaders = {
 "name",                 "sex"
 "Edward Wilmot Blyden", "Male"
 "W. E. B. Du Bois",     "Male"
 "Haile Selassie",       "Male"
 "Patrice Lumumba",      "Male"
 "Kwame Nkrumah",        "Male"
 "Jomo Kenyatta",        "Male"
 "Amílcar Cabral",       "Male"
 "Julius Nyerere",       "Male"
 "Nelson Mandela",       "Male"
}

flag="africa"
flag_alt = "-"
style = "Tropical"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="algerian", "angolan", "beninese", "bissau-guinean",
 "botswanan", "brazzaville-congolese", "burkinabe", "burundian",
 "cameroonian", "cape verdean", "central african", "comorian", "congolese",
 "djiboutian", "egyptian arab", "equatoguinean", "eritrean", "ethiopian",
 "gabonese", "gambian", "ghanaian", "guinean", "ivoirian", "kenyan",
 "lesothoan", "liberian", "libyan", "malagasy", "malawian", "malian",
 "mauritanian", "mauritian", "mozambican", "namibian", "nigerian",
 "nigerien", "rwandan", "senegalese", "santomean", "seychellois",
 "sierra leonean", "somali", "south african", "sudanese", "swazi",
 "tanzanian", "togolese", "tunisian", "ugandan", "sahrawi", "zambian",
 "zimbabwean"
civilwar_nations="algerian", "angolan", "beninese", "bissau-guinean",
 "botswanan", "brazzaville-congolese", "burkinabe", "burundian",
 "cameroonian", "cape verdean", "central african", "comorian", "congolese",
 "djiboutian", "egyptian arab", "equatoguinean", "eritrean", "ethiopian",
 "gabonese", "gambian", "ghanaian", "guinean", "ivoirian", "kenyan",
 "lesothoan", "liberian", "libyan", "malagasy", "malawian", "malian",
 "mauritanian", "mauritian", "mozambican", "namibian", "nigerian",
 "nigerien", "rwandan", "senegalese", "santomean", "seychellois",
 "sierra leonean", "somali", "south african", "sudanese", "swazi",
 "tanzanian", "togolese", "tunisian", "ugandan", "sahrawi", "zambian",
 "zimbabwean"
cities=
; Sites of AU institutions
 "Addis Abeba",
 "Mitrand",
 "Banjul",
 "Abuja",
 "Tarabulus",
 "Yaoundé"
; Subsequent cities fetched from city lists of member nations

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
