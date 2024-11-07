package com.ruoyi.web.controller.system;

import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

public class TaskManager {
    private static final ConcurrentHashMap<Long, TaskStatus> tasks = new ConcurrentHashMap<>();
    private static final AtomicLong taskIdGenerator = new AtomicLong(0);

    public static long createTask() {
        long taskId = taskIdGenerator.incrementAndGet();
        tasks.put(taskId, new TaskStatus(taskId));
        return taskId;
    }

    public static TaskStatus getTaskStatus(long taskId) {
        return tasks.getOrDefault(taskId, null);
    }

    public static void updateTaskStatus(long taskId, String status, String result) {
        TaskStatus taskStatus = tasks.get(taskId);
        if (taskStatus != null) {
            taskStatus.setStatus(status);
            taskStatus.setResult(result);
        }
    }

    public static void removeTask(long taskId) {
        tasks.remove(taskId);
    }

    public static class TaskStatus {
        private long taskId;
        private String status;
        private String result;

        public TaskStatus(long taskId) {
            this.taskId = taskId;
            this.status = "PENDING";
            this.result = "";
        }

        public long getTaskId() {
            return taskId;
        }

        public String getStatus() {
            return status;
        }

        public void setStatus(String status) {
            this.status = status;
        }

        public String getResult() {
            return result;
        }

        public void setResult(String result) {
            this.result = result;
        }
    }
}
