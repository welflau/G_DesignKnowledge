# Freeciv(nation) · vietnamese

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/vietnamese.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的vietnamese定义

## 正文
```ruleset
[nation_vietnamese]

name=_("Vietnamese")
plural=_("?plural:Vietnamese")
groups="Medieval", "Early Modern", "Modern", "Asian"
legend=_("The Vietnamese nation was founded in the first century CE by\
 twin sisters who became the war leaders of a revolt against a Chinese\
 military governor.")

leaders = {
 "name",                "sex"
 "Trưng Trắc",          "Female"
 "Trưng Nhị",           "Female"
 "Ly Bon",              "Male"
 "Gia Long",            "Male"
 "Bảo Đại",             "Male"
 "Hồ Chí Minh",         "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Monarchy",        _("Emperor %s"),   _("Empress %s")
}

flag="vietnam"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "south vietnamese", "cham"

; City order from:
; http://de.wikipedia.org/wiki/Liste_der_Städte_in_Vietnam
; Vietnamese orthography from:
; http://en.wikipedia.org/wiki/List_of_cities_in_Vietnam

cities =
  "Hà Nội",
  "Thành phố Hồ Chí Minh",	; alt. "Sài Gòn"
  "Hải Phòng",
  "Đà Nẵng",
  "Biên Hòa",
  "Huế",
  "Nha Trang",
  "Cần Thơ",
  "Rạch Giá",
  "Qui Nhơn",
  "Vũng Tàu",
  "Nam Định",
  "Phan Thiết",
  "Long Xuyên",
  "Hạ Long",			; alt. "Hong Gai"
  "Buôn Mê Thuột",
  "Cam Ranh",
  "Cẩm Phả",
  "Thái Nguyên",
  "Đà Lạt",
  "Mỹ Tho",
  "Sóc Trăng",
  "Pleiku",
  "Thanh Hóa",
  "Cà Mau",
  "Bạc Liêu",
  "Vinh",
  "Hòa Bình",
  "Vĩnh Long",
  "Kontum",
  "An Lộc",
  "Bến Tre",
  "Cao Bằng",
  "Lạng Sơn",
  "Điện Biên Phủ",
  "Hội An",
  "Quảng Ngãi",
  "Tuyên Quang"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
