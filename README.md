# Codex 科研项目模板

这是一份可在本机或远程服务器上使用的**项目模板**，不是某个课题的实验记录。它把项目规则放在 `AGENTS.md`，把每轮进度放在 `handoff.md`，把论文、复现、数据和实验分别管理。

## 新项目

在 GitHub 使用本仓库的 **Use this template** 创建新仓库，再把新仓库克隆到执行 Codex 的机器上，并将该目录设为 Codex 项目目录。首次对话请提供：项目名与一句话研究问题、目标投稿或截止日期、领域标准术语。把这些信息填入 `AGENTS.md` 后再开展实质研究。

Codex 应从项目根目录读取 `AGENTS.md`；每轮还应读写 `handoff.md`。新项目的 `handoff.md`、测评协议和结果记录必须从空白状态开始，不能沿用旧课题的数据。

## 接入已有项目

把本仓库克隆到执行 Codex 的机器上，在目标项目之外运行：

```bash
python3 scripts/bootstrap.py /path/to/existing-project
```

脚本只补缺失文件，不覆盖现有文件。若目标已有 `AGENTS.md` 等同名文件，脚本会跳过并列出；请先比较再手动合并规则。运行前可以加 `--dry-run` 预览。

## Skill 与外部工具

模板中的 `AGENTS.md` 是项目规则，克隆项目即可被 Codex 读取；它**不会自动安装**其他 skill 或 CLI。若需要 [research-workflow](https://github.com/skJack/research-workflow) 的论文抓取脚本，请在**执行对话的远程主机**安装整个 skill 文件夹，包含 `SKILL.md`、`scripts/` 和 `assets/`，安装后验证 Codex 可识别。只下载单个 `SKILL.md` 不等于装好了脚本。

DeepXiv 的 skill、CLI、认证同样要在使用它的主机上分别检查和配置。无需在尚未确定研究问题时启动检索或下载。不要把密钥写进 Git 仓库。

给远程 Codex 的一句话：

> 请先检查本机是否已有 `research-workflow` 与 `deepxiv-cli`。若缺少 `research-workflow`，从 https://github.com/skJack/research-workflow 安装到这台主机的 Codex skill 目录，保留完整文件夹；验证 `SKILL.md` 和论文抓取脚本可用。DeepXiv 也需单独安装并验证。不要开始检索或下载论文；先报告检查结果和仍需我提供的认证信息。

## 模板边界

- `dataset/` 下的数据、论文 PDF/LaTeX 源码、模型权重和实验产物不属于模板，不应提交到模板仓库。
- `experiment/evaluation.md` 有待确定项时，不得开始比较方法或临时挑选指标。
- `/loop` 是工作方式要求；使用前先确认当前 Codex 环境支持它，并设定可验证的停止条件。若不可用，先说明，不要假称已经使用。
