package com.ruoyi.system.service;

import java.util.List;
import com.ruoyi.system.domain.NewyorkCounts;

/**
 * 纽约时报报道量Service接口
 * 
 * @author childa
 * @date 2024-11-08
 */
public interface INewyorkCountsService 
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
     * 批量删除纽约时报报道量
     * 
     * @param citynames 需要删除的纽约时报报道量主键集合
     * @return 结果
     */
    public int deleteNewyorkCountsByCitynames(String[] citynames);

    /**
     * 删除纽约时报报道量信息
     * 
     * @param cityname 纽约时报报道量主键
     * @return 结果
     */
    public int deleteNewyorkCountsByCityname(String cityname);
}
