import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

public class ConsoleUI {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Hello :)\n" +
                "Enter the password length you want to generate:");
        int l = scan.nextInt();
        scan.nextLine();
        System.out.println(
                """
                        To generate password you can use this alphabets or a combination of them through the ",":
                        1 - latin lower case
                        2 - latin upper case
                        3 - numbers
                        4 - special symbols""");
        String combinationAlphabet = scan.nextLine();
        List<String> fileNames = FileUtils.fileNames(combinationAlphabet);
        List<Character> alphabet = new ArrayList<>();
        for (String s: fileNames){
            alphabet.addAll(Objects.requireNonNull(FileUtils.readAlphabet(s)));
        }
        String password = PasswordGenerator.password(l, alphabet);
        System.out.println("Password: " + password);

        List<Long> inputDuration = new ArrayList<>();
        for (int i = 0; i < l; i++){
            long start = System.currentTimeMillis();
            scan.nextLine();
            long end = System.currentTimeMillis();
            inputDuration.add(end - start);
        }

        DefaultCategoryDataset barDataset = new DefaultCategoryDataset();
        char[] passwordAsCharArr = password.toCharArray();
        for (int i = 0; i < l; i++){
            barDataset.setValue((Number) (inputDuration.get(i) / 1_000), "Time", passwordAsCharArr[i]);
        }

        JFreeChart chart = ChartFactory.createBarChart(
                "Passphrase entry speed", "Symbol", "Time, c", barDataset,
                PlotOrientation.VERTICAL, false, true, false);

        ChartFrame chartFrame = new ChartFrame("Vertical Bar Chart", chart);
        chartFrame.setVisible(true);
        chartFrame.setSize(560, 350);
    }



}
