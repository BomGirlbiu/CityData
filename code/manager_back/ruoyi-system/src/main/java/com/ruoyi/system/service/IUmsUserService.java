package com.ruoyi.system.service;

import com.ruoyi.system.domain.UmsUser;

import java.util.List;

/**
 * 用户 业务层
 * 
 * @author ruoyi
 */
public interface IUmsUserService
{
    /**
     * 查询用户信息集合
     *
     * @param user 用户信息
     * @return 用户列表
     */
    public List<UmsUser> selectUmsUserList(UmsUser user);

    /**
     * 查询所有用户
     *
     * @return 用户列表
     */
    public List<UmsUser> selectUmsUserAll();

    /**
     * 通过用户编码查询用户信息
     *
     * @param id 用户ID
     * @return 角色对象信息
     */
    public UmsUser selectUmsUserById(String id);

    /**
     * 删除用户信息
     *
     * @param id 用户ID
     * @return 结果
     */
    public int deleteUmsUserById(String id);

    /**
     * 批量删除用户信息
     *
     * @param ids 需要删除的用户ID
     * @return 结果
     */
    public int deleteUmsUserByIds(String[] ids);

    /**
     * 新增保存用户信息
     *
     * @param user 用户信息
     * @return 结果
     */
    public int insertUmsUser(UmsUser user);

    /**
     * 修改保存用户信息
     *
     * @param user 用户信息
     * @return 结果
     */
    public int updateUmsUser(UmsUser user);
}
