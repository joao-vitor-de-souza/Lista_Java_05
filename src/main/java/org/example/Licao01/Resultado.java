package org.example.Licao01;
public class Resultado {

    public static void verificarAprovacao(double media) {

        // PUBLICO = PODE SER CHAMADO DE QUALQUER LUGAR DO PROGRAMA \\
        // STATIC = PODE SER CHAMDADO SEM CRIAR INSTACIA
        // VOID = O METODO NÃO RETORNA NENHUM VALOR



        if (media >= 7) { // SE A NOTA FOR MAIOR QUE 7
            System.out.println("Aluno aprovado!"); // PRINTE "Aluno aprovado!"


        } else { // SE NÃO
            System.out.println("Aluno reprovado."); // PRINTE 'Aluno reprovado'


        }




    }
}