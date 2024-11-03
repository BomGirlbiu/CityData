package com.douyuehan.doubao.utils;

import java.lang.annotation.*;

@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target({ ElementType.FIELD, ElementType.ANNOTATION_TYPE})
public @interface GenerateUUID {
    String value() default "";
}
