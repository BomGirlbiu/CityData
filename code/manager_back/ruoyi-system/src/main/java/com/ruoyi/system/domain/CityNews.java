package com.ruoyi.system.domain;

import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import com.ruoyi.common.annotation.Excel;
import com.ruoyi.common.core.domain.BaseEntity;

/**
 * 新闻列表对象 city_news
 * 
 * @author zrt
 * @date 2024-11-07
 */
public class CityNews extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 城市 */
    @Excel(name = "城市")
    private String city;

    /** 省份 */
    @Excel(name = "省份")
    private String province;

    /** 标题 */
    private String title;

    /** 链接 */
    private String newsURL;

    /** 主键 */
    private Long newsID;

    public void setCity(String city) 
    {
        this.city = city;
    }

    public String getCity() 
    {
        return city;
    }
    public void setProvince(String province) 
    {
        this.province = province;
    }

    public String getProvince() 
    {
        return province;
    }
    public void setTitle(String title) 
    {
        this.title = title;
    }

    public String getTitle() 
    {
        return title;
    }
    public void setNewsURL(String newsURL) 
    {
        this.newsURL = newsURL;
    }

    public String getNewsURL() 
    {
        return newsURL;
    }
    public void setNewsID(Long newsID) 
    {
        this.newsID = newsID;
    }

    public Long getNewsID() 
    {
        return newsID;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
            .append("city", getCity())
            .append("province", getProvince())
            .append("title", getTitle())
            .append("newsURL", getNewsURL())
            .append("newsID", getNewsID())
            .toString();
    }
}
