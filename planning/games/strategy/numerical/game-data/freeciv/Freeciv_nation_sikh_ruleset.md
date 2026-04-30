# Freeciv(nation) · sikh

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/sikh.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的sikh定义

## 正文
```ruleset
[nation_sikh]

name=_("Sikh")
plural=_("?plural:Sikhs")
groups="Asian", "Early Modern"
legend=_("Sikhs are the followers of a monotheistic religion originating\
 from the Indian Subcontinent in the 15th century. The Punjab, on the\
 border of Pakistan and India, is the heartland of Sikhism. In the 19th\
 century a Sikh Empire existed in the region.")

leaders = {
 "name",                        "sex"
 "Nanak Dev",                   "Male"
 "Angad Dev",                   "Male"
 "Amar Das",                    "Male"
 "Ram Das",                     "Male"
 "Arjan Dev",                   "Male"
 "Har Gobind",                  "Male"
 "Har Rai",                     "Male"
 "Har Krishan",                 "Male"
 "Tegh Bahadur",                "Male"
 "Gobind Singh",                "Male"
 "Nawab Kapur Singh",           "Male"
 "Bibi Sahib Kaur",             "Female"
 "Ranjit Singh",                "Male"
 "Jind Kaur",                   "Female"
 "Sher Singh Attariwalla",      "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Raja %s"),      _("Rani %s")
 "Fundamentalism",  _("Guru %s"),      _("?female:Guru %s")
 "Monarchy",        _("Maharaja %s"),  _("Maharani %s")
}

flag = "sikh"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""

init_units=""
conflicts_with = "chola"
civilwar_nations = "afghani", "pakistani", "indian"

cities =
"Amritsar",
"Lahore",
"Gujranwala",
"Bathinda",
"Chandigarh",
"Jalandhar",
"Ludhiana",
"Patiala",
"Rawalpindi",
"Jatoi",
"Chiniot",
"Firoza",
"Attock",
"Khanpur",
"Talagang",
"Sheikhupura",
"Wazirabad",
"Kamoke",
"Jampur",
"Sahiwal",
"Taxila",
"Chakwal",
"Okara",
"Ahmadpur East",
"Toba Tek Singh",
"Qaidabad",
"Ahmed Nager Chatha",
"Sialkot",
"Jaranwala",
"Chunian",
"Kot Addu",
"Isa Khel",
"Phalla",
"Dera Ghazi Khan",
"Daska",
"Rabwah",
"Faisalabad",
"Kharian",
"Kasur",
"Lodhran",
"Bhakkar",
"Baghalchur",
"Rahimyar Khan",
"Rojhan",
"Multan",
"Haroonabad",
"Renala Khurd",
"Nurpur",
"Samundri",
"Bahawalnagar",
"Sadiqabad",
"Choa Saidan Shah",
"Mithankot",
"Dhaular",
"Rajanpur",
"Gujar Khan",
"Yazman",
"Dunyapur",
"Chaubara",
"Gojra",
"Burewala",
"Pasrur",
"Jahania",
"Karor",
"Bhalwal",
"Vihari",
"Jhang Sadar",
"Pakpattan",
"Dinga",
"Kamalia",
"Jand",
"Jhelum",
"Kalur Kot",
"Muzaffargarh",
"Shahpur",
"Gujrat",
"Dipalpur",
"Shakargarh",
"Fatehjang",
"Sargodha",
"Hasilpur",
"Leiah",
"Pind Dadan Khan",
"Shaher Sultan",
"Hafizabad",
"Liaqatpur",
"Wah",
"Mandi Burewala",
"Mianwali",
"Khushab",
"Mailsi",
"Murree",
"Arifwala",
"Khanewal",
"Narowaal",
"Chichawatni",
"Mankera",
"Bahawalpur"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
