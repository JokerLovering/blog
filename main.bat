@echo off
setlocal enabledelayedexpansion

rem 设置命令行编码为 UTF-8
chcp 65001 >nul

rem 运行 mkdocs serve 命令
python -m mkdocs serve

rem 检查错误级别
if %errorlevel% neq 0 (
    echo.
    echo 错误: mkdocs serve 命令执行失败 (错误代码: %errorlevel%)
) else (
    echo.
    echo mkdocs serve 命令执行成功
)

rem 防止窗口关闭
pause
endlocal