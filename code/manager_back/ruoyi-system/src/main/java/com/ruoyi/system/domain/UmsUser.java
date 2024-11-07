package com.ruoyi.system.domain;

import com.ruoyi.common.annotation.Excel;
import com.ruoyi.common.annotation.Excel.ColumnType;
import com.ruoyi.common.annotation.Excel.Type;
import com.ruoyi.common.core.domain.BaseEntity;
import com.ruoyi.common.xss.Xss;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;
import org.springframework.data.annotation.Id;

import javax.validation.constraints.Email;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;

/**
 * 用户对象 ums_user
 *
 * @author ruoyi
 */
public class UmsUser extends BaseEntity
{
    private static final long serialVersionUID = 1L;

    /** 用户ID */
    @Id
    @Excel(name = "用户序号", type = Type.EXPORT, cellType = ColumnType.NUMERIC, prompt = "用户编号")
    private String id;

    /** 用户账号 */
    @Excel(name = "登录名称")
    private String username;

    /** 用户昵称 */
    @Excel(name = "用户名称")
    private String alias;

    /** 密码 */
    private String password;

    /** 用户头像 */
    private String avatar = "https://s3.ax1x.com/2020/12/01/DfHNo4.jpg";

    /** 用户邮箱 */
    @Excel(name = "用户邮箱")
    private String email;

    /** 手机号码 */
    @Excel(name = "手机号码", cellType = ColumnType.TEXT)
    private String mobile;

    /** 用户职业 */
    @Excel(name = "用户职业", readConverterExp = "0=男,1=女,2=未知")
    private String bio;

    /** 用户积分 */
    @Excel(name = "用户积分")
    private Integer score = 0;

    /** token */
    @Excel(name = "token")
    private String token;

    /** 是否激活 */
    @Excel(name = "active")
    private Boolean active = true;

    /** 帐号状态（1:使用，0:已停用） */
    @Excel(name = "帐号状态", readConverterExp = "1:使用，0:已停用")
    private Boolean status = true;


    /** 角色ID */
    @Excel(name = "role_id")
    private Integer roleId;


    public UmsUser()
    {

    }
    @Xss(message = "用户昵称不能包含脚本字符")
    @Size(min = 0, max = 30, message = "用户昵称长度不能超过30个字符")
    public String getAlias()
    {
        return alias;
    }

    public void setAlias(String alias)
    {
        this.alias = alias;
    }

    @Xss(message = "用户账号不能包含脚本字符")
    @NotBlank(message = "用户账号不能为空")
    @Size(min = 0, max = 30, message = "用户账号长度不能超过30个字符")
    public String getUsername()
    {
        return username;
    }

    public void setUsername(String username)
    {
        this.username = username;
    }

    @Email(message = "邮箱格式不正确")
    @Size(min = 0, max = 50, message = "邮箱长度不能超过50个字符")
    public String getEmail()
    {
        return email;
    }

    public void setEmail(String email)
    {
        this.email = email;
    }

    @Size(min = 0, max = 11, message = "手机号码长度不能超过11个字符")
    public String getMobile()
    {
        return mobile;
    }

    public void setMobile(String mobile)
    {
        this.mobile = mobile;
    }


    public String getAvatar()
    {
        return avatar;
    }

    public void setAvatar(String avatar)
    {
        this.avatar = avatar;
    }

    public String getPassword()
    {
        return password;
    }

    public void setPassword(String password)
    {
        this.password = password;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getBio() {
        return bio;
    }

    public void setBio(String bio) {
        this.bio = bio;
    }

    public Integer getScore() {
        return score;
    }

    public void setScore(Integer score) {
        this.score = score;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public Boolean getActive() {
        return active;
    }

    public void setActive(Boolean active) {
        this.active = active;
    }

    public Boolean getStatus() {
        return status;
    }

    public void setStatus(Boolean status) {
        this.status = status;
    }

    public Integer getRoleId() {
        return roleId;
    }

    public void setRoleId(Integer roleId) {
        this.roleId = roleId;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this,ToStringStyle.MULTI_LINE_STYLE)
                .append("id", getId())
                .append("username", getUsername())
                .append("alias", getAlias())
                .append("password", getPassword())
                .append("avatar", getAvatar())
                .append("email", getEmail())
                .append("mobile", getMobile())
                .append("score", getScore())
                .append("token", getToken())
                .append("bio", getBio())
                .append("active", getActive())
                .append("status", getStatus())
                .append("roleId", getRoleId())
                .append("status", getStatus())
                .append("createTime", getCreateTime())
                .append("updateTime", getUpdateTime())
                .toString();
    }
}
