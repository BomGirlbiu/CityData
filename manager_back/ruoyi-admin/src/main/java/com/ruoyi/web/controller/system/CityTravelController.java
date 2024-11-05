package com.ruoyi.web.controller.system;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import org.apache.commons.lang3.ArrayUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.ruoyi.common.annotation.Log;
import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.domain.AjaxResult;
import com.ruoyi.system.domain.CityTravel;
import com.ruoyi.common.enums.BusinessType;
import com.ruoyi.common.utils.StringUtils;
import com.ruoyi.system.service.ICityTravelService;

/**
 * 部门信息
 * 
 * @author ruoyi
 */
@RestController
@RequestMapping("/system/city/cityTravel")
public class CityTravelController extends BaseController
{
    @Autowired
    private ICityTravelService cityTravelService;

    /**
     * 获取部门列表
     */
    @PreAuthorize("@ss.hasPermi('system:dept:list')")
    @GetMapping("list")
    public AjaxResult list(CityTravel dept)
    {
        List<CityTravel> depts = cityTravelService.selectCityTravelList(dept);
        return success(depts);
    }

    @PreAuthorize("@ss.hasPermi('system:dept:list')")
    @GetMapping("fetch")
    public AjaxResult fetch()
    {
        System.out.println("开始执行Python爬虫");

        String osName = System.getProperty("os.name").toLowerCase();
        String virtualEnvPath = "C:\\Users\\Childd\\OneDrive\\文档\\WeChat Files\\wxid_363gjm3h5v3y22\\FileStorage\\File\\2024-11\\Project_SoftwareTraining\\env"; // 替换为你的虚拟环境路径

        String pythonExecutable;
        String scriptPath = "C:\\Users\\Childd\\OneDrive\\文档\\WeChat Files\\wxid_363gjm3h5v3y22\\FileStorage\\File\\2024-11\\Project_SoftwareTraining\\trvl_spider.py";

        if (osName.contains("win")) {
            pythonExecutable = virtualEnvPath + "\\Scripts\\python.exe";
        } else if (osName.contains("mac") || osName.contains("nix") || osName.contains("nux")) {
            pythonExecutable = virtualEnvPath + "/bin/python3";
        } else {
            return error("不支持的操作系统: " + osName);
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

            return success("ok");
        } catch (Exception e) {
            e.printStackTrace();
            return error("执行Python脚本时发生错误: " + e.getMessage());
        }
    }


    /**
     * 查询部门列表（排除节点）
     */
    @PreAuthorize("@ss.hasPermi('system:dept:list')")
    @GetMapping("/list/exclude/{deptId}")
    public AjaxResult excludeChild(@PathVariable(value = "deptId", required = false) Long deptId)
    {
        List<CityTravel> depts = cityTravelService.selectCityTravelList(new CityTravel());
        depts.removeIf(d -> d.getId().intValue() == deptId || ArrayUtils.contains(StringUtils.split(d.getTitle(), ","), deptId + ""));
        return success(depts);
    }

    /**
     * 根据部门编号获取详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:dept:query')")
    @GetMapping(value = "/{deptId}")
    public AjaxResult getInfo(@PathVariable Long deptId)
    {
        cityTravelService.checkDeptDataScope(deptId);
        return success(cityTravelService.selectDeptById(deptId));
    }


    /**
     * 删除部门
     */
    @PreAuthorize("@ss.hasPermi('system:dept:remove')")
    @Log(title = "部门管理", businessType = BusinessType.DELETE)
    @DeleteMapping("/{deptId}")
    public AjaxResult remove(@PathVariable Long deptId)
    {
        if (cityTravelService.hasChildByDeptId(deptId))
        {
            return warn("存在下级部门,不允许删除");
        }
        if (cityTravelService.checkDeptExistUser(deptId))
        {
            return warn("部门存在用户,不允许删除");
        }
        cityTravelService.checkDeptDataScope(deptId);
        return toAjax(cityTravelService.deleteDeptById(deptId));
    }
}
