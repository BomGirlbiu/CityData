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
import com.ruoyi.system.domain.Wordcloud;
import com.ruoyi.system.service.IWordcloudService;
import com.ruoyi.common.utils.poi.ExcelUtil;
import com.ruoyi.common.core.page.TableDataInfo;

/**
 * 词云Controller
 * 
 * @author childa
 * @date 2024-11-08
 */
@RestController
@RequestMapping("/system/wordcloud")
public class WordcloudController extends BaseController
{
    @Autowired
    private IWordcloudService wordcloudService;

    /**
     * 查询词云列表
     */
    @PreAuthorize("@ss.hasPermi('system:wordcloud:list')")
    @GetMapping("/list")
    public TableDataInfo list(Wordcloud wordcloud)
    {
        startPage();
        List<Wordcloud> list = wordcloudService.selectWordcloudList(wordcloud);
        return getDataTable(list);
    }

    /**
     * 导出词云列表
     */
    @PreAuthorize("@ss.hasPermi('system:wordcloud:export')")
    @Log(title = "词云", businessType = BusinessType.EXPORT)
    @PostMapping("/export")
    public void export(HttpServletResponse response, Wordcloud wordcloud)
    {
        List<Wordcloud> list = wordcloudService.selectWordcloudList(wordcloud);
        ExcelUtil<Wordcloud> util = new ExcelUtil<Wordcloud>(Wordcloud.class);
        util.exportExcel(response, list, "词云数据");
    }

    /**
     * 获取词云详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:wordcloud:query')")
    @GetMapping(value = "/{cityName}")
    public AjaxResult getInfo(@PathVariable("cityName") String cityName)
    {
        return success(wordcloudService.selectWordcloudByCityName(cityName));
    }

    /**
     * 新增词云
     */
    @PreAuthorize("@ss.hasPermi('system:wordcloud:add')")
    @Log(title = "词云", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@RequestBody Wordcloud wordcloud)
    {
        return toAjax(wordcloudService.insertWordcloud(wordcloud));
    }

    /**
     * 修改词云
     */
    @PreAuthorize("@ss.hasPermi('system:wordcloud:edit')")
    @Log(title = "词云", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@RequestBody Wordcloud wordcloud)
    {
        return toAjax(wordcloudService.updateWordcloud(wordcloud));
    }

    /**
     * 删除词云
     */
    @PreAuthorize("@ss.hasPermi('system:wordcloud:remove')")
    @Log(title = "词云", businessType = BusinessType.DELETE)
	@DeleteMapping("/{cityNames}")
    public AjaxResult remove(@PathVariable String[] cityNames)
    {
        return toAjax(wordcloudService.deleteWordcloudByCityNames(cityNames));
    }
}
