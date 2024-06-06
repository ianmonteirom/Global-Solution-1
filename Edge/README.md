# 🤖 Global Solution Maio/Junho 2024 - Edge Computing
![image](https://github.com/ianmonteirom/Global-Solution-1/assets/152393807/21448e81-a0eb-425a-a421-b7b24ae61abc)

## 💻 Desenvolvido Por
- Nome: Ian Monteiro Moreira
- RM: 558652
- Turma: 1ESPH

## 🌊 O Cliente
![image](https://github.com/ianmonteirom/Global-Solution-1/assets/152393807/8e473de9-45aa-4970-a181-5a4522750a57)
A Global Solution de 2024 trouxe o grupo Oceans 20, ou O20, um grupo de engajamento da sociedade civil focado nos oceanos criado pelo G20, grupo formado pelos 20 países mais ricos do mundo.

## 🤔 O Problema que nos foi passado
Os oceanos estão sofrendo com a exploração desenfreada do ser humano, com toneladas de lixo sendo depositadas todos os dias, poluição de substâncias tóxicas, pesca desenfreada, e outros problemas. Nós devemos criar soluções inteligentes para ao menos tentar amenizar esses problemas.

## ✅ A Solução pensada
Resolvi focar no problema da superexploração da pesca, que causa desequilíbrios alarmantes na vida marítima e na sua cadeia alimentar, podendo até mesmo causar a extinção de espécies de peixes.
- Para isso, pensei no desenvolvimento de um sistema que será utilizado por pescadores e funcionários do Ministério da Pesca e da Agricultura, responsáveis pela regulamentação da pesca, apelidado como "Fish Track". O Fish Track contará com as funcionalidades:
  - Registro dos pescadores com a geração de um ID único para cada um.
  - Relatórios diários de pesca dos pescadores, com a quantidade de peixes pescados por espécie
  - Registro e visualização de áreas de pesca no sistema, com seu status (Liberada ou Proibida para pesca)
  - Registro e visualização de espécies de peixes no sistema, com seu status (Liberada para pesca ou em Risco/Ameaça)
- O sistema auxiliará na organização de ambos os lados, para mantê-los sempre atualizados com as áreas e espécies liberadas e proibidas para pesca, para ajudar os pescadores a pescarem de acordo com a lei, e para auxiliar os funcionários do governo a multar corretamente.

## 💡 Agregando Edge Computing à Solução Pensada
![image](https://github.com/ianmonteirom/Global-Solution-1/assets/152393807/8d6108de-7b26-4b04-8f93-05a417c50603)
- Para tornar o sistema mais completo, desenvolvi um projeto em Arduino que terá na sua versão completa um GPS imbutido, captando as coordenadas de onde os pescadores estarão localizados, e retornando em um display se a área está liberada ou proibida, além disso, caso a área for proibida, o led vermelho do protótipo acenderá e a buzina começará a apitar, para facilitar o entendimento de que é uma área proibida. Caso seja uma área liberada, o led verde do protótipo acenderá.
![image](https://github.com/ianmonteirom/Global-Solution-1/assets/152393807/f0266143-98d1-403a-94f7-76ff1e283f58)

- Neste protótipo, o usuário digita a Latitude e Longitude da área manualmente no Serial: 
![image](https://github.com/ianmonteirom/Global-Solution-1/assets/152393807/c491b922-39cc-41fe-b2ac-ca3ff41774f6)
- As perguntas de Latitude e Longitude também aparecem no display:
![image](https://github.com/ianmonteirom/Global-Solution-1/assets/152393807/3933b410-dbe2-47d0-8c10-08ee010e0f3c)
![image](https://github.com/ianmonteirom/Global-Solution-1/assets/152393807/f4db9108-fcbb-4919-8755-b89602b2da3e)
- Caso a área seja liberada, o Display mostra e o Led Verde acende:
![image](https://github.com/ianmonteirom/Global-Solution-1/assets/152393807/db4e9048-1b65-40d8-b8c1-17244793e98f)
- Caso a área esteja proibida, o Display mostra e o Led Vermelho acende, além de a buzina apitar: 
![image](https://github.com/ianmonteirom/Global-Solution-1/assets/152393807/109c3ba7-8b3f-4e76-b9c8-7e0e40137e28)
- Neste protótipo, é escolhido aleatoriamente se a área é proibida ou liberada, entretanto em um projeto em seu estágio final ele teria um GPS imbutido captando coordenadas reais de onde o pescador está, e também um banco de dados com as áreas registradas, seu status (liberada ou proibida) e suas coordenadas reais, assim o projeto conseguirá de fato auxiliar os usuários.

## 🛠️ Link para o Projeto Desenvolvido no Wokwi
- https://wokwi.com/projects/399890970001703937

## 📝 Lista de Materiais
- x1 Microcontrolador Arduino Uno;
- x1 Breadboard;
- x1 Display LCD 16x2 (I2C);
- x1 Buzzer (Buzina);
- x1 Led Vermelho;
- x1 Led Verde;
- x2 Resistores de 220Ω;
- x8 Cabos Jumper;

## 👨🏻‍💻 O Código do Projeto 
#include <LiquidCrystal_I2C.h>

#define LEDR 7
#define LEDG 8
#define buzzerPin 2

String inputString = "";         // String para armazenar a entrada
boolean stringComplete = false;  // Indicador de quando a entrada está completa
int latitude = 0;                // Variável para armazenar a latitude
int longitude = 0;
int aleatorio = 0;               
boolean askingForLatitude = true;  // Indicador para saber se estamos perguntando pela latitude

LiquidCrystal_I2C lcd(0x27, 16, 2); // Endereço de acesso: 0x3F ou 0x27

void setup() {
  // Inicialize a comunicação serial para depuração
  Serial.begin(9600);
  randomSeed(analogRead(0));
  pinMode(LEDR, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  lcd.init();   // Inicialização do LCD
  lcd.backlight();  // Ligando o backlight do LCD

  // Solicita a latitude inicialmente
  Serial.println("----- Fish Track - Leitura de Áreas de Pesca -----");
  Serial.println("Digite as coordenadas da área de pesca ");

  lcd.clear();
  lcd.setCursor(3, 0);
  lcd.print("Fish Track");
  lcd.setCursor(0, 1);
  lcd.print("Leitura de Areas");

  delay(5000);

  solicitarLatitude();
}

void loop() {
  digitalWrite(LEDG, LOW);
  digitalWrite(LEDR, LOW);
  // Checa se a string está completa
  if (stringComplete) {
    if (askingForLatitude) {
      // Converte a string em um inteiro e armazena na latitude
      latitude = inputString.toInt();
      
      // Exibe a latitude lida
      Serial.print("Latitude digitada: ");
      Serial.println(latitude);
      Serial.println("");
      
      // Solicita a longitude ao usuário
      solicitarLongitude();
      
      // Indica que a próxima entrada será a longitude
      askingForLatitude = false;
    } else {
      // Converte a string em um inteiro e armazena na longitude
      longitude = inputString.toInt();
      
      // Exibe a longitude lida
      Serial.print("Longitude digitada: ");
      Serial.println(longitude);

      // Mostra se a área está liberada ou bloqueada
      aleatorio = random(0, 2);
      if (aleatorio == 0) {
        digitalWrite(LEDG, HIGH);
        digitalWrite(LEDR, LOW);

        lcd.clear();
        lcd.setCursor(6, 0);
        lcd.print("AREA");
        lcd.setCursor(4, 1);
        lcd.print("LIBERADA");
        Serial.println("ÁREA LIBERADA");
      } else {
        digitalWrite(LEDG, LOW);
        digitalWrite(LEDR, HIGH);

        lcd.clear();
        lcd.setCursor(6, 0);
        lcd.print("AREA");
        lcd.setCursor(4, 1);
        lcd.print("PROIBIDA");
        Serial.println("ÁREA PROIBIDA");
        tone(buzzerPin, 2000, 7500);
      }

      // Pausa para que o usuário veja o resultado
      delay(7500);

      // Solicita a latitude novamente para nova entrada
      solicitarLatitude();
      
      // Indica que a próxima entrada será a latitude
      askingForLatitude = true;
    }

    // Limpa a string e redefine o indicador
    inputString = "";
    stringComplete = false;
  }
}

void solicitarLatitude() {
  Serial.println("");
  Serial.println("Digite a latitude e pressione Enter:");
  lcd.clear();
  lcd.setCursor(4, 0);
  lcd.print("Digite a");
  lcd.setCursor(4, 1);
  lcd.print("Latitude");
}

void solicitarLongitude() {
  Serial.println("Digite a longitude e pressione Enter:");
  lcd.clear();
  lcd.setCursor(4, 0);
  lcd.print("Digite a");
  lcd.setCursor(4, 1);
  lcd.print("Longitude");
}

// Esta função é chamada sempre que novos dados chegam na porta serial
void serialEvent() {
  while (Serial.available()) {
    // Obtenha o byte que chega
    char inChar = (char)Serial.read();
    
    // Adiciona o caractere à string de entrada
    inputString += inChar;
    
    // Verifica se a entrada está completa (Enter pressionado)
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}


