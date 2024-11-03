package com.ruoyi.web.controller.system;

import com.ruoyi.common.annotation.Log;
import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.domain.AjaxResult;
import com.ruoyi.common.core.page.TableDataInfo;
import com.ruoyi.common.enums.BusinessType;
import com.ruoyi.common.utils.poi.ExcelUtil;
import com.ruoyi.framework.web.domain.server.Sys;
import com.ruoyi.system.domain.BmsPost;
import com.ruoyi.system.service.IBmsPostService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.util.List;
import java.util.UUID;

/**
 * 作品信息操作处理
 * 
 * @author ruoyi
 */
@RestController
@RequestMapping("/system/post")
public class BmsPostController extends BaseController
{
    @Autowired
    private IBmsPostService postService;

    /**
     * 获取作品列表
     */
    @PreAuthorize("@ss.hasPermi('system:post:list')")
    @GetMapping("/list")
    public TableDataInfo list(BmsPost post)
    {
        startPage();
        System.out.println(post);
        List<BmsPost> list = postService.selectPostList(post);
        return getDataTable(list);
    }
    
    @Log(title = "作品管理", businessType = BusinessType.EXPORT)
    @PreAuthorize("@ss.hasPermi('system:post:export')")
    @PostMapping("/export")
    public void export(HttpServletResponse response, BmsPost post)
    {
        List<BmsPost> list = postService.selectPostList(post);
        ExcelUtil<BmsPost> util = new ExcelUtil<BmsPost>(BmsPost.class);
        util.exportExcel(response, list, "作品数据");
    }

    /**
     * 根据作品编号获取详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:post:query')")
    @GetMapping(value = "/{postId}")
    public AjaxResult getInfo(@PathVariable Integer postId)
    {

        System.out.println("根据作品编号查找");
        return success(postService.selectPostById(postId));
    }

    /**
     * 新增作品
     */
    @PreAuthorize("@ss.hasPermi('system:post:add')")
    @Log(title = "作品管理", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@Validated @RequestBody BmsPost post)
    {
        post.setId(UUID.randomUUID().toString());
        System.err.println(post.getPostId());
//        if (!postService.checkPostNameUnique(post))
//        {
//            return error("新增作品'" + post.getPostName() + "'失败，作品名称已存在");
//        }
//        else if (!postService.checkPostCodeUnique(post))
//        {
//            return error("新增作品'" + post.getPostName() + "'失败，作品编码已存在");
//        }
        post.setCreateBy(getUsername());
        return toAjax(postService.insertPost(post));
    }

    /**
     * 修改作品
     */
    @PreAuthorize("@ss.hasPermi('system:post:edit')")
    @Log(title = "作品管理", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@Validated @RequestBody BmsPost post)
    {
//        if (!postService.checkPostNameUnique(post))
//        {
//            return error("修改作品'" + post.getPostName() + "'失败，作品名称已存在");
//        }
//        else if (!postService.checkPostCodeUnique(post))
//        {
//            return error("修改作品'" + post.getPostName() + "'失败，作品编码已存在");
//        }

        post.setUpdateBy(getUsername());//更新者
        System.out.println(getUsername());
        return toAjax(postService.updatePost(post));
    }
//
    /**
     * 删除作品
     */
    @PreAuthorize("@ss.hasPermi('system:post:remove')")
    @Log(title = "作品管理", businessType = BusinessType.DELETE)
    @DeleteMapping("/{postIds}")
    public AjaxResult remove(@PathVariable int[] postIds)
    {
        return toAjax(postService.deletePostByIds(postIds));
    }

    /**
     * 获取作品选择框列表
     */
    @GetMapping("/optionselect")
    public AjaxResult optionselect()
    {
        List<BmsPost> posts = postService.selectPostAll();
        return success(posts);
    }
}
