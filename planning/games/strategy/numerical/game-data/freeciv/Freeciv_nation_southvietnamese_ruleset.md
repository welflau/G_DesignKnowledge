# Freeciv(nation) · southvietnamese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/southvietnamese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的southvietnamese定义

## 正文
```ruleset
[nation_southvietnamese]

name=_("South Vietnamese")
plural=_("?plural:South Vietnamese")
groups="Asian"
legend=_("South Vietnam, officially the Republic of Vietnam, was the\
 American-backed state during the Vietnam War. The country was reunited\
 with North Vietnam after it was conquered by communist forces in 1975.")

leaders = {
 "name",                "sex"
 "Ngô Đình Diệm",       "Male"
 "Ngô Đình Nhu",        "Male"
 "Trần Lệ Xuân",        "Female"
 "Dương Văn Minh",      "Male"
 "Nguyễn Cao Kỳ",       "Male"
 "Nguyễn Văn Thiệu",    "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Communism",       _("Chairman %s"),     _("Chairwoman %s")
 "Despotism",       _("General %s"),      _("Madame %s")
 "Fundamentalism",  _("Archbishop %s"),   _("?female:Archbishop %s")
 "Monarchy",        _("Emperor %s"),      _("Empress %s")
}

flag="rvn"
flag_alt = "vietnam"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "badian", "catalan" ;similar flags , "cham"
civilwar_nations = "vietnamese"

cities =
  "Sài Gòn",
  "Đà Nẵng",
  "Biên Hòa",
  "Huế",
  "Nha Trang",
  "Cần Thơ",
  "Rạch Giá",
  "Qui Nhơn",
  "Vũng Tàu",
  "Phan Thiết",
  "Long Xuyên",
  "Buôn Ma Thuột",
  "Cam Ranh",
  "Đà Lạt",
  "Mỹ Tho",
  "Sóc Trăng",
  "Pleiku",
  "Cà Mau",
  "Bạc Liêu",
  "Vĩnh Long",
  "Kontum",
  "An Lộc",
  "Bến Tre",
  "Hội An",
  "Quảng Ngãi",
  "Mỹ Lai",
  "Long Xuyên",
  "Châu Đốc",
  "Cao Lãnh",
  "Phan Rang-Tháp Chàm",
  "Tam Kỳ",
  "Tân An",
  "Tuy Hòa",
  "Tân Sơn Nhất",
  "Ấp Bắc",
  "Đắk Tô",
  "Khe Sanh",
  "Quảng Trị",
  "Xuân Lộc"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
