# Freeciv(nation) · lipkatatar

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/lipkatatar.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的lipkatatar定义

## 正文
```ruleset
[nation_lipkatatar]

name=_("Lipka Tatar")
plural=_("?plural:Lipka Tatars")
groups="European", "Medieval", "Early Modern"
legend=_("The Lipka Tatars are descendants of Tatars who migrated to the\
 Polish-Lithuanian Commonwealth from the Crimean Khanate and the\
 Golden Horde. Their name comes from the Turkish name of Lithuania.\
 In addition to Lithuania, they also live in Poland and Belarus.\
 Some Lipka Tatars have preserved their culture and traditional religion\
 to the present day.")

leaders = {
 "name",                        "sex"
 "Dżalal ad-Din",               "Male"   ; son of Tokhtamysh Khan;
                                         ; commander of the Tatars in the
                                         ; Battle of Grunwald (1410)
 "Aleksander Romanowicz",       "Male"   ; Russian and Polish general
                                         ; of Lipka Tatar origin
 "Aleksander Sulkiewicz",       "Male"
 "Aleksander Kryczyński",       "Male"   ; leader of Lipka Rebellion
 "Aleksander Jeljaszewicz",     "Male"
 "Matwiej Sulejman Sulkiewicz", "Male"
}

ruler_titles = {
 "government",     "male_title",         "female_title"
 "Despotism",      _("%s Bey"),          _("?female:%s Bey")
 "Republic",       _("Hetman %s"),       _("?female:Hetman %s")
 "Fundamentalism", _("Grand Mufti %s"),  _("?female:Grand Mufti %s")
}

flag="lipkatatar"
flag_alt="-"
style = "European"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Crimean Tatar", "Tatar", "Polish", "Lithuanian",
 "Belarusian", "Ukrainian"

cities =

;Polish and Lithuanian communities of Muslim Tatars:

;Transliterated from Classical Belarusian

  "Byelastok",		; Białystok / Беласток 
;  "Kruszyniany",
;  "Bohoniki",
;  "Vinkšnupiai",
  "Gdansk",		; Gdańsk / Гданьск
  "Vilnya",		; Vilnius / Вільня
  "Kowna",		; Kaunas / Коўна
  "Troki",		; Trakai / Трокі
  "Horadnya",		; Hrodna / Горадня
  "Mensk",		; Minsk / Менск
  "Navahradak",		; Navagrudak / Наваградак
;  "Rejże",
  "Lyublin",		; Lublin / Люблін
  "Markushaw",		; Markuszów / Маркушаў
  "Vrotslaw",		; Wrocław / Уроцлаў
  "Horaw Vyalikapolski" ; Gorzów Wielkopolski / Гораў Вялікапольскі

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
