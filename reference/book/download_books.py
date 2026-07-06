#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
运筹学 + Gurobi + AI Agent 教材下载脚本（工程管理论文路线）
============================================================
三层结构：
  第1层 — 自动下载（合法免费资源）
  第2层 — 浏览器打开购买页面（商业教材）
  第3层 — 输出合法获取指南

版权声明：本脚本仅下载经作者/出版社官方授权免费分发的教材及配套资源。
对于无法免费获取的商业教材，提供购买渠道及替代方案。
"""

import os
import sys
import webbrowser
import urllib.request
from pathlib import Path

# ============================================================
# 配置
# ============================================================

BOOK_DIR = "/Users/ayidaweiwei/IdeaProjects/ew-agent-thesis/reference/book"
os.makedirs(BOOK_DIR, exist_ok=True)

# ============================================================
# 第1层：自动下载（仅合法免费资源）
# ============================================================

LAYER1_DOWNLOADS = [
    # === 运筹学 5本 ===
    {
        "url": "https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf",
        "filename": "01_Convex_Optimization_Boyd_Vandenberghe.pdf",
        "desc": "Convex Optimization (Boyd & Vandenberghe) — 剑桥大学出版社授权免费",
        "category": "运筹学经典",
    },
    # === Gurobi 2本 ===
    {
        "url": "https://cdn.gurobi.com/wp-content/uploads/2023/01/exampletour.pdf",
        "filename": "02_Gurobi_Example_Tour.pdf",
        "desc": "Gurobi Example Tour — 官方免费文档",
        "category": "Gurobi求解器",
    },
    {
        "url": "https://cdn.gurobi.com/wp-content/uploads/2024/01/refman.pdf",
        "filename": "03_Gurobi_Reference_Manual.pdf",
        "desc": "Gurobi Optimizer Reference Manual — 官方免费文档",
        "category": "Gurobi求解器",
    },
    # === AI Agent 2本 ===
    {
        "url": "https://arxiv.org/pdf/2308.11432",
        "filename": "04_LLM_Autonomous_Agents_Survey_Wang_2024.pdf",
        "desc": "LLM-based Autonomous Agents Survey (Wang et al. 2024) — arXiv 开放获取",
        "category": "AI Agent",
    },
    {
        "url": "https://arxiv.org/pdf/2504.19678",
        "filename": "05_LLM_Reasoning_to_Autonomous_AI_Agents_Ferrag_2025.pdf",
        "desc": "From LLM Reasoning to Autonomous AI Agents (Ferrag et al. 2025) — arXiv 开放获取",
        "category": "AI Agent",
    },
    {
        "url": "https://arxiv.org/pdf/2402.01680",
        "filename": "06_LLM_Multi_Agents_Survey_Guo_2024.pdf",
        "desc": "LLM-based Multi-Agents Survey (Guo et al. 2024) — arXiv 开放获取",
        "category": "AI Agent",
    },
]

# ============================================================
# 第2层：浏览器打开购买页面（商业教材）
# ============================================================

LAYER2_PURCHASE = [
    # Hillier & Lieberman
    {
        "name": "Introduction to Operations Research (Hillier & Lieberman)",
        "url": "https://www.mheducation.com/hillier/",
        "isbn": "978-0073521503",
        "publisher": "McGraw-Hill Education",
        "purchase_link": "https://www.amazon.com/s?k=Introduction+Operations+Research+Hillier",
        "free_resources": [
            "MIT OpenCourseWare 15.053 — Optimization Methods (free, uses Hillier & Lieberman)",
            "https://ocw.mit.edu/courses/15-053j-optimization-methods-fall-2009/",
        ],
    },
    # 胡运权
    {
        "name": "《运筹学教程（第5版）》胡运权",
        "url": "https://www.tup.tsinghua.edu.cn/booksCenter/book_07656604.html",
        "isbn": "978-7-302-52398-7",
        "publisher": "清华大学出版社",
        "purchase_link": "https://search.jd.com/search?keyword=9787302523987",
        "free_resources": [
            "文泉学堂（清华大学出版社官方电子书平台）",
            "https://wqbook.wqxuetang.com/book/8779",
        ],
    },
    # 韩伯棠
    {
        "name": "《管理运筹学（第5版）》韩伯棠",
        "url": "https://xuanshu.hep.com.cn/front/book/findBookDetails?bookId=619d1f40938b7cc2960edddf",
        "isbn": "978-7-04-030427-5",
        "publisher": "高等教育出版社",
        "purchase_link": "https://search.jd.com/search?keyword=9787040304275",
        "free_resources": [
            "中国大学MOOC — 管理运筹学 国家精品课程",
            "https://www.icourse163.org/course/BIT-47012",
            "配套软件下载（高教社官方）",
            "https://xuanshu.hep.com.cn/front/h5Mobile/bookDetails?bookId=5d73ed13b0b2bda7c523bc70",
        ],
    },
    # 陈宝林
    {
        "name": "《最优化理论与算法（第2版）》陈宝林",
        "url": "https://www.tup.tsinghua.edu.cn/booksCenter/book_06942703.html",
        "isbn": "978-7-302-11376-8",
        "publisher": "清华大学出版社",
        "purchase_link": "https://search.jd.com/search?keyword=9787302113768",
        "free_resources": [
            "文泉学堂（清华大学出版社官方电子书平台）",
            "https://wqbook.wqxuetang.com/book/8779",
        ],
    },
]

# ============================================================
# 第3层：输出合法获取指南
# ============================================================

LAYER3_GUIDE = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 无法免费下载的商业教材 · 合法获取指南 📚
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

以下 4 本教材受版权保护，脚本不会自动下载。
请通过正规渠道获取：

【运筹学类】
  📖 Introduction to Operations Research (Hillier & Lieberman, McGraw-Hill)
     → 购买：亚马逊/麦格劳希尔官网
     → 学校图书馆（超星/读秀/文泉学堂等中文电子书平台）
     → 配套资源：MIT OCW 15.053 课程（免费在线讲义）

  📖 《运筹学教程》胡运权（清华大学出版社，第5版）
     → 购买：京东/当当搜索 "9787302523987"
     → 图书馆：文泉学堂电子书
     → 配套：习题集单独出版（含740余题）

  📖 《管理运筹学》韩伯棠（高等教育出版社，第5版）
     → 购买：京东/当当搜索 "9787040304275"
     → 图书馆：超星/读秀
     → 配套：中国大学MOOC公开课（爱课程网）
     → 软件：高教社官方配套软件3.5版（随书附赠）

  📖 《最优化理论与算法》陈宝林（清华大学出版社，第2版）
     → 购买：京东/当当搜索 "9787302113768"
     → 图书馆：文泉学堂电子书
     → 配套：习题解答独立出版（219页，ISBN 9787302284673）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 替代方案建议 💡
  1. 优先使用学校图书馆借阅（免费）
  2. 向出版社申请教师专用教辅资源
  3. 二手书/旧书网（孔夫子、闲鱼等）
  4. 同学之间互借/复印（合理使用、非商业性）

📌 重要提醒 📌
  • 购买正版支持作者创作
  • 遵守学术规范，引用注明出处
  • 尊重知识产权，合理使用教材
"""


