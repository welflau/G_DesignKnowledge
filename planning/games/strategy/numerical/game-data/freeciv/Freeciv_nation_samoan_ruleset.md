# Freeciv(nation) · samoan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/samoan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的samoan定义

## 正文
```ruleset
[nation_samoan]

name=_("Samoan")
plural=_("?plural:Samoans")
groups="Oceanian", "Modern"
legend=_("Samoa is a country occupying the Western part of the Samoan\
 islands of the Central Pacific; the Eastern part is governed by the\
 United States as American Samoa. Samoa was settled by Austronesian\
 peoples around 1500 BCE. It was probably from Samoa that the Polynesians\
 started the expansion throughout the Pacific. Colonized by Germany and\
 New Zealand, Samoa became independent in 1962.")

leaders = {
 "name",                                "sex"
 "Tui Manu'a",                          "Male"
 "Malietoa Savea",                      "Male"
 "Malietoa Laupepa",                    "Male"
 "Lauaki Namulau'ulu Mamoe",            "Male"
 "Fiame Mata'afa Faumuina Mulinu'u II", "Male"
 "Malietoa Tanumafili II",              "Male"
 "Matatumua Maimoana",                  "Female"
}

flag="samoa"
flag_alt = "-"
style = "Tropical"

ruler_titles = {
 "government",     "male_title",                    "female_title"
 "Fundamentalism", _("Elder %s"),                   _("?female:Elder %s")
 "Monarchy",       _("Paramount Chief %s"),         _("?female:Paramount Chief %s")
 "Republic",       _("Chief of the Government %s"), _("?female:Chief of the Government %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with = "burmese", "taiwanese" ;similar flags
civilwar_nations = "fijian", "tongan"

cities =
 "Apia",
 "Safotulafai",
 "Afega",
 "Satupa'itea",
 "Leulumoega",
 "Vailoa i Palauli",
 "Lufilufi",
 "Asau",
 "Mulifanua",
 "Sale'aula",
 "Samamea",
 "Aopo",
 "Vaitele",
 "Faleasiu",
 "Vailele",
 "Le'auva'a",
 "Vaiusu",
 "Faleula",
 "Lauli'i",
 "Malie",
 "Siusega",
 "Nofoali'i",
 "Fasito'outa",
 "Solosolo",
 "Fagali'i",
 "Nu'u",
 "Safotu",
 "Manono Uta",
 "Fasito'o Tai",
 "Tuana'i",
 "Satapuala",
 "Samatau",
 "Fuailolo'o",
 "Falefa",
 "Sapulu",
 "Gataivai",
 "Matavai",
 "Sili",
 "Siumu",
 "Lotofaga",
 "Tanumapua",
 "Sa'anapu Uta",
 "Tufuele",
 "Samalae'ulu",
 "Fa'ala",
 "Luatuanu'u",
 "Sataua",
 "Levi",
 "Sataoa Uta",
 "Talimatau",
 "Matautu"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
