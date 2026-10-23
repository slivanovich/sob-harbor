{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRoy Andersson: Roy Arne Lennart Andersson (born 31 March 1943) is an acclaimed Swedish film director, best known for \"A Swedish Love Story\" (1970) and his \"Living trilogy,\" which includes \"Songs from the Second Floor\" (2000), \"You, the Living\" (2007) and \"A Pigeon Sat on a Branch Reflecting on Existence\" (2014).  \"Songs from the Second Floor\", more than any other, cemented and exemplified his personal style – which is characterized by long takes, absurdist comedy, stiff caricaturing of Swedish culture and Felliniesque grotesque.  He has spent much of his professional life working on advertisement spots, directing over 400 commercials and two short films, but only directing six feature-length films in six decades.  His 2014 film \"A Pigeon Sat on a Branch Reflecting on Existence\" won the Golden Lion award at 71st Venice International Film Festival, making Andersson the only Swedish director and the second Scandinavian director to win the award in the history of the festival, after Danish Carl Theodor Dreyer won in 1955.  Anderson is considered one of the most important living European film directors, having four films officially submitted for the Academy Award for Best Foreign Language Film as Swedish entries.\n\nCulture of Denmark: The culture of Denmark has a rich intellectual and artistic heritage.  The astronomical discoveries of Tycho Brahe (1546–1601), Ludwig A. Colding's (1815–1888) neglected articulation of the principle of conservation of energy, and the foundational contributions to atomic physics of Niels Bohr (1885–1962); in this century Lene Vestergaard Hau (born 1959) in quantum physics involving the stopping of light, advances in nano-technology, and contributions to the understanding of Bose-Einstein Condensates, demonstrate the range and endurance of Danish scientific achievement.  The fairy tales of Hans Christian Andersen (1805–1875), the philosophical essays of Søren Kierkegaard (1813–1855), the short stories of Karen Blixen, penname Isak Dinesen, (1885–1962), the plays of Ludvig Holberg (1684–1754), modern authors such as Herman Bang and Nobel laureate Henrik Pontoppidan and the dense, aphoristic poetry of Piet Hein (1905–1996), have earned international recognition, as have the symphonies of Carl Nielsen (1865–1931).  From the mid-1990s, Danish films have attracted international attention, especially those associated with Dogme 95 like those of Lars Von Trier.  Denmark has had a strong tradition of movie making and Carl Theodor Dreyer has been recognised as one of the world's greatest film directors.\n\nPræsidenten: Præsidenten (The President) is a 1919 Danish silent film by Carl Theodor Dreyer.  It is the first feature film directed by Dreyer and it is an adaptation of the 1884 novel \"Der Präsident\" by Karl Emil Franzos.\n\nOrdet: Ordet (] , meaning \"The Word\" and originally released as The Word in English) is a 1955 Danish drama film, directed by Carl Theodor Dreyer.  It is based on a play by Kaj Munk, a Danish Lutheran priest, first performed in 1932.  The film won the Golden Lion at the 16th Venice International Film Festival, and was the only film by Dreyer to be both a critical and financial success.\n\nJohn Sturges: John Eliot Sturges ( ; January 3, 1910 – August 18, 1992) was an American film director.  His movies include \"Bad Day at Black Rock\" (1955), \"Gunfight at the O.K. Corral\" (1957), \"The Magnificent Seven\" (1960), \"The Great Escape\" (1963), and \"Ice Station Zebra\" (1968).  In 2013, \"The Magnificent Seven\" was selected for preservation in the United States National Film Registry by the Library of Congress as being \"culturally, historically, or aesthetically significant\".  He was not related to director Preston Sturges.\n\nCarl Th. Dreyer—My Metier: Carl Th.  Dreyer: My Metier (Danish: Carl Th.  Dreyer: Min metier ) is a 1995 Danish documentary film directed by Torben Skjødt Jensen, about the film career of Carl Theodor Dreyer.\n\nCarl Theodor Dreyer: Carl Theodor Dreyer (] ; 3 February 1889 – 20 March 1968), commonly known as Carl Th.  Dreyer, was a Danish film director.  He is regarded by many critics and filmmakers as one of the greatest directors in cinema.  His best known films include \"The Passion of Joan of Arc\" (1928), \"Vampyr\" (1932), \"Day of Wrath\" (1943), \"Ordet\" (1955), and \"Gertrud\" (1964).\n\nThe Passion of Joan of Arc: The Passion of Joan of Arc (French: La Passion de Jeanne d'Arc ) is a 1928 silent French film based on the actual record of the trial of Joan of Arc.  The film was directed by Carl Theodor Dreyer and stars Renée Jeanne Falconetti as Joan.  It is widely regarded as a landmark of cinema, especially for its production, Dreyer's direction and Falconetti's performance, which is often listed as one of the finest in cinema history.  The film summarizes the time that Joan of Arc was a captive of England, depicting her trial and execution.\n\nJean Hugo: Jean Hugo (19 November 1894 – 21 June 1984) was a painter, illustrator, theatre designer and author.  He was born in Paris and died in his home at the Mas de Fourques, near Lunel, France.  Brought up in a lively artistic environment, he began teaching himself drawing and painting and wrote essays and poetry from a very early age.  His artistic career spans the 20th century, from his early sketches of the First World War, through the creative ferment of the Parisian interwar years, and up to his death in 1984.  He was part of a number of artistic circles that included Jean Cocteau, Raymond Radiguet, Pablo Picasso, Georges Auric, Erik Satie, Blaise Cendrars, Marie-Laure de Noailles, Paul Eluard, Francis Poulenc, Charles Dullin, Louis Jouvet, Colette, Marcel Proust, Jacques Maritain, Max Jacob, Carl Theodor Dreyer, Marie Bell, Louise de Vilmorin, Cecil Beaton and many others.\n\nVampyr: Vampyr (German: \"Vampyr – Der Traum des Allan Gray\" , 'Vampyr: The Dream of Allan Gray' ) is a 1932 German–French horror film directed by Danish director Carl Theodor Dreyer.  The film was written by Dreyer and Christen Jul based on elements from J. Sheridan Le Fanu's collection of supernatural stories \"In a Glass Darkly\".  \"Vampyr\" was funded by Nicolas de Gunzburg who starred in the film under the name of Julian West among a mostly non-professional cast.  Gunzburg plays the role of Allan Grey, a student of the occult who enters the village of Courtempierre, which is under the curse of a vampire.\n\nQuestion: Carl Theodor Dreyer and John Sturges have what career in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"common_profession\": {\n      \"type\": \"string\",\n      \"description\": \"The specific career or profession shared by the individuals.\"\n    },\n    \"profession_category\": {\n      \"type\": \"string\",\n      \"description\": \"A broader category for the shared profession.\"\n    },\n    \"individuals_involved\": {\n      \"type\": \"array\",\n      \"description\": \"A list of individuals sharing the common profession, including their name and nationality.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the individual.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"nationality\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"common_profession\",\n    \"profession_category\",\n    \"individuals_involved\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "common_profession": {
        "type": "string",
        "description": "The specific career or profession shared by the individuals."
      },
      "profession_category": {
        "type": "string",
        "description": "A broader category for the shared profession."
      },
      "individuals_involved": {
        "type": "array",
        "description": "A list of individuals sharing the common profession, including their name and nationality.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the individual."
            }
          },
          "required": [
            "name",
            "nationality"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "common_profession",
      "profession_category",
      "individuals_involved"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
