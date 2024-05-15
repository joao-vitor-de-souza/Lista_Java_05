package org.example.Licao02;

class Calculo {
    public static double calcularDescontoINSS(double salarioBruto) {
        return salarioBruto * 0.20;
    }

    public static double calcularDescontoIRPF(double salario) {
        return salario * 0.10;
    }

    public static double calcularDescontoPlanoSaude(double salarioBruto) {
        return salarioBruto * 0.05;
    }

    public static double calcularHorasExtras(double salarioBruto, int horasExtras) {
        double valorHoraNormal = salarioBruto / 160;
        double valorHoraExtra = valorHoraNormal * 1.5;
        return horasExtras * valorHoraExtra;
    }

    public static double calcularSalarioLiquido(double salarioBruto, double descontoINSS, double descontoIRPF, double descontoPlanoSaude, double acrescimoHorasExtras) {

        return salarioBruto - descontoINSS - descontoIRPF - descontoPlanoSaude + acrescimoHorasExtras;
    }
}