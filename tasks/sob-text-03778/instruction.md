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
Justice Party (Ukraine): The Justice Party (; formerly Party of All-Ukrainian Union of the Left "Justice" (Ukrainian: Партія Всеукраїнського об'єднання лівих „Справедливість“)) is a left-wing political party in Ukraine.  The party merged into the (then) new party United Left and Peasants (Ukrainian: Об'єднані ліві і селяни ) in December 2011.  Justice Party leader Stanislav Nikolaenko became the first party leader of United Left and Peasants.  United Left and Peasants changed its name to Justice Party in 2014.

United Left (Argentina): The United Left (Spanish: Izquierda Unida ) was a political party in Argentina.  It was an alliance of several groups, chiefly the Communist Party of Argentina and the Socialist Workers' Movement.

Socialist Worker: Socialist Worker is the name of a number of newspapers currently or formerly associated with the International Socialist Tendency (IST).  It is a weekly newspaper published by the Socialist Workers Party (SWP) in the United Kingdom, a monthly (and daily web site) published by the International Socialist Organization (ISO) in the United States, a monthly published by the International Socialists in Canada, a biweekly published by the Socialist Workers Party in Ireland, a quarterly published by the International Socialist Organisation in Zimbabwe and was a monthly published by the former International Socialist Organisation in Australia.  Socialist Worker was also the name of an IST political group in Aotearoa/New Zealand.

Socialist Workers Party (Cuba): The Socialist Workers Party (Spanish: "Partido Obrero Socialista" , POS), initially known as the Workers Party of Cuba (Spanish: "Partido Obrero de Cuba" ), was a political party in Cuba.  The party published "La Voz Obrera".  It was founded by a group of workers in Havana in 1904.  In the party was joined by Carlos Baliños, who had formed the Socialist Propaganda Club 1903.  Baliños became the leading figure of the party, and the name was changed to POS.  The party also adopted a socialist programme.  In November 1906 POS merged with the International Socialist Group, forming the Socialist Party of the Island of Cuba.  "La Voz Obrera" was taken over by the new party as its organ.

United Left (Ireland): United Left was a left-wing political party in Ireland founded in 2013.  The founders were TDs Clare Daly and Joan Collins, who had been elected at the 2011 election as members of the Socialist Party and People Before Profit Alliance respectively.  United Left was added to the official register of political parties in May 2013.  Its registered officers were Daly, Collins, Declan Bree of Sligo County Council and Pat Dunne of Dublin City Council, all formerly of the United Left Alliance.  As of December 2015, it is no longer a registered political party.

Socialist Workers Party (Ireland): The Socialist Workers Party (SWP; Irish: "Páirtí Sóisialach na nOibrithe" ) is an Irish Trotskyist political party founded in 1971 as the Socialist Workers Movement (SWM).  The party is a founding member of the People Before Profit Alliance and is a member of the European United Left-Nordic Green Left and International Socialist Tendency.

Socialist Workers Movement (Mexico): The Socialist Workers Movement (MTS) is an extreme left Mexican political grouping.  It was formed in 2014 by the former "League of Workers for Socialism - Countercurrent" (Liga de Trabajadores por el Socialismo - Contracorriente, LTS-CC) for registration with the National Electoral Institute.

Alonso José Puerta: Alonso José Puerta Gutiérrez (born 24 March 1944) is a Spanish politician from Avilés, Asturias.  He was a member of the European Parliament from 1987 to 2004, representing the European United Left–Nordic Green Left.  Puerta was initially a Spanish Socialist Workers' Party (PSOE) member and was elected for that party to the Spanish Congress of Deputies at the 1977 election for Madrid but later joined United Left.  He also represented the PSOE on Madrid city council.

Communist Party of Argentina: The Communist Party of Argentina (Spanish: "Partido Comunista de la Argentina" , also simply known as "PC") is a communist party in Argentina.  It was founded in 1918.

Independent Socialist Workers Party: The Independent Socialist Party (Czech: "Neodvislá socialistická strana" ) was a political party in Czechoslovakia.  The party was founded in March 1923.  The party included a number of former anarchists, who had joined the Czech Socialist Party in 1918.  They had however been expelled from the Czechoslovak Socialist Party in 1923, as they opposed the Defense of the Republic Act.  In the Czechoslovak National Assembly, the Independent Socialists formed a joint parliamentary group (Socialist Association) together with the Independent Radical Social Democratic Party of V. Brodecký.  The two groups were set to merge, but Brodecký's group decided to merge with the Czechoslovak Social Democratic Workers Party.  The Independent Socialist Party took the name Independent Socialist Workers Party (Czech: "Neodvislá socialistická strana dělnická" ) at a congress in June 1924.

Question: When was the political party, which along with the Socialist Workers Movement are the chief contributors to the United Left in Argentina, founded

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "party_name": {
      "type": "string",
      "description": "The name of the political party."
    },
    "country": {
      "type": "string",
      "description": "The country where the political party is active."
    },
    "role_in_alliance": {
      "type": "string",
      "description": "Describes the party's contribution or role within an alliance."
    },
    "alliance_name": {
      "type": "string",
      "description": "The name of the political alliance the party is part of."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the political party was founded."
    }
  },
  "required": [
    "party_name",
    "country",
    "role_in_alliance",
    "alliance_name",
    "founding_year"
  ],
  "additionalProperties": false
}
