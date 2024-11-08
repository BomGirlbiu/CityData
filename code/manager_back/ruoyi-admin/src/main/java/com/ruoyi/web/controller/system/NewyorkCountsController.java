package com.ruoyi.web.controller.system;

import java.util.List;
import javax.servlet.http.HttpServletResponse;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.ruoyi.common.annotation.Log;
import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.domain.AjaxResult;
import com.ruoyi.common.enums.BusinessType;
import com.ruoyi.system.domain.NewyorkCounts;
import com.ruoyi.system.service.INewyorkCountsService;
import com.ruoyi.common.utils.poi.ExcelUtil;
import com.ruoyi.common.core.page.TableDataInfo;

/**
 * 纽约时报报道量Controller
 * 
 * @author childa
 * @date 2024-11-08
 */
@RestController
@RequestMapping("/system/counts")
public class NewyorkCountsController extends BaseController
{
    @Autowired
    private INewyorkCountsService newyorkCountsService;

    /**
     * 查询纽约时报报道量列表
     */
    @PreAuthorize("@ss.hasPermi('system:counts:list')")
    @GetMapping("/list")
    public TableDataInfo list(NewyorkCounts newyorkCounts)
    {
        startPage();
        List<NewyorkCounts> list = newyorkCountsService.selectNewyorkCountsList(newyorkCounts);
        return getDataTable(list);
    }

    /**
     * 导出纽约时报报道量列表
     */
    @PreAuthorize("@ss.hasPermi('system:counts:export')")
    @Log(title = "纽约时报报道量", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, NewyorkCounts newyorkCounts)
    {
        List<NewyorkCounts> list = newyorkCountsService.selectNewyorkCountsList(newyorkCounts);
        ExcelUtil<NewyorkCounts> util = new ExcelUtil<NewyorkCounts>(NewyorkCounts.class);
        util.exportExcel(response, list, "纽约时报报道量数据");
    }

    /**
     * 获取纽约时报报道量详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:counts:query')")
    @GetMapping(value = "/{cityname}")
    public AjaxResult getInfo(@PathVariable("cityname") String cityname)
    {
        return success(newyorkCountsService.selectNewyorkCountsByCityname(cityname));
    }

    /**
     * 新增纽约时报报道量
     */
    @PreAuthorize("@ss.hasPermi('system:counts:add')")
    @Log(title = "纽约时报报道量", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody NewyorkCounts newyorkCounts)
    {
        return toAjax(newyorkCountsService.insertNewyorkCounts(newyorkCounts));
    }

    /**
     * 修改纽约时报报道量
     */
    @PreAuthorize("@ss.hasPermi('system:counts:edit')")
    @Log(title = "纽约时报报道量", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody NewyorkCounts newyorkCounts)
    {
        return toAjax(newyorkCountsService.updateNewyorkCounts(newyorkCounts));
    }

    /**
     * 删除纽约时报报道量
     */
    @PreAuthorize("@ss.hasPermi('system:counts:remove')")
    @Log(title = "纽约时报报道量", businessType = BusinessType.DELETE)
	@DeleteMapping("/{citynames}")
    public AjaxResult remove(@PathVariable String[] citynames)
    {
        return toAjax(newyorkCountsService.deleteNewyorkCountsByCitynames(citynames));
    }
}