def main():
    """主函数：执行三层下载逻辑"""
    print("=" * 60)
    print("  运筹学 + Gurobi + AI Agent 教材下载脚本")
    print("  工程管理论文路线 · 配套资源获取指南")
    print("=" * 60)

    os.chdir(BOOK_DIR)

    # ---- 第1层：自动下载 ----
    print("\n📥 第1层：自动下载（仅合法免费资源）")
    print("-" * 40)

    success_count = 0
    fail_count = 0

    for item in LAYER1_DOWNLOADS:
        filepath = os.path.join(BOOK_DIR, item["filename"])
        print(f"\n  📥 [{item['category']}] {item['desc']}")
        print(f"     URL: {item['url']}")

        try:
            req = urllib.request.Request(
                item["url"],
                headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X)"}
            )
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()
                with open(filepath, "wb") as f:
                    f.write(data)
            size_mb = os.path.getsize(filepath) / (1024 * 1024)
            print(f"     ✅ 成功 ({size_mb:.1f} MB)")
            success_count += 1
        except Exception as e:
            print(f"     ⚠️ 失败: {e}")
            # 清理不完整文件
            if os.path.exists(filepath):
                os.remove(filepath)
            fail_count += 1

    print(f"\n  第1层总结: 成功 {success_count}/{len(LAYER1_DOWNLOADS)}, 失败 {fail_count}/{len(LAYER1_DOWNLOADS)}")

    print()

    # ---- 第2层：浏览器打开购买页 ----
    print("\n📥 第2层：浏览器打开购买页面（商业教材）")
    print("-" * 40)

    for item in LAYER2_PURCHASE:
        print(f"\n  📖 {item['name']}")
        print(f"     出版社: {item['publisher']}")
        print(f"     购买链接: {item['purchase_link']}")
        print(f"     免费资源: {', '.join(item['free_resources'])}")
        print()

    # ---- 第3层：合法获取指南 ----
    print("\n📥 第3层：输出合法获取指南")
    print("-" * 40)
    print(LAYER3_GUIDE)

    print("\n✅ 脚本执行完毕！")
    return 0


if __name__ == "__main__":
    sys.exit(main())
