package com.ruoyi.system.service;

import com.ruoyi.system.domain.BmsPost;

import java.util.List;

/**
 * 作品信息 服务层
 * 
 * @author ruoyi
 */
public interface IBmsPostService
{
    /**
     * 查询作品信息集合
     * 
     * @param post 作品信息
     * @return 作品列表
     */
    public List<BmsPost> selectPostList(BmsPost post);

    /**
     * 查询所有作品
     *
     * @return 作品列表
     */
    public List<BmsPost> selectPostAll();

    /**
     * 通过作品编码查询作品信息
     *
     * @param id 作品ID
     * @return 角色对象信息
     */
    public BmsPost selectPostById(Integer postId);

    /**
     * 根据作者编码获取作品选择框列表
     *
     * @param userId 用户ID
     * @return 选中作品ID列表
     */
    public List<BmsPost> selectPostListByUserId(String userId);

//    /**
//     * 校验作品名称
//     *
//     * @param post 作品信息
//     * @return 结果
//     */
//    public boolean checkPostNameUnique(BmsPost post);
//
//    /**
//     * 校验作品编码
//     *
//     * @param post 作品信息
//     * @return 结果
//     */
//    public boolean checkPostCodeUnique(BmsPost post);

//    /**
//     * 通过作品ID查询作品使用数量
//     *
//     * @param postId 作品ID
//     * @return 结果
//     */
//    public int countUserPostById(Long postId);
//
    /**
     * 删除作品信息
     *
     * @param id 作品ID
     * @return 结果
     */
    public int deletePostById(int postId);

    /**
     * 批量删除作品信息
     *
     * @param ids 需要删除的作品ID
     * @return 结果
     */
    public int deletePostByIds(int[] postIds);

    /**
     * 新增保存作品信息
     *
     * @param post 作品信息
     * @return 结果
     */
    public int insertPost(BmsPost post);

    /**
     * 修改保存作品信息
     *
     * @param post 作品信息
     * @return 结果
     */
    public int updatePost(BmsPost post);
}
