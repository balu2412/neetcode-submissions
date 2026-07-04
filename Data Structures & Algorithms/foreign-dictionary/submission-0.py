class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # -----------------------------
        # Step 1: Create adjacency list
        # -----------------------------
        adj = {}

        # Add every unique character as a node
        for word in words:
            for ch in word:
                if ch not in adj:
                    adj[ch] = set()

        # -----------------------------
        # Step 2: Create indegree array
        # -----------------------------
        indegree = {}

        for ch in adj:
            indegree[ch] = 0

        # ----------------------------------------
        # Step 3: Compare every adjacent word pair
        # ----------------------------------------
        for i in range(len(words) - 1):

            word1 = words[i]
            word2 = words[i + 1]

            minimumLength = min(len(word1), len(word2))

            # Invalid case
            # Example:
            # abc
            # ab
            if len(word1) > len(word2) and word1[:minimumLength] == word2[:minimumLength]:
                return ""

            # Find first different character
            for j in range(minimumLength):

                if word1[j] != word2[j]:

                    parent = word1[j]
                    child = word2[j]

                    # Avoid duplicate edges
                    if child not in adj[parent]:
                        adj[parent].add(child)
                        indegree[child] += 1

                    # Only first difference matters
                    break

        # -----------------------------
        # Step 4: Push indegree 0 nodes
        # -----------------------------
        queue = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)

        # -----------------------------
        # Step 5: Topological Sort (BFS)
        # -----------------------------
        answer = []

        while queue:

            current = queue.popleft()

            answer.append(current)

            for neighbor in adj[current]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # -----------------------------
        # Step 6: Detect Cycle
        # -----------------------------
        if len(answer) != len(adj):
            return ""

        # -----------------------------
        # Step 7: Return Result
        # -----------------------------
        return "".join(answer)