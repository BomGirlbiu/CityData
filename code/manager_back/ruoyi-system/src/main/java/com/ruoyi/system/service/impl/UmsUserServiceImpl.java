package com.ruoyi.system.service.impl;

import com.ruoyi.system.domain.UmsUser;
import com.ruoyi.system.mapper.UmsUserMapper;
import com.ruoyi.system.service.IUmsUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 *社区用户 业务层处理
 * 
 * @author ruoyi
 */
@Service
public class UmsUserServiceImpl implements IUmsUserService
{
    @Autowired
    private UmsUserMapper umsUserMapper;

//    @Autowired
//    private SysUserPostMapper userPostMapper;

    /**
     * 查作品信息集合
     *
     * @param user 作品信息
     * @return作品信息集合
     */
    @Override
    public List<UmsUser> selectUmsUserList(UmsUser user)
    {
        return umsUserMapper.selectUmsUserList(user);
    }

    /**
     * 查询所作品
     *
     * @return作品列表
     */
    @Override
    public List<UmsUser> selectUmsUserAll()
    {
        return umsUserMapper.selectUmsUserAll();
    }

    /**
     * 通作品ID查作品信息
     *
     * @param id 作品ID
     * @return 角色对象信息
     */
    @Override
    public UmsUser selectUmsUserById(String id)
    {
        return umsUserMapper.selectUmsUserById(id);
    }

//    /**
//     * 根据作者编码获作品选择框列表
//     *
//     * @param id 作者ID
//     * @return 选作品ID列表
//     */
//    @Override
//    public List<UmsUser> selectUmsUserListByUserId(String id)
//    {
////        return umsUserMapper.selectPostListByUserId(userId);
//        return umsUserMapper.selectUmsUsersById(id);
//    }
//
//    /**
//     * 校作品名称是否唯一
//     *
//     * @param user 作品信息
//     * @return 结果
//     */
//    @Override
//    public boolean checkPostNameUnique(SysPost user)
//    {
//        Long userId = StringUtils.isNull(user.getPostId()) ? -1L : user.getPostId();
//        SysPost info = umsUserMapper.checkPostNameUnique(user.getPostName());
//        if (StringUtils.isNotNull(info) && info.getPostId().longValue() != userId.longValue())
//        {
//            return UserConstants.NOT_UNIQUE;
//        }
//        return UserConstants.UNIQUE;
//    }
//
//    /**
//     * 校作品编码是否唯一
//     *
//     * @param user作品信息
//     * @return 结果
//     */
//    @Override
//    public boolean checkPostCodeUnique(SysPost user)
//    {
//        Long userId = StringUtils.isNull(user.getPostId()) ? -1L : user.getPostId();
//        SysPost info = umsUserMapper.checkPostCodeUnique(user.getPostCode());
//        if (StringUtils.isNotNull(info) && info.getPostId().longValue() != userId.longValue())
//        {
//            return UserConstants.NOT_UNIQUE;
//        }
//        return UserConstants.UNIQUE;
//    }
//
//    /**
//     * 通作品ID查作品使用数量
//     *
//     * @param userId作品ID
//     * @return 结果
//     */
//    @Override
//    public int countUserPostById(Long userId)
//    {
//        return userPostMapper.countUserPostById(userId);
//    }
//
    /**
     * 删作品信息
     *
     * @param id 作品ID
     * @return 结果
     */
    @Override
    public int deleteUmsUserById(String id)
    {
        return umsUserMapper.deleteUmsUserById(id);
    }

    /**
     * 批量删作品信息
     *
     * @param ids 需要删除作品ID
     * @return 结果
     */
    @Override
    public int deleteUmsUserByIds(String[] ids)
    {
//        for (int id : ids)
//        {
//            UmsUser user = selectPostById(id);
//            if (countUserPostById(id) > 0)
//            {
//                throw new ServiceException(String.format("%1$s已分配,不能删除", user.getPostName()));
//            }
//        }
        return umsUserMapper.deleteUmsUserByIds(ids);
    }
//
    /**
     * 新增保作品信息
     *
     * @param user 作品信息
     * @return 结果
     */
    @Override
    public int insertUmsUser(UmsUser user)
    {
        return umsUserMapper.insertUmsUser(user);
    }

    /**
     * 修改保作品信息
     *
     * @param user 作品信息
     * @return 结果
     */
    @Override
    public int updateUmsUser(UmsUser user)
    {
        return umsUserMapper.updateUmsUser(user);
    }
}
