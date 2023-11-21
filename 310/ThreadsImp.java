import java.util.concurrent.*;

class Loar extends Thread {
    public void run() {
        for (int i = 30; i >= 0; i--) {
            System.out.println(i + "A");
        }
    }
}

class Loader implements Runnable {
    public void run() {
        for (int i = 30; i >= 0; i--) {
            System.out.println(i + "B");
        }
    }
}

class PrintChar extends Thread {
    private String stringToPrint; // The character to print
    private int n; // The number of times to repeat

    public PrintChar(String character, int number) {
        stringToPrint = character;
        n = number;

    }

    public void run() {
        for (int i = 0; i <= n; i++) {
            System.out.println(i + " " + stringToPrint);
        }
    }
}

public class ThreadsImp {

    public static void main(String[] args) {
        /*
         * Thread obj = new Thread(new Loader());
         * Loar obj2 = new Loar();
         */

        /*
         * obj2.start();
         * obj.start();
         */

        ExecutorService executor = Executors.newFixedThreadPool(4);
        executor.execute(new PrintChar("THREAD1", 100));
        executor.execute(new PrintChar("THREAD2", 100));
        executor.execute(new PrintChar("THREAD3", 100));
        executor.execute(new PrintChar("THREAD4", 100));

        executor.shutdown();
    }
}
