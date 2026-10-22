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
Claudia Pavlovich Arellano: Claudia Artemiza Pavlovich Arellano (born 17 June 1969) is a Mexican politician and lawyer affiliated with the Institutional Revolutionary Party (PRI).  She currently serves as Governor of Sonora, the first woman to govern the state, and currently the only female governor of any Mexican state.  Previously she served as Senator of the LXII Legislature of the Mexican Congress representing Sonora.

Fernando Adames Torres: Fernando Adames Torres was born around the 3rd decade of the 19th century in Siquisique, a small city near Barquisimeto on Lara State in the country of Venezuela.  He was the son of Juan Bautista Adames and Magdalena Torres.  During his early years prior to entering the Military, Fernando Adames spent most of his time as a business entrepreneur, until March 1858 where he joined the military during the Revolution of 1858 serving under the orders of Mariscal Falcon.  This revolution lasted five years and ended with the formation of the "Federacion Venezolana".

Chiapas: Chiapas (] ), officially the Free and Sovereign State of Chiapas (Spanish: "Estado Libre y Soberano de Chiapas" ), is one of the 31 states that, with the Federal District, make up the 32 federal entities of Mexico.  It is divided into 122 municipalities and its capital city is Tuxtla Gutiérrez.  Other important population centers in Chiapas include Ocosingo, Tapachula, San Cristóbal de las Casas, Comitán and Arriaga.  It is the southernmost state, bordered by the states of Oaxaca to the west, Veracruz to the northwest and Tabasco to the north, and by the Petén, Quiché, Huehuetenango and San Marcos departments of Guatemala to the east and southeast.  Chiapas has a coastline along the Pacific Ocean to the south.

María Rodríguez Preciado: María Magdalena Rodríguez Preciado (born 11 November 1978) is a Mexican politician from the National Action Party.  In 2009 she served as Deputy of the LX Legislature of the Mexican Congress representing Guanajuato.

Magdalena González Furlong: Magdalena Adriana González Furlong (born 4 March 1958) is a Mexican politician who was affiliated with the National Action Party.  As of 2014 she served as Deputy of the LIX Legislature of the Mexican Congress representing the State of Mexico.

Magdalena Macedo Domínguez: María Magdalena Macedo Domínguez (born 25 May 1955) is a Mexican politician from the National Action Party.  In 2009 she served as Deputy of the LX Legislature of the Mexican Congress representing the State of Mexico.

Carlos Alberto Torres Torres: Carlos Alberto Torres Torres (born 18 November 1975) is a Mexican politician from the National Action Party.  From 2006 to 2009, he served as Deputy of the LX Legislature of the Mexican Congress representing Baja California.

Obdulia Torres Abarca: Obdulia Magdalena Torres Abarca (born 3 September 1961) is a Mexican politician from the Party of the Democratic Revolution.  From 2009 to 2012 she served as Deputy of the LXI Legislature of the Mexican Congress representing Chiapas.

Patricia Castillo Romero: Patricia Obdulia de Jesús Castillo Romero (born 6 March 1963) is a Mexican politician from the Citizens' Movement.  From 2006 to 2009 she served as Deputy of the LX Legislature of the Mexican Congress representing Nayarit.

Ivonne Ortega Pacheco: Ivonne Aracelly Ortega Pacheco (born November 27, 1972) is a Mexican politician from Yucatán affiliated with the Institutional Revolutionary Party (PRI), former Governor of Yucatán and current federal deputy to the LXIII Legislature of the Mexican Congress.  She is Yucatan's first elected female governor, although the second to serve, after Dulce María Sauri who served as interim governor from 1991 to 1994.  She is the sixth woman to serve as governor of a Mexican state.

Question: What is the capital of the Mexican state that Obdulia Magdalena Torres Abarca represented in the Mexican Congress from 2009 to 2012?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "politician_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the politician."
        },
        "party_affiliation": {
          "type": "string",
          "description": "The political party the politician is affiliated with."
        }
      },
      "required": [
        "name",
        "party_affiliation"
      ],
      "additionalProperties": false
    },
    "represented_state_info": {
      "type": "object",
      "properties": {
        "state_name": {
          "type": "string",
          "description": "The name of the Mexican state represented by the politician."
        },
        "state_capital": {
          "type": "string",
          "description": "The capital city of the represented state."
        },
        "number_of_municipalities": {
          "type": "integer",
          "description": "The number of municipalities in the represented state."
        }
      },
      "required": [
        "state_name",
        "state_capital"
      ],
      "additionalProperties": false
    },
    "congressional_term": {
      "type": "object",
      "properties": {
        "legislature": {
          "type": "string",
          "description": "The legislature number of the Mexican Congress."
        },
        "role": {
          "type": "string",
          "description": "The role held by the politician in the Congress (e.g., Deputy, Senator)."
        },
        "start_year": {
          "type": "integer",
          "description": "The start year of the congressional term."
        },
        "end_year": {
          "type": "integer",
          "description": "The end year of the congressional term."
        }
      },
      "required": [
        "legislature",
        "role",
        "start_year",
        "end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "politician_details",
    "represented_state_info",
    "congressional_term"
  ],
  "additionalProperties": false
}
