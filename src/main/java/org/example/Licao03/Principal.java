package org.example.Licao03;



import java.util.Scanner;


public class Principal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o salário atual: ");
        double salario = scanner.nextDouble();

        System.out.print("Digite o valor que deseja emprestar: ");
        double valorSolicitado = scanner.nextDouble();

        double valorEmprestimo = Emprestimo.calcularValorEmprestimo(salario, valorSolicitado);
        double valorParcela = Emprestimo.calcularValorParcela(valorEmprestimo);

        if (Emprestimo.verificarEmprestimo(salario, valorParcela) && valorSolicitado <= 200000) {
            Emprestimo.exibirResultado(salario, valorSolicitado, valorEmprestimo, valorParcela);
        } else {
            System.out.println("Empréstimo não pode ser realizado.");
        }

        scanner.close();
    }
}