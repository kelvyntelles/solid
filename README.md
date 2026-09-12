# 💎 Princípios SOLID

Este repositório contém uma explicação prática e direta sobre os princípios **SOLID**, um conjunto de cinco diretrizes de design de software para a Programação Orientada a Objetos (POO). Esses princípios ajudam a criar códigos mais limpos, fáceis de testar, manter e expandir.

---

## 🚀 Os 5 Princípios

| Letra | Princípio | Descrição Prática |
| :---: | :--- | :--- |
| **S** | **Single Responsibility**<br>*(Responsabilidade Única)* | Uma classe deve ter apenas um motivo para mudar (uma única função). |
| **O** | **Open-Closed**<br>*(Aberto-Fechado)* | O código deve ser aberto para extensão, mas fechado para modificação. |
| **L** | **Liskov Substitution**<br>*(Substituição de Liskov)* | Classes filhas devem poder substituir suas classes mães sem quebrar o código. |
| **I** | **Interface Segregation**<br>*(Segregação de Interface)* | É melhor ter várias interfaces específicas do que uma genérica cheia de métodos inúteis. |
| **D** | **Dependency Inversion**<br>*(Inversão de Dependência)* | Dependa de abstrações (interfaces/classes abstratas), não de implementações concretas. |

---

## 🔍 Detalhando cada Princípio

### 🟢 S — Single Responsibility Principle (SRP)
> *"Uma classe deve ter um, e apenas um, motivo para mudar."*
* **Problema:** Classes "Deus" (God Classes) que fazem tudo (ex: salvam no banco, enviam e-mail e processam pagamento).
* **Solução:** Dividir as responsabilidades em classes menores e focadas.

### 🔵 O — Open-Closed Principle (OCP)
> *"Entidades de software devem ser abertas para extensão, mas fechadas para modificação."*
* **Problema:** Toda vez que surge uma nova regra de negócio, você precisa alterar um código que já funciona.
* **Solução:** Usar herança ou interfaces para que novos comportamentos sejam adicionados criando novas classes.

### 🟡 L — Liskov Substitution Principle (LSP)
> *"Classes derivadas devem ser capazes de substituir totalmente suas classes base."*
* **Problema:** Uma classe filha herda de uma classe mãe, mas joga uma exceção `NotImplementedException` em algum método.
* **Solução:** Se a classe filha não consegue fazer tudo o que a mãe faz, a modelagem está errada.

### 🟣 I — Interface Segregation Principle (ISP)
> *"Uma classe não deve ser forçada a depender de métodos que não utiliza."*
* **Problema:** Criar uma interface gigante que obriga uma classe simples a implementar métodos vazios.
* **Solução:** Criar interfaces menores, mais específicas e modulares.

### 🟠 D — Dependency Inversion Principle (DIP)
> *"Dependa de abstrações e não de implementações."*
* **Problema:** Uma classe de alto nível cria diretamente uma instância de uma classe de baixo nível (alto acoplamento).
* **Solução:** Injetar a dependência através de uma interface, permitindo trocar a implementação facilmente (ex: mudar o banco de dados sem alterar a lógica principal).
