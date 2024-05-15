package org.example.Licao01;
// IMPORTANDO CLASSE SCANNER PARA A INTERAÇÃO DO USUARIO
import java.util.Scanner;

public class MainPrincipal {


    public static void main(String[] args) { // CRIANDO OS INPUTS \\
        Scanner scanner = new Scanner(System.in);


        System.out.println("Informe as duas notas do aluno:");// ESCREVEMOS PRINTLN PARA MOSTRAR ALGUM TEXTO\\



        // UTILIZAMOS O DOUBLE PARA ARMAZENARMOS ALGUM NUMERO \\
        double nota1 = EntradaSaida.pedirNota(scanner, "primeira");
        double nota2 = EntradaSaida.pedirNota(scanner, "segunda");



        System.out.println("Qual média deseja calcular? (Digite 'A' para aritmética ou 'P' para ponderada):"); // EXPICACAO LINHA 12 \\
        String opcao = scanner.next(); //SIMPLIFICANDO... ELE PULA PRA PARTE LOGICA \\

        // LOGICA \\

        double media; // CRIAMOS UMA VARIAVEL COM NOME 'MEDIA'


        // 'opcao' nome da variavel. 'equalsIgnoreCase' faz com que a resposta seja maiuscula ou minuscula\\
        if (opcao.equalsIgnoreCase("A")) {

            media = Calculo.calcularMediaAritmetica(nota1, nota2);
            // 'media' aqui iremos armazenar resultado do calculo aritmetica
            // 'Calculo' nome da classe
            // 'calcularMediaAritmetica(nota1, nota2)' ele faz o calculo



        } else if (opcao.equalsIgnoreCase("P")) { // explicacao linha 30 \\


            // CRIANDO AS VARIAVEIS \\

            double peso1 = EntradaSaida.pedirPeso(scanner, "primeira"); // PEDIMOS QUE ELE VA EM ENTRADA E EXECUTE O 'PedirPeso' \\
            double peso2 = EntradaSaida.pedirPeso(scanner, "segunda"); // /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\



            media = Calculo.calcularMediaPonderada(nota1, nota2, peso1, peso2);  // 'calcularMediaAritmetica(nota1, nota2)' ele faz Calular Ponderada


        } else {
            System.out.println("Opção inválida. Encerrando o programa."); // se user digitar algo errado ele encerra o programa
            return;
        }


        System.out.println("A média do aluno é: " + media); // EXIBE NO CONSOLE A MEDIA DO ALUNO

        Resultado.verificarAprovacao(media); // AQUI MOSTRA SE ELE FOI APROVADO OU REPROVADO


    }
}