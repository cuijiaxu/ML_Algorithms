import com.sun.istack.internal.NotNull;

import java.util.*;
import java.io.BufferedReader;
import java.io.IOException;

/**
 * ChineseSegment
 */
public class ChineseSegment {

    public static final int MAXLEN=7;    //词条的最大长度，每个汉字两个字节
    private static final String COLUMN_SEPARATOR = "\\s+"; //字典分隔符
    private DoubleArrayTrie dat = new DoubleArrayTrie();
    private String dismatchWord;
    private List<String> dismatchWords;
    private List<String> matchWords;

    //获取词典
    public ChineseSegment(@NotNull String dictionaryFile) {
        initdat(dictionaryFile);
    }

    //使用Double Array Trie构建字典
    private void initdat(@NotNull String dictionaryFile){
        BufferedReader reader;
        List<String> words = new ArrayList<String>();
        try {
            reader = FileOperUtil.read(dictionaryFile);
            for (String line; (line = reader.readLine()) != null;) {
                String [] cols = line.split(COLUMN_SEPARATOR);
                // 只添加每一行的第一个词到词典
                words.add(cols[0]);
            }
            reader.close();
            Collections.sort(words);
            dat.build(words);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /*
	 * 这里输入的是已经经过预处理的段落
	 * 逆向最大匹配分词
	 * @return 输入文本的位置是否切分
	 * */
    public boolean ReverseMaxMatch(@NotNull String sentence) {
        int sentenceLength = sentence.length();
        if (sentence.length() <= 0) return false;

        matchWords = new ArrayList<>();
        dismatchWords = new ArrayList<>();
        dismatchWord = "";
        String subString;
        int offset;

        while(sentence!=null&&sentenceLength>0){
            if(sentenceLength>MAXLEN){
                subString=sentence.substring(sentenceLength-MAXLEN,sentenceLength);
            }else{
                subString=sentence.substring(0,sentenceLength);
            }
           offset=getMaxMatchPosition(subString);
           if (offset == 1) {
                checkEnAndNum(subString);//如果不匹配，则进行英文与数字处理
           }
           sentenceLength-=offset;
        }

        if (!dismatchWord.isEmpty()) {
            checkEnAndNum("");
        }

        return true;
    }

    //逆向查找最大词
    private int getMaxMatchPosition(String subString){    //查找某一字符串以及其子串是否在词库中
		String temp=null;
		for(int i=0;i<subString.length();i++){     //制作子串
            temp = subString.substring(i);
            int a = dat.exactMatchSearch(temp);
            if (a>=0) {
                if (!dismatchWord.isEmpty()) {
                    checkEnAndNum("");
                }
                //System.out.println(temp);
                matchWords.add(temp);
                return MAXLEN-i;
            }
        }
		return 1;
    }
    
    /**
     * 正向最大分词
     * @param sentence
     * @return
     */
    public boolean ForwardMaxMatch(@NotNull String sentence) {
        int sentenceLength = sentence.length();
        if (sentence.length() <= 0) return false;

        matchWords = new ArrayList<>();
        dismatchWords = new ArrayList<>();
        dismatchWord = "";

        while (sentenceLength > 0) {
            String word = sentence;
            int wordLength = word.length();
            boolean hasWord = false;
            int index = 0;
            for (; index < wordLength; index++) {
                String tmpWord = word.substring(index);
                int a = dat.exactMatchSearch(tmpWord);
                if (a>=0) {
                    if (!dismatchWord.isEmpty()) {
                        checkEnAndNum("");
                    }
                    matchWords.add(tmpWord);
                    hasWord = true;
                    break;
                }
            }

            if (hasWord)
                sentence = sentence.substring(0, index);
            else {
                checkEnAndNum(sentence.substring(sentenceLength - 1));
                sentence = sentence.substring(0, sentenceLength - 1);
            }

            sentenceLength = sentence.length();
        }

        if (!dismatchWord.isEmpty()) {
            checkEnAndNum("");
        }

        return true;
    }

    private void checkEnAndNum(@NotNull String newCharacter) {
        newCharacter = newCharacter.trim();
        int oldType = StringUtil.getType(dismatchWord);
        int newType = StringUtil.getType(newCharacter);

        oldType = oldType == StringUtil.WORD_TYPE_NULL_OR_EMPTY ? newType : oldType;

        if (oldType == newType) {
            dismatchWord = newCharacter + dismatchWord;
        } else {
            if (oldType == StringUtil.WORD_TYPE_NM || oldType == StringUtil.WORD_TYPE_EN) {
                matchWords.add(dismatchWord);
            } else {
                dismatchWords.add(dismatchWord);
            }
            dismatchWord = newCharacter;
        }
    }

    private String wordsToString(@NotNull List<String> words, @NotNull String wordSeparator) {
        String resultStr = "";
        for (String word : words) {
            resultStr = word + wordSeparator + resultStr;
        }
        // 去除最后一个分隔符
        if (resultStr.lastIndexOf(wordSeparator) != -1)
            resultStr = resultStr.substring(0, resultStr.lastIndexOf(wordSeparator));
        return resultStr;
    }

    public void printMatchWords() {
        System.out.println("Match Words: " + wordsToString(matchWords, "\t"));
        System.out.println("Dismatch Words: " + wordsToString(dismatchWords, "\t"));
    }
}
