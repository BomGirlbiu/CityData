package com.douyuehan.doubao.model.entity.BigscreenEntity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;

@TableName("cityattributes")
public class CityAttributes {
    @TableId(type = IdType.AUTO)//id为自增主键
    @TableField(value = "cityid")
    private int cityid;//城市编号
    @TableField(value = "cityname")
    private String cityName;//城市名称
    private float searchin;//搜索引擎影响力
    private float network;//网络传播影响力
    private float mediatr;//媒体报道影响力
    private float tourism;//国际访客影响力
    private float social;//社交媒体影响力
    private float totalrate;//传世传播指数
    public CityAttributes() {
    }

    @Override
    public String toString() {
        return "[" +
                searchin + "," +
                network + "," +
                mediatr + "," +
                tourism + "," +
                social+
                "]";
    }

    public CityAttributes(int cityid, String cityName, float totalrate, float network, float mediatr, float social, float tourism, float searchin) {
        this.cityid = cityid;
        this.cityName = cityName;
        this.totalrate = totalrate;
        this.network = network;
        this.mediatr = mediatr;
        this.social = social;
        this.tourism = tourism;
        this.searchin = searchin;
    }

    public int getCityid() {
        return cityid;
    }

    public void setCityid(int cityid) {
        this.cityid = cityid;
    }

    public float getTotalrate() {
        return totalrate;
    }

    public void setTotalrate(float totalrate) {
        this.totalrate = totalrate;
    }

    public float getNetwork() {
        return network;
    }

    public void setNetwork(float network) {
        this.network = network;
    }

    public float getMediatr() {
        return mediatr;
    }

    public void setMediatr(float mediatr) {
        this.mediatr = mediatr;
    }

    public float getSocial() {
        return social;
    }

    public void setSocial(float social) {
        this.social = social;
    }

    public float getTourism() {
        return tourism;
    }

    public void setTourism(float tourism) {
        this.tourism = tourism;
    }

    public float getSearchin() {
        return searchin;
    }

    public void setSearchin(float searchin) {
        this.searchin = searchin;
    }


    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }


}
