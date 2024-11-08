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
import com.ruoyi.system.domain.Cityattributes;
import com.ruoyi.system.service.ICityattributesService;
import com.ruoyi.common.utils.poi.ExcelUtil;
import com.ruoyi.common.core.page.TableDataInfo;

/**
 * 城市传播指数Controller
 * 
 * @author zrt
 * @date 2024-11-08
 */
@RestController
@RequestMapping("/system/cityattributes")
public class CityattributesController extends BaseController
{
    @Autowired
    private ICityattributesService cityattributesService;

    /**
     * 查询城市传播指数列表
     */
    @PreAuthorize("@ss.hasPermi('system:cityattributes:list')")
    @GetMapping("/list")
    public TableDataInfo list(Cityattributes cityattributes)
    {
        startPage();
        List<Cityattributes> list = cityattributesService.selectCityattributesList(cityattributes);
        return getDataTable(list);
    }

    /**
     * 导出城市传播指数列表
     */
    @PreAuthorize("@ss.hasPermi('system:cityattributes:export')")
    @Log(title = "城市传播指数", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, Cityattributes cityattributes)
    {
        List<Cityattributes> list = cityattributesService.selectCityattributesList(cityattributes);
        ExcelUtil<Cityattributes> util = new ExcelUtil<Cityattributes>(Cityattributes.class);
        util.exportExcel(response, list, "城市传播指数数据");
    }

    /**
     * 获取城市传播指数详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:cityattributes:query')")
    @GetMapping(value = "/{cityID}")
    public AjaxResult getInfo(@PathVariable("cityID") Integer cityID)
    {
        return success(cityattributesService.selectCityattributesByCityID(cityID));
    }

    /**
     * 新增城市传播指数
     */
    @PreAuthorize("@ss.hasPermi('system:cityattributes:add')")
    @Log(title = "城市传播指数", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody Cityattributes cityattributes)
    {
        return toAjax(cityattributesService.insertCityattributes(cityattributes));
    }

    /**
     * 修改城市传播指数
     */
    @PreAuthorize("@ss.hasPermi('system:cityattributes:edit')")
    @Log(title = "城市传播指数", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody Cityattributes cityattributes)
    {
        return toAjax(cityattributesService.updateCityattributes(cityattributes));
    }

    /**
     * 删除城市传播指数
     */
    @PreAuthorize("@ss.hasPermi('system:cityattributes:remove')")
    @Log(title = "城市传播指数", businessType = BusinessType.DELETE)
	@DeleteMapping("/{cityIDs}")
    public AjaxResult remove(@PathVariable Integer[] cityIDs)
    {
        return toAjax(cityattributesService.deleteCityattributesByCityIDs(cityIDs));
    }
}
