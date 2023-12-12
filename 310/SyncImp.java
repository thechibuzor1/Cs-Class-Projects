import java.util.concurrent.*;
import java.util.concurrent.locks.*;

public class SyncImp {

    private static Account account = new Account();

    public static void main(String[] args) {
        ExecutorService executor = Executors.newCachedThreadPool();
        for (int i = 0; i < 100; i++) {
            executor.execute(new AddAPennyTask());
        }
        executor.shutdown();

        while (!executor.isTerminated()) {

        }
        System.out.println("What is balance? " + account.getBalance());

    }

    private static class AddAPennyTask implements Runnable {

        public void run() {
            account.deposit(1);
        }
    }

    private static class Account {
        /* create a lock */
        private static Lock lock = new ReentrantLock();
        private int balance = 0;

        public int getBalance() {
            return balance;
        }

        public /* synchronized */ void deposit(int amount) {
            lock.lock();
            // before synchronize
            /*
             * int newBalance = amount + balance;
             * try {
             * Thread.sleep(5);
             * } catch (InterruptedException ex) {
             * 
             * }
             * balance = newBalance;
             */

            try {
                int newBalance = amount + balance;
                Thread.sleep(5);
                balance = newBalance;
            } catch (InterruptedException ex) {

            } finally {
                lock.unlock();
            }

        }

    }

}
