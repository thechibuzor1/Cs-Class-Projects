public class Person {
    private String name;
    private int age;

    Person(String n) { // constructor
        this.name = n;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    public void setAge(int a) {
        this.age = a;
    }
}