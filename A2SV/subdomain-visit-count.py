class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for cp in cpdomains:
            num, domains = cp.split(" ")
            dic[domains] = dic.get(domains,0) + int(num)

            for i in range(len(cp)-1, -1, -1):
                if cp[i] == ".":
                    dic[cp[i+1:]] = dic.get(cp[i+1:], 0) + int(num)
        ans = []
        for key,value in dic.items():
            ans.append(f"{value} {key}")
        return ans