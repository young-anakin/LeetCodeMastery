class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []

        ing = defaultdict(list)
        dep = defaultdict(int)

        for i, val in enumerate(recipes):
            for j in ingredients[i]:
                ing[j].append(val)    
                dep[val] +=1        

        # print(ing)
        queue = deque(supplies)
        while queue:
            element = queue.popleft()
            for val in ing[element]:
                dep[val] -=1
                if dep[val] == 0:
                    ans.append(val)
                    queue.append(val)
        
        return ans