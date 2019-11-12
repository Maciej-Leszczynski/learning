package machine;
import java.util.Scanner;
 
public class CoffeeMachine {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
 
        Machine coffeeMachine = new Machine(400, 540, 120, 9, 550);
                                           
        while (coffeeMachine.turnOn) {
            String typeOfAction = coffeeMachine.action();
            switch (typeOfAction) {
                case "buy":
                    String typeOfCoffee = coffeeMachine.coffee();
                    if (typeOfCoffee.equals("1")) {
                        int waterEspresso = 250;
                        int coffeeEspresso = 16;
                        if (coffeeMachine.waterInCoffeeMachine >= waterEspresso && coffeeMachine.coffeeBeansInCoffeeMachine >= coffeeEspresso) {
                            System.out.println("I have enough resources, making you a coffee!");
                            coffeeMachine.waterInCoffeeMachine -= waterEspresso;
                            coffeeMachine.coffeeBeansInCoffeeMachine -= coffeeEspresso;
                            coffeeMachine.moneyInCoffeeMachine += 4;
                            coffeeMachine.cupsInCoffeeMachine -= 1;
                        } else if (waterEspresso > coffeeMachine.waterInCoffeeMachine) {
                            System.out.println("Sorry, not enough water!");
                        } else if (coffeeEspresso > coffeeMachine.coffeeBeansInCoffeeMachine) {
                            System.out.println("Sorry, not enough coffee beans!");
                        } else if (coffeeMachine.cupsInCoffeeMachine == 0) {
                            System.out.println("Sorry, not enough cups!");
                        }
                    } else if(typeOfCoffee.equals("2")) {
                        int waterLatte = 350;
                        int milkLatte = 75;
                        int coffeeLatte = 20;
                        if (coffeeMachine.waterInCoffeeMachine >= waterLatte && coffeeMachine.milkInCoffeeMachine >= milkLatte && coffeeMachine.coffeeBeansInCoffeeMachine >=coffeeLatte) {
                            System.out.println("I have enough resources, making you a coffee!");
                            coffeeMachine.waterInCoffeeMachine -= waterLatte;
                            coffeeMachine.milkInCoffeeMachine -= milkLatte;
                            coffeeMachine.coffeeBeansInCoffeeMachine -= coffeeLatte;
                            coffeeMachine.moneyInCoffeeMachine += 7;
                            coffeeMachine.cupsInCoffeeMachine -= 1;
                        } else if (waterLatte > coffeeMachine.waterInCoffeeMachine) {
                            System.out.println("Sorry, not enough water!");
                        } else if (coffeeLatte > coffeeMachine.coffeeBeansInCoffeeMachine) {
                            System.out.println("Sorry, not enough coffee beans!");
                        } else if (coffeeMachine.cupsInCoffeeMachine == 0) {
                            System.out.println("Sorry, not enough cups!");
                        } else if (milkLatte > coffeeMachine.milkInCoffeeMachine) {
                            System.out.println("Sorry, not enough milk!");
                        }
                    } else if(typeOfCoffee.equals("3")) {
                        int waterCappuccino = 200;
                        int milkCappuccino = 100;
                        int coffeeCappuccino = 12;
                        if (coffeeMachine.waterInCoffeeMachine >= waterCappuccino && coffeeMachine.milkInCoffeeMachine >= milkCappuccino && coffeeMachine.coffeeBeansInCoffeeMachine >= coffeeCappuccino) {
                            System.out.println("I have enough resources, making you a coffee!");
                            coffeeMachine.waterInCoffeeMachine -= waterCappuccino;
                            coffeeMachine.milkInCoffeeMachine -= milkCappuccino;
                            coffeeMachine.coffeeBeansInCoffeeMachine -= coffeeCappuccino;
                            coffeeMachine.moneyInCoffeeMachine += 6;
                            coffeeMachine.cupsInCoffeeMachine -= 1;
                        } else if (waterCappuccino > coffeeMachine.waterInCoffeeMachine) {
                            System.out.println("Sorry, not enough water!");
                        } else if (coffeeCappuccino > coffeeMachine.coffeeBeansInCoffeeMachine) {
                            System.out.println("Sorry, not enough coffee beans!");
                        } else if (coffeeMachine.cupsInCoffeeMachine == 0) {
                            System.out.println("Sorry, not enough cups!");
                        } else if (milkCappuccino > coffeeMachine.milkInCoffeeMachine) {
                            System.out.println("Sorry, not enough milk!");
                        }
                    } else if(typeOfCoffee.equals("back")) {
                        break;
                    }
                    break;
                case "fill":
                    System.out.println("Write how many ml of water do you want to add:");
                    int water = scanner.nextInt();
                    coffeeMachine.waterInCoffeeMachine += water;
                    System.out.println("Write how many ml of milk do you want to add: ");
                    int milk = scanner.nextInt();
                    coffeeMachine.milkInCoffeeMachine += milk;
                    System.out.println("Write how many grams of coffee beans do you want to add:");
                    int coffee = scanner.nextInt();
                    coffeeMachine.coffeeBeansInCoffeeMachine += coffee;
                    System.out.println("Write how many disposable cups of coffee do you want to add:");
                    int cups = scanner.nextInt();
                    coffeeMachine.cupsInCoffeeMachine += cups;
                    break;
                case "take":
                    System.out.println("I gave you $" + coffeeMachine.moneyInCoffeeMachine);
                    coffeeMachine.moneyInCoffeeMachine = 0;
                    break;
                case "remaining":
                    System.out.println("The coffee machine has:");
                    System.out.println(coffeeMachine.waterInCoffeeMachine + " of water");
                    System.out.println(coffeeMachine.milkInCoffeeMachine + " of milk");
                    System.out.println(coffeeMachine.coffeeBeansInCoffeeMachine + " of coffee beans");
                    System.out.println(coffeeMachine.cupsInCoffeeMachine + " of disposable cups");
                    System.out.println(coffeeMachine.moneyInCoffeeMachine + " of money");
                    break;
                case "exit":
                    coffeeMachine.turnOn = false;
                    break;
            }
        }
    }
}
class Machine {
    Scanner scanner = new Scanner(System.in);
    boolean turnOn = true;
 
    // Resources in coffee machine:
    int waterInCoffeeMachine;
    int milkInCoffeeMachine;
    int coffeeBeansInCoffeeMachine;
    int cupsInCoffeeMachine;
    int moneyInCoffeeMachine;
 
    public Machine(int waterInCoffeeMachine, int milkInCoffeeMachine,
                        int coffeeBeansInCoffeeMachine, int cupsInCoffeeMachine,
                        int moneyInCoffeeMachine) {
 
        this.waterInCoffeeMachine = waterInCoffeeMachine;
        this.milkInCoffeeMachine = milkInCoffeeMachine;
        this.coffeeBeansInCoffeeMachine = coffeeBeansInCoffeeMachine;
        this.cupsInCoffeeMachine = cupsInCoffeeMachine;
        this.moneyInCoffeeMachine = moneyInCoffeeMachine;
    }
 
    public String action() {
        System.out.println("Write action (buy, fill, take, remaining, exit):");
        String actionType = scanner.next();
        return actionType;
    }
 
