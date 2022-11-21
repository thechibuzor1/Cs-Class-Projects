class Square {

    public static int getPow(int x, int n) {
        int start = x;

        while (n > 1) {
            x = x * start;
            n = n - 1;
        }
        return x;
    }

    public static void main(String[] args) {
        System.out.println(getPow(7, 5));
    }
}