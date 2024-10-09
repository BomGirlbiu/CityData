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
@TableName("cityimages")
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
}
