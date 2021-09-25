class Solution {
    public boolean isPalindrome(int x) {
        int z=x;
        int i=0;
        if(x<0){
            return false;
        }
                
        while(x!=0){
           i=i*10+x%10;
            
            x=(int)x/10 ;
        }
            
        
        if( i==z){
            return true;
        }
            
        else{
           return false; 
        }
            
    }
}
