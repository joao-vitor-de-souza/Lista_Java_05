package org.example.Licao01;

import java.util.Scanner;
public class EntradaSaida {


    public static double pedirNota(Scanner scanner, String ordem) {

        double nota;  // AQUI IREMOS GUARDAR A NOTA SOLICITDA PELO USUARIO


        // EXECUTANDO UM LOOP NO WHILE
        do {
            System.out.println("Digite a " + ordem + " nota:"); // APENAS PRINTANDO NO CONSOLE ESSA MENSAGEM
            nota = scanner.nextDouble(); // ELE LÊ O VALOR DIGITADO E ARMAZENA NA VARIAVEL NOTA


        } while (!Validacao.validarNota(nota)); // FAZ A VALIDACAO DA NOTA
        return nota; // RETORNA A NOTA JA VALIDADA.
    }
    public static double pedirPeso(Scanner scanner, String ordem) { // ELE RECEBE: Scanner scanner,String ordem E RETORNA COMO DOUBLE

        System.out.println("Digite o peso da " + ordem + " nota:"); // SOLICITA O USUARIO PARA DIGITAR OVALOR DA NOTA
        return scanner.nextDouble(); // LE O VALOR DIGITADO E RETORNA O VALOR
    }
}