

def convert(s):
    _, res = dfs(s, 0)
    return res


def dfs(s, i):
    res = []
    n = i+1
    while n < len(s):
        if s[n] == ',':
            n += 1
            continue
        elif s[n] == ']':
            return n+1, res
        elif s[n] == '[':
            tn, tmp = dfs(s, n)
            n = tn
            res.append(tmp)
        else:
            res.append(int(s[n]))
            n += 1


if __name__ == '__main__':
    s = '[1,2,[3,4],[5,[6,[7]]],8,9]'
    res = convert(s)
    for i in res:
        if isinstance(i, list):
            print '------------------'
            for ii in i:
                print ii
            print 'end-----------'
        else:
            print i

# 1
# 2
# [3, 4]
# [5, [6, [7]]]
# 8
# 9
"""
public class Test {
    public static void main(String[] args) {
        String str = "[1,2,[3,4],[6,[7]],[1,2,[2,[2]]]]";
        Test test = new Test();
        List<Object> rest = test.getRes(str);
        //System.out.println(rest.size());
        for (int i = 0; i < rest.size(); i++) {
            System.out.println(rest.get(i));
        }
    }    
    
    
    public List<Object> getRes(String str) {
        Stack<List<Object>> stack = new Stack();
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch == '[') {
                stack.add(new ArrayList());
            } else if (ch == ']') {
                List<Object> cur = stack.pop();
                if (i == str.length() - 1) return cur;
                stack.peek().add(cur);
            } else if (ch != ',') {
                stack.peek().add(ch);
            }
        }
        return null;
    }

"""