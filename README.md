# 🎯 岗位调研报告生成器

> 一个自动化的岗位市场调研工具，帮助求职者深入了解目标岗位的要求、趋势和竞争格局。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Manus Skill](https://img.shields.io/badge/Manus-Skill-blueviolet.svg)](https://manus.im)

## 📖 项目概述

这个项目是一个强大的岗位调研工具，能够自动化地从 Boss 直聘上收集岗位信息，分析岗位要求，提炼核心能力关键词，并生成交互式的可视化报告。

**核心功能：**
- 🔍 **自动岗位搜索** - 从 Boss 直聘自动收集 20 个相关岗位
- 📊 **能力分析** - 提取并排序岗位中最常见的 10 个核心能力
- 📈 **数据可视化** - 生成薪资分布、公司类型、能力频率等交互式图表
- 🏢 **公司对比** - 对比大厂和创业公司的能力要求差异
- 🎯 **关键词匹配** - 展示每个能力在具体岗位中的应用

## 🚀 快速开始

### 作为 Manus 技能使用

如果您已安装 Manus，可以直接使用斜杠命令：

```bash
/job-research
```

系统会引导您输入：
1. **目标岗位** - 例如：AI 产品经理、产品经理、数据分析师
2. **目标城市** - 例如：深圳、北京、上海
3. **工作经验** - 例如：3-5 年、5-10 年
4. **期望薪资** - 例如：20K+、30K+

### 本地运行

#### 前置要求
- Python 3.8+
- Node.js 16+ (用于生成报告网页)
- pnpm 或 npm

#### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/jojohuang123/ai-pm-research-report.git
cd ai-pm-research-report

# 安装 Python 依赖
pip install -r requirements.txt

# 安装前端依赖
cd client
pnpm install
```

#### 运行工具

```bash
# 执行岗位调研
python scripts/extract_competencies.py

# 启动开发服务器
cd client
pnpm dev
```

## 📊 输出示例

### 研究成果

以"深圳 AI 产品经理（3-5 年，20K+）"为例：

| 指标 | 数值 |
|------|------|
| 岗位总数 | 20 |
| 平均薪资 | 32.2K |
| 大厂占比 | 25% |
| 创业公司占比 | 75% |

### 核心能力排名

| 排名 | 能力 | 频率 | 描述 |
|------|------|------|------|
| 1 | 从0到1落地能力 | 14/20 (70%) | 独立领导产品从概念到上线 |
| 2 | 跨团队协作与沟通 | 13/20 (65%) | 与技术、设计、运营等团队协调 |
| 3 | 大模型/LLM理解 | 9/20 (45%) | 理解大语言模型的能力和局限 |
| 4 | 场景挖掘与定义 | 9/20 (45%) | 发现和定义 AI 的应用场景 |
| 5 | 数据驱动与分析 | 8/20 (40%) | 用数据指导产品决策 |

### 大厂 vs 创业公司对比

**大厂的优势能力：**
- 跨团队协作（62%）
- 数据驱动与分析（63%）
- 项目管理（50%）

**创业公司的优势能力：**
- 从0到1落地能力（71%）
- Agent/智能体理解（80%）
- 场景挖掘与定义（67%）

## 📁 项目结构

```
ai-pm-research-report/
├── README.md                          # 项目说明
├── SKILL.md                           # Manus 技能文档
├── requirements.txt                   # Python 依赖
│
├── scripts/
│   └── extract_competencies.py        # 能力提取脚本
│
├── references/
│   ├── job_search_strategy.md         # 岗位搜索策略
│   ├── competency_extraction_guide.md # 能力提取指南
│   └── report_structure.md            # 报告结构设计
│
├── client/                            # 前端项目
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Home.tsx              # 主页
│   │   │   ├── KeywordMapping.tsx    # 关键词匹配页
│   │   │   └── CompanyComparison.tsx # 公司对比页
│   │   └── components/
│   ├── package.json
│   └── pnpm-lock.yaml
│
└── data/
    └── job_data.json                  # 岗位数据示例
```

## 🎨 报告页面

### 1. 主页 (Home)
展示岗位市场的全景视图：
- 关键指标卡片（总数、平均薪资、公司类型分布）
- 薪资分布柱状图
- 公司类型饼图
- 核心能力排名
- 典型岗位示例
- 行业洞察

### 2. 关键词匹配页 (Keyword Mapping)
详细展示每个能力在岗位中的应用：
- 可展开的能力卡片
- 每个能力出现的岗位列表
- 岗位描述中的具体引用
- 能力频率统计

### 3. 公司对比页 (Company Comparison)
对比大厂和创业公司的差异：
- 能力要求对比图表
- 详细的对比表格
- 公司类型特征描述
- 求职建议

## 💡 核心特性

### 🔄 自动化流程
- 自动搜索岗位信息
- 自动提取能力关键词
- 自动生成可视化报告
- 自动分类和统计

### 📊 数据可视化
- 交互式图表（Recharts）
- 响应式设计
- 平滑动画效果
- 多维度数据展示

### 🎯 智能分析
- 频率统计
- 趋势分析
- 公司类型对比
- 能力分布分析

### 📱 跨平台支持
- 桌面端优化
- 平板端适配
- 移动端响应式
- 深色/浅色主题

## 🛠️ 技术栈

### 后端
- **Python 3.8+** - 数据处理和分析
- **BeautifulSoup4** - 网页爬取（如需）
- **Pandas** - 数据处理

### 前端
- **React 19** - UI 框架
- **TypeScript** - 类型安全
- **Tailwind CSS 4** - 样式框架
- **Recharts** - 数据可视化
- **shadcn/ui** - UI 组件库
- **Wouter** - 路由管理

### 部署
- **Vite** - 构建工具
- **Express.js** - 静态服务
- **Manus** - 托管平台

## 📚 文档

### 用户文档
- [SKILL.md](./SKILL.md) - 完整的技能使用指南
- [job_search_strategy.md](./references/job_search_strategy.md) - 岗位搜索最佳实践

### 开发文档
- [competency_extraction_guide.md](./references/competency_extraction_guide.md) - 能力提取算法说明
- [report_structure.md](./references/report_structure.md) - 报告设计和实现

## 🔍 使用场景

### 1. 求职准备
- 了解目标岗位的核心要求
- 识别需要提升的能力
- 对标市场薪资水平
- 准备面试和自我介绍

### 2. 职业规划
- 分析不同公司类型的差异
- 了解职业发展路径
- 评估自身与市场的匹配度
- 制定能力提升计划

### 3. 招聘方参考
- 了解市场竞争格局
- 优化岗位描述
- 确定合理的薪资范围
- 识别关键能力需求

### 4. 教育和培训
- 了解行业需求
- 设计课程内容
- 评估学生就业竞争力
- 指导学生职业发展

## 📈 数据来源

- **Boss 直聘** (https://www.zhipin.com) - 主要数据源
- 支持扩展到其他招聘平台

## 🤝 贡献指南

欢迎贡献！请按以下步骤操作：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 改进方向
- [ ] 支持更多招聘平台
- [ ] 改进能力提取算法
- [ ] 添加更多可视化图表
- [ ] 支持多语言
- [ ] 添加导出功能（PDF、Excel）
- [ ] 实现趋势追踪（历史数据对比）

## 📝 许可证

本项目采用 MIT 许可证。详见 [LICENSE](./LICENSE.txt) 文件。

## 👨‍💻 作者

**JoJo Huang**
- GitHub: [@jojohuang123](https://github.com/jojohuang123)
- 项目地址: [ai-pm-research-report](https://github.com/jojohuang123/ai-pm-research-report)

## 🙏 致谢

感谢以下项目和工具的支持：
- [Manus](https://manus.im) - AI 代理平台
- [React](https://react.dev) - UI 框架
- [Tailwind CSS](https://tailwindcss.com) - 样式框架
- [Recharts](https://recharts.org) - 数据可视化
- [shadcn/ui](https://ui.shadcn.com) - UI 组件

## 📞 联系方式

- 📧 Email: [your-email@example.com]
- 💬 GitHub Issues: [提交问题](https://github.com/jojohuang123/ai-pm-research-report/issues)
- 🐦 Twitter: [@your-twitter]

## 🎯 路线图

### v1.0.0 (已发布)
- ✅ 基础岗位搜索和分析
- ✅ 能力提取和排名
- ✅ 交互式报告生成
- ✅ 公司类型对比
- ✅ Manus 技能集成

### v1.1.0 (计划中)
- [ ] 支持 LinkedIn 数据源
- [ ] 历史数据追踪
- [ ] 高级筛选功能
- [ ] 自定义报告模板

### v2.0.0 (未来)
- [ ] AI 驱动的能力评估
- [ ] 个性化求职建议
- [ ] 实时薪资预测
- [ ] 多语言支持

## ⭐ 如果有帮助，请给个 Star！

如果这个项目对您有帮助，请考虑给它一个 Star ⭐，这将激励我继续改进和维护这个项目。

---

**最后更新**: 2026 年 3 月
**版本**: 1.0.0
**状态**: 积极维护中 🚀
