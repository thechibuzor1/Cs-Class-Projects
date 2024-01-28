import java.util.concurrent.*;
import java.util.concurrent.locks.*;

public class Dining {

    public static void main(String[] args) {
        // create a list of type forks
        Fork[] fork = new Fork[5];

        // Create 5 fork objects
        for (int i = 0; i < 5; i++) {
            fork[i] = new Fork(i + 1);
        }

        // initailize a threadpool
        ExecutorService executor = Executors.newCachedThreadPool();

        // Simulate a round table

        for (int i = 0; i < 5; i++) {

            int nextFork = (i + 1) % 5; // Circular ordering
            executor.execute(new Philosopher(fork[i], fork[nextFork], i + 1));
        }

        executor.shutdown();
        while (!executor.isTerminated()) {
        }

    }

    public static class Philosopher implements Runnable {
        // "Philosopher"
        private int PhilosopherId; // each Philosopher has a unique id
        private Fork Left; // left "fork"
        private Fork Right;// right "fork"
        private int timesPhilosopherAte = 0; // keep track of how many times each Philosopher has eaten.

        Philosopher(Fork A, Fork B, int id) {
            // constructor
            PhilosopherId = id;
            Left = A;
            Right = B;
        }

        public boolean getForks() {
            // get both right and left fork
            return (Left.lock.tryLock() && Right.lock.tryLock());
        }

        public boolean getLeftFork() {
            // get left fork
            return (Left.lock.tryLock());
        }

        public boolean getRightFork() {
            // get right fork
            return (Right.lock.tryLock());
        }

        public void run() {
            try {

                /* All picked left waiting for the other to release the right: livelock */

                /*
                 * while (timesPhilosopherAte == 0) {
                 * if (getLeftFork()) {
                 * Thread.sleep(1000);
                 * if (getRightFork()) {
                 * 
                 * try {
                 * System.out.println(
                 * "Philosopher " + PhilosopherId +
                 * " is eating. ");
                 * 
                 * Thread.sleep(1000);
                 * timesPhilosopherAte += 1;
                 * 
                 * } finally {
                 * Left.lock.unlock();
                 * Right.lock.unlock();
                 * 
                 * }
                 * } else {
                 * Thread.sleep(1000);
                 * System.out.println("Philosopher " + PhilosopherId + " is thinking.");
                 * 
                 * }
                 * } else {
                 * Thread.sleep(1000);
                 * System.out.println("Philosopher " + PhilosopherId + " is thinking.");
                 * 
                 * }
                 * }
                 */

                /*
                 * starvation: one or more Philosopher keep failing to acquire the lock and run
                 * to completion.
                 */

                while (timesPhilosopherAte == 0) {
                    if (getForks()) {

                        try {
                            System.out.println(
                                    "Philosopher " + PhilosopherId +
                                            " is eating. ");

                            Thread.sleep(1000);
                            timesPhilosopherAte += 1;

                        } finally {
                            Left.lock.unlock();
                            Right.lock.unlock();

                        }
                    } else {
                        Thread.sleep(1000);
                        System.out.println("Philosopher " + PhilosopherId + " is thinking.");
                    }
                }

                /*
                 * fixed synchronization. first, pick left. if it cant get right. DROP LEFT and
                 * WAIT
                 */

                /*
                 * while (timesPhilosopherAte < 10) {
                 * if (getLeftFork()) {
                 * 
                 * if (getRightFork()) {
                 * 
                 * try {
                 * 
                 * // Simulating a philisopher eating
                 * 
                 * System.out.println("Philosopher " + PhilosopherId + " is eating.");
                 * timesPhilosopherAte += 1;
                 * Thread.sleep(1000);
                 * } catch (InterruptedException e) {
                 * 
                 * }
                 * 
                 * finally {
                 * // release the locks when done
                 * Left.lock.unlock();
                 * Right.lock.unlock();
                 * Thread.sleep(1000);
                 * 
                 * }
                 * } else {
                 * Left.lock.unlock();
                 * }
                 * } else {
                 * System.out.println("Philosopher " + PhilosopherId + " is thinking.");
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

    public static class Fork {
        // "fork" class
        private Lock lock = new ReentrantLock();
        private int id;

        Fork(int n) {
            id = n;
        }

        public int getId() {
            return id;
        }

    }

}
