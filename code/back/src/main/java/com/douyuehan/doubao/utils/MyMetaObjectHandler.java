package com.douyuehan.doubao.utils;

import com.baomidou.mybatisplus.core.handlers.MetaObjectHandler;
import com.baomidou.mybatisplus.core.toolkit.IdWorker;
import com.douyuehan.doubao.utils.GenerateUUID;
import org.apache.ibatis.reflection.MetaObject;
import org.springframework.stereotype.Component;

import java.lang.reflect.Field;

@Component
public class MyMetaObjectHandler implements MetaObjectHandler {
    @Override
    public void insertFill(MetaObject metaObject) {
        Object originalObject = metaObject.getOriginalObject();
        try{
            Class clazz = originalObject.getClass();
            for (Field declaredField : clazz.getDeclaredFields()) {
                declaredField.setAccessible(true);
                if (declaredField.isAnnotationPresent(GenerateUUID.class) && declaredField.get(originalObject) == null){
                    this.setFieldValByName(declaredField.getName(), IdWorker.get32UUID(),metaObject);
                }
            }
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void updateFill(MetaObject metaObject) {
    }
}
