class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hsmap=dict()
        count=0
        for link in cpdomains:
            count, domain= link.split(" ")
            domains= domain.split(".")
            domains=['.'.join(domains[i:]) for i in range(len(domains))]
            for i in domains:
                if i in hsmap:
                    hsmap[i] += int(count)
                else:
                    hsmap[i] = int(count)
        result=[f"{value} {key}" for  key, value in hsmap.items()]
        return result