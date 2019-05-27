import java.util.ArrayList;

public class Fridge {
    ArrayList<String> fridgeContents;

    public Fridge() {
        fridgeContents = new ArrayList<>();
    }

    public ArrayList<String> getFridgeContents() {
        return fridgeContents;
    }

    public void add(String item) {
        fridgeContents.add(item);
    }
}
