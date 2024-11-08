package com.ruoyi.system.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.ruoyi.common.annotation.Excel;
import com.ruoyi.common.core.domain.BaseEntity;

/**
 * 纽约时报报道量对象 newyork_counts
 * 
 * @author childa
 * @date 2024-11-08
 */
public class NewyorkCounts extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 城市名 */
    @Excel(name = "城市名")
    private String cityname;

    /** 开始时间 */
    @Excel(name = "开始时间")
    private String starttime;

    /** 结束时间 */
    @Excel(name = "结束时间")
    private String endtime;

    /** 次数 */
    @Excel(name = "次数")
    private Long counts;

    public void setCityname(String cityname) 
    {
        this.cityname = cityname;
    }

    public String getCityname() 
    {
        return cityname;
    }
    public void setStarttime(String starttime) 
    {
        this.starttime = starttime;
    }

    public String getStarttime() 
    {
        return starttime;
    }
    public void setEndtime(String endtime) 
    {
        this.endtime = endtime;
    }

    public String getEndtime() 
    {
        return endtime;
    }
    public void setCounts(Long counts) 
    {
        this.counts = counts;
    }

    public Long getCounts() 
    {
        return counts;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
            .append("cityname", getCityname())
            .append("starttime", getStarttime())
            .append("endtime", getEndtime())
            .append("counts", getCounts())
            .toString();
    }
}
