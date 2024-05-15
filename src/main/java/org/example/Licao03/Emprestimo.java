package org.example.Licao03;



public class Emprestimo {
    public static double calcularValorEmprestimo(double salario, double valorSolicitado) {
        double valorTotal = valorSolicitado * 1.35; // Valor total do empréstimo com 35% de juros
        return valorTotal;
    }

    public static double calcularValorParcela(double valorEmprestimo) {
        double valorParcela = valorEmprestimo / 24; // Valor da parcela mensal em 24 meses
        return valorParcela;
    }

    public static boolean verificarEmprestimo(double salario, double valorParcela) {
        double limiteParcela = salario * 0.15; // Limite de 15% do salário para a parcela
        return valorParcela <= limiteParcela;
    }

    public static void exibirResultado(double salario, double valorSolicitado, double valorEmprestimo, double valorParcela) {
        System.out.println("Valor total do empréstimo: R$" + valorEmprestimo);
        System.out.println("Valor de cada parcela (24 meses): R$" + valorParcela);
        System.out.println("Valor total a ser pago: R$" + (valorEmprestimo + (valorEmprestimo * 0.35)));
    }
}

