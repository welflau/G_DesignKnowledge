# Freeciv(sandbox) · parser

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/sandbox/parser.lua
> 分类：numerical
> 标签：文明, 4X策略, 规则集, sandbox

## 概述
Freeciv sandbox规则集的parser定义

## 正文
```lua
-- Copyright (c) 2007-2020 Freeciv21 and Freeciv contributors. This file is
--   part of Freeciv21. Freeciv21 is free software: you can redistribute it
--   and/or modify it under the terms of the GNU General Public License
--   as published by the Free Software Foundation, either version 3
--   of the License,  or (at your option) any later version.
--   You should have received a copy of the GNU General Public License
--   along with Freeciv21. If not, see https://www.gnu.org/licenses/.

-- This file is for lua-functionality for parsing luadata.txt
-- of this ruleset.

function turn_callback(turn, year)
  msg = luadata.get_str(string.format("turn_%d.msg", turn))
  if msg then
    log.debug("Turn %d msg: %s", turn, msg)
    notify.event(nil, nil, E.SCRIPT, msg)
  end
end

signal.connect('turn_begin', 'turn_callback')

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
