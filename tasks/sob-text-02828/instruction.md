Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Juan Carlos Ferrero: Juan Carlos Ferrero Donat (] ; born 12 February 1980) is a retired professional tennis player, and a former world No. 1 player, from Spain.  He captured the men's singles title at the 2003 French Open, and in September of that year, became the 21st player to hold the world No. 1 ranking.  He was also the runner-up at the 2002 French Open and the 2003 US Open.  His nickname is "Mosquito" due to his speed and his slight physical build.  Ferrero retired from the game after the 2012 Valencia Open 500.

Janko Tipsarević: Janko Tipsarević (, ] ; born 22 June 1984) is a Serbian professional tennis player.  His career-high singles ranking is world No. 8, achieved on 2 April 2012.  In his career, he has won four ATP World Tour titles, one ATP doubles title, three Futures, and 15 Challenger titles.  Tipsarević also won the 2001 Australian Open Junior title.  Tipsarević has achieved two victories over a World No. 1 player, having defeated compatriot Novak Djokovic twice.  He also has thirteen victories against other players in the top 10: four wins against Tomáš Berdych, and one each against Fernando González, Mikhail Youzhny, David Ferrer, James Blake, Gaël Monfils, Andy Murray and Juan Mónaco.  He holds victories over former World No. 1 players Carlos Moyá, Marat Safin, Lleyton Hewitt, Juan Carlos Ferrero and Andy Roddick.  His best results at a Grand Slam have been reaching the quarterfinals at the US Open in 2011 and 2012.  He is only the second Serb to reach the final 16 at all four different grand slams.

2016 China Open – Men's Doubles: Vasek Pospisil and Jack Sock were the defending champions, but Pospisil chose to play in Tokyo instead.  Sock played alongside Bernard Tomic but lost in the final to Pablo Carreño Busta and Rafael Nadal, who won 6−7, 6−2, [10−8].

2017 Kunal Patel San Francisco Open – Singles: Zhang Ze won the title after defeating Vasek Pospisil 7–5, 3–6, 6–2 in the final.

2017 ABN AMRO World Tennis Tournament – Doubles: Nicolas Mahut and Vasek Pospisil were the defending champions, but Pospisil chose not to participate this year.  Mahut played alongside Pierre-Hugues Herbert, but lost in the semifinals to Ivan Dodig and Marcel Granollers.

2016 BNP Paribas Open – Men's Doubles: Vasek Pospisil and Jack Sock were the defending champions, but lost in the final to Pierre-Hugues Herbert and Nicolas Mahut, 3–6, 6–7.

2010 Abierto Mexicano Telcel – Men's Singles: Nicolás Almagro was the defending champion; however, he lost 1–6, 7–5, 2–6 to Juan Carlos Ferrero in the quarterfinals. David Ferrer won in the final 6–3, 3–6, 6–1 against Juan Carlos Ferrero.

Vasek Pospisil: Vasek Pospisil (, ] ; born June 23, 1990) is a Canadian professional tennis player.  He is the No. 3 male ranked player in Canada, after Milos Raonic and Denis Shapovalov.  Pospisil has a career-high World singles ranking of 25, and No. 4 in doubles.  As Canada's currently ranked No. 3 in singles and No. 3 in doubles, he is an important member of the Canada Davis Cup team.  Along with partner Jack Sock, he won the 2014 Wimbledon Championships and the 2015 Indian Wells Masters men's doubles titles.  He also reached the quarterfinals in singles at the 2015 Wimbledon Championships.

2011 Jalisco Open – Doubles: Vasek Pospisil and Bobby Reynolds won the first edition of this tournament, beating Pierre-Ludovic Duclos and Ivo Klec 6–4, 6–7(6), [10–6] in the final.

2015 Swiss Indoors – Doubles: Vasek Pospisil and Nenad Zimonjić were the defending champions, but Pospisil decided not to participate.  Zimonjić plays alongside Marcin Matkowski but lost to Alexander Peya and Bruno Soares in the quarterfinals.

Question: Juan Carlos Ferrero and Vasek Pospisil, have which mutual occupation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_one": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "player_two": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "mutual_occupation": {
      "type": "string",
      "description": "The shared occupation of both players."
    }
  },
  "required": [
    "player_one",
    "player_two",
    "mutual_occupation"
  ],
  "additionalProperties": false
}
