package org.example.Licao01;

public class Validacao {

    public static boolean validarNota(double nota) { // RECEBE O PARAMETRO DO TIPO DOUBLE CHAMADO ' NOTA '

        return nota >= 0 && nota <= 10; // VENDO SE NOTA É MAIOR QUE 0 E SE NOTA É MENOR QUE 10
    }
}

