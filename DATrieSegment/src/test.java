/**
 * test
 */
public class test {

    public static void main(String[] args) {
        System.out.println("System user dir: " + System.getProperty("user.dir") + "该目录在run configuration下更改");
        ChineseSegment segment = new ChineseSegment(".\\resource\\ICTdic.txt");
        //segment.ReverseMaxMatch("因早盘低开大幅低开，抄底资金纷纷进入，指数亦被拉升，截至中午收盘，上证指数下跌50.53点。");
        segment.ReverseMaxMatch("总体词数越少越好，在相同字数的情况下，总词数越少，说明语义单元越少，那么相对的单个语义单元的权重会越大，因此准确性会越高。");
        //segment.ForwardMaxMatch("总体词数越少越好，在相同字数的情况下，总词数越少，说明语义单元越少，那么相对的单个语义单元的权重会越大，因此准确性会越高。");
        segment.printMatchWords();
    }
}
