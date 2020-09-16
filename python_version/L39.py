# @Time : 2020/3/30 13:56
# @Author : Xylia_Yang
# @Description :

class Solution:
    def combinationSum(self, candidates, target):
        if not candidates :
            return [[]]

        self.res=[]
        candidates.sort()

        def combinationCore(candidates,cur_ls,cur_sum,target):
            for candidate in candidates:
                if cur_sum+candidate>target:
                    break

                elif cur_sum+candidate==target:
                    cur_res=cur_ls+[candidate]
                    cur_res.sort()
                    if cur_res not in self.res:  # 去重
                        self.res.append(cur_res)

                    break
                else:
                    combinationCore(candidates,cur_ls+[candidate],cur_sum+candidate,target)
            if cur_ls:
                cur_sum -= cur_ls[-1]
                cur_ls.pop()
            return
        combinationCore(candidates,[],0,target)
        return self.res

if __name__=='__main__':
    solution=Solution()
    candidates=[2,3,6,7]
    target=7
    print(solution.combinationSum(candidates,target))
