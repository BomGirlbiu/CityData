package com.ruoyi.system.mapper;
import com.ruoyi.system.domain.BmsPost;


import java.util.List;


/**
 * 作品信息 数据层
 *
 * @author ruoyi
 */
public interface BmsPostMapper {
    /**
     * 查询作品ID数据集合
     *
     * @param post 作品ID信息
     * @return 作品ID数据集合
     */
    public List<BmsPost> selectPostList(BmsPost post);

    /**
     * 查询所有作品
     *
     * @return 作品ID列表
     */
    public List<BmsPost> selectPostAll();

    /**
     * 通过作品ID查询作品信息
     *
     * @param postId 作品ID
     * @return 角色对象信息
     */
    public BmsPost selectPostById(Integer postId);
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
     * 根据作者编号获取查询作品信息
     *
     * @param userId 作者编号
     * @return 结果
     */
    public List<BmsPost> selectPostsByUserId(String userId);


    /**
     * 删除作品信息
     *
     * @param postId 作品ID
     * @return 结果
     */
    public int deletePostById(int postId);

    /**
     * 批量删除作品
     *
     * @param postId 需要删除的作品ID
     * @return 结果
     */
    public int deletePostByIds(int[] postId);

    /**
     * 修改作品信息
     *
     * @param post 作品信息
     * @return 结果
     */
    public int updatePost(BmsPost post);


    /**
     * 新增作品信息
     *
     * @param post 作品信息
     * @return 结果
     */
    public int insertPost(BmsPost post);


//    /**
//     * 校验作者名称
//     *
//     * @param userId 作者名称
//     * @return 结果
//     */
//    public BmsPost checkPostUserIdUnique(String userId);
//
//    /**
//     * 校验作品编码
//     *
//     * @param id 作品编码
//     * @return 结果
//     */
//    public BmsPost checkPostIdUnique(String id);

}
