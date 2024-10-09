package com.douyuehan.doubao.model.entity.cityInfoEntity;


import com.baomidou.mybatisplus.annotation.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.experimental.Accessors;


/**
 * 城市信息·新闻实体类
 */

@Data
@Builder
@Accessors(chain = true)
@TableName("citynews")
@NoArgsConstructor
@AllArgsConstructor
public class CityNews {
    private static final long serialVersionUID = 1L;
    /**
     * 主键
     */
    @TableId(type = IdType.AUTO)
    private Integer newsID;

    /**
     * 新闻归属省份
     */
    @TableField("province")
    private String province;

    /**
     * 新闻归属城市
     */
    @TableField("city")
    private String city;

    /**
     * 新闻标题
     */
    @TableField("title")
    private String title;

    /**
     * 新闻来源网址
     */
    @TableField("imagesURL")
    private String imagesURL;
}
