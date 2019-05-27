import java.util.ArrayList;

public class Food {
    private String name;
    private ArrayList<String> recipe;

    public Food(String name) {
        this.name = name;
        recipe = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public ArrayList<String> getRecipe() {
        return recipe;
    }

    public void add(String item) {
        recipe.add(item);
    }
}
