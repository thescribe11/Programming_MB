import java.util.Scanner;

public class FTC_New {
	public static final  double  LOW_TEMP_F_WARNING = 0.;
	public static final  double  HIGH_TEMP_F_WARNING = 100.;
	public static final  int     MAX_LOOP = 5;

	public static void main(String[] args) {
		double Farenheit = 0.;
		double Celsius = 0.;
		double Kelvin = 0.;
		Scanner sc = new Scanner(System.in);

		for (int i=0; i<MAX_LOOP; i++) {
			System.out.print("Enter a temperature (F): ");
			if (sc.hasNextDouble())
			{
				Farenheit = sc.nextDouble();
				Celsius = ( Farenheit - 32.) * 5./9.;
				Kelvin = GetKelvin(Farenheit);
				System.out.printf("\nThat is equivalent to %.2f degrees Celsius.\n", Celsius);
				System.out.printf("It is also equal to %.3f degrees Kelvin.\n", Kelvin);
			} else {
				System.out.println("[!] Data entry error!");
				System.exit(-1);
			}

			if (Farenheit > HIGH_TEMP_F_WARNING) {
				System.out.println("Remember to hydrate!\n");
			} else if (Farenheit < LOW_TEMP_F_WARNING) {
				System.out.println("Remember to pack long underwear!\n");
			} else {
				System.out.println("");
			}
		}
		System.exit(-1);
	}

	public static double GetKelvin (double Farenheit) {
		double numerator = (Farenheit-32) * 5;
		double denominator = 9;
		double result = numerator / denominator;
		
		return result + 273.15;
	}
}
