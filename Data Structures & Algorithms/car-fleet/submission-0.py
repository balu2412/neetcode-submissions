class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l=sorted(zip(position,speed), reverse=True)
        st=[]
        for i,j in l:
            time=(target-i)/j
            if not st or time>st[-1]:
                st.append(time)
        return len(st)