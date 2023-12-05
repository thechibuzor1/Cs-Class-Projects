import java.util.concurrent.*;
import java.util.concurrent.locks.*;

public class Dining {

    public static void main(String[] args) {
        Account[] accounts = new Account[5];

        // Create 5 accounts
        for (int i = 0; i < 5; i++) {
            accounts[i] = new Account(i + 1);
        }

        ExecutorService executor = Executors.newCachedThreadPool();
        // Simulate transactions between accounts
        for (int i = 0; i < 5; i++) {
            int nextAccountIndex = (i + 1) % 5; // Circular ordering
            executor.execute(new Transactions(accounts[i], accounts[nextAccountIndex], i + 1));
        }

        executor.shutdown();
        while (!executor.isTerminated()) {
        }

    }

    public static class Transactions implements Runnable {

        private int transactionId;
        private Account sender;
        private Account receiver;

        Transactions(Account A, Account B, int id) {
            transactionId = id;
            sender = A;
            receiver = B;
        }

        public void run() {

            try {
                /* all picked left */
                /*
                 * if (sender.lock.tryLock()) {
                 * System.out.println("Transaction " + transactionId +
                 * " acquired lock to account " + sender.id);
                 * if (receiver.lock.tryLock()) {
                 * System.out.println("Transaction " + transactionId +
                 * " acquired lock to account " + receiver.id);
                 * try {
                 * System.out.println(
                 * "Account " + sender.id + " performing transaction with Account " +
                 * receiver.id);
                 * // Simulating a transaction
                 * Thread.sleep(1000);
                 * System.out.println("Transaction between Account " + sender.id +
                 * " and Account "
                 * + receiver.id + " completed.");
                 * 
                 * } finally {
                 * receiver.lock.unlock();
                 * System.out.println(
                 * "Transaction " + transactionId + " released lock to account " + receiver.id);
                 * }
                 * } else {
                 * System.out.println(
                 * "Transaction " + transactionId + " failed to acquire lock to account " +
                 * receiver.id);
                 * }
                 * } else {
                 * System.out.println(
                 * "Transaction " + transactionId + " failed to acquire lock to account " +
                 * sender.id);
                 * }
                 */

                /* starvation: only two transactions can happen. the remaining 3 starve */

                if (sender.lock.tryLock() && receiver.lock.tryLock()) {
                    System.out.println("Transaction " + transactionId + " acquired locks to account " + sender.id
                            + " and account" + receiver.id);

                    try {
                        System.out.println(
                                "Account " + sender.id + " performing transaction with Account " + receiver.id);
                        // Simulating a transaction
                        Thread.sleep(1000);
                        System.out.println("Transaction between Account " + sender.id + " and Account "
                                + receiver.id + " completed.");
                        break;
                    } finally {
                        receiver.lock.unlock();
                        System.out.println(
                                "Transaction " + transactionId + " released lock to account " + receiver.id);
                    }

                } else {
                    System.out.println(
                            "Transaction " + transactionId + " failed to acquire lock to account " + sender.id);
                }
            } catch (InterruptedException e) {
                /* Thread.currentThread().interrupt(); */
            } finally {
                sender.lock.unlock();
                System.out.println("Transaction " + transactionId + " released lock to account " + sender.id);
            }

        }
    }

    public static class Account {

        private int balance = 2000;
        private Lock lock = new ReentrantLock();
        private int id;

        Account(int n) {
            id = n;
        }

        public int getId() {
            return id;
        }

        public int getBalance() {
            return balance;
        }

        public void debit(int amount) {

            try {
                if (balance > amount) {
                    balance = balance - amount;
                    System.out.println("Transaction successful!");
                    Thread.sleep(5);

                } else {
                    System.out.println("Insufficient Balance");
                }

            } catch (InterruptedException ex) {

            }
        }

        public void credit(int amount) {

            try {
                {
                    balance = balance + amount;
                    System.out.println("Transaction successful!");
                    Thread.sleep(5);

                }

            } catch (InterruptedException ex) {

            }
        }
    }

}
