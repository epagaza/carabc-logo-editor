# Carabc Logo Editor v1.0.0 — Community Edition

**创建者：Eduardo Pagaza** · Copyright © 2026 Eduardo Pagaza

本软件是免费、完全**离线**运行的 HTML 工具，仅替换兼容 Allwinner IMAGEWTY 固件内的**静态启动图片**。不会覆盖原始固件，也不会向设备刷写文件。

**语言：**默认英语，可切换西班牙语和简体中文。**界面：**默认深色，也可选择浅色；浏览器允许时会保存偏好。

## 使用步骤

1. 解压 ZIP，使用新版 Chrome 或 Edge 打开 `Carabc_Logo_Editor_v1.0.0.html`，无需联网。
2. 在 **Load Firmware** 中选择制造商专门为设备**确切型号和硬件版本**提供的、未经修改的 `.img` 文件。
3. 在 **Customize Logo** 中选择 JPG、PNG、BMP 或 WebP。可设置保持比例的适配模式、10–200% 缩放、九点对齐、X/Y 偏移，以及纯色、渐变或图片背景。透明像素将与背景合成成不透明 JPEG。
4. 点击 **Preview result**，检查实际编码后的 JPEG。如果修改过图像设置，请重新预览。
5. 在 **Review & Save** 中阅读并确认警告。生成时只需选择一次文件名：浏览器支持时使用系统“另存为”，否则使用应用内对话框。
6. 在 **Verify Firmware** 中比较原始固件与自定义 `.img`，保存验证报告。
7. 阅读 **Next steps**，了解备份和兼容性注意事项。刷写设备需要另外遵循制造商针对具体设备的说明，本工具不提供刷写功能。

**背景提示：**已经包含在不透明 JPG 内的背景不能自动移除。若希望在黑色标志后显示浅色背景，应使用真正带透明通道的 PNG。生成的 JPEG 必须符合固件的大小和编码要求。

## 安全与兼容性

本软件可识别已知的 `IMAGEWTY 0x300/0x403` 容器结构，但**识别成功不表示固件能在某台设备上启动**。除启动图片、图片长度及相关校验和以外，固件其余字节应保持不变。

项目所有者报告在一台 Carabc HW601/DB601 V1.49、`txw38S0-nogps` 上成功安装了修改后的静态启动图。**这不代表对其他型号或硬件版本的兼容性保证。**请参阅 [已知兼容性](KNOWN_COMPATIBILITY.md) 和 [安全与限制](SAFETY_AND_COMPATIBILITY.md)。

工具包包括 HTML 程序、MIT 许可证 `LICENSE`、只读 Python 3 校验器 `tools/verify_imagewty.py`、`TEST_REPORT_v1.0.0.md` 和 `CHANGELOG.md`。

**本项目为独立社区工具，与 Carabc、Allwinner、BMW 或相关制造商没有隶属关系，也没有获得其认可或官方支持。**未随附第三方固件、品牌图片、驱动或刷机工具。
