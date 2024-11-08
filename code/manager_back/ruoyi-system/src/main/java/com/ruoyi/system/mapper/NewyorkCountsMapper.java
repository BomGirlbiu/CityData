package com.ruoyi.system.mapper;

import java.util.List;
import com.ruoyi.system.domain.NewyorkCounts;

/**
 * 纽约时报报道量Mapper接口
 * 
 * @author childa
 * @date 2024-11-08
 */
public interface NewyorkCountsMapper 
{
    /**
     * 查询纽约时报报道量
     * 
     * @param cityname 纽约时报报道量主键
     * @return 纽约时报报道量
     */
    public NewyorkCounts selectNewyorkCountsByCityname(String cityname);

    /**
     * 查询纽约时报报道量列表
     * 
     * @param newyorkCounts 纽约时报报道量
     * @return 纽约时报报道量集合
     */
    public List<NewyorkCounts> selectNewyorkCountsList(NewyorkCounts newyorkCounts);

    /**
     * 新增纽约时报报道量
     * 
     * @param newyorkCounts 纽约时报报道量
     * @return 结果
     */
    public int insertNewyorkCounts(NewyorkCounts newyorkCounts);

    /**
     * 修改纽约时报报道量
     * 
     * @param newyorkCounts 纽约时报报道量
     * @return 结果
     */
    public int updateNewyorkCounts(NewyorkCounts newyorkCounts);

    /**
     * 删除纽约时报报道量
     * 
     * @param cityname 纽约时报报道量主键
     * @return 结果
     */
    public int deleteNewyorkCountsByCityname(String cityname);

    /**
     * 批量删除纽约时报报道量
     * 
     * @param citynames 需要删除的数据主键集合
     * @return 结果
     */
    public int deleteNewyorkCountsByCitynames(String[] citynames);
}
