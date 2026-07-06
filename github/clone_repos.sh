#!/bin/bash
# =============================================================================
# GitHub 项目批量克隆脚本
# 论文：AI Agent + Skill + MCP + Gurobi 实现代码重构优化
# 目标：20 个相关项目 → /Users/ayidaweiwei/IdeaProjects/ew-agent-thesis/github/
# =============================================================================
# 用法：bash clone_repos.sh
# 使用 --depth 1 浅克隆以节省空间和时间
# =============================================================================

set -e

TARGET_DIR="/Users/ayidaweiwei/IdeaProjects/ew-agent-thesis/github"
mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"

echo "============================================================"
echo "  GitHub 项目批量克隆 (20个)"
echo "  论文：AI Agent + Skill + MCP + Gurobi 代码重构优化"
echo "============================================================"

# ============================================================
# 分类 A：AI Agent 代码重构（6个）
# ============================================================
echo ""
echo "--- A. AI Agent 代码重构 (6个) ---"

echo "[1/20] agent-claude-refactoring — Claude AI 自主重构 + AST分析"
git clone --depth 1 https://github.com/JosephKisler/agent-claude-refactoring.git && echo "  ✅"

echo "[2/20] refrax — 多LLM智能重构代理(A2A协议)"
git clone --depth 1 https://github.com/cqfn/refrax.git && echo "  ✅"

echo "[3/20] AI-CodeCompass — AI代码助手（语义搜索+重构建议）"
git clone --depth 1 https://github.com/KANSADWALA/AI-CodeCompass.git && echo "  ✅"

echo "[4/20] sexy-code-machine — AI生成代码清理重构"
git clone --depth 1 https://github.com/fr-mm/sexy-code-machine.git && echo "  ✅"

echo "[5/20] LLM-Agent-SE-Survey — LLM Agent软件工程综述"
git clone --depth 1 https://github.com/lisaGuojl/LLM-Agent-SE-Survey.git && echo "  ✅"

echo "[6/20] Awesome-Issue-Solving — Agentic软件问题解决综述"
git clone --depth 1 https://github.com/ZhonghaoJiang/Awesome-Issue-Solving.git && echo "  ✅"

# ============================================================
# 分类 B：运筹学 / Gurobi 建模（4个）
# ============================================================
echo ""
echo "--- B. 运筹学 / Gurobi 建模 (4个) ---"

echo "[7/20] modeling-examples — Gurobi官方建模案例(LP/MILP/QP)"
git clone --depth 1 https://github.com/Gurobi/modeling-examples.git && echo "  ✅"

echo "[8/20] Optimization-Tutorial — OR教程(PuLP+SciPy+CVXPY+Pyomo+Gurobi)"
git clone --depth 1 https://github.com/Harrypatria/Basic-to-Advanced-Optimization-Tutorial-with-PuLP-Python.git && echo "  ✅"

echo "[9/20] LumiX — 类型安全优化框架(ORM集成+Gurobi)"
git clone --depth 1 https://github.com/tdelphi1981/LumiX.git && echo "  ✅"

echo "[10/20] PyEPO — Predict-then-Optimize(PyTorch+Gurobi)"
git clone --depth 1 https://github.com/khalil-research/PyEPO.git && echo "  ✅"

# ============================================================
# 分类 C：MCP + Skill + Agent 框架（5个）
# ============================================================
echo ""
echo "--- C. MCP + Skill + Agent 框架 (5个) ---"

echo "[11/20] skills-mcp — Claude Skills→任意MCP代理"
git clone --depth 1 https://github.com/skills-mcp/skills-mcp.git && echo "  ✅"

echo "[12/20] agent-skills — Agent Skills精选集+MCP服务器"
git clone --depth 1 https://github.com/kambleakash0/agent-skills.git && echo "  ✅"

echo "[13/20] skills-server — MCP Skills服务器(懒加载+热重载)"
git clone --depth 1 https://github.com/ivanenev/skills-server.git && echo "  ✅"

echo "[14/20] claude-orchestra — Claude Code 技能/代理/MCP编排"
git clone --depth 1 https://github.com/Momo2323-ui/claude-orchestra.git && echo "  ✅"

echo "[15/20] multi-agent-with-mcp — LangGraph+MCP多代理编码团队"
git clone --depth 1 https://github.com/danmas0n/multi-agent-with-mcp.git && echo "  ✅"

# ============================================================
# 分类 D：代码质量 / 度量（3个）
# ============================================================
echo ""
echo "--- D. 代码质量 / 度量 (3个) ---"

echo "[16/20] kiss — LLM代理代码质量反馈(圈复杂度/重复率)"
git clone --depth 1 https://github.com/dsweet99/kiss.git && echo "  ✅"

echo "[17/20] repomind — AI仓库智能分析(健康度/架构/风险)"
git clone --depth 1 https://github.com/ApacheWang/repomind.git && echo "  ✅"

echo "[18/20] claude-code-recipes — 47个Claude Code工作流(重构/审查/迁移)"
git clone --depth 1 https://github.com/Sagargupta16/claude-code-recipes.git && echo "  ✅"

# ============================================================
# 分类 E：自主编码代理平台（2个）
# ============================================================
echo ""
echo "--- E. 自主编码代理平台 (2个) ---"

echo "[19/20] SWE-agent — Princeton 自主软件工程代理(ACI架构)"
git clone --depth 1 https://github.com/princeton-nlp/SWE-agent.git && echo "  ✅"

echo "[20/20] OpenHands — 通用AI编码代理平台(原OpenDevin)"
git clone --depth 1 https://github.com/All-Hands-AI/OpenHands.git && echo "  ✅"

# ============================================================
# 验证
# ============================================================
echo ""
echo "============================================================"
echo "  克隆完成！统计："
echo "============================================================"
echo ""
echo "目录数: $(ls -d */ 2>/dev/null | wc -l | tr -d ' ')"
echo "总大小: $(du -sh . 2>/dev/null | cut -f1)"
echo ""
echo "--- 目录列表 ---"
ls -d */ 2>/dev/null | sed 's/\/$//' | while read d; do
    size=$(du -sh "$d" 2>/dev/null | cut -f1)
    echo "  📁 $d ($size)"
done
echo ""
echo "✅ 全部完成！"
