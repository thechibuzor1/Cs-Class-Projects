import java.util.concurrent.*;
import java.util.concurrent.locks.*;

public class Dining {

    /*
     * Imagine 5 accounts at the table. In this analogy, the accounts are the forks.
     * Any two accounts can participate in a transaction. Transactions ==
     * philosophers. So in this example the transactions (philosopher) can not only
     * sit at the edge of the table between two accounts (forks).
     */

    public static void main(String[] args) {
        // create a list of type "Acount"
        Account[] accounts = new Account[5];

        // Create 5 accounts
        for (int i = 0; i < 5; i++) {
            accounts[i] = new Account(i + 1);
        }

        // initailize a threadpool
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
        // "Philosopher"
        private int transactionId; // each transaction ('Philosopher') has a unique id
        private Account sender; // left "fork"
        private Account receiver;// right "fork"
        private int transactionCount = 0; // keep track of how many times each "Philosopher" has eaten.

        Transactions(Account A, Account B, int id) {
            // constructor
            transactionId = id;
            sender = A;
            receiver = B;
        }

        public boolean getLocks() {
            // get both right and left fork
            return (sender.lock.tryLock() && receiver.lock.tryLock());
        }

        public boolean getLeftLock() {
            // get left fork
            return (sender.lock.tryLock());
        }

        public boolean getRightLock() {
            // get right fork
            return (receiver.lock.tryLock());
        }

        public void run() {
            try {

                /* All picked left waiting for the other to release the right: livelock */

                while (transactionCount == 0) {
                    if (getLeftLock()) {
                        System.out.println("Transaction " + transactionId +
                                " acquired lock to account " + sender.id);
                        if (getRightLock()) {
                            System.out.println("Transaction " + transactionId +
                                    " acquired lock to account " + receiver.id);
                            try {
                                System.out.println(
                                        "Account " + sender.id + " performing transaction with Account " +
                                                receiver.id);
                                // Simulating a transaction
                                Thread.sleep(1000);
                                transactionCount += 1;
                                System.out.println("Transaction between Account " + sender.id +
                                        " and Account "
                                        + receiver.id + " completed.");

                            } finally {
                                receiver.lock.unlock();
                                sender.lock.unlock();
                                System.out.println(
                                        "Transaction " + transactionId + " released lock to account " + receiver.id);
                            }
                        } else {
                            System.out.println(
                                    "Transaction " + transactionId + " failed to acquire lock to account " +
                                            receiver.id);
                        }
                    } else {
                        System.out.println(
                                "Transaction " + transactionId + " failed to acquire lock to account " +
                                        sender.id);
                        Thread.sleep(1000);
                    }
                }

                /*
                 * starvation: one or more transactions keep failing to acquire the lock and run
                 * to completion.
                 */

                /*
                 * while (transactionCount == 0) {
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
                 * }
                 */

                /*
                 * fixed synchronization. first, pick left. if it cant get right. DROP LEFT and
                 * WAIT
                 */

                /*
                 * while (transactionCount == 0) {
                 * if (getLeftLock()) {
                 * 
                 * if (getRightLock()) {
                 * System.out.println("Transaction " + transactionId +
                 * " acquired locks to account " + sender.id
                 * + " and account " + receiver.id);
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
                 * } catch (InterruptedException e) {
                 * 
                 * }
                 * 
                 * finally {
                 * // release the locks when done
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
                 * sender.lock.unlock();
                 * }
                 * } else {
                 * System.out.println("Transaction " + transactionId +
                 * " failed to acquire locks to account " + sender.id
                 * + " and account " + receiver.id);
                 * Thread.sleep(1000);
                 * 
                 * }
                 * }
                 */

            } catch (

            InterruptedException e) {
            }

        }
    }

    public static class Account {
        // "fork" class
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
