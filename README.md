# Documentação do Cluster MongoDB para Sistema de Gerenciamento de Estoque

## Contexto

Este cluster foi projetado para um sistema de gerenciamento de estoque destinado a uma cadeia de supermercados com filiais em várias cidades. O sistema é crucial para o controle eficiente de um grande volume de produtos em estoque em cada filial.

## Requisitos do Sistema

- **Capacidade de Gerenciamento:** O sistema deve ser capaz de lidar com milhões de registros de produtos.
- **Performance:** As consultas de estoque e atualizações de inventário devem ser rápidas e eficientes para não impactar as operações diárias das filiais.
- **Escalabilidade:** O design do sistema deve acomodar a adição de novas filiais sem a necessidade de uma reestruturação significativa, garantindo facilidade e agilidade na expansão.

## Configuração do Cluster

### 1. Propósito do Cluster

O cluster é dedicado ao gerenciamento de estoque para suportar as operações logísticas de todas as filiais, permitindo um controle centralizado e eficiente dos produtos.

### 2. Escolha dos Componentes

A seleção dos componentes do MongoDB foi influenciada pelo alto volume de acessos, tanto de leitura quanto de escrita, que o banco de dados deverá suportar, garantindo performance sob demanda intensiva.

### 3. Acesso Intensivo e Desempenho

As configurações do cluster são direcionadas para suportar o alto volume de operações nas cinco filiais, garantindo que operações de leitura e escrita sejam executadas sem latências que impactem o fluxo de trabalho.

### 4. Escalabilidade Horizontal

Inicialmente projetado para cinco filiais, o cluster possui capacidade de expansão horizontal. Isso permite a integração de novas filiais ao sistema de maneira eficiente, sem a necessidade de alterações significativas na infraestrutura existente.

### 5. Roteadores

O cluster inclui três roteadores para otimizar o tráfego de solicitações, proporcionar alta disponibilidade e escalabilidade. Essa estrutura suporta a distribuição equitativa da carga e a continuidade dos serviços mesmo com variações significativas de demanda entre as filiais.

### 6. Config Servers

Com três Config Servers, o cluster assegura alta disponibilidade e consistência dos metadados. Essa redundância fortalece a resiliência do sistema contra falhas, mantendo a integridade dos dados constantemente sincronizada e segura.

### 7. Shards

A implementação de três Shards com redundância de dados visa maximizar o desempenho e a disponibilidade. Essa configuração permite a execução de mais transações simultâneas, melhorando a eficiência das consultas e atualizações de inventário em tempo real.

## Conclusão

O design do cluster MongoDB foi meticulosamente planejado para atender às necessidades específicas do sistema de gerenciamento de estoque da cadeia de supermercados. A estrutura atual não só cumpre os requisitos atuais de desempenho e escalabilidade mas também está preparada para acomodar o crescimento futuro, garantindo a continuidade e a eficiência das operações comerciais.

## Relatório de Testes

### Metodologia dos Testes

Os testes foram realizados utilizando a técnica de multi-threading, empregando os três roteadores configurados no cluster para inserção de dados. Este método visou simular um ambiente de alta demanda e verificar a capacidade de resposta do sistema sob diferentes volumes de carga. Todos os testes foram conduzidos utilizando operações de inserção (`insert`) no banco de dados.

### Configuração do Ambiente de Testes

Os testes foram executados em um ambiente Docker configurado na seguinte máquina host:

- **Processador:** Intel Core i5-13600K
- **Memória:** 32GB (2x16GB), DDR5, 6800MHz
- **Placa Mãe:** AsRock B760M PRO RS, DDR5
- **GPU:** RTX 4070
- **SSD:** M.2 NVMe, Leitura: 7400MB/s

### Resultados dos Testes

- **Teste 1:**
  - **Volume de Dados:** 20.000 linhas
  - **Tempo Médio de Execução:** 0.446 segundos

- **Teste 2:**
  - **Volume de Dados:** 6.000.000 linhas
  - **Tempo Médio de Execução:** 70.569 segundos

- **Teste 3:**
  - **Volume de Dados:** 8.000.000 linhas
  - **Tempo Médio de Execução:** 326.939 segundos

### Observações

Foi observada uma perda de desempenho significativa a partir do Teste 2, onde os tempos de inserção aumentaram drasticamente com o incremento no volume de dados. Essa degradação do desempenho torna-se evidente com a inserção simultânea de 6.000.000 de linhas, sugerindo uma possível saturação dos recursos disponíveis nos roteadores. É recomendável uma análise detalhada para determinar se essa perda de desempenho é aceitável para os requisitos operacionais e de negócios da cadeia de supermercados.

## Conclusão

Os resultados indicam que o cluster MongoDB atende aos requisitos de desempenho para operações de baixo e médio volume de dados com eficiência. No entanto, para altos volumes de inserção, como observado nos Testes 2 e 3, é crucial considerar ajustes na configuração ou na arquitetura para manter a performance desejada. Estes resultados fornecem uma base sólida para futuras otimizações e escalonamentos do sistema.


<img src="Images/cluster mongodb.png">
