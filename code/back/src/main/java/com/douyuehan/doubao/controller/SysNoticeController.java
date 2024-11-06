package com.douyuehan.doubao.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.douyuehan.doubao.common.api.ApiResult;
import com.douyuehan.doubao.model.entity.SysNotice;
import com.douyuehan.doubao.service.IBmsSysNoticeService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.util.List;

@RestController
@RequestMapping("/billboard")
public class SysNoticeController extends BaseController {

    @Resource
    private IBmsSysNoticeService ibmsSysNoticeService;

    @GetMapping("/show")
    public ApiResult<SysNotice> getNotices(){

        System.out.println(">>>");
        List<SysNotice> list = ibmsSysNoticeService.list(new
                LambdaQueryWrapper<SysNotice>().eq(SysNotice::getStatus,"0"));
        if(list.size()<=0){
            SysNotice emp = new SysNotice();
            emp.setNoticeTitle("暂无公告");
            list.add(emp);
        }
        return ApiResult.success(list.get(list.size()- 1));
    }
}
