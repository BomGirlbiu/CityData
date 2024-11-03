package com.ruoyi.system.service.impl;

import com.ruoyi.system.domain.BmsPost;
import com.ruoyi.system.domain.BmsPost;
import com.ruoyi.system.mapper.BmsPostMapper;
import com.ruoyi.system.service.IBmsPostService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 *作品信息 服务层处理
 * 
 * @author ruoyi
 */
@Service
public class BmsPostServiceImpl implements IBmsPostService
{
    @Autowired
    private BmsPostMapper postMapper;

//    @Autowired
//    private SysUserPostMapper userPostMapper;

    /**
     * 查作品信息集合
     * 
     * @param post 作品信息
     * @return作品信息集合
     */
    @Override
    public List<BmsPost> selectPostList(BmsPost post)
    {
        return postMapper.selectPostList(post);
    }

    /**
     * 查询所作品
     *
     * @return作品列表
     */
    @Override
    public List<BmsPost> selectPostAll()
    {
        return postMapper.selectPostAll();
    }

    /**
     * 通作品ID查作品信息
     *
     * @param id 作品ID
     * @return 角色对象信息
     */
    @Override
    public BmsPost selectPostById(Integer postId)
    {
        return postMapper.selectPostById(postId);
    }

    /**
     * 根据作者编码获作品选择框列表
     *
     * @param userId 作者ID
     * @return 选作品ID列表
     */
    @Override
    public List<BmsPost> selectPostListByUserId(String userId)
    {
//        return postMapper.selectPostListByUserId(userId);
        return postMapper.selectPostsByUserId(userId);
    }
//
//    /**
//     * 校作品名称是否唯一
//     *
//     * @param post 作品信息
//     * @return 结果
//     */
//    @Override
//    public boolean checkPostNameUnique(SysPost post)
//    {
//        Long postId = StringUtils.isNull(post.getPostId()) ? -1L : post.getPostId();
//        SysPost info = postMapper.checkPostNameUnique(post.getPostName());
//        if (StringUtils.isNotNull(info) && info.getPostId().longValue() != postId.longValue())
//        {
//            return UserConstants.NOT_UNIQUE;
//        }
//        return UserConstants.UNIQUE;
//    }
//
//    /**
//     * 校作品编码是否唯一
//     *
//     * @param post作品信息
//     * @return 结果
//     */
//    @Override
//    public boolean checkPostCodeUnique(SysPost post)
//    {
//        Long postId = StringUtils.isNull(post.getPostId()) ? -1L : post.getPostId();
//        SysPost info = postMapper.checkPostCodeUnique(post.getPostCode());
//        if (StringUtils.isNotNull(info) && info.getPostId().longValue() != postId.longValue())
//        {
//            return UserConstants.NOT_UNIQUE;
//        }
//        return UserConstants.UNIQUE;
//    }
//
//    /**
//     * 通作品ID查作品使用数量
//     *
//     * @param postId作品ID
//     * @return 结果
//     */
//    @Override
//    public int countUserPostById(Long postId)
//    {
//        return userPostMapper.countUserPostById(postId);
//    }
//
    /**
     * 删作品信息
     *
     * @param postId 作品ID
     * @return 结果
     */
    @Override
    public int deletePostById(int postId)
    {
        return postMapper.deletePostById(postId);
    }

    /**
     * 批量删作品信息
     *
     * @param postIds 需要删除作品ID
     * @return 结果
     */
    @Override
    public int deletePostByIds(int[] postIds)
    {
//        for (int id : ids)
//        {
//            BmsPost post = selectPostById(id);
//            if (countUserPostById(id) > 0)
//            {
//                throw new ServiceException(String.format("%1$s已分配,不能删除", post.getPostName()));
//            }
//        }
        return postMapper.deletePostByIds(postIds);
    }
//
    /**
     * 新增保作品信息
     *
     * @param post 作品信息
     * @return 结果
     */
    @Override
    public int insertPost(BmsPost post)
    {
        return postMapper.insertPost(post);
    }

    /**
     * 修改保作品信息
     *
     * @param post 作品信息
     * @return 结果
     */
    @Override
    public int updatePost(BmsPost post)
    {
        return postMapper.updatePost(post);
    }
}
