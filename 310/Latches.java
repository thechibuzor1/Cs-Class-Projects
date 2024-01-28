import java.util.concurrent.Semaphore;

public class Latches {
    public static void main(String[] args) {
        Semaphore semaphore = new Semaphore(1); // Initializing with a count of 3

        Runnable task = () -> {
            try {
                semaphore.acquire(); // Acquire access to the shared resource
                System.out.println("Hekoooooooo");
                // Access the shared resource
                semaphore.release(); // Release access to the shared resource
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        };

        // Creating threads and starting operations
        new Thread(task).start();
        new Thread(task).start();
        new Thread(task).start();
    }
}
