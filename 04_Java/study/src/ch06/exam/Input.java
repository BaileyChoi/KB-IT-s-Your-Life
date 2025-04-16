package ch06.exam;

import java.util.Scanner;

public class Input {

    static String read(String title) {
        System.out.print(title + ": ");

        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();

        return str;
    }

    static String read(String title, String defaultValue) {
        System.out.print(title + "(" +defaultValue + "): ");

        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();

        if (str.equals("")) {
            return defaultValue;
        } else {
            return str;
        }
    }

    static int readInt(String title) {
        System.out.print(title + ": ");

        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();

        return Integer.parseInt(str);
    }

    static boolean confirm(String title, boolean defaultValue) {
        System.out.print(title);

        if (defaultValue) {
            System.out.print(" (Y/n): ");
        } else if (!defaultValue) {
            System.out.println(" (y/N): ");
        }

        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();

        if (str.equals("Y")) {
            return true;
        } else if (str.equals("n")) {
            return false;
        }

        return defaultValue;
    }

    static boolean confirm(String title) {
        return confirm(title, true);
    }


}
