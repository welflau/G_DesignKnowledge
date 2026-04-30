# Freeciv(nation) · sotho

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sotho.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sotho定义

## 正文
```ruleset
[nation_sotho]

name=_("Sotho")
plural=_("?plural:Basotho")
groups="African"
legend=_("A Bantu people in Southern Africa, the ancestors of the Basotho\
 first arrived in the region by the end of the first millennium CE. The\
 Basotho first formed a unified polity in the early 19th century under\
 king Moshoeshoe I. Today, there are about 2 million Sotho in the Kingdom\
 of Lesotho and almost twice that number in South Africa.")

leaders = {
 "name",                     "sex"
 "Moshoeshoe I",             "Male"
 "Lerotholi",                "Male"
 "Mantsebo Amelia 'Matsaba", "Female"
 "Leabua Jonathan",          "Male"
 "Moshoeshoe II",            "Male"
 "Ntsu Mokhehle",            "Male"
 "Cedric Phatudi",           "Male"
 "Kenneth Mopeli",           "Male"
}

flag="lesotho_old"
flag_alt = "-"
style = "Celtic"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="tswana", "lesothoan", "south african"

cities =
;alternating cities in Lesotho and South Africa
 "Maseru",
 "Seshego",
 "Teyateyaneng",
 "Phuthaditjhaba",
 "Mafeteng",
 "Lebowakgomo",
 "Hlotse",
 "Maluti a Phofung",
 "Quthing",
 "Mphahlele",
 "Butha-Buthe",
 "Polokwane",
 "Namahadi",
 "Tswelopele",
 "Mokhotlong",
 "Sebokeng",
 "Thaba-Tseka",
 "Boipatong",
 "Maputsoa",
 "Ngwathe",
 "Peka",
 "Matjhabeng",
 "Roma",
 "Botshabelo",
 "Thaba Bosiu",
 "Bophelong",
 "Nyakosoba",
 "Impumelelo",
 "Nkoebe",
 "Metsimaholo",
 "Seshote",
 "Moqhaka",
 "Khomo-Phatsoa",
 "Setsoto",
 "Makhunoane",
 "Nala",
 "Semonkong",
 "Kopanong",
 "Makhalaneng",
 "Mookgophong",
 "Monyake",
 "Mafube",
 "Malumeng",
 "Bela-Bela",
 "Seforong",
 "Rafolatsane",
 "Mosetoa",
 "Kao",
 "Makheka",
 "Mabote",
 "Manka",
 "Mantsonyane",
 "Ha Baroana",
 "Marakabei"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
