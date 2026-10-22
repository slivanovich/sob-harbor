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
San Juan River (Argentina): The San Juan River is, together with the Jáchal, the most important river of the Argentine province of San Juan.  Both join the Desaguadero/Colorado system that ends at the Atlantic Ocean.

Cuyo (Argentina): Cuyo is the name given to the wine-producing, mountainous area of central-west Argentina.  Historically it comprised the provinces of San Juan, San Luis and Mendoza and was influenced by Chile.  The modern term New Cuyo indicates both Cuyo proper and the province of La Rioja.  New Cuyo is a political and economic macroregion, but culturally La Rioja is part of the North-West rather than of Cuyo.

San Juan, Argentina: San Juan (] ) is the capital city of the Argentine province of San Juan in the Cuyo region, located in the Tulúm Valley, west of the San Juan River, at 650 m above mean sea level, with a population of around 112,000 as per the 2001 census (over 500,000 in the metropolitan area).

Army of the Andes: The Army of the Andes (Spanish: "Ejército de los Andes" ) was a military force created by the United Provinces of the Río de la Plata (Argentina) and mustered by general José de San Martín in his campaign to free Chile from the Spanish Empire.  In 1817, it crossed the Andes Mountains from the Argentine province of Cuyo (his staging point being the current-day province of Mendoza, Argentina), and succeeded in its objective by dislodging the Spanish from the country.

Argentine Confederation: The Argentine Confederation (Spanish: "Confederación Argentina") is one of the official names of Argentina according to the Argentine Constitution, Article 35.  It was the name of the country from 1831 to 1852, when the provinces were organized as a confederation without a head of state.  The governor of Buenos Aires Province (Juan Manuel de Rosas during most of the period) managed foreign relations during this time.  Under his rule, the Argentine Confederation resisted attacks by Brazil, Bolivia, Uruguay, France and the UK, as well other Argentine factions during the Argentine Civil Wars.

Hermes Binner: Hermes Juan Binner (born June 5, 1943) is an Argentine physician and a politician.  He was elected Governor of Santa Fe in 2007.  Binner is the first Socialist to become the governor of an Argentine province, and the first non-Justicialist to rule Santa Fe since 1983.

Patagonia Rebelde: Patagonia Rebelde (or Patagonia Trágica) ("Rebel Patagonia" or "Tragic Patagonia" in English) was the name given to the violent suppression of a rural worker's strike in the Argentine province of Santa Cruz in Patagonia between 1920 and 1922.  The uprising was put down by colonel Héctor Benigno Varela's 10th Cavalry Regiment of the Argentine Army under the orders of President Hipólito Yrigoyen.  Approximately 1,500 rural workers were shot and killed by the Argentine Army in the course of the operations, many of them executed by firing squads after surrendering.  Most of the executed were Spanish and Chilean workers who had sought refuge in Argentina's Patagonia after their strike in the city of Puerto Natales in southern Chile on 27 July 1920 was crushed by the Chilean authorities, at the cost of four carabineers killed.  At least two Argentine soldiers (corporal Domingo Montenegro and private Fernando Pablo Fischer), three local policemen (sergeant Tomás Rosa and constables Ernesto Bozán and Juan Campos) and a number of ranch owners and their relatives also died during the strife.

List of Governors of Tierra del Fuego: The Governor of Tierra del Fuego, Antarctica and South Atlantic Islands (Spanish: "Gobernadora de Tierra del Fuego, Antártida e Islas del Atlántico Sur" ) is the highest executive officer of the Argentine province of Tierra del Fuego.  The Governor is directly elected by the people of the province for a four-year term.  The Lieutenant Governor is elected at the same time and can assume office in the absence, death or suspension of the Governor.

Decembrist revolution (Argentina): The Decembrist revolution (Spanish: "Revolución decembrina" ) was a military coup in the Buenos Aires Province, Argentina.  Juan Lavalle, returning with the troops that fought in the Argentine-Brazilian War, made a coup on December 1, 1828, deposed the governor Manuel Dorrego and closed the legislature.  Dorrego was captured and executed a short time afterwards.  The rancher Juan Manuel de Rosas organized militias that fought against Lavalle and removed him from power, restoring the legislature.  However, as the coup had reignited the Argentine Civil Wars, Rosas was appointed governor of the Buenos Aires province to wage the war against the Unitarian League.  José María Paz made from Córdoba a league of provinces, and so did Rosas.  The conflict ended a short time after the unexpected capture of Paz, who mistook enemy troops for his own.

Juan Jufré: Juan Jufré de Loayza y Montesa (1516–1578) was a Spanish conquistador who participated in the 1541 expedition of Pedro de Valdivia to Chile.  He was the first alcalde of Santiago, Chile (in 1541) and held the position of governor of the Argentine province of Cuyo.  He founded the city of San Juan de la Frontera and re-founded the city of Mendoza.

Question: Juan Jufré was the governor of the Argentine province that historially comprised which provinces?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "governor_name": {
      "type": "string",
      "description": "The name of the governor."
    },
    "governed_region": {
      "type": "string",
      "description": "The name of the region or province governed."
    },
    "region_type": {
      "type": "string",
      "description": "The type of administrative division the region represents."
    },
    "historically_comprised_provinces": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of provinces that historically comprised the governed region."
    }
  },
  "required": [
    "governor_name",
    "governed_region",
    "region_type",
    "historically_comprised_provinces"
  ],
  "additionalProperties": false
}
