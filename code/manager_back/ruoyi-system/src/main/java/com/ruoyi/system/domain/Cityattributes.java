package com.ruoyi.system.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.ruoyi.common.annotation.Excel;
import com.ruoyi.common.core.domain.BaseEntity;

/**
 * 城市传播指数对象 cityattributes
 * 
 * @author zrt
 * @date 2024-11-08
 */
public class Cityattributes extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 城市编号 */
    @Excel(name = "城市编号")
    private Integer cityID;

    /** 城市名 */
    @Excel(name = "城市名")
    private String cityName;

    /** 搜索引擎影响力 */
    @Excel(name = "搜索引擎影响力")
    private Double searchin;

    /** 网络传播影响力 */
    @Excel(name = "网络传播影响力")
    private Double network;

    /** 媒体报道影响力 */
    @Excel(name = "媒体报道影响力")
    private Double mediatr;

    /** 国际访客影响力 */
    @Excel(name = "国际访客影响力")
    private Double tourism;

    /** 社交媒体影响力 */
    @Excel(name = "社交媒体影响力")
    private Double social;

    /** 综合城市传播指数 */
    @Excel(name = "综合城市传播指数")
    private Double totalrate;

    public void setCityID(Integer cityID) 
    {
        this.cityID = cityID;
    }

    public Integer getCityID() 
    {
        return cityID;
    }
    public void setCityName(String cityName) 
    {
        this.cityName = cityName;
    }

    public String getCityName() 
    {
        return cityName;
    }
    public void setSearchin(Double searchin) 
    {
        this.searchin = searchin;
    }

    public Double getSearchin() 
    {
        return searchin;
    }
    public void setNetwork(Double network) 
    {
        this.network = network;
    }

    public Double getNetwork() 
    {
        return network;
    }
    public void setMediatr(Double mediatr) 
    {
        this.mediatr = mediatr;
    }

    public Double getMediatr() 
    {
        return mediatr;
    }
    public void setTourism(Double tourism) 
    {
        this.tourism = tourism;
    }

    public Double getTourism() 
    {
        return tourism;
    }
    public void setSocial(Double social) 
    {
        this.social = social;
    }

    public Double getSocial() 
    {
        return social;
    }
    public void setTotalrate(Double totalrate) 
    {
        this.totalrate = totalrate;
    }

    public Double getTotalrate() 
    {
        return totalrate;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
            .append("cityID", getCityID())
            .append("cityName", getCityName())
            .append("searchin", getSearchin())
            .append("network", getNetwork())
            .append("mediatr", getMediatr())
            .append("tourism", getTourism())
            .append("social", getSocial())
            .append("totalrate", getTotalrate())
            .toString();
    }
}
