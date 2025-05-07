package Command;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        FileService fs = new FileService();

        Command[] commands = {
                new AddCommand(),
                new OpenCommand(),
                new PrintCommand(),
                new ExitCommand(),

                () -> System.out.println("Lambda Command"),    // 람다식
                Main::exit,  // 람다식  () -> Main.exit()
                fs::open,   // () -> fs.open()
                fs::print,  // () -> fs.print()
        };

        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("1: Add, 2: Open, 3: Print, 4: Exit 5: Lambda-Print 6: Lambda-Exit 7: FileService-open 8: FileService-print");
            System.out.print("선택: ");
            int sel = scanner.nextInt();

            commands[sel - 1].execute();
        }
    }

    public static void exit() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("종료할까요?(Y/n) ");
        String answer = scanner.nextLine();

        scanner.close();
        if (answer.isEmpty() || answer.equalsIgnoreCase("Y")) {
            System.exit(0);
        }
    }
}
