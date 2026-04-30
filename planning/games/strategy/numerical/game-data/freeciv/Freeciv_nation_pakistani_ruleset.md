# Freeciv(nation) · pakistani

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/pakistani.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的pakistani定义

## 正文
```ruleset
[nation_pakistani]

name=_("Pakistani")
plural=_("?plural:Pakistanis")
groups="Modern", "Asian"
legend=_("The Federation of Pakistan was formed from the\
 predominantly Muslim regions of British India in 1947.")

leaders = {
 "name",                "sex"
 "Zulfikar Ali Bhutto", "Male"
 "Muhammad Zia-ul-Haq", "Male"
 "Benazir Bhutto",      "Female"
 "Muhammad Ali Jinnah", "Male"
 "Khawaja Nazimuddin",  "Male"
}
ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Raja %s"),      _("Rani %s")
 "Fundamentalism",  _("Mullah %s"),    _("?female:Mullah %s")
 "Monarchy",        _("Maharaja %s"),  _("Maharani %s")
}
flag="pakistan"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Bangladeshi", "Pashtun", "Kashmiri"

; http://de.wikipedia.org/wiki/Liste_der_Städte_in_Pakistan
cities =
 "Karachi",
 "Lahore",
 "Faisalabad",
 "Rawalpindi",
 "Multan",
 "Gujranwala",
 "Hyderabad",
 "Peshawar",
 "Islamabad",
 "Quetta",
 "Bahawalpur",
 "Sargodha",
 "Sialkot",
 "Sukkur",
 "Larkana",
 "Shekhupura",
 "Jhang",
 "Rahim Yar Khan",
 "Gujrat",
 "Mardan",
 "Kasur",
 "Dera Ghazi Khan",
 "Wah",
 "Sahiwal",
 "Nawabshah",
 "Mingaora",
 "Okara",
 "Mirpur Khas",
 "Kamoke",
 "Chiniot",
 "Sadiqabad",
 "Burewala",
 "Jacobabad",
 "Muridike",
 "Muzaffargarh",
 "Jhelum",
 "Shikarpur",
 "Khanewal",
 "Hafizabad",
 "Kohat",
 "Khuzdar",
 "Dadu",
 "Khanpur",
 "Gojra",
 "Mandi Bahauddin",
 "Tando Allah Yar",
 "Abottabad",
 "Daska",
 "Pakpattan",
 "Bahawalnagar",
 "Tando Adam",
 "Khairpur",
 "Chishtian Mandi",
 "Jaranwala",
 "Ahmadpur East",
 "Vihari",
 "Kamalia",
 "Kot Addu",
 "Khushab",
 "Chakwal",
 "Wazirabad",
 "Dera Ismail Khan",
 "Lodhran",
 "Swabi"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
