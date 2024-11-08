package com.ruoyi.web.controller.system;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.domain.AjaxResult;

@RestController
@RequestMapping("/system/fetch")
public class FetchController extends BaseController{
    private final ExecutorService executorService = Executors.newFixedThreadPool(5);

    private ProcessBuilder getProcessBuilder(String type,String sPath,String wPath,long taskId){
        // 替换为你的虚拟环境路径;
        String virtualEnvPath="C:\\Users\\Childd\\OneDrive\\文档\\WeChat Files\\wxid_363gjm3h5v3y22\\FileStorage\\File\\2024-11\\Project_SoftwareTraining\\env";
        String osName = System.getProperty("os.name").toLowerCase();
        List<String> command = new ArrayList<>();
        if("python".equals(type)){
            String pythonExecutable;
            if (osName.contains("win")) {
                pythonExecutable = virtualEnvPath + "\\Scripts\\python.exe";
            } else if (osName.contains("mac") || osName.contains("nix") || osName.contains("nux")) {
                pythonExecutable = virtualEnvPath + "/bin/python3";
            } else {
                TaskManager.updateTaskStatus(taskId, "FAILED", "不支持的操作系统");
                return null;
            }
            command.add(pythonExecutable);
            command.add(sPath);
            return new ProcessBuilder(command);
        }
        else{
            if (!osName.contains("win")) {
                TaskManager.updateTaskStatus(taskId, "FAILED", "不支持的操作系统");
                return null;
            }
            command.add(sPath);
            command.add(virtualEnvPath);
            ProcessBuilder processBuilder = new ProcessBuilder(command);
            processBuilder.directory(new File(wPath)); // 设置工作目录
            return processBuilder;
        }
    }
    @GetMapping("")
    protected AjaxResult fetch(@RequestParam(value = "name", required = false) String name)
    {
        if (name == null || name.isEmpty()) {
            return error("参数 name 不能为空");
        }
        System.out.println("开始执行Python爬虫");
        long taskId = TaskManager.createTask();
        Runnable task = () -> {
            try {
                ProcessBuilder processBuilder = null;
                if("travel".equals(name)){
                    processBuilder = getProcessBuilder(
                        "python",
                        "D:\\临时\\code\\pyscripts\\pys\\trvl_spider.py",
                        "",
                        taskId);
                }
                else if("food".equals(name)){
                    processBuilder=getProcessBuilder(
                        "python",
                        "D:\\临时\\code\\pyscripts\\pys\\sfd_spider.py",
                        "",
                        taskId);
                }
                else if("visualChina".equals(name)){
                    processBuilder=getProcessBuilder(
                        "bat",
                        "D:\\临时\\code\\pyscripts\\VisualChinaGroup_spider\\run.bat",
                        "D:\\临时\\code\\pyscripts\\VisualChinaGroup_spider",
                        taskId);
                }
                if(processBuilder==null){
                    TaskManager.updateTaskStatus(taskId, "FAILED", "未知错误！");
                    return;
                }
                processBuilder.directory(new File("D:\\临时\\code\\pyscripts\\VisualChinaGroup_spider")); // 设置工作目录

                Process proc = processBuilder.start();
                //Process proc = Runtime.getRuntime().exec(command.toArray(new String[0]));

                // 获取Python脚本的标准输出
                BufferedReader stdoutReader = new BufferedReader(new InputStreamReader(proc.getInputStream()));
                BufferedReader stderrReader = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
                StringBuilder output = new StringBuilder();
                StringBuilder errorOutput = new StringBuilder();

                String line;
                while ((line = stdoutReader.readLine()) != null) {
                    System.out.println(line);
                    output.append(line).append("\n");
                }
                while ((line = stderrReader.readLine()) != null) {
                    System.out.println(line);
                    errorOutput.append(line).append("\n");
                }

                int exitCode = proc.waitFor();
                stdoutReader.close();
                stderrReader.close();

                if (exitCode == 0) {
                    TaskManager.updateTaskStatus(taskId, "COMPLETED", output.toString());
                } else {
                    TaskManager.updateTaskStatus(taskId, "FAILED", errorOutput.toString());
                }
            } catch (Exception e) {
                e.printStackTrace();
                TaskManager.updateTaskStatus(taskId, "FAILED", "爬取失败！");
            }
        };
        executorService.submit(task);

        return success(taskId);
    }

    @GetMapping("/status")
    protected AjaxResult getTaskStatus(@RequestParam long taskId) {
        System.out.println("任务");
        TaskManager.TaskStatus taskStatus = TaskManager.getTaskStatus(taskId);
        if (taskStatus == null) {
            return error("无效的任务ID");
        }

        return success(taskStatus);
    }
}
