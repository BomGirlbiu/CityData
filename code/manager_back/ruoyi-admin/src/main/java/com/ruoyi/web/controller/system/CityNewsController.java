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
import com.ruoyi.system.domain.CityNews;
import com.ruoyi.system.service.ICityNewsService;
import com.ruoyi.common.utils.poi.ExcelUtil;
import com.ruoyi.common.core.page.TableDataInfo;

/**
 * 新闻列表Controller
 * 
 * @author zrt
 * @date 2024-11-07
 */
@RestController
@RequestMapping("/system/news")
public class CityNewsController extends BaseController
{
    @Autowired
    private ICityNewsService cityNewsService;

    /**
     * 查询新闻列表列表
     */
    @PreAuthorize("@ss.hasPermi('system:news:list')")
    @GetMapping("/list")
    public TableDataInfo list(CityNews cityNews)
    {
        startPage();
        List<CityNews> list = cityNewsService.selectCityNewsList(cityNews);
        return getDataTable(list);
    }

    /**
     * 导出新闻列表列表
     */
    @PreAuthorize("@ss.hasPermi('system:news:export')")
    @Log(title = "新闻列表", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, CityNews cityNews)
    {
        List<CityNews> list = cityNewsService.selectCityNewsList(cityNews);
        ExcelUtil<CityNews> util = new ExcelUtil<CityNews>(CityNews.class);
        util.exportExcel(response, list, "新闻列表数据");
    }

    /**
     * 获取新闻列表详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:news:query')")
    @GetMapping(value = "/{newsID}")
    public AjaxResult getInfo(@PathVariable("newsID") Long newsID)
    {
        return success(cityNewsService.selectCityNewsByNewsID(newsID));
    }

    /**
     * 新增新闻列表
     */
    @PreAuthorize("@ss.hasPermi('system:news:add')")
    @Log(title = "新闻列表", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody CityNews cityNews)
    {
        return toAjax(cityNewsService.insertCityNews(cityNews));
    }

    /**
     * 修改新闻列表
     */
    @PreAuthorize("@ss.hasPermi('system:news:edit')")
    @Log(title = "新闻列表", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody CityNews cityNews)
    {
        return toAjax(cityNewsService.updateCityNews(cityNews));
    }

    /**
     * 删除新闻列表
     */
    @PreAuthorize("@ss.hasPermi('system:news:remove')")
    @Log(title = "新闻列表", businessType = BusinessType.DELETE)
	@DeleteMapping("/{newsIDs}")
    public AjaxResult remove(@PathVariable Long[] newsIDs)
    {
        return toAjax(cityNewsService.deleteCityNewsByNewsIDs(newsIDs));
    }
}
