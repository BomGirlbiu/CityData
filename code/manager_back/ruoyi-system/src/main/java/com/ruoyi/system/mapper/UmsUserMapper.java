package com.ruoyi.system.mapper;

import com.ruoyi.system.domain.UmsUser;

import java.util.List;

/**
 * 用户表 数据层
 * 
 * @author ruoyi
 */
public interface UmsUserMapper
{
    /**
     * 查询用户数据集合
     *
     * @param umsUser 作品ID信息
     * @return 作品ID数据集合
     */
    public List<UmsUser> selectUmsUserList(UmsUser umsUser);

    /**
     * 查询所有作品
     *
     * @return 作品ID列表
     */
    public List<UmsUser> selectUmsUserAll();

    /**
     * 通过作品ID查询作品信息
     *
     * @param id 用户ID
     * @return 角色对象信息
     */
    public UmsUser selectUmsUserById(String id);
//
//    /**
//     * 根据作品标题获取查询作品信息
//     *
//     * @param title 作品标题
//     * @return 选中作品标题
//     */
//    public String selectPostListByTitle(String title);
//
    /**
     * 根据用户姓名获取查询作品信息
     *
     * @param username 作者编号
     * @return 结果
     */
    public List<UmsUser> selectUmsUsersById(String username);


    /**
     * 删除作品信息
     *
     * @param id 作品ID
     * @return 结果
     */
    public int deleteUmsUserById(String id);

    /**
     * 批量删除作品
     *
     * @param id 需要删除的作品ID
     * @return 结果
     */
    public int deleteUmsUserByIds(String[] id);

    /**
     * 修改作品信息
     *
     * @param umsUser 作品信息
     * @return 结果
     */
    public int updateUmsUser(UmsUser umsUser);


    /**
     * 新增作品信息
     *
     * @param umsUser 作品信息
     * @return 结果
     */
    public int insertUmsUser(UmsUser umsUser);



}
