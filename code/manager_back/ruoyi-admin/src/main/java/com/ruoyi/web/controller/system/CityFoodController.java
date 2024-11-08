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
import com.ruoyi.system.domain.CityFood;
import com.ruoyi.system.service.ICityFoodService;
import com.ruoyi.common.utils.poi.ExcelUtil;
import com.ruoyi.common.core.page.TableDataInfo;

/**
 * 美食数据（1）Controller
 * 
 * @author zrt
 * @date 2024-11-07
 */
@RestController
@RequestMapping("/system/food")
public class CityFoodController extends BaseController
{
    @Autowired
    private ICityFoodService cityFoodService;

    /**
     * 查询美食数据（1）列表
     */
    @PreAuthorize("@ss.hasPermi('system:food:list')")
    @GetMapping("/list")
    public TableDataInfo list(CityFood cityFood)
    {
        startPage();
        List<CityFood> list = cityFoodService.selectCityFoodList(cityFood);
        return getDataTable(list);
    }

    /**
     * 导出美食数据（1）列表
     */
    @PreAuthorize("@ss.hasPermi('system:food:export')")
    @Log(title = "美食数据（1）", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, CityFood cityFood)
    {
        List<CityFood> list = cityFoodService.selectCityFoodList(cityFood);
        ExcelUtil<CityFood> util = new ExcelUtil<CityFood>(CityFood.class);
        util.exportExcel(response, list, "美食数据（1）数据");
    }

    /**
     * 获取美食数据（1）详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:food:query')")
    @GetMapping(value = "/{id}")
    public AjaxResult getInfo(@PathVariable("id") Long id)
    {
        return success(cityFoodService.selectCityFoodById(id));
    }

    /**
     * 新增美食数据（1）
     */
    @PreAuthorize("@ss.hasPermi('system:food:add')")
    @Log(title = "美食数据（1）", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody CityFood cityFood)
    {
        return toAjax(cityFoodService.insertCityFood(cityFood));
    }

    /**
     * 修改美食数据（1）
     */
    @PreAuthorize("@ss.hasPermi('system:food:edit')")
    @Log(title = "美食数据（1）", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody CityFood cityFood)
    {
        return toAjax(cityFoodService.updateCityFood(cityFood));
    }

    /**
     * 删除美食数据（1）
     */
    @PreAuthorize("@ss.hasPermi('system:food:remove')")
    @Log(title = "美食数据（1）", businessType = BusinessType.DELETE)
	@DeleteMapping("/{ids}")
    public AjaxResult remove(@PathVariable Long[] ids)
    {
        return toAjax(cityFoodService.deleteCityFoodByIds(ids));
    }
}
