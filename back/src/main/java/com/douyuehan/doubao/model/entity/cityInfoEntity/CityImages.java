package com.douyuehan.doubao.model.entity.cityInfoEntity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.Accessors;

@Data
@Builder
@Accessors(chain = true)
@TableName("city_images")
@NoArgsConstructor
@AllArgsConstructor
public class CityImages {
    private static final long serialVersionUID = 1L;
    /**
     * 主键
     */
    @TableId(type = IdType.AUTO)
    private Integer imagesID;

    /**
     * 图片归属省份
     */
    @TableField("province")
    private String province;

    /**
     * 图片归属城市
     */
    @TableField("city")
    private String city;

    /**
     * 图片来源网址
     */
    @TableField("imagesURL")
    private String imagesURL;

    public Integer getImagesID() {
        return imagesID;
    }

    public void setImagesID(Integer imagesID) {
        this.imagesID = imagesID;
    }

    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getImagesURL() {
        return imagesURL;
    }

    public void setImagesURL(String imagesURL) {
        this.imagesURL = imagesURL;
    }
}
