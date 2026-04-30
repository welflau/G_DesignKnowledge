# Freeciv(nation) · rhodesia

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/rhodesia.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的rhodesia定义

## 正文
```ruleset
[nation_rhodesia]

name=_("Rhodesia")
plural=_("?plural:Rhodesians")
groups= "African", "Modern"
legend=_("Rhodesia was an unrecognised state located in southern\
 Africa during the Cold War. From 1965 to 1979, it comprised the\
 region now known as Zimbabwe. The country was considered a de facto\
 successor state to the former British colony of Southern Rhodesia.\
 During an effort to delay an immediate transition to black majority\
 rule, Rhodesia's predominantly white government issued its own\
 Unilateral Declaration of Independence (UDI) from the United Kingdom\
 on 11 November 1965. Following a brutal guerrilla war fought with two\
 rival African nationalist organisations Rhodesian premier Ian Smith\
 conceded to biracial democracy in 1978. Rhodesia reverted briefly to\
 colonial status pending elections under a universal franchise.\
 Independence deemed legitimate by Britain and the United Nations\
 was finally achieved in April 1980; the nation was concurrently\
 renamed the Republic of Zimbabwe.")

leaders = {
 "name",                    "sex"
 "Ian Smith",               "Male"
 "Cecil Rhodes",            "Male"
 "Edgar Whitehead",         "Male"
 "Abel Muzerowa",           "Female"
 "Godfrey Huggins",         "Male"
 "Robert Mugabe",           "Male"
 "Joshua Nkomo",            "Male"
 "Charles Coghlan",         "Male"
 "Winston Field",           "Male"
}

ruler_titles = {
"government", 		"male_title",			"female_title"
"Monarchy", 		_("King %s"),			_("?Queen %s")
"Democracy", 		_("Prime Minister %s"), 	_("?female:Prime Minister %s")
"Fundamentalism",	_("Archbishop %s"), 		_("?Mother Superior %s")
"Communism", 		_("First Secretary %s"), 	_("?female:First Secretary %s")
}

flag="rhodesia"
flag_alt = "nigeria"  ; Similar colors
style = "European"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "boer", "botswanan", "mozambican", "zambian", "angolan", "tanzanian"

cities =
 "Salisbury",
 "Bulawayo",
 "Chipinga",
 "Umtali",
 "Epworth",
 "Gwelo",
 "Kwekwe",
 "Kadoma",
 "Masvingo",
 "Norton",
 "Marandellas",
 "Ruwa",
 "Hartley",
 "Shabani",
 "Bindura",
 "Beitbridge",
 "Redcliff",
 "Victoria Falls",
 "Rusape",
 "Chiredzi",
 "Kariba",
 "Karoi",
 "Gokwe",
 "Selukwe",
 "Gatooma",
 "Melsetter",
 "Plumtree",
 "Que Que",
 "Rusape",
 "Traingle",
 "Umvukwes",
 "Wankie",
 "Birchenough Bridge",
 "Shurugwi",
 "Gwanda",
 "Mashava",
 "Chivhu",
 "Shamva",
 "Mazowe"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
