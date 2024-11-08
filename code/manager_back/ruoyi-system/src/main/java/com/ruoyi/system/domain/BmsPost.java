package com.ruoyi.system.domain;

import com.ruoyi.common.annotation.Excel;
import com.ruoyi.common.annotation.Excel.ColumnType;
import com.ruoyi.common.core.domain.BaseEntity;
import com.ruoyi.common.utils.uuid.UUID;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import org.springframework.data.annotation.Id;

/**
 * 作品展示栏 bms_post
 * 
 * @author ruoyi
 */
public class BmsPost extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 作品编号 */
    @Excel(name = "序列", cellType = ColumnType.NUMERIC)
    @Id
    private int postId;

    /** 作品编号 */
    @Excel(name = "作品编号")
    private String id;

    /** 作品标题 */
    @Excel(name = "作品标题")
    private String title;

    /** 作品内容 */
    @Excel(name = "作品内容")
    private String content;


    /** 作者编号 */
    @Excel(name = "作者编号")
    private String userId;

    /** 评论数 */
    @Excel(name = "评论数")
    private Integer comments = 0;

    /** 收藏数 */
    @Excel(name = "收藏数")
    private Integer collects = 0;
    /** 浏览数 */
    @Excel(name = "浏览数")
    private Integer view = 0;

    /** 修改人姓名 */
    @Excel(name = "修改人姓名")
    private String updateBy;

    /** 置顶 */
    private Boolean top = false;

    /** 加精 */
    private Boolean essence = false;

    /** 是否分栏目 */
    private Integer sectionId = 0;

    public int getPostId() {
        return postId;
    }

    public void setPostId(int postId) {
        this.postId = postId;
    }

    public Integer getSectionId() {
        return sectionId;
    }

    public void setSectionId(Integer sectionId) {
        this.sectionId = sectionId;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = UUID.randomUUID().toString();
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public Integer getComments() {
        return comments;
    }

    public void setComments(Integer comments) {
        this.comments = comments;
    }

    public Integer getCollects() {
        return collects;
    }

    public void setCollects(Integer collects) {
        this.collects = collects;
    }

    public Integer getView() {
        return view;
    }

    public void setView(Integer view) {
        this.view = view;
    }
    @Override
    public String getUpdateBy() {
        return updateBy;
    }
    @Override
    public void setUpdateBy(String updateBy) {
        this.updateBy = updateBy;
    }

    public Boolean getTop() {
        return top;
    }

    public void setTop(Boolean top) {
        this.top = top;
    }

    public Boolean getEssence() {
        return essence;
    }

    public void setEssence(Boolean essence) {
        this.essence = essence;
    }
    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
                .append("postId", getPostId())
                .append("id", getId())
                .append("title", getTitle())
                .append("content", getContent())
                .append("userId", getUserId())
                .append("comments", getComments())
                .append("collects", getCollects())
                .append("view", getView())
                .append("updateBy", getUpdateBy())
                .append("top", getTop())
                .append("essence", getEssence())
                .append("createTime", getCreateTime())
                .append("updateTime", getUpdateTime())
                .toString();
    }

}
