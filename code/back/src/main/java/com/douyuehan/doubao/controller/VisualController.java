package com.douyuehan.doubao.controller;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import com.douyuehan.doubao.model.entity.BigscreenEntity.*;
import com.douyuehan.doubao.mapper.BigscreenMapper.*;
import com.douyuehan.doubao.model.entity.BigscreenEntity.googlesearch;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.List;

@RestController
@CrossOrigin
public class VisualController {
    @Autowired
    private SearchMapper searchMapper;
    @Autowired
    private CityAttributesMapper cityAttributesMapper;
    @Autowired
    private FansMapper fansMapper;
    @Autowired
    private EmotionMapper emotionMapper;
    @Autowired
    private TourMapper tourMapper;
    @Autowired
    private  CloudMapper cloudMapper;
    @Autowired
    private NewYorkMapper newYorkMapper;

    @PostMapping("/index/visual/search/google")
    public List<googlesearch> findgooglebyname(String cityname) {
        List<googlesearch> list = searchMapper.findgooglebyname(cityname);
        System.out.println(list);
        return list;
    }

    @PostMapping("/index/visual/social/fans")
    public List<Fans> findfansbyname(String cityname) {
        List<Fans> list = fansMapper.findfansbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }
    @PostMapping("/index/visual/social/emotion")
    public List<Emotion> findemotionbyname(String cityname) {
        List<Emotion> list = emotionMapper.findbilibili(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }
    @PostMapping("/index/visual/social/youtube")
    public List<Emotion> findyoutube(String cityname) {
        List<Emotion> list = emotionMapper.findyoutube(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }

    @PostMapping("/index/visual/nation/tourism")
    public List<Tourism> findtourbyname(String cityname) {
        List<Tourism> list = tourMapper.findtourbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }

    @PostMapping("/index/visual/conclusion")
    public List<CityAttributes> findallbyname(String cityname) {
        List<CityAttributes> list = cityAttributesMapper.findallbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }
    @PostMapping("/index/visual/media/newyork")
    public List<NewYork> findnewyorkcountsbyname(String cityname) {
        List<NewYork> list = newYorkMapper.findcountsbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }

    @PostMapping("/index/visual/network/cloud")
    public List<WordCloud> findcloudbyname(String cityname) {
        List<WordCloud> list = cloudMapper.findwordbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }

    @GetMapping("/index/visual")
    public List<CityAttributes> findcities() {
        List<CityAttributes> list = cityAttributesMapper.selectList(null);
        System.out.println(list);
        return list;
    }
    @PostMapping("/index/visual/search/googlefuture")
    public List<Forecast.ForecastResult> getForecast(String cityname) throws IOException, InterruptedException {
        return Forecast.getForecast(cityname);
    }
}

class Forecast {

    public static class ForecastResult {
        private String cityName;
        private double counts;
        private String week;

        public ForecastResult(String cityName, double counts, String week) {
            this.cityName = cityName;
            this.counts = counts;
            this.week = week;
        }

        public String getCityName() {
            return cityName;
        }

        public double getCounts() {
            return counts;
        }

        public String getWeek() {
            return week;
        }

        @Override
        public String toString() {
            return "ForecastResult{" +
                    "cityName='" + cityName + '\'' +
                    ", counts=" + counts +
                    ", week='" + week + '\'' +
                    '}';
        }
    }

    public static List<ForecastResult> getForecast(String cityName) throws IOException, InterruptedException {
        // 执行Python脚本
        System.out.println(cityName);
        ProcessBuilder processBuilder = new ProcessBuilder("python", "D:\\临时\\code\\pyscripts\\Gtrends_forecast\\forecast.py","google", cityName);
        processBuilder.redirectErrorStream(true);
        Process process = processBuilder.start();
//        process.waitFor();

        BufferedReader stdoutReader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        BufferedReader stderrReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
         StringBuilder output = new StringBuilder();
        StringBuilder errorOutput = new StringBuilder();

        String line_;
         while ((line_ = stdoutReader.readLine()) != null) {
         System.out.println(line_);
         output.append(line_).append("\n");
         }
         while ((line_ = stderrReader.readLine()) != null) {
         System.out.println(line_);
         errorOutput.append(line_).append("\n");
         }

         int exitCode = process.waitFor();
          stdoutReader.close();
         stderrReader.close();


        // 读取CSV文件
        String csvFilePath = "D:\\临时\\code\\pyscripts\\Gtrends_forecast\\temp/forecast_results_" + cityName + ".csv";
        File csvFile = new File(csvFilePath);
        if (!csvFile.exists()) {
            throw new IOException("CSV file not found: " + csvFilePath);
        }

        List<ForecastResult> results = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            String line;
            boolean isFirstLine = true;
            while ((line = br.readLine()) != null) {
                if (isFirstLine) {
                    isFirstLine = false;
                    continue; // 跳过标题行
                }
                String[] values = line.split(",");
                String week = values[0];
                double counts = Double.parseDouble(values[1]);
                results.add(new ForecastResult(cityName, counts, week));
            }
        }

        return results;
    }
}