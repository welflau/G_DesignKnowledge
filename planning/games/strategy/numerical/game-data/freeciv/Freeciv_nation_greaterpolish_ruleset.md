# Freeciv(nation) · greaterpolish

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/greaterpolish.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的greaterpolish定义

## 正文
```ruleset
[nation_greaterpolish]

name=_("Greater Polish")
plural=_("?plural:Greater Poles")
groups="European", "Medieval"
legend=_("Greater Poland or Wielkopolska is a historic and geographic\
 region of central-western Poland.")

leaders = {
 "name",                        "sex"
 "Mieszko III Stary",           "Male"
 "Władysław III Laskonogi",     "Male"
 "Władysław Odonic",            "Male"
 "Przemysł I",                  "Male"
 "Bolesław Pobożny",            "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Despotism",       _("Prince %s"),          _("Princess %s")
 "Fundamentalism",  _("Archbishop %s"),      _("Mother Superior %s")
 "Monarchy",        _("Grand Prince %s"),    _("Grand Princess %s")
 "Communism",       _("First Secretary %s"), _("?female:First Secretary %s")
}

flag = "greater_poland"
flag_alt = "-"
style = "European"
init_techs=""
init_buildings=""
init_units=""

civilwar_nations = "polish", "silesian", "cuyavian"

cities =
  "Poznań",
"Gniezno",
"Kalisz",
"Konin",
"Piła",
"Ostrów Wielkopolski",
"Leszno",
"Swarzędz",
"Śrem",
"Krotoszyn",
"Września",
"Luboń",
"Turek",
"Jarocin",
"Wągrowiec",
"Kościan",
"Koło",
"Środa Wielkopolska",
"Rawicz",
"Gostyń",
"Chodzież",
"Szamotuły",
"Złotów",
"Oborniki",
"Pleszew",
"Trzcianka",
"Nowy Tomyśl",
"Kępno",
"Ostrzeszów",
"Grodzisk Wielkopolski",
"Słupca",
"Wolsztyn",
"Mosina",
"Wronki",
"Czarnków",
"Rogoźno",
"Międzychód",
"Murowana Goślina",
"Puszczykowo",
"Opalenica",
"Kostrzyn",
"Pobiedziska",
"Jastrowie",
"Witkowo",
"Trzemeszno",
"Pniewy",
"Kórnik",
"Zbąszyń",
"Kłodawa",
"Koźmin Wielkopolski",
"Krzyż Wielkopolski",
"Buk",
"Sieraków",
"Wieleń",
"Stęszew",
"Śmigiel",
"Wyrzysk",
"Czempiń",
"Odolanów",
"Nowe Skalmierzyce",
"Zduny",
"Golina",
"Szamocin",
"Kleczew",
"Krobia",
"Skoki",
"Okonek",
"Ujście",
"Krajenka",
"Sompolno",
"Miłosław",
"Gołańcz",
"Tuliszków",
"Nekla",
"Rakoniewice",
"Pyzdry",
"Ślesin",
"Miejska Górka",
"Kobylin",
"Łobżenica",
"Margonin",
"Zagórów",
"Bojanowo",
"Lwówek",
"Poniec",
"Sulmierzyce",
"Książ Wielkopolski",
"Wysoka",
"Rydzyna",
"Klecko",
"Czerniejewo",
"Borek Wielkopolski",
"Rychwał",
"Olbrzycko",
"Osieczna",
"Żerków",
"Raszków",
"Pogorzela",
"Dąbie",
"Ostroróg",
"Grabów nad Prosną",
"Jutrosin",
"Mikstat",
"Przedecz",
"Wielichowo",
"Krzywiń",
"Stawiszyn",
"Dolsk",
"Dobra"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
