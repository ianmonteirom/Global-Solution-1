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
      } else {
        digitalWrite(LEDG, LOW);
        digitalWrite(LEDR, HIGH);

        lcd.clear();
        lcd.setCursor(6, 0);
        lcd.print("AREA");
        lcd.setCursor(4, 1);
        lcd.print("PROIBIDA");
        tone(buzzerPin, 2000, 10000);
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
