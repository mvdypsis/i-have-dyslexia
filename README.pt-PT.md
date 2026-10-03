<p align="center">
  <img src="assets/logo.svg" alt="i-have-dyslexia" width="120" />
</p>

<h1 align="center">i-have-dyslexia</h1>

<p align="center">
  <strong>As pessoas com dislexia passam a vida a encontrar outro caminho.<br/>Esta skill ensina o Claude a fazer o mesmo.</strong>
</p>

<p align="center">
  <a href="README.md">English</a> · <b>Português</b>
</p>

<p align="center">
  <img src="assets/demo.gif" alt="Demonstração de um dia de trabalho: um engenheiro bloqueado no CI recebe um palpite e uma verificação, uma conversa de 60 mensagens vira uma resposta, e um fundador a cortar custos desenha um mapa e encontra o nó." width="720">
</p>

<p align="center">
  <b>Não é preciso ter dislexia.</b> Se ficas bloqueado, isto também é para ti.
</p>

---

## Instalar numa frase

Cola isto no Claude Code, ou noutro agente de programação:

```text
Install the i-have-dyslexia skill/plugin from https://github.com/mvdypsis/i-have-dyslexia, refer to the repo's AGENTS.md for instructions.
```

Depois escreve **`/i-have-dyslexia setup`**. O Claude faz-te 5 perguntas, uma de cada vez, e fica a saber como gostas de trabalhar.

A partir daí, liga-se sozinho em cada sessão. Diz **"stop dyslexia mode"** para o pausar.

Também funciona na app do Claude, no Codex, no Gemini CLI e no Cursor: vê o [INSTALL.md](INSTALL.md), em inglês.

<p align="center">
  <a href="https://mvdypsis.github.io/i-have-dyslexia/"><b>🧭 Não sabes por onde começar? Encontra a tua estratégia em 10 segundos ➜</b></a>
</p>

---

## O que faz

### 1. O Claude pensa como quem tem dislexia

Muitas pessoas com dislexia veem o todo, pensam em imagens e encontram caminhos que os outros não veem.
Esta skill junta essas estratégias, partilhadas por pessoas com dislexia, livros e entrevistas públicas.
O Claude usa-as quando **qualquer pessoa** fica bloqueada.

### 2. O Claude trabalha como as pessoas com dislexia dizem que ajuda

- A resposta primeiro, sem paredes de texto.
- Nenhum comentário à ortografia.
- Ideias em imagens, e um passo de cada vez.

---

## Um dia normal de trabalho

<table>
<tr>
<th width="50%">Sem a skill</th>
<th width="50%">Com a skill</th>
</tr>
<tr><td colspan="2"><b>🧭 Product manager, 9h50, stand-up daqui a 10 minutos</b></td></tr>
<tr>
<td>

> **"Resume esta conversa de 60 mensagens no Slack sobre o erro no checkout"**
>
> A conversa começa com um relato do suporte, na segunda-feira, sobre falhas intermitentes no checkout, depois do qual vários engenheiros discutiram causas possíveis, incluindo uma alteração recente à integração com o fornecedor de pagamentos, enquanto a equipa de design levantou uma questão separada sobre o texto da mensagem de erro...

</td>
<td>

> **O checkout falha em cerca de 2% dos pagamentos com cartão desde segunda. A correção sai na quinta.**
>
> - Causa: o novo fornecedor de pagamentos desiste ao fim de 10 segundos.
> - A Ana trata da correção. O Rui muda a mensagem de erro.
>
> **Para ti:** pede ao suporte que ofereça PayPal até quinta.

</td>
</tr>
<tr><td colspan="2"><b>🛠️ Engenheiro, 16h00, duas horas no mesmo erro</b></td></tr>
<tr>
<td>

> **"Os testes passam no meu computador mas falham no CI e não sei porquê"**
>
> Aqui estão 10 causas comuns: 1. Variáveis de ambiente. 2. Versões diferentes do Node. 3. Fusos horários. 4. Ordem dos testes. 5. Cache. 6. Chamadas à rede. 7. Caminhos de ficheiros...

</td>
<td>

> Vamos tentar **Jump to the answer, then check**.
>
> Qual é o teu palpite: o ambiente, o tempo, ou a ordem em que os testes correm?
>
> Escolhe um, e eu dou-te o único comando que o prova.

</td>
</tr>
<tr><td colspan="2"><b>🎨 Designer, 11h00, um estudo de 30 páginas para ler</b></td></tr>
<tr>
<td>

> **"O que diz este estudo sobre o onboarding?"**
>
> O relatório apresenta as conclusões de 14 entrevistas feitas ao longo de três semanas. Os participantes descreveram experiências variadas, e surgiram vários temas nas sessões, incluindo incerteza, pressa e confiança...

</td>
<td>

> Vamos **Picture what you read**. Três imagens guardam o estudo:
>
> 1. 🧭 **Uma pessoa perdida num centro comercial:** os utilizadores não sabem em que passo estão.
> 2. ⏰ **Um telemóvel numa paragem de autocarro:** a maioria regista-se em menos de 2 minutos, em movimento.
> 3. 🔒 **Uma porta trancada:** pedir o cartão no passo 2 faz sair 6 em 14.
>
> Para qual queres desenhar primeiro?

