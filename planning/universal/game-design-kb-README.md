# Game Design Knowledge Base

A structured, agent-indexable knowledge base extracted from **8 classic game design books**, containing **362 rule cards** organized across **13 design topics**. Designed to be loaded as a skill by AI agents (Claude Code, etc.) for on-demand game design expertise retrieval.

## Source Books

| Book | Author | Pages | Extraction |
|------|--------|-------|------------|
| Designing Games: A Guide to Engineering Experiences (体验引擎) | Tynan Sylvester | 429 | Text |
| 236 Tips for Game Design (游戏设计的236个技巧) | Koji Ohno | 929 | Text |
| Nintendo's Experience Design (任天堂的体验设计) | Shinichiro Tamaki | 196 | Text |
| The Art of Game Design, 2nd Edition (游戏设计艺术) | Jesse Schell | 638 | OCR |
| Genesis Theory: Game System Design Guide (创世学说) | — | 331 | OCR |
| Game Feel: A Game Designer's Guide to Virtual Sensation (游戏感) | Steve Swink | 377 | OCR |
| Level Up! The Guide to Great Video Game Design (通关！游戏设计之道) | Scott Rogers | 376 | OCR |
| Game Design Workshop (游戏设计梦工厂) | Tracy Fullerton | 529 | OCR |

## Knowledge Base Structure

```
game-design-kb/
├── SKILL.md              # Skill entry point with retrieval instructions
├── INDEX.md              # Master topic index with cross-references
├── topics/               # 13 topic files, 362 rule cards
│   ├── core-loop.md          (37 cards) Core loops & experience design
│   ├── player-psychology.md  (31 cards) Player psychology & motivation
│   ├── game-feel.md          (42 cards) Game feel & character action
│   ├── enemy-ai.md           (32 cards) Enemy design & AI
│   ├── level-design.md       (37 cards) Level design
│   ├── camera-design.md      (28 cards) Camera design
│   ├── narrative-design.md   (31 cards) Narrative & story design
│   ├── balance-decisions.md  (30 cards) Decisions & balance
│   ├── multiplayer.md        (11 cards) Multiplayer design
│   ├── ux-interface.md       (21 cards) UI & interaction design
│   ├── emotion-surprise.md   (12 cards) Emotion & surprise design
│   ├── process-iteration.md  (35 cards) Development process & iteration
│   └── market-business.md    (15 cards) Business & market design
```

## Rule Card Format

Each card follows a consistent structure:

```markdown
## [Rule/Principle Name]
- **来源**: [Book] Chapter X
- **核心**: One-sentence summary
- **详述**: 1-3 paragraphs of detailed explanation
- **适用场景**: When to apply
- **示例**: Concrete game examples

---
```

## Usage

### As a Claude Code Skill

1. Copy this directory to `~/.claude/skills/game-design-kb/`
2. Add to `~/.claude/settings.json`:
   ```json
   {
     "enabledPlugins": {
       "game-design-kb@local": true
     }
   }
   ```
3. The skill will auto-load when game design tasks are detected

### Manual Retrieval

Use `grep` to search across topic files:

```bash
# Find all rules about "flow"
grep -r "心流" topics/

# Find balance-related rules
grep -r "平衡" topics/balance-decisions.md
```

Consult `INDEX.md` for topic-to-design-phase and topic-to-game-genre mappings.

## Topic Cross-Reference

| Design Phase | Relevant Topics |
|-------------|----------------|
| Concept | core-loop, player-psychology, emotion-surprise |
| Prototyping | process-iteration, game-feel, balance-decisions |
| Content | level-design, enemy-ai, narrative-design, camera-design |
| Polish | ux-interface, multiplayer, balance-decisions |
| Ship | market-business, process-iteration |

## Tools Used

- **PyMuPDF** — PDF text extraction
- **RapidOCR** — OCR for scanned PDFs (Chinese text recognition)
- **Parallel sub-agents** — Rule card extraction from raw text

## License

[MIT](LICENSE)

## Acknowledgments

All knowledge is derived from the works of the respective authors. This knowledge base is intended for educational and reference purposes. Please support the original authors by purchasing their books.
