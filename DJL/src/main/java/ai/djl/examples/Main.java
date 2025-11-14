package ai.djl.examples;

import ai.djl.ModelException;
import ai.djl.huggingface.translator.QuestionAnsweringTranslatorFactory;
import ai.djl.inference.Predictor;
import ai.djl.modality.nlp.qa.QAInput;
import ai.djl.repository.zoo.Criteria;
import ai.djl.repository.zoo.ZooModel;
import ai.djl.training.util.ProgressBar;
import ai.djl.translate.TranslateException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.io.IOException;

public class Main {
    private static final Logger logger = LoggerFactory.getLogger(Main.class);

    private Main() {}

    public static void main(String[] args) throws IOException, TranslateException, ModelException {
        String answer = Main.predict();
        logger.info("Output: {}", answer);
        System.out.println("Output: " + answer);
    }

    public static String predict() throws IOException, TranslateException, ModelException {
        String question = "When did BBC Japan start broadcasting?";
        String paragraph =
                "BBC Japan was a general entertainment Channel. "
                        + "Which operated between December 2004 and April 2006. "
                        + "It ceased operations after its Japanese distributor folded.";

        QAInput input = new QAInput(question, paragraph);
        logger.info("Paragraph: {}", input.getParagraph());
        logger.info("Question: {}", input.getQuestion());

        Criteria<QAInput, String> criteria =
                Criteria.builder()
                        .setTypes(QAInput.class, String.class)
                        .optModelUrls(
                                "djl://ai.djl.huggingface.pytorch/deepset/minilm-uncased-squad2")
                        .optEngine("PyTorch")
                        .optTranslatorFactory(new QuestionAnsweringTranslatorFactory())
                        .optArgument("detail", true)
                        .optProgress(new ProgressBar())
                        .build();

        try (ZooModel<QAInput, String> model = criteria.loadModel();
             Predictor<QAInput, String> predictor = model.newPredictor()) {
            return predictor.predict(input);
        }
    }
}
