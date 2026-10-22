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
Sisters (1973 film): Sisters (also known as "Blood Sisters" in the United Kingdom) is a 1973 American psychological horror film directed by Brian De Palma and starring Margot Kidder, Jennifer Salt and Charles Durning.  The plot focuses on a French Canadian model whose separated Siamese twin is suspected of a brutal murder witnessed by a newspaper reporter in Staten Island.

Jenn Proske: Jennifer Proske (born August 8, 1987) is a Canadian American actress, best known for portraying Becca Crane in the film "Vampires Suck".

Are You Afraid of the Dark?: Are You Afraid of the Dark?  is a Canadian American horror fantasy-themed anthology television series.  The original series was created by D.J. MacHale and Ned Kandel, and was picked up by Nickelodeon in 1991.  MacHale, Kandel, and Nickelodeon teamed up with the Canadian company Cinar, and as a part of the deal the show was filmed in Richmond, British Columbia and in the Greater Montreal area of Quebec, including their suburbs.

Katharine Isabelle: Katharine Isabelle Murray (born November 2, 1981) is a Canadian actress best known as a scream queen for her roles in various horror films.  Born in Vancouver, British Columbia, she made her screen debut as a child in "Cousins" (1989), followed by supporting roles in numerous films and television series.  Initially credited as Katie Murray, she later began using the name Katherine Isobel and subsequently Katharine Isabelle.  She has starred in the werewolf horror films, "Ginger Snaps" (2000), its sequel, "" (2004), and "" (2004).  Her portrayal of the death-obsessed teen, Ginger Fitzgerald, became one of her most notable roles.  Additional roles in horror films include "Disturbing Behavior" (1998), "Carrie" (2002), "Freddy vs. Jason" (2003), "" (2010), and "American Mary" (2012).  For her performance in the horror film, "American Mary" (2012), she earned several nominations for best actress, including Fangoria Chainsaw Awards, Screamfest Horror Film Festival and Toronto After Dark Film Festival.

Margot Kidder: Margaret Ruth "Margot" Kidder (born October 17, 1948) is a Canadian American actress and activist.  She rose to fame in 1978 for her role as Lois Lane in the "Superman film series", opposite Christopher Reeve.  Kidder began her career in the 1960s appearing in low-budget Canadian films and television series, before landing a lead role in "Quackser Fortune Has a Cousin in the Bronx" (1970).

J. Gordon Edwards filmography: J. Gordon Edwards (1867–1925) was a Canadian American film director, screenwriter, and producer of the silent era.  His oeuvre consists of over fifty feature films made between 1914 and 1924.  He is perhaps best known for directing twenty-four films starring vamp actress Theda Bara—including "Cleopatra", her most famous role— and also the 1921 epic "The Queen of Sheba".  Edwards was born in Montreal and educated at a military academy with the expectation that he would pursue a career as a British Army officer.  He decided against a life in the military in favor of a future in theater.  At the time, the Canadian theater and film industry was limited primarily to repertory theatre, so Edwards became one of many to emigrate to the United States to work in the field.  He had a short career as an actor before becoming a stage director.  By 1910, he was working for American motion picture producer William Fox, who sent him to Europe to study film production.

Louie Gong: Louie Gong (born August 8, 1974) is a Canadian American visual artist, activist, public speaker, educator, and entrepreneur.  His work focuses on Indigenous and multiracial identity, exploring race and identity through art, and expanding business leadership and capacity for Native artists.

Nadine van der Velde: Nadine van der Velde (born May 14, 1962) is a Canadian American actress, producer and writer.  She is a 3 time Emmy award winner, two-time Annie Award winner and a recipient of a Humanitas Award.

Tina Ona Paukstelis: Tina Ona Paukstelis is an American actress.  She was born November 20, 1970 in Kenosha, Wisconsin.  The majority of her film work is in the horror film genre.  Her debut was the lead role of 'Katrina' in the 1994 vampire film "Aswang" - the first horror film to screen at the "Sundance Film Festival".  Paukstelis next starred as an endangered teenager in the cult movie "5 Dark Souls" (1996) and its 1998 and 2003 sequels.  Throughout the 2000s she continued to land lead and supporting roles in the horror films "Julia Wept" (2000), "October Moon" (2005), "" (2008), and "The Legend Trip" (2006).  Her most recent film is the haunted house thriller "Safe Inside (film)" (2013).

Pamela Anderson: Pamela Denise Anderson (born July 1, 1967) is a Canadian American actress and model.  Anderson is best known for her roles on the television series "Home Improvement", "Baywatch" and "V.I.P." after rising to fame as Playmate of the Month for "Playboy" magazine in February 1990.  Anderson has also appeared in films such as "Raw Justice" (1994), "Barb Wire" (1996) and "Blonde and Blonder" (2008) and was inducted into Canada's Walk of Fame in 2006.

Question: Who was a Canadian American actress and activist who starred in a horror film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the individual."
    },
    "nationalities": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of nationalities the person holds."
    },
    "occupations": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of occupations the person is known for."
    },
    "starred_in_horror_film": {
      "type": "boolean",
      "description": "True if the person starred in at least one horror film."
    },
    "horror_film_roles": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "film_title": {
            "type": "string",
            "description": "The title of the horror film."
          },
          "film_year": {
            "type": "integer",
            "description": "The release year of the horror film."
          },
          "film_genre": {
            "type": "string",
            "description": "The genre of the horror film."
          }
        },
        "required": [
          "film_title",
          "film_year",
          "film_genre"
        ],
        "additionalProperties": false
      },
      "description": "Details of the horror films the person starred in."
    }
  },
  "required": [
    "person_name",
    "nationalities",
    "occupations",
    "starred_in_horror_film",
    "horror_film_roles"
  ],
  "additionalProperties": false
}
