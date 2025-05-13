public class IMCcalculator {
    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Ingrese su peso(kg): ");
            double peso = scanner.nextDouble();

            System.out.print("Ingrese su altura(mts): ");
            double altura = scanner.nextDouble();

            // Calcular IMC
            double imc = peso / (altura * altura);

            // Imprimir el resultado
            System.out.println("Su Indice de Masa Corporal es: " + imc);

            // Clasificar el IMC
            if (imc < 18.5) {
                System.out.println("Estado: Peso bajo");
            } else if (imc >= 18.5 && imc < 25) {
                System.out.println("Estado: Peso normal");
            } else if (imc >= 25 && imc < 30) {
                System.out.println("Estado: Sobrepeso");
            } else if (imc >= 30 && imc < 35) {
                System.out.println("Estado: Obesidad grado 1");
            } else if (imc >= 35 && imc < 40) {
                System.out.println("Estado: Obesidad grado 2");
            } else {
                System.out.println("Estado: Obesidad grado 3");
            }

            scanner.close();
        }
    }