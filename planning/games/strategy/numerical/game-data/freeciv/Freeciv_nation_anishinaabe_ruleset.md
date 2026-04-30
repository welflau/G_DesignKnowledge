# Freeciv(nation) · anishinaabe

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/anishinaabe.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的anishinaabe定义

## 正文
```ruleset
[nation_anishinaabe]

name=_("Anishinaabe")
plural=_("?plural:Anishinaabeg")
groups="American", "Early Modern"
legend=_("The Anishinaabeg are a group of closely related Native American\
 tribes in the North American Great Lakes region, including the Ottawa,\
 Ojibwe, Algonkin and Potawatomi. They speak Algonquian languages.\
 Together they are one of the most numerous indigenous peoples of North\
 America.")

leaders = {
 "name",                "sex"
 "Pontiac",             "Male"
 "Egushawa",            "Male"
 "Ningweegon",          "Male"
 "Shup-Shewana",        "Male"
 "Aazhawigiizhigokwe",  "Female"
 "Gichiweshkiinh",      "Male"
 "Ozaawindib",          "Male"
 "Waabaanakwad",        "Male"
 "Eshkibagikoonzhe",    "Male"
 "Leonard Peltier",     "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Democracy",       _("Principal Chief %s"), _("?female:Principal Chief %s")
 "Fundamentalism",  _("Great Shaman %s"),    _("?female:Great Shaman %s")
 "Monarchy",        _("Great Chief %s"),     _("?female:Great Chief %s")
}

flag="anishinaabe"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "cree", "quebecois"

cities =
 "Gnoozhekaaning",
 "Wemitigoozhiiwitigwaaning",
 "Zhiibaahaasing",
 "Aazhoomog",
 "Bikoganaagan",
 "Agaming",
 "Gibaakwa'iganing",
 "Mooningwanekaaning",
 "Namekaawa'iganing",
 "Nagaajiwanaang",
 "Gaa-zhiigwanaabikokaag",
 "Neyaashiing",
 "Chi-minising",
 "Gaa-mitaawangaagamaag",
 "Manoominikaan-zaaga'iganiing",
 "Minisinaakwaang",
 "Asinikaaning",
 "Ne-zhingwaakokaag",
 "Gichi-oodenaang",
 "Oshki-oodenaang",
 "Wiikwegamaang",
 "Zaagawaamikaag-wiidwedong",
 "Mooz-eskani-zaaga'iganiing",
 "Onigamiinsing",
 "Namaygoosisagagun",
 "Minjikaning",
 "Shapawe",
 "Chi-achaabaaning",
 "Gaa-mitaawangaagamaag",
 "Siipiising",
 "Makadewaagamijiwanong",
 "Iskatewi-zaaga'iganiing",
 "Azaadiwi-ziibi",
 "Asabiinyashkosiwagong",
 "Gitigaan-ziibi",
 "Bizhiw-zaaga'iganiing",
 "Gasabaanakaa",
 "Gichi-namegosib ininiwag",
 "Misi-zhaaga'iganiing"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
