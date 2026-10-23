{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFouchet Plan: The Fouchet Plan was a plan proposed by President Charles de Gaulle of France in 1961 as part of De Gaulle's grand design for Europe at the time.  His plan included a three-power directorate, consisting of France, Britain and the United States.  His plan also included the Fouchet Plan.  It was written by Christian Fouchet, France's ambassador to Denmark.  The idea was to form a new 'Union of States', an intergovernmental alternative to the European Communities.  De Gaulle feared a loss of French national influence in the European Communities, which was becoming more and more supranational so the Plan was an attempt to keep the balance of power in France's favor.  The success of the European Communities and the lack of enthusiasm of other states for the idea stopped the implementation of the Fouchet Plan.\n\nCharles de Gaulle (born 1948): Charles de Gaulle (born 25 September 1948 in Dijon) is a French politician.  He is the eldest child of Admiral Philippe de Gaulle and grandson of General Charles de Gaulle, and served as a member of the European Parliament (MEP), from 1994 to 2004 (as a member of the Movement for France).\n\nCharles de Gaulle Airport: Paris Charles de Gaulle Airport (French: \"Aéroport de Paris-Charles-de-Gaulle\" , IATA: CDG, ICAO: LFPG ), also known as Roissy Airport (name of the local district), is the largest international airport in France.  It is named after Charles de Gaulle (1890–1970), leader of the Free French Forces during the Second World War, founder of the French Fifth Republic and President of France from 1959 to 1969.  Charles de Gaulle Airport is located within portions of several communes 25 km to the northeast of Paris.  Charles de Gaulle Airport serves as the principal hub for Air France as well as a European hub for fellow SkyTeam alliance partner Delta Air Lines.  Additionally, the airport serves as a focus city for low-cost carriers Vueling and Norwegian Air Shuttle.\n\nPlace Charles de Gaulle: The Place Charles de Gaulle, historically known as the Place de l'Étoile (] ), is a large road junction in Paris, France, the meeting point of twelve straight avenues (hence its historic name, which translates as \"Square of the Star\") including the Champs-Élysées.  It was renamed in 1970 following the death of General and President Charles de Gaulle.  It is still often referred to by its original name, and the nearby metro station retains the designation Charles de Gaulle – Étoile.\n\nFrench Committee of National Liberation: The French Committee of National Liberation (French: \"Comité français de Libération nationale\" ) was a provisional government of Free France formed by the French generals Henri Giraud and Charles de Gaulle to provide united leadership, organize and coordinate the campaign to liberate France from Nazi Germany during World War II.  The committee was formed on 3 June 1943 and after a period of joint leadership, on November 9 it came under the chairmanship of Gen. de Gaulle.  The committee directly challenged the legitimacy of the Vichy regime and unified all the French forces that fought against the Nazis and collaborators.  The committee functioned as a provisional government for Algeria (then a part of metropolitan France) and the liberated parts of the colonial empire.  Later it evolved into the Provisional Government of the French Republic, under the premiership of Charles de Gaulle.\n\nCharles de Gaulle: Charles André Joseph Marie de Gaulle (] ; 22 November 1890 – 9 November 1970) was a French general and statesman.  He was the leader of Free France (1940–44) and the head of the Provisional Government of the French Republic (1944–46).  In 1958, he founded the Fifth Republic and was elected as the President of France, a position he held until his resignation in 1969.  He was the dominant figure of France during the Cold War era and his memory continues to influence French politics.\n\nMusée de l'Ordre de la Libération: The Musée de l'Ordre de la Libération is a military museum located in the 7th arrondissement at 51 bis boulevard de La Tour-Maubourg, Paris, France.  It is open daily except Sunday; admission is free.  The museum is dedicated to the Ordre de la Libération, France's second national order after the Légion d'honneur, which was created in 1940 by General Charles de Gaulle, leader of the Free French Forces.  In 1967 de Gaulle moved the Order of the Liberation into Les Invalides.  The museum contains three galleries and six rooms (total 1,000 m²) documenting the history of the Free French Forces, de Gaulle's manuscripts, resistance activities, and the concentration camps.  Showcases contain more than 4,000 objects including uniforms, weapons, clandestine press and leaflets, transmitters, flags taken to the enemy on the battlefields of Africa and Europe, the first naval flags of Free France, and relics from the camps.  The hall of honor is dedicated to General de Gaulle.\n\nHenri de Gaulle: Henri de Gaulle (1848-1932) was a French civil servant and later a schoolteacher.  He was the father of Charles de Gaulle, a general of the French army and President of France.\n\nPhilippe de Gaulle: Philippe de Gaulle (born 28 December 1921) is a retired French admiral and senator.  He is the eldest child and only son of General Charles de Gaulle, the first President of the French Fifth Republic, and his wife Yvonne, and is the only one of de Gaulle's three children still living as of September 2017.\n\nVive le Québec libre: \"\"Vive le Québec libre!\"\"  (] , \"Long live free Quebec!\")  was a controversial phrase in a speech delivered by President Charles de Gaulle of France on July 24, 1967, during an official visit to Canada under the pretext of attending Expo 67 in Montreal, Quebec.  While giving an address to a large crowd from a balcony at Montreal City Hall, he uttered \"\"Vive Montréal; Vive le Québec!\"\"  (\"Long live Montreal, Long live Quebec!\")  and then added, followed by loud applause, \"\"Vive le Québec \"libre\"!\"\"  (\"Long live \"free\" Quebec!\")  with particular emphasis on the word 'libre'.  The phrase, a slogan used by Quebecers who favoured Quebec sovereignty, and de Gaulle's use of it was seen by them as giving his support to the movement.  The speech sparked a diplomatic incident with Canada's government, and was condemned by Prime Minister Lester B. Pearson, saying that \"Canadians do not need to be liberated\".  In France, though many were sympathetic to the cause of Quebec nationalism, de Gaulle's speech was criticized as a breach of protocol.\n\nQuestion: What country of origin does Henri de Gaulle and Charles de Gaulle have in common?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"shared_country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country of origin that both individuals share.\"\n    },\n    \"individuals\": {\n      \"type\": \"array\",\n      \"description\": \"A list of individuals mentioned in the question with their respective countries of origin.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the individual.\"\n          },\n          \"country_of_origin\": {\n            \"type\": \"string\",\n            \"description\": \"The country of origin for the individual.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"country_of_origin\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"do_they_share_origin\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether both individuals share the same country of origin.\"\n    }\n  },\n  \"required\": [\n    \"shared_country_of_origin\",\n    \"individuals\",\n    \"do_they_share_origin\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "shared_country_of_origin": {
        "type": "string",
        "description": "The country of origin that both individuals share."
      },
      "individuals": {
        "type": "array",
        "description": "A list of individuals mentioned in the question with their respective countries of origin.",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the individual."
            },
            "country_of_origin": {
              "type": "string",
              "description": "The country of origin for the individual."
            }
          },
          "required": [
            "name",
            "country_of_origin"
          ],
          "additionalProperties": false
        }
      },
      "do_they_share_origin": {
        "type": "boolean",
        "description": "Indicates whether both individuals share the same country of origin."
      }
    },
    "required": [
      "shared_country_of_origin",
      "individuals",
      "do_they_share_origin"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
