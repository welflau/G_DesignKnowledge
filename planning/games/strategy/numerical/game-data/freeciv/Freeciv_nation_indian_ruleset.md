# Freeciv(nation) · indian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/indian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的indian定义

## 正文
```ruleset
[nation_indian]

translation_domain="freeciv"

name=_("Indian")
plural=_("?plural:Indians")
groups="Modern", "Asian", "Core"
legend=_("The Republic of India was created in 1950 following a\
 non-violent independence movement led by Mahatma Gandhi. With more\
 than a billion inhabitants it is the world's second most populous\
 country as well as the world's largest democracy.")

leaders = {
 "name",                "sex"
 "Chandragupta",        "Male"
 "Ashoka",              "Male"
 "Shivaji",             "Male"
 "Subhas Chandra Bose", "Male"
 "Mohandas Gandhi",     "Male"
 "Jawaharlal Nehru",    "Male"
 "Indira Gandhi",       "Female"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Raja %s"),      _("Rani %s")
 "Fundamentalism",  _("Guru %s"),      _("?female:Guru %s")
 "Monarchy",        _("Maharaja %s"),  _("Maharani %s")
 "Republic",        _("Mahatma %s"),   _("?female:Mahatma %s")
}

flag="india"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Gupta", "Chola", "Mughal", "Marathi"
civilwar_nations="Bengali", "Sikh", "Kashmiri", "Assamese", "Marathi"

cities =
 "Delhi",
 "Mumbai",		; Bombay
 "Chennai",		; Madras
 "Bangalore",
 "Kolkata",		; Calcutta
 "Ahmedabad",		; Ahmadabad
 "Kanpur",
 "Hyderabad",
 "Lucknow",
 "Varanasi",		; Benares
 "Chandigarh",
 "Madurai",
 "Coimbatore",
 "Kozhikode",		; Calicut
 "Thiruvananthapuram",	; Trivandrum
 "Nagpur",
 "Amritsar",
 "Srinagar",
 "Agra",
 "Bhopal",
 "Patna",
 "Surat",
 "Jaipur",
 "Varanasi",
 "Allahabad",
 "Indore",
 "Mysore",
 "Raipur",
 "Gaya",
 "Kanpur",		; Cawnpore
 "Pune (hills)",	; Poona
 "Ranchi",
 "Bhubaneswar",
 "Thiruvananthapuram",
 "Tiruchirappalli",
 "Dehradun",
 "Aizawl",
 "Gandhinagar",
 "Imphal",
 "Thane",
 "Ludhiana",
 "Pimpri-Chinchwad",
 "Nashik",
 "Vadodara",
 "Faridabad",
 "Ghaziabad",
 "Rajkot",
 "Meerut",
 "Kalyan-Dombivali",
 "Navi Mumbai",
 "Aurangabad",
 "Solapur",
 "Jabalpur",
 "Visakhapatnam",
 "Howrah",
 "Jodhpur",
 "Guwahati",
 "Vijayawada",
 "Mira-Bhayandar",
 "Gwalior",
 "Hubballi-Dharwad"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
