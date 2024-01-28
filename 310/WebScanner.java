import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class WebScanner {

    public static String getWebsiteText(String url) throws IOException {
        Document document = Jsoup.connect(url).get();
        Elements paragraphs = document.select("p");
        StringBuilder text = new StringBuilder();

        for (Element paragraph : paragraphs) {
            text.append(paragraph.text()).append("\n");
        }

        return text.toString();
    }

    public static Set<String> cleanAndTokenize(String text) {
        String[] words = text.replaceAll("[^a-zA-Z ]", "").toLowerCase().split("\\s+");
        Set<String> stopWords = new HashSet<>(Arrays.asList("a", "an", "the", "and", "is", "in", "to", "of"));
        Set<String> filteredWords = new HashSet<>();

        for (String word : words) {
            if (!stopWords.contains(word)) {
                filteredWords.add(word);
            }
        }

        return filteredWords;
    }

    public static int calculateScore(Set<String> queryWords, Set<String> textWords) {
        int score = 0;

        for (String word : queryWords) {
            if (textWords.contains(word)) {
                score++;
            }
        }

        return score;
    }

    public static Map.Entry<String, Integer> findRelevantParagraph(String url, String query) throws IOException {
        String websiteText = getWebsiteText(url);
        Set<String> queryWords = cleanAndTokenize(query);
        Set<String> textWords = cleanAndTokenize(websiteText);

        Map.Entry<String, Integer> bestParagraph = null;
        int bestScore = 0;

        String[] paragraphs = websiteText.split("\n");

        for (int i = 0; i < paragraphs.length; i++) {
            int score = calculateScore(queryWords, cleanAndTokenize(paragraphs[i]));

            if (score > bestScore) {
                bestScore = score;
                bestParagraph = Map.entry(paragraphs[i], i + 1);
            }
        }

        return bestParagraph;
    }

    public static void main(String[] args) {
        String websiteUrl = "https://example.com"; // Replace with the URL of the website you want to scan
        String searchQuery = "your search query"; // Replace with your search query

        try {
            Map.Entry<String, Integer> relevantParagraph = findRelevantParagraph(websiteUrl, searchQuery);

            if (relevantParagraph != null) {
                System.out.println("Relevant Paragraph:");
                System.out.println(relevantParagraph.getKey());
                System.out.println("\nDirect link to the relevant paragraph:");
                System.out.println(websiteUrl + "#paragraph-" + relevantParagraph.getValue());
            } else {
                System.out.println("No relevant paragraph found.");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
