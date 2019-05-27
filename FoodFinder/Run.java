import java.util.Scanner;
import java.util.ArrayList;

public class Run {
    public static ArrayList<Food> recipes = new ArrayList<>();
    public static ArrayList<Food> options = new ArrayList<>();

    public static void main(String[] args) {
        Fridge myFridge = new Fridge();

        Food taco = new Food("Taco");
        taco.add("Meat");
        taco.add("Tortilla");
        taco.add("Cheese");
        Food sandwich = new Food("Sandwich");
        sandwich.add("Bread");
        sandwich.add("Cheese");
        sandwich.add("Meat");
        sandwich.add("Mayo");

        recipes.add(taco);
        recipes.add(sandwich);

        Scanner s = new Scanner(System.in);
        System.out.println("What is in your fridge?");
        String input = s.nextLine();

        while(!input.equals("")) {
            myFridge.add(input);
            input = s.nextLine();
        }

        for(int i = 0; i < recipes.size(); i++) {
            int count = 0;

            for(int j = 0; j < recipes.get(i).getRecipe().size(); j++) {
                if(myFridge.getFridgeContents().contains(recipes.get(i).getRecipe().get(j))) {
                    count++;
                }
            }

            if(count == recipes.get(i).getRecipe().size()) {
                options.add(recipes.get(i));
            }
        }

        if(options.size() == 0) {
            System.out.println("You can't make anything in our database");
        } else {
            for(int x = 0; x < options.size(); x++) {
                System.out.println("You Can Make . . .");
                System.out.println(options.get(x).getName() + "\n");
                System.out.println("What You Need . . .");
                for(int y = 0; y < options.get(x).getRecipe().size(); y++) {
                    System.out.println(options.get(x). getRecipe().get(y));
                }
                System.out.println();
            }
        }

        System.out.println("\n Program Terminated");
    }
}
