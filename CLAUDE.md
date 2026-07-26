# 工程管理硕士研究生学位论文 — 项目级 CLAUDE.md

> 成都理工大学 专业学位硕士学位论文
> 研究方向：基于AI Agent的工程优化建模与求解集成研究
> 作者：庄为维

---

## 项目概述

本仓库为硕士研究生学位论文工作空间，研究方向为基于AI Agent的工程运筹建模与求解集成研究。核心目标是利用SysML系统建模语言进行工程管理优化建模，通过AI Agent实现优化模型的自动编排与求解器（Gurobi）集成。

## 当前工作目录

**仅 `essay3/` 为当前活跃工作目录**。`essay/` 和 `essay2/` 目录已删除，不再使用。

### essay3 目录结构

```
essay3/
├── plan.md                    # 论文规划要点与工作记录
├── 小论文.md                   # 小论文正文草稿（面向工程管理的运筹学建模AI Agent编排与调试研究）
└── 导师级提示词文件.md          # AI导师全流程提示词（角色定义、行为约束、写作流程）
```

### 其他重要目录

```
proposal/       # 开题报告
reference/      # 参考文献
skill/          # 工具与技能
github/         # GitHub相关资源
```

## 技术栈

- **建模语言：** SysML（系统建模语言）、XML（中间格式）
- **求解器：** Gurobi
- **AI框架：** SPADE（多Agent框架）
- **开发语言：** Python 3.x
- **研究方法：** 文献研究法、案例分析法、系统开发法、对比实验法

## 写作技能

项目 `.claude/skills/` 目录下配置了以下写作辅助技能：

| 技能 | 用途 |
|------|------|
| `paper-writing-skill` | 学术论文写作（Arpit Gupta编辑原则） |
| `academic-research-skills` | 学术研究方法论 |
| `econ-top-journal` | 经济/管理类期刊写作规范 |
| `research-skills` | 通用研究方法 |
| `graduation-thesis` | 毕业论文写作 |
| `thesis-proposal` | 开题报告写作 |
| `paper-polishing` | 论文润色与修改 |

## 关键约定

1. 所有论文写作工作以 `essay3/` 为核心工作目录
2. 小论文题目（待确认）：基于AI Agent的工程优化建模与求解集成研究
3. 导师级提示词文件定义了完整的AI导师指导流程，可通过 `/thesis-mentor` 调用
4. 不引入与当前研究方向无关的技术栈
