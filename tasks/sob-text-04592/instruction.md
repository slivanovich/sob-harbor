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
Wisseloord Studios: The Wisseloord Studio is a recording studio in Hilversum, Netherlands.  It was officially opened on 19 January 1978 by Prince Claus.  The studios were founded by electronics company Philips, to enable their PolyGram artists to record in a professional environment.  Initially there were three studios, nowadays there are five.

Mansoob Murshed: Mansoob Murshed is a Professor of International Industrial Economics at the University of Birmingham whose research interests are development, globalisation and conflict / post-conflict reconstruction.  Alongside his post at Birmingham he also holds a Professorship at the Institute of Social Studies (ISS) The Hague, on the Economies of Conflict and Peace.  He holds an honorary fellowship at the Peace Research Institute (PRIO) Oslo and his having been the first to be awarded the "Prince Claus rotating Chair in Development and Equity" (established in memory of Prince Claus, a Prince Consort of the Netherlands).

Drakensteyn Castle: Drakensteyn Castle (Dutch: "Drakensteyn", sometimes "Drakesteijn" or "Drakestein") is a small castle at 8 Slotlaan in the hamlet of Lage Vuursche, in the municipality of Baarn, Netherlands.  It is owned by Princess Beatrix of the Netherlands, the country's former Queen who abdicated in 2013.  Beatrix bought the castle in 1959, when she was the heir to the Dutch throne, and took up residence in 1963.  After her marriage in 1966 she continued to live there with her husband, Prince Claus and later their three sons as well.  After Beatrix succeeded her mother Juliana as Queen of the Netherlands in 1980, the family moved to The Hague in 1981.

Lu Guang (photographer): Lu Guang (卢广) (born in 1961) is a Chinese photojournalist.  His work is focused on social, environmental, and economic issues.  He has received an award from World Press Photo, the Henri Nannen Prize from Gruner + Jahr, the W. Eugene Smith Grant, a photography grant from National Geographic and the Prince Claus Award.

Prince Claus Conservatoire: The Prince Claus Conservatoire (Dutch: "Prins Claus Conservatorium" ) is one of the nine conservatoires in the Netherlands.  It is a constituent of the Hanze University of Applied Sciences in Groningen.

Jumoke Oduwole: Olajumoke Omoniyi Oduwole is a Nigerian jurist and academic.  She was appointed the Prince Claus Chair holder from 2013–2015.

Prince Claus of the Netherlands: Prince Claus of the Netherlands, Jonkheer van Amsberg (né "Klaus-Georg Wilhelm Otto Friedrich Gerd von Amsberg"; 6 September 1926 – 6 October 2002), was the husband of Queen Beatrix, and the Prince Consort of the Netherlands from Beatrix's ascension in 1980 until his death in 2002.

Men Who Save the World: Men Who Save the World (Malay: Lelaki Harapan Dunia ) is a 2014 internationally co-produced comedy film written and directed by Liew Seng Tat.  It is produced by Sharon Gan and is a co-production project between Everything Films Sdn.  Bhd. (Malaysia) and Volya Films (The Netherlands), Flying Moon Filmproduktion (Germany) and Mandra Films (France) with support from Ministry of Information, Communication and Culture (Malaysia), Torino Film Lab (Italy), Hubert Bals Fund (The Netherlands), Netherlands Film Fund, World Cinema Fund (Germany), Visions Sud Est (Switzerland), Fondation Groupama Gan pour le Cinéma - Cinefondation (France), Prince Claus (The Netherlands), Sundance Institute Mahindra Global Filmmaking Award, Sundance Institute Feature Film Program dan the Doris Duke Foundation (USA).

Baroness Gösta von dem Bussche-Haddenhausen: Baroness Gösta von dem Bussche-Haddenhausen (German: "Freiin Gösta Julie Adelheid Marion Marie von dem Bussche-Haddenhausen" ; 26 January 1902 – 13 June 1996) was the mother of Prince Claus of the Netherlands, who was the Prince Consort of Queen Beatrix of the Netherlands, thus making her the mother-in-law of the former Dutch Queen.  She is also the paternal grandmother of King Willem-Alexander of the Netherlands, who is the current Dutch King.

Prince Claus Fund: The Prince Claus Fund was established in 1996, named in honor of Prince Claus of the Netherlands.  It receives an annual subsidy from the Dutch Ministry of Foreign Affairs.

Question: The Prince Claus Fund, established in 1996, was named after the husband of what Queen?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "queen_name": {
      "type": "string",
      "description": "The name of the Queen who was married to Prince Claus."
    },
    "prince_consort_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Prince Consort."
        },
        "role": {
          "type": "string",
          "description": "The role held by the Prince Consort."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "fund_details": {
      "type": "object",
      "properties": {
        "fund_name": {
          "type": "string",
          "description": "The name of the fund established in honor of the Prince."
        },
        "establishment_year": {
          "type": "integer",
          "description": "The year the fund was established."
        }
      },
      "required": [
        "fund_name",
        "establishment_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "queen_name",
    "prince_consort_details",
    "fund_details"
  ],
  "additionalProperties": false
}
