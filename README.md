# ZippyComponentUI - 脚本启动器UI

一个基于PyQt6的简单UI，用于脚本配置和启动。

## 安装

```bash
pip install script-launcher-ui
```

## 使用

```python
from script_launcher_ui import ScriptLauncherUI

def on_submit():
    print("配置已提交")

ui = ScriptLauncherUI(style='light')
ui.add_label('欢迎使用脚本启动器')
ui.add_text_input_module('script_path', '脚本路径', '请输入脚本路径')
ui.add_button("提交", on_submit)
ui.start()
```

## 功能

- 简单直观的UI界面
- 可自定义样式
- 配置保存与加载
- 易于与现有脚本集成

## 许可证

MIT
