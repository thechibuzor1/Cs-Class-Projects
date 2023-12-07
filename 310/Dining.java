import java.util.concurrent.*;
import java.util.concurrent.locks.*;

public class Dining {

    public static void main(String[] args) {
        Account[] accounts = new Account[5];

        // Create 5 accounts
        for (int i = 0; i < 5; i++) {
            accounts[i] = new Account(i + 1);
        }

        // Create a custom ThreadFactory to set thread priorities

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
        private int transactionCount = 0;

        Transactions(Account A, Account B, int id) {
            transactionId = id;
            sender = A;
            receiver = B;
        }

        public boolean getLocks() {
            return (sender.lock.tryLock() && receiver.lock.tryLock());
        }

        public boolean getLeftLock() {
            return (sender.lock.tryLock());
        }

        public boolean getRightLock() {
            return (receiver.lock.tryLock());
        }

        public void run() {
            try {
                while (true) {

                    /* All picked left waiting for the other to release the right: lifelock */

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

                    /*
                     * starvation: one or more transactions keep failing to acquire the lock and run
                     * to completion.
                     */

                    /*
                     * if (transactionCount == 0) {
                     * if (getLocks()) {
                     * 
                     * System.out.println("Transaction " + transactionId +
                     * " acquired locks to account " + sender.id
                     * + " and account" + receiver.id);
                     * 
                     * try {
                     * 
                     * System.out.println(
                     * "Account " + sender.id + " performing transaction with Account " +
                     * receiver.id);
                     * 
                     * // Simulating a transaction
                     * 
                     * System.out.println("Transaction " + transactionId + " completed.");
                     * transactionCount += 1;
                     * Thread.sleep(1000);
                     * } catch (Exception e) {
                     * Thread.currentThread().interrupt();
                     * }
                     * 
                     * finally {
                     * receiver.lock.unlock();
                     * sender.lock.unlock();
                     * Thread.sleep(1000);
                     * 
                     * System.out.println(
                     * "Transaction " + transactionId + " released lock to account " + sender.id
                     * + " and  account " + receiver.id);
                     * 
                     * }
                     * } else {
                     * System.out.println("Transaction " + transactionId +
                     * " failed to acquire locks to account " + sender.id
                     * + " and account" + receiver.id);
                     * Thread.sleep(1000);
                     * 
                     * }
                     * } else {
                     * Thread.sleep(1000);
                     * }
                     */

                    /*
                     * fixed synchronization. first, pick left. if it cant get right. DROP LEFT and
                     * WAIT
                     */

                    if (transactionCount == 0) {
                        if (getLeftLock()) {

                            if (getRightLock()) {
                                System.out.println("Transaction " + transactionId +
                                        " acquired locks to account " + sender.id
                                        + " and account " + receiver.id);

                                try {

                                    System.out.println(
                                            "Account " + sender.id + " performing transaction with Account " +
                                                    receiver.id);

                                    // Simulating a transaction

                                    System.out.println("Transaction " + transactionId + " completed.");
                                    transactionCount += 1;
                                    Thread.sleep(1000);
                                } catch (InterruptedException e) {

                                }

                                finally {
                                    receiver.lock.unlock();
                                    sender.lock.unlock();
                                    Thread.sleep(1000);

                                    System.out.println(
                                            "Transaction " + transactionId + " released lock to account " + sender.id
                                                    + " and  account " + receiver.id);

                                }
                            } else {
                                sender.lock.unlock();
                            }
                        } else {
                            System.out.println("Transaction " + transactionId +
                                    " failed to acquire locks to account " + sender.id
                                    + " and account " + receiver.id);
                            Thread.sleep(1000);

                        }
                    } else {
                        Thread.sleep(1000);
                    }

                }
            } catch (

            InterruptedException e) {
            }

        }
    }

    public static class Account {

        private Lock lock = new ReentrantLock();
        private int id;

        Account(int n) {
            id = n;
        }

        public int getId() {
            return id;
        }

    }

}
