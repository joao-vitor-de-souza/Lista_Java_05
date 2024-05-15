package org.example.Licao02;


import java.util.InputMismatchException;
import java.util.Scanner;

public class MainPrincipal {

    public static void main(String[] args) { // CRIANDO OS INPUTS \\
        Scanner scanner = new Scanner(System.in);

        double salarioBruto = 0, descontoINSS, descontoIRPF, descontoPlanosaude, Horasextra, salarioLiquido;
        
        try {
            while (true) {
                System.out.println("Digite seu salário bruto: ");
                salarioBruto = scanner.nextDouble();
                if (!Validacao.validarEntradaSalario(salarioBruto)) {
                    continue;

                }
                break;
            }
            
        }catch (InputMismatchException e){
            System.err.println("Valor Inválido");
            scanner.next();
        }
        


        System.out.println("Digite suas horas extras: ");
        int horasExtras = scanner.nextInt();

        descontoINSS = Calculo.calcularDescontoINSS(salarioBruto);
        descontoIRPF = Calculo.calcularDescontoIRPF(salarioBruto);
        descontoPlanosaude = Calculo.calcularDescontoPlanoSaude(salarioBruto);
        Horasextra = Calculo.calcularHorasExtras(salarioBruto, horasExtras);
        salarioLiquido = Calculo.calcularSalarioLiquido(salarioBruto, descontoINSS, descontoIRPF, descontoPlanosaude, Horasextra);

        EntradaSaida.mostrarFolhaPagamento(salarioBruto, descontoINSS, descontoIRPF, descontoPlanosaude, Horasextra, salarioLiquido);


    }
}







