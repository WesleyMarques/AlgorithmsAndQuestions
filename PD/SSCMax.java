/*The algorithm search the max longest increasing subsequence of a list
*/ 
public class SSCMax{
	//return a list with all possibilities
	private int[] SSCMaxPD(int[] A, int N){
	int[] c = new int[N];
	for (int m = 0;m < N;m++) {
		c[m] = 1;
		for (int i = m-1;i >= 0 ; i--) {
			if (A[i] <= A[m] && c[i]+1 > c[m]) {
				c[m] = c[i]+1;
			}			
		}
	}
	return c;
	}

}