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
French literature: French literature is, generally speaking, literature written in the French language, particularly by citizens of France; it may also refer to literature written by people living in France who speak traditional languages of France other than French.  Literature written in French language, by citizens of other nations such as Belgium, Switzerland, Canada, Senegal, Algeria, Morocco, etc. is referred to as Francophone literature.  As of 2006, French writers have been awarded more Nobel Prizes in Literature than novelists, poets and essayists of any other country.  France itself ranks first in the list of Nobel Prizes in literature by country.

Thomas Mann Prize: Thomas Mann Prize ("German": Thomas-Mann-Preis) is a literary prize of Germany.  In full the title is "Thomas Mann Prize of the city of Lübeck and the Bavarian Academy of Fine Arts".  It is given in alternate years in Lübeck and in Munich.  The award is the product of a merger of two prizes in 2010, the Thomas Mann Preis der Hansestadt Lübeck (Thomas Mann Prize Lübeck) and the Großen Literaturpreis (Great Literature Prize) of the Bavarian Academy of Fine Arts.  The Thomas Mann Prize Lübeck was first awarded in 1975; the Great Literature Prize was first awarded in 1950.

List of Nobel laureates in Chemistry: The Nobel Prize in Chemistry (Swedish: "Nobelpriset i kemi" ) is awarded annually by the Royal Swedish Academy of Sciences to scientists in the various fields of chemistry.  It is one of the five Nobel Prizes established by the 1895 will of Alfred Nobel, who died in 1896.  These prizes are awarded for outstanding contributions in chemistry, physics, literature, peace, and physiology or medicine.  As dictated by Nobel's will, the award is administered by the Nobel Foundation and awarded by a committee that consists of five members elected by the Royal Swedish Academy of Sciences.  The first Nobel Prize in Chemistry was awarded in 1901 to Jacobus Henricus van 't Hoff, of the Netherlands.  Each recipient receives a medal, a diploma and a monetary award prize that has varied throughout the years.  In 1901, van 't Hoff received 150,782 SEK, which is equal to 7,731,004 SEK in December 2007.  The award is presented in Stockholm at an annual ceremony on December 10, the anniversary of Nobel's death.

Thomas Mann House: The Thomas Mann House at 1550 San Remo Drive in Pacific Palisades, Los Angeles, California, was designed by the modernist architect JR Davidson for the exiled German writer Thomas Mann in 1941.  Mann lived at the house between 1942 and 1952 before his emigration to Switzerland, where he spent the last three years of his life.  The house was sold by Mann to an American lawyer and his wife, and remained in their family until its 2016 purchase by the German government.  A restoration of the house is planned, and it is intended that the house will become an artist's residence, like the nearby Villa Aurora, the home of fellow German exile Lion Feuchtwanger.

List of female Nobel laureates: The Nobel Prizes are awarded annually by the Royal Swedish Academy of Sciences, the Swedish Academy, the Karolinska Institute, and the Norwegian Nobel Committee to individuals who make outstanding contributions in the fields of Chemistry, Physics, Literature, Peace, Physiology or Medicine and Economics.  All but the economics prize were established by the 1895 will of Alfred Nobel, which dictates that the awards should be administered by the Nobel Foundation.  The Nobel prize in Economics, or The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel, was established in 1968 by the Sveriges Riksbank, the central bank of Sweden, for outstanding contributions in the field of Economics.  Each prize is awarded by a separate committee; the Royal Swedish Academy of Sciences awards the Prizes in Physics, Chemistry, and Economics, the Swedish Academy awards the Prize in Literature, the Karolinska Institute awards the Prize in Physiology or Medicine, and the Norwegian Nobel Committee awards the Prize in Peace.  Each recipient receives a medal, a diploma and a cash prize that has varied throughout the years.

Golo Mann: Golo Mann (27 March 1909 – 7 April 1994), born Angelus Gottfried Thomas Mann, was a popular historian, essayist and writer.  He was the third child of the novelist Thomas Mann and his wife Katia Mann.

Nobel Prize controversies: After his death in 1896, the will of Swedish industrialist Alfred Nobel established the Nobel Prizes. Nobel's will specified that annual prizes are to be awarded for service to humanity in the fields of physics, chemistry, physiology or medicine, literature, and peace.  Similarly, the Bank of Sweden Prize in Economic Sciences in Memory of Alfred Nobel is awarded along with the Nobel Prizes.  Since the first award in 1901, the prizes have occasionally engendered criticism and controversy.

Mann family: The Mann family is a German Hanseatic family, members of the small ruling class of the city republic of Lübeck.  The family's most famous member is Nobel Prize for Literature laureate Thomas Mann, who portrayed his own family and social class in the novel "Buddenbrooks".  The family became part of the commercial elite of Lübeck from the late 18th century.  In 1877, Thomas Mann's father Thomas Johann Heinrich Mann was elected Senator of Lübeck (corresponding to Minister of Finance in other German states).

Thomas Mann: Paul Thomas Mann (] ; 6 June 1875 – 12 August 1955) was a German novelist, short story writer, social critic, philanthropist, essayist, and the 1929 Nobel Prize in Literature laureate.  His highly symbolic and ironic epic novels and novellas are noted for their insight into the psychology of the artist and the intellectual.  His analysis and critique of the European and German soul used modernized German and Biblical stories, as well as the ideas of Goethe, Nietzsche and Schopenhauer.

T. R. Pearson: Thomas Reid Pearson (born 1956) is an American writer.  Pearson also writes crime fiction under the pen name Rick Gavin.

Question: Who won more Nobel prizes, Thomas Mann or T. R. Pearson?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "string",
      "description": "Indicates which individual won more Nobel Prizes."
    },
    "individual_with_more_prizes": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the individual who won more Nobel Prizes."
        },
        "nobel_prizes_won": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "year": {
                "type": "integer",
                "description": "The year the Nobel Prize was awarded."
              },
              "category": {
                "type": "string",
                "description": "The category of the Nobel Prize."
              }
            },
            "required": [
              "year",
              "category"
            ],
            "additionalProperties": false
          },
          "description": "Details of the Nobel Prizes won by this individual."
        },
        "total_prizes": {
          "type": "integer",
          "description": "The total number of Nobel Prizes won by this individual."
        }
      },
      "required": [
        "name",
        "nobel_prizes_won",
        "total_prizes"
      ],
      "additionalProperties": false
    },
    "individual_with_fewer_prizes": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the individual who won fewer Nobel Prizes."
        },
        "total_prizes": {
          "type": "integer",
          "description": "The total number of Nobel Prizes won by this individual."
        }
      },
      "required": [
        "name",
        "total_prizes"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "comparison_result",
    "individual_with_more_prizes",
    "individual_with_fewer_prizes"
  ],
  "additionalProperties": false
}
