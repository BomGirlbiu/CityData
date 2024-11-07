package com.ruoyi.web.controller.system;

import com.ruoyi.common.annotation.Log;
import com.ruoyi.common.core.controller.BaseController;
import com.ruoyi.common.core.domain.AjaxResult;
import com.ruoyi.common.core.page.TableDataInfo;
import com.ruoyi.common.enums.BusinessType;
import com.ruoyi.common.utils.poi.ExcelUtil;
import com.ruoyi.common.utils.uuid.SnowflakeIdUtils;
import com.ruoyi.system.domain.UmsUser;
import com.ruoyi.system.service.IUmsUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.util.List;

/**
 * 用户信息
 * 
 * @author ruoyi
 */
@RestController
@RequestMapping("/system/comUser")
public class UmsUserController extends BaseController
{
    @Autowired
    private IUmsUserService userService;

    /**
     * 获取用户列表
     */
    @PreAuthorize("@ss.hasPermi('system:user:list')")
    @GetMapping("/list")
    public TableDataInfo list(UmsUser user)
    {
        startPage();
        System.out.println(user);
        List<UmsUser> list = userService.selectUmsUserList(user);
        return getDataTable(list);
    }

    @Log(title = "用户管理", businessType = BusinessType.EXPORT)
    @PreAuthorize("@ss.hasPermi('system:user:export')")
    @PostMapping("/export")
    public void export(HttpServletResponse response, UmsUser user)
    {
        List<UmsUser> list = userService.selectUmsUserList(user);
        ExcelUtil<UmsUser> util = new ExcelUtil<UmsUser>(UmsUser.class);
        util.exportExcel(response, list, "用户数据");
    }

    /**
     * 根据用户编号获取详细信息
     */
    @PreAuthorize("@ss.hasPermi('system:user:query')")
    @GetMapping(value = "/{id}")
    public AjaxResult getInfo(@PathVariable String id)
    {

        System.out.println("根据用户编号查找");
        return success(userService.selectUmsUserById(id));
    }

    /**
     * 新增用户
     */
    @PreAuthorize("@ss.hasPermi('system:user:add')")
    @Log(title = "用户管理", businessType = BusinessType.INSERT)
    @PostMapping
    public AjaxResult add(@Validated @RequestBody UmsUser user)
    {

        String id = String.valueOf(new SnowflakeIdUtils(5,8).nextId());
        System.err.println("id"+id);
        user.setId(id);
        System.err.println(user);
//        user.setId(UUID.randomUUID().toString());
//        System.err.println(user.getId());
//        if (!userService.checkUmsUserNameUnique(user))
//        {
//            return error("新增用户'" + user.getUmsUserName() + "'失败，用户名称已存在");
//        }
//        else if (!userService.checkUmsUserCodeUnique(user))
//        {
//            return error("新增用户'" + user.getUmsUserName() + "'失败，用户编码已存在");
//        }
//        user.setCreateBy(getUsername());
        return toAjax(userService.insertUmsUser(user));
    }

    /**
     * 修改用户
     */
    @PreAuthorize("@ss.hasPermi('system:user:edit')")
    @Log(title = "用户管理", businessType = BusinessType.UPDATE)
    @PutMapping
    public AjaxResult edit(@Validated @RequestBody UmsUser user)
    {
//        if (!userService.checkPostNameUnique(user))
//        {
//            return error("修改用户'" + user.getPostName() + "'失败，用户名称已存在");
//        }
//        else if (!userService.checkPostCodeUnique(user))
//        {
//            return error("修改用户'" + user.getPostName() + "'失败，用户编码已存在");
//        }

//        user.setUpdateBy(getUsername());//更新者
//        System.out.println(getUsername());
        return toAjax(userService.updateUmsUser(user));
    }
//
    /**
     * 删除用户
     */
    @PreAuthorize("@ss.hasPermi('system:user:remove')")
    @Log(title = "用户管理", businessType = BusinessType.DELETE)
    @DeleteMapping("/{ids}")
    public AjaxResult remove(@PathVariable String[] ids)
    {
        return toAjax(userService.deleteUmsUserByIds(ids));
    }

    /**
     * 获取用户选择框列表
     */
    @GetMapping("/optionselect")
    public AjaxResult optionselect()
    {
        List<UmsUser> users = userService.selectUmsUserAll();
        return success(users);
    }
}
