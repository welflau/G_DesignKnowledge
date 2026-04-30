# LoreFlow模板 · tsconfig

> 来源：Galygious/Lore-Flow
> 原始链接：https://github.com/Galygious/Lore-Flow
> 分类：gameplay
> 标签：世界观构建, 模板

## 概述
LoreFlow的.json模板文件

## 正文
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "useDefineForClassFields": true,
    "lib": [
      "DOM",
      "DOM.Iterable",
      "ESNext"
    ],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": false,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "module": "ESNext",
    "moduleResolution": "Node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": [
    "src"
  ],
  "references": [
    {
      "path": "./tsconfig.node.json"
    }
  ]
}

```

## 策划参考价值
世界观条目的结构化模板参考。
