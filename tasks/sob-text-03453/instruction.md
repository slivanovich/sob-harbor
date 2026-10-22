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
1967 Blue Swords: The 1967 Blue Swords (German: Pokal der Blauen Schwerter ) was an international senior-level figure skating competition organized in Karl-Marx-Stadt, East Germany.  Medals were awarded in the disciplines of men's singles, ladies' singles, pair skating and ice dancing.  East Germany's Günter Zöller outscored the Soviet Union's Vladimir Kurenbin for gold in the man's category.  East Germans swept the ladies' podium, led by Beate Richter, who won her first gold medal at the event after three previous podium results.  Soviet ice dancers Lyudmila Pakhomova / Aleksandr Gorshkov defeated the defending champions, Annerose Baier / Eberhard Rüger of East Germany, who had beaten them a year earlier.

Alexei Soloviev: Alexei Soloviev (Russian: Алексей Соловьёв ) is a Soviet former ice dancer.  He is a two-time (1980, 1981) World Junior champion with partner Elena Batanova.  On the senior level, they won the 1982 NHK Trophy and 1984 Soviet national title.  They were coached by Lyudmila Pakhomova and later Tatiana Tarasova.

1970 Prize of Moscow News: The 1970 Prize of Moscow News was the fifth edition of an international figure skating competition organized in Moscow, Soviet Union.  It was held December 17–20, 1970.  Medals were awarded in the disciplines of men's singles, ladies' singles, pair skating and ice dancing.  Soviets swept the men's podium, with Sergei Chetverukhin defeating Sergey Volkov for the title.  Marina Titova took the ladies' title ahead of skaters from East and West Germany.  Lyudmila Smirnova / Andrei Suraikin won the pairs title ahead of Olympic champions Ludmila Belousova / Oleg Protopopov.  Soviets also swept the ice dancing podium, led by World champions Lyudmila Pakhomova / Alexander Gorshkov.

1966 Blue Swords: The 1966 Blue Swords (German: Pokal der Blauen Schwerter ) was an international senior-level figure skating competition organized in Karl-Marx-Stadt, East Germany.  Medals were awarded in the disciplines of men's singles, ladies' singles, pair skating and ice dancing.  East German national champion Günter Zöller won the first of his four consecutive Blue Swords titles, defeating Czechoslovakia's Marian Filc and West Germany's Reinhard Ketterer.  East Germans swept the ladies' and pairs' podiums, led by Gabriele Seyfert, who won her fourth straight gold medal at the event, and Heidemarie Steiner / Heinz-Ulrich Walther.  Annerose Baier / Eberhard Rüger won gold ahead of the Soviet Union's Lyudmila Pakhomova / Aleksandr Gorshkov and British duo Susan Getty / Roy Bradshaw.

1968 Blue Swords: The 1968 Blue Swords (German: Pokal der Blauen Schwerter ) was an international senior-level figure skating competition organized in Karl-Marx-Stadt, East Germany.  Medals were awarded in the disciplines of men's singles, ladies' singles, pair skating and ice dancing.  East Germany's Günter Zöller won his third consecutive title by defeating the Soviet Union's Valeri Meshkov and Vladimir Kurenbin.  His teammate, Sonja Morgenstern, won her first Blue Swords title, outscoring Austria's Eva Kriegelstein.  The Soviet Union's Lyudmila Pakhomova / Aleksandr Gorshkov won the ice dancing title for the second year in a row.

Viktor Ryzhkin: Viktor Ivanovich Ryzhkin (Russian: Виктор Иванович Рыжкин ; born 26 April 1937 in Moscow) is a former ice dancer who competed for the Soviet Union.  With Lyudmila Pakhomova, whom he had initially coached, he won three Soviet national titles and placed 10th at the 1966 World Championships.  Their partnership ended in 1966.  With his next partner Irina Grishkova, Ryzhkin finished 4th at the 1968 European Championships and 5th at the 1968 World Championships.  They won gold medals at the 1967 Prague Skate and twice at the Prize of Moscow News.

1972 Prize of Moscow News: The 1972 Prize of Moscow News was the seventh edition of an international figure skating competition organized in Moscow, Soviet Union.  It was held December 9–13, 1972.  Medals were awarded in the disciplines of men's singles, ladies' singles, pair skating and ice dancing.  Sergei Chetverukhin won the men's title for the third consecutive year.  Canada's Cathy Lee Irwin took the ladies' title ahead of West Germany's Isabel de Navarre and the Soviet Union's Tatiana Oleneva.  Irina Vorobieva / Alexander Vlasov defeated Olympic champions Ludmila Belousova / Oleg Protopopov for gold in the pairs' category.  In the ice dancing category, world champions Lyudmila Pakhomova / Alexander Gorshkov won their fourth gold medal at the event.

Lyudmila Pakhomova: Lyudmila Alekseyevna Pakhomova (Russian: Людмила Алексеевна Пахомова ; 31 December 1946 – 17 May 1986) was an ice dancer who competed for the Soviet Union.  With partner Alexandr Gorshkov, she was the 1976 Olympic champion.

1971 Prize of Moscow News: The 1971 Prize of Moscow News was the sixth edition of an international figure skating competition organized in Moscow, Soviet Union.  It was held November 25–28, 1971.  Medals were awarded in the disciplines of men's singles, ladies' singles, pair skating and ice dancing.  Soviets swept the men's podium, led by Sergei Chetverukhin.  The ladies' category was won by Marina Titova, who took the title for the second consecutive year.  Olympic champions Ludmila Belousova / Oleg Protopopov won the pairs' title, defeating two pairs who had beaten them a year earlier.  World champions Lyudmila Pakhomova / Alexander Gorshkov took gold in the ice dancing event for the third consecutive year.

Aleksandr Gorshkov (figure skater): Aleksandr Georgievich Gorshkov (Russian: Александр Георгиевич Горшков , born 8 October 1946) is a former ice dancer who competed internationally for the Soviet Union.  With partner Lyudmila Pakhomova, he is the 1976 Olympic champion.  Since 2010, Gorshkov is the president of the Figure Skating Federation of Russia (FFKKR).

Question: What language does Lyudmila Alekseyevna Pakhomova speak?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "origin_country": {
      "type": "string",
      "description": "The country the person competed for or is associated with."
    },
    "language_spoken": {
      "type": "string",
      "description": "The language associated with the person's name or origin."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of how the language was determined from the context."
    }
  },
  "required": [
    "person_name",
    "origin_country",
    "language_spoken",
    "reasoning"
  ],
  "additionalProperties": false
}
