class Solution {
    public int firstMissingPositive(int[] nums) {
        HashMap<Integer,Boolean> hm  = new HashMap<>(); 
        int max = Integer.MIN_VALUE;
        for(int i : nums){
            hm.put(i,true);
            max = Math.max(max,i);
        }
        if(max<0)
            return 1;
        for(int i = 1;i<max;i++){
            if(hm.get(i) == null)
                return i;
        }
       
        return max+1;
    }
}