</td>
</tr>
<tr><td colspan="2"><b>🚀 Fundador, 22h00, o update mensal aos investidores</b></td></tr>
<tr>
<td>

> **"corrige isto: fexamos 3 clientes novos este mes e a recieta cresceu 12%, o burn baixou, estamos a contartar um cto"**
>
> Aqui está a versão corrigida. Nota: "fexamos" escreve-se "fechámos", "recieta" escreve-se "receita", e "contartar" escreve-se "contratar"...

</td>
<td>

> **Update: setembro**
>
> Fechámos 3 clientes novos, e a receita cresceu 12%. O burn baixou. Estamos a contratar um CTO.
>
> Queres que junte os números numa tabela pequena?

</td>
</tr>
</table>

---

## 25 maneiras de pensar

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/strategy-map-dark.svg">
  <img src="assets/strategy-map-light.svg" alt="Mapa mental de 25 estratégias, agrupadas pelas seis competências do Dyslexic Thinking." width="100%">
</picture>

O Claude escolhe **uma** estratégia, diz qual é, e faz o primeiro passo **contigo**.

📥 [Descarrega o mapa em PNG](assets/strategy-map.png), para partilhar no LinkedIn, em apresentações ou numa conversa.

Algumas das estratégias:

| Estratégia | Numa linha |
|---|---|
| 🗺️ **Draw it as a map** | Põe o problema no meio, e encontra o nó. |
| 🎞️ **Explain it with a movie** | Explica uma situação com uma cena de filme que todos conhecem. |
| 📸 **Picture what you read** | Transforma o que lês em imagens, e lembra-te das imagens. |
| 🛤️ **Find another path** | Quando o caminho normal está bloqueado, encontra outros três. |
| 🏷️ **Name it, don't number it** | Dá nomes que se imaginam, não códigos. |
| 🎬 **Run the movie forward** | Imagina o futuro a acontecer, e vê onde se parte. |

Vêm de pessoas com dislexia que as partilharam, e dos [melhores pensadores e livros](READING-LIST.md).
Entre eles: Ingvar Kamprad, do IKEA, Richard Branson, Charles Schwab, a Nobel Carol Greider, John Irving e Jamie Oliver.
Cada fonte está ligada e foi verificada.

---

## No trabalho

As mesmas estratégias, nas palavras da tua profissão.
O Claude lê o guia do teu papel e fala a língua dele.

| Papel | Por exemplo |
|---|---|
| 🧭 **[Produto](skills/i-have-dyslexia/roles/product.md)** | A planear um lançamento? Run the movie forward: um pre-mortem. |
| 🛠️ **[Engenharia](skills/i-have-dyslexia/roles/engineering.md)** | Um bug que não encontras? Jump to the answer, then check: o teu palpite mais forte, e a linha de log que o prova. |
| 🎨 **[Design](skills/i-have-dyslexia/roles/design.md)** | Um fluxo que não está bem? Run the movie forward: percorre-o como o utilizador, ecrã a ecrã. |
| 🚀 **[Fundadores e líderes](skills/i-have-dyslexia/roles/leadership.md)** | Uma decisão difícil? Run the movie forward: imagina cada opção daqui a seis meses. |

No [site](https://mvdypsis.github.io/i-have-dyslexia/#role-product), escolhe o teu papel para ver cada momento e a estratégia certa.

---

## Partilha como pensas

Uma skill não treina o Claude. É um conjunto de instruções que o Claude lê e segue.
A forma de o ensinar é escrever como pensam as pessoas com dislexia.

1. Preenches um [formulário curto](https://github.com/mvdypsis/i-have-dyslexia/issues/new?template=share-a-strategy.yml): sem código, sem git. **A ortografia não interessa.**
2. Escrevemos a estratégia contigo, e tu confirmas as palavras.
3. Entra na biblioteca com o teu nome, e o Claude usa-a para ajudar a próxima pessoa.

Os formulários estão em inglês, mas podes escrever em português.

---

## Os princípios

As estratégias são o que fazes. Os princípios são o que te faz continuar.

Quando alguém falha, se sente lento, ou quer desistir, o Claude usa **um** destes, numa linha, e passa ao próximo passo. Sem sermões.

> **Começa pelo amor** · **Dá o teu melhor** · **Aprende a gostar do que fazes** · **Sê curioso** · **Aprende com os melhores** · **Disciplina e determinação** · **Nunca desistas** · **Equilíbrio**

Partilhados pelo fundador.

---

## Escrever em português e em inglês

- **A variante certa.** Português quer dizer Portugal, a não ser que digas Brasil.
- **A tua voz fica.** Uma mensagem rápida continua rápida.
- **Melhorar, se quiseres.** Pede, e o Claude mostra os teus 3 padrões mais comuns. Nunca uma lista de erros.

---

## Créditos

- As seis competências do **Dyslexic Thinking** são da [Made By Dyslexia](https://www.madebydyslexia.org/).
- A forma deste repositório inspira-se no [i-have-adhd](https://github.com/ayghri/i-have-adhd).
- Criado por [Miguel Vicente](https://github.com/mvdypsis), que tem dislexia. Os princípios, e as estratégias com o nome dele, são dele.

## Licença

[MIT](LICENSE). Usa, copia, muda, partilha.

<p align="center">
  ⭐ <b>Dá uma estrela se o Claude te ajudou a encontrar outro caminho.</b>
</p>
