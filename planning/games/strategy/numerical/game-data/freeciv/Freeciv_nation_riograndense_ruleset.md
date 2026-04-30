# Freeciv(nation) · riograndense

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/riograndense.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的riograndense定义

## 正文
```ruleset
[nation_riograndense]

name=_("Rio-Grandense")
plural=_("?plural:Rio-Grandenses")
groups="American"
legend=_("The Rio-Grandense Republic or Piratini Republic existed in the\
 Brazilian state of Rio Grande do Sul from 1836 to 1845. It fought the\
 War of Tatters against the Brazilian Imperial Army and was supported by\
 Giuseppe Garibaldi amongst others.")

leaders = {
 "name",                        "sex"
 "Antônio de Sousa Neto",       "Male"
 "Bento Gonçalves da Silva",    "Male"
 "José Garibaldi",              "Male"
 "Davi Canabarro",              "Male"
}

ruler_titles = {
 "government",      "male_title",   "female_title"
 "Fundamentalism",  _("Bishop %s"), _("Mother Superior %s")
}
flag = "piratini"
flag_alt = "-"
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "Brazilian", "Argentine", "Uruguayan", "Tupi"

cities =
 "Piratini",
 "Alegrete",
 "Caçapava do Sul",
 "Porto Alegre (ocean)",
 "Rio Grande (river)",
 "Bagé",
 "São Borja",
 "Santa Maria",
 "Caixas do Sul",
 "Pelotas",
 "Canoas",
 "Gravataí",
 "Viamão",
 "Novo Hamburgo",
 "Alvorada",
 "São Leopoldo",
 "Passo Fundo",
 "Uruguaiana",
 "Sapucaia do Sul",
 "Cachoeirinha",
 "Santa Cruz do Sul",
 "Guaíbas",
 "Bento Gonçalves",
 "Erechim",
 "Santana do Livramento",
 "Esteio",
 "Sapiranga",
 "Alegrete",
 "Cachoeira do Sul",
 "Ijuí",
 "Farroupilha",
 "Lajeado",
 "Cruz Alta",
 "Santo Ãngelo",
 "Carazinho",
 "Santa Rosa",
 "Vacaria",
 "Montenegro",
 "São Gabriel",
 "Camaquã",
 "Campo Bom",
 "Parobé",
 "Taquara",
 "Santiago",
 "Estância Velha",
 "Venâncio Aires"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
