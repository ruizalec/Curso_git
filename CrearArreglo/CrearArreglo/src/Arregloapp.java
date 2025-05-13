

public class Arregloapp {
    public static void main(String[] args) throws Exception {
      try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
          System.out.println("Ingrese el inicio del rango: ");
          int inicio = Integer.parseInt(scanner.nextLine());
          System.out.println("Ingrese el fin del rango: ");
          int fin = Integer.parseInt(scanner.nextLine());
          int[] arreglo = java.util.stream.IntStream.range(inicio, fin).toArray();
            System.out.println("Arreglo creado: " + java.util.Arrays.toString(arreglo));
      }
    }
}
