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
import com.ruoyi.system.domain.CityTravel;
import com.ruoyi.system.service.ICityTravelService;
import com.ruoyi.common.utils.poi.ExcelUtil;
import com.ruoyi.common.core.page.TableDataInfo;

/**
 * 城市旅游Controller
 * 
 * @author zrt
 * @date 2024-11-07
 */
@RestController
@RequestMapping("/system/travel")
public class CityTravelController extends BaseController
{
    @Autowired
    private ICityTravelService cityTravelService;

    /**
     * 查询城市旅游列表
     */
    @PreAuthorize("@ss.hasPermi('system:travel:list')")
    @GetMapping("/list")
    public TableDataInfo list(CityTravel cityTravel)
    {
        startPage();
        List<CityTravel> list = cityTravelService.selectCityTravelList(cityTravel);
        return getDataTable(list);
    }

    /**
     * 导出城市旅游列表
     */
    @PreAuthorize("@ss.hasPermi('system:travel:export')")
    @Log(title = "城市旅游", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, CityTravel cityTravel)
    {
        List<CityTravel> list = cityTravelService.selectCityTravelList(cityTravel);
        ExcelUtil<CityTravel> util = new ExcelUtil<CityTravel>(CityTravel.class);
        util.exportExcel(response, list, "城市旅游数据");
    }

    /**
     * 获取城市旅游详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:travel:query')")
    @GetMapping(value = "/{id}")
    public AjaxResult getInfo(@PathVariable("id") Long id)
    {
        return success(cityTravelService.selectCityTravelById(id));
    }

    /**
     * 新增城市旅游
     */
    @PreAuthorize("@ss.hasPermi('system:travel:add')")
    @Log(title = "城市旅游", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody CityTravel cityTravel)
    {
        return toAjax(cityTravelService.insertCityTravel(cityTravel));
    }

    /**
     * 修改城市旅游
     */
    @PreAuthorize("@ss.hasPermi('system:travel:edit')")
    @Log(title = "城市旅游", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody CityTravel cityTravel)
    {
        return toAjax(cityTravelService.updateCityTravel(cityTravel));
    }

    /**
     * 删除城市旅游
     */
    @PreAuthorize("@ss.hasPermi('system:travel:remove')")
    @Log(title = "城市旅游", businessType = BusinessType.DELETE)
	@DeleteMapping("/{ids}")
    public AjaxResult remove(@PathVariable Long[] ids)
    {
        return toAjax(cityTravelService.deleteCityTravelByIds(ids));
    }
}
