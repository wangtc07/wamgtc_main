package Polymorphism.Polymorphism_03_ex;

public class Animal {
    public String name ;
    public int age ;

    public Animal(){

    }

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }

    public void eat() {
        System.out.println("Animal eat");
    }
    
}
