import com.sun.istack.internal.NotNull;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * StringUtil
 */
public class StringUtil {

    public static int getType(@NotNull String word) {
        if (word == null || word.isEmpty()) return WORD_TYPE_NULL_OR_EMPTY;
        else if (word.trim().isEmpty()) return WORD_TYPE_TAB_OR_SPACE;
        else if (isNumber(word)) return WORD_TYPE_NM;
        else if (isEnglish(word)) return WORD_TYPE_EN;
        else if (isChinese(word)) return WORD_TYPE_CN;
        else return WORD_TYPE_UNDEFINED;
    }

    public static final int WORD_TYPE_NULL_OR_EMPTY = -2;       // 字符串为空或其长度为空
    public static final int WORD_TYPE_TAB_OR_SPACE = -1;        // 字符串为tab键或空格
    public static final int WORD_TYPE_UNDEFINED = 0;            // 未定义的词语类型
    public static final int WORD_TYPE_NM = 1;                   // 数值
    public static final int WORD_TYPE_EN = 2;                   // 英文
    public static final int WORD_TYPE_CN = 3;                   // 中文


    private static boolean isChinese(String word) {
        return matchPattern(word, "^[\u4E00-\u9FA5]+$");            // 匹配：长度大于1的中文字符串
    }

    private static boolean isEnglish(String word) {
        return matchPattern(word, "^[a-zA-Z]+$");                   // 匹配：长度大于1的英文字符串
    }

    private static boolean isNumber(String word) {
        return matchPattern(word, "^[\\-\\+]?[0-9]+\\.?[0-9]+$|" +  // 匹配：正负小数
                                  "^[\\-\\+]?\\.[0-9]+$|" +         // 匹配：-.6 类型的小数
                                  "^[\\-\\+]?[0-9]+\\.$|" +         // 匹配：-6. 类型的小数
                                  "^[\\-\\+]?[0-9]+$");             // 匹配：整数
    }

    private static boolean matchPattern(String word, String patternString) {
        Pattern pattern = Pattern.compile(patternString);
        Matcher matcher = pattern.matcher(word);
        return matcher.matches();
    }

}
