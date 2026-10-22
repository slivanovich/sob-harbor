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
Mohammed Dewji: Mohammed "Mo" Gulamabbas Dewji (born 8 May 1975) is a Tanzanian businessman,philanthropist, and former politician.  He is the president and CEO of MeTL Group, a Tanzanian conglomerate founded by his father in the 1970s.  Dewji served as Member of Parliament from 2005 – 2015 for his home town of Singida.  In March 2015 "Forbes" magazine named him as the 21st richest person in Africa, with his net worth an estimated US $1.1 billion, having also been the first billionaire in Tanzanian "Forbes" Magazine in 2013.

Ospedale railway station: Ospedale (Italian: "Stazione di Ospedale" ) is a railway station in the Italian city of Bari, in the Province of Bari, Apulia.  The station lies on the Bari–San Paolo railway.  The train services are operated by Ferrotramviaria.

Techint: Techint is an Italian-Argentine conglomerate founded in Milan in 1945 by Italian industrialist Agostino Rocca and headquartered in Milan (Italy) and Buenos Aires (Argentina).  Today the Techint Group is composed of six main companies with an international reach, all global or regional leaders in their fields, in the following areas of business: engineering, construction, steel, mining, oil & gas, industrial plants, healthcare.  Techint, with its subsidiaries, is the largest steel making company in Latin America.  Techint is the world's largest manufacturer of seamless steel tubes, mainly used in the oil industry.

Marino, Lazio: Marino ("Marinum" or "Castrimoenium" in Latin, "Marini" in local dialect) is an Italian city and "comune" in Lazio (central Italy), on the Alban Hills, Italy, 21 km southeast of Rome, with a population of 37,684 and a territory of 26.10 km2 .  It is bounded by other communes, Castel Gandolfo, Albano Laziale, Rocca di Papa, Grottaferrata, and Ciampino.  Marino is famous for its white wine, and for its "Grape Festival", which has been celebrated since 1924.

Paolo Rocca: Paolo Rocca (born 1952) is an Argentine-Italian businessman, CEO of the Techint Group, which holds Tenaris, Ternium and other companies that operate in the engineering, construction and energy sectors.  He is also Chairman and CEO of Tenaris, and Chairman of Ternium.

Greka: The Greka Group is a privately held oil and gas conglomerate founded in 1997 by businessman and entrepreneur Randeep Grewal.  Greka entities include London Stock Exchange-listed Green Dragon Gas and Greka Drilling, as well as Greka Engineering & Technology and Greka Integrated.  Grewal currently serves as chairman and CEO of all of these companies.

1999 Giro d'Italia: The 1999 Giro d'Italia was the 82nd edition of the Giro d'Italia, one of cycling's Grand Tours.  The Giro began on May 15 with a mass-start stage that stretched from Agrigento to Modica.  The race came to a close on June 6 with a mass-start stage that ended in the Italian city of Milan.  Eighteen teams entered the race that was won by the Italian Ivan Gotti (sub judice )of the Team Polti team.  Second and third were the Italians riders Paolo Savoldelli and Gilberto Simoni.

San Gabriele railway station: San Gabriele (Italian: "Stazione di San Gabriele" ) is a railway station in the Italian city of Bari, in the Province of Bari, Apulia.  The station lies on the Bari–San Paolo railway.  The train services are operated by Ferrotramviaria.

2002 Giro d'Italia: The 2002 Giro d'Italia was the 85th edition of the Giro d'Italia, one of cycling's Grand Tours.  The Giro began with a 6.5 km prologue that navigated through the streets of the Dutch city Groningen.  The race came to a close with a mass-start stage that ended in the Italian city of Milan.  Twenty-two teams entered the race that was won by the Italian Paolo Savoldelli of the Index Alexia team.  Second and third were the American Tyler Hamilton and Italian Pietro Caucchioli.

B.Grimm: B.Grimm (Thai: บี.กริม ) is a multinational conglomerate founded in 1878, based in Bangkok, Thailand.  The large-scale conglomerate is active in healthcare, energy, building & industrial systems, real estate, e-commerce, and transport; with 22% annual growth in recent years.  The company is wholly owned and operated by the Link family.  The chairman and CEO, Harald Link, is a noted polo player and philanthropist.

Question: Paolo Rocca is a CEO of the conglomerate founded in what Italian city in 1945

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "conglomerate": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the conglomerate."
        },
        "founding_year": {
          "type": "integer",
          "description": "The year the conglomerate was founded."
        },
        "founding_city": {
          "type": "string",
          "description": "The Italian city where the conglomerate was founded."
        },
        "founding_country": {
          "type": "string",
          "description": "The country where the conglomerate was founded."
        }
      },
      "required": [
        "name",
        "founding_year",
        "founding_city",
        "founding_country"
      ],
      "additionalProperties": false
    },
    "ceo": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the CEO."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "relationship": {
      "type": "string",
      "description": "Describes the relationship between the CEO and the conglomerate."
    }
  },
  "required": [
    "conglomerate",
    "ceo",
    "relationship"
  ],
  "additionalProperties": false
}
