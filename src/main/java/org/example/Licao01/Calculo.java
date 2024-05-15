package org.example.Licao01;

public class Calculo {



    public static double calcularMediaAritmetica(double nota1, double nota2) {
        // PUBLICO = PODE SER CHAMADO DE QUALQUER LUGAR DO PROGRAMA \\
        // STATIC = PODE SER CHAMDADO SEM CRIAR INSTACIA

        return (nota1 + nota2) / 2; // AQUI ELE PEGA 2 VALORES, SOMA ELES E DIVIDE POR 2 \\
    }

    public static double calcularMediaPonderada(double nota1, double nota2, double peso1, double peso2) {
        // PUBLICO = PODE SER CHAMADO DE QUALQUER LUGAR DO PROGRAMA \\
        // STATIC = PODE SER CHAMDADO SEM CRIAR INSTACIA

        return (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2); // AQUI ELE FAZ OS CALCULOS\\
    }
}

