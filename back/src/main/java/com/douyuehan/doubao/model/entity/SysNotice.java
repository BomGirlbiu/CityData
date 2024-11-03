package com.douyuehan.doubao.model.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.*;
import lombok.experimental.Accessors;

import java.io.Serializable;

/**
 * 通知公告表 sys_notice
 * 
 * @author ruoyi
 */

@Data
@Builder
@Accessors(chain = true)
@TableName("sys_notice")
@NoArgsConstructor
@AllArgsConstructor
public class SysNotice implements Serializable
{
    private static final long serialVersionUID = 1L;

    /** 公告ID */
    private Long noticeId;

    /** 公告标题 */
    private String noticeTitle;

    /** 公告类型（1通知 2公告） */
    private String noticeType;

    /** 公告内容 */
    private String noticeContent;

//    /** 公告状态（0正常 1关闭） */
//    private String status;

    /**
     * 1：展示中，0：过期
     */
    @Getter
    @Builder.Default
    @TableField("`status`")
    private String status ="0";
}
