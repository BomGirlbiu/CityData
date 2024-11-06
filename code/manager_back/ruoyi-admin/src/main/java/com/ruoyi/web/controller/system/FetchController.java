package com.ruoyi.web.controller.system;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.domain.AjaxResult;

@RestController
@RequestMapping("/system/fetch")
public class FetchController extends BaseController{
    @GetMapping("")
    protected AjaxResult fetch(@RequestParam(value = "name", required = false) String name)
    {
        if (name == null || name.isEmpty()) {
            return error("参数 name 不能为空");
        }
        System.out.println("开始执行Python爬虫");
        String virtualEnvPath="C:\\Users\\Childd\\OneDrive\\文档\\WeChat Files\\wxid_363gjm3h5v3y22\\FileStorage\\File\\2024-11\\Project_SoftwareTraining\\env"; // 替换为你的虚拟环境路径;
        String scriptPath= "D:\\临时\\code\\pyscripts\\pys\\trvl_spider.py";
        String osName = System.getProperty("os.name").toLowerCase();
        if("travel".equals(name)){
            virtualEnvPath = "C:\\Users\\Childd\\OneDrive\\文档\\WeChat Files\\wxid_363gjm3h5v3y22\\FileStorage\\File\\2024-11\\Project_SoftwareTraining\\env"; // 替换为你的虚拟环境路径
            scriptPath = "D:\\临时\\code\\pyscripts\\pys\\trvl_spider.py";// 替换为你的Python脚本路径
        }
        String pythonExecutable;
        if (osName.contains("win")) {
            pythonExecutable = virtualEnvPath + "\\Scripts\\python.exe";
        } else if (osName.contains("mac") || osName.contains("nix") || osName.contains("nux")) {
            pythonExecutable = virtualEnvPath + "/bin/python3";
        } else {
            return error("不支持的操作系统");
        }

        String[] args = { pythonExecutable, scriptPath };

        try {
            Process proc = Runtime.getRuntime().exec(args);

            // 获取Python脚本的标准输出
            BufferedReader stdoutReader = new BufferedReader(new InputStreamReader(proc.getInputStream()));
            String line;
            StringBuilder output = new StringBuilder();
            while ((line = stdoutReader.readLine()) != null) {
                output.append(line).append("\n");
            }
            System.out.println("Python脚本输出: " + output.toString());

            // 获取Python脚本的标准错误输出
            BufferedReader stderrReader = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
            StringBuilder errorOutput = new StringBuilder();
            while ((line = stderrReader.readLine()) != null) {
                errorOutput.append(line).append("\n");
            }
            System.out.println("Python脚本错误输出: " + errorOutput.toString());

            int exitCode = proc.waitFor();
            System.out.println("Python脚本退出码: " + exitCode);

            // 关闭输入输出流
            stdoutReader.close();
            stderrReader.close();

            return success("爬取成功！");
        } catch (Exception e) {
            e.printStackTrace();
            return error("爬取失败！");
        }
    }
}
