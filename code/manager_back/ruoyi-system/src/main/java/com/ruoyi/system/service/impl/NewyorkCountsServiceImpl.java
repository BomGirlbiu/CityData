package com.ruoyi.system.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ruoyi.system.mapper.NewyorkCountsMapper;
import com.ruoyi.system.domain.NewyorkCounts;
import com.ruoyi.system.service.INewyorkCountsService;

/**
 * 纽约时报报道量Service业务层处理
 * 
 * @author childa
 * @date 2024-11-08
 */
@Service
public class NewyorkCountsServiceImpl implements INewyorkCountsService 
{
    @Autowired
    private NewyorkCountsMapper newyorkCountsMapper;

    /**
     * 查询纽约时报报道量
     * 
     * @param cityname 纽约时报报道量主键
     * @return 纽约时报报道量
     */
    @Override
    public NewyorkCounts selectNewyorkCountsByCityname(String cityname)
    {
        return newyorkCountsMapper.selectNewyorkCountsByCityname(cityname);
    }

    /**
     * 查询纽约时报报道量列表
     * 
     * @param newyorkCounts 纽约时报报道量
     * @return 纽约时报报道量
     */
    @Override
    public List<NewyorkCounts> selectNewyorkCountsList(NewyorkCounts newyorkCounts)
    {
        return newyorkCountsMapper.selectNewyorkCountsList(newyorkCounts);
    }

    /**
     * 新增纽约时报报道量
     * 
     * @param newyorkCounts 纽约时报报道量
     * @return 结果
     */
    @Override
    public int insertNewyorkCounts(NewyorkCounts newyorkCounts)
    {
        return newyorkCountsMapper.insertNewyorkCounts(newyorkCounts);
    }

    /**
     * 修改纽约时报报道量
     * 
     * @param newyorkCounts 纽约时报报道量
     * @return 结果
     */
    @Override
    public int updateNewyorkCounts(NewyorkCounts newyorkCounts)
    {
        return newyorkCountsMapper.updateNewyorkCounts(newyorkCounts);
    }

    /**
     * 批量删除纽约时报报道量
     * 
     * @param citynames 需要删除的纽约时报报道量主键
     * @return 结果
     */
    @Override
    public int deleteNewyorkCountsByCitynames(String[] citynames)
    {
        return newyorkCountsMapper.deleteNewyorkCountsByCitynames(citynames);
    }

    /**
     * 删除纽约时报报道量信息
     * 
     * @param cityname 纽约时报报道量主键
     * @return 结果
     */
    @Override
    public int deleteNewyorkCountsByCityname(String cityname)
    {
        return newyorkCountsMapper.deleteNewyorkCountsByCityname(cityname);
    }
}
