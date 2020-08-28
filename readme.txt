使用步骤：
1、nessus导出英文版漏洞扫描结果example.csv文件。
2、python3环境下运行translater.py脚本，即cd到本目录下然后执行translater.py example.csv。
3、生成经过翻译的example_translation.csv文件，导入测评能手漏洞审计模块。

注意事项：
1、初次使用可能需要一些依赖包，根据报错提示在python3环境下执行pip install xxx即可。
2、目前字典vulLib.db不够全面，无法覆盖全部漏洞，且部分翻译存在特殊字符（例如？）需要手动检查导入结果并做二次编辑。
3、有一些特殊字符可能存在编码问题，需要根据cmd执行过程中的提示，在程序运行结束后手动排查一下是否有错误翻译。
