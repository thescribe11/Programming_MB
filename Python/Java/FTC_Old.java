import java.util.Scanner;

public class FTC_Old {
	public static final  double  LOW_TEMP_F_WARNING = 0.;
	public static final  double  HIGH_TEMP_F_WARNING = 100.;
	public static final  int     MAX_LOOP = 5;

	public static void main(String[] args) {
		double Farenheit = 0;
		double Celsius = 0;
		Scanner sc = new Scanner(System.in);

		for (int i=0; i<MAX_LOOP; i++) {
			System.out.print("\nEnter a temperature (F): ");
			if (sc.hasNextDouble())
			{
				Farenheit = sc.nextDouble();
				Celsius = ( Farenheit - 32.) * 5./9.;
			} else {
				System.out.println("[!] Data entry error!");
				System.exit(-1);
			}

			if (Farenheit > HIGH_TEMP_F_WARNING) {
				System.out.println("Remember to hydrate!\n");
			}
			
			if (Farenheit < LOW_TEMP_F_WARNING) {
				System.out.println("Remember to pack long underwear!\n");
			}
		}
		System.exit(-1);
	}
}
