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
International air travel from the United Kingdom: International air travel from the United Kingdom refers to the commercial carriage of passengers between the UK and the rest of the world.  In 2008, London Heathrow Airport which is also the busiest international airport on Earth handled 67,054,745 passengers which is more than the total population of the United Kingdom.  The 20 busiest airports in the UK handled close to 230 million passengers in 2008 (185 million of whom were international passengers).  The geographical size of the UK means that many flights that would be considered domestic in for example the United States are actually international (i.e. the distance from Heathrow to Charles de Gaulle Airport is roughly the same as the distance between John F. Kennedy International Airport and Washington Dulles International Airport).  The London airports, Heathrow, Gatwick and Stansted alongside Manchester Airport rank amongst the world's busiest airports by international passenger traffic.  According to 2008 statistics the best served nations by direct flights from the UK were France, Italy, Spain, the United States and Germany with 50, 34, 33, 31 and 29 respectively.  Overall Spain was the nation that saw the most passengers arrive from the UK in 2008, with a total of 34,557,729 (almost double the number that flew to the United States)

A1 autoroute: The A1 Autoroute, also known as l'autoroute du Nord (the Northern Motorway), is the busiest of France's autoroutes.  With a length of 211 km , it connects Paris with the northern city of Lille.  It is managed by the Société des Autoroutes du Nord et de l'Est de la France (SANEF).  The autoroute serves the northern suburbs of Paris, including the Stade de France, Le Bourget, Paris' Roissy Charles de Gaulle Airport, and Parc Astérix.  From there it crosses Picardy, without directly passing through any of the major cities of the "région".  Throughout Picardy, the A1 runs parallel to the LGV Nord.

Parc des Expositions de Villepinte: The Parc des expositions de Paris-Nord Villepinte ("English: Paris Nord Villepinte") is a large convention center located in Villepinte near Paris-Charles de Gaulle Airport.  The center opened in 1982 and is the second-largest in France.  The center encompasses 115 hectares and has 246,000 m of convention space in eight halls.  The center is served by the Parc des Expositions station on the RER B.  Paris Nord Villepinte is one metro stop from Charles de Gaulle Airport and 30 minutes from Gare du Nord, Chatelet-Les Halles, Saint Michel RER B stations in Paris city.

XL Airways France: XL Airways France, formerly "Star Airlines", is a French airline with its head offices on the grounds of Paris-Charles de Gaulle Airport.  It operates scheduled flights mainly to long-haul destinations in Africa, the Middle East, the United States and the Caribbean as well as charter flights to medium-haul destinations in the Mediterranean, mostly out of Charles de Gaulle Airport.

Aéroport Charles de Gaulle 2 TGV: Aéroport Charles de Gaulle 2 TGV is a major passenger railway station in Tremblay-en-France, Paris, France.  It is located directly beneath terminal two of Paris Charles de Gaulle Airport (between the C/D and E/F concourses) and is operated by the SNCF.  The station was opened in 1994.  It connects the airport to Paris and to various others cities in France, as well as to Belgium.

Adolfo Suárez Madrid–Barajas Airport: Adolfo Suárez Madrid–Barajas Airport (Spanish: "Aeropuerto Adolfo Suárez Madrid-Barajas" ] ) (IATA: MAD, ICAO: LEMD) , commonly known as Madrid–Barajas Airport, is the main international airport serving Madrid in Spain.  At 3,050 ha in area, it is the largest airport in Europe by physical size along with Paris–Charles de Gaulle Airport.  In 2016, 50.4 million passengers used Madrid–Barajas making it the country's largest and busiest airport, and Europe's sixth busiest.

Mehran Karimi Nasseri: Mehran Karimi Nasseri (مهران کریمی ناصری pronounced ] ; born 1942), also known as Sir, Alfred Mehran, is an Iranian refugee who lived in the departure lounge of Terminal One in Charles de Gaulle Airport from 26 August 1988 until July 2006, when he was hospitalized for an unspecified ailment.  His autobiography has been published as a book, "The Terminal Man", in 2004.  His story was the inspiration for the 2004 Tom Hanks movie "The Terminal".

Charles de Gaulle Airport: Paris Charles de Gaulle Airport (French: "Aéroport de Paris-Charles-de-Gaulle" , IATA: CDG, ICAO: LFPG ), also known as Roissy Airport (name of the local district), is the largest international airport in France.  It is named after Charles de Gaulle (1890–1970), leader of the Free French Forces during the Second World War, founder of the French Fifth Republic and President of France from 1959 to 1969.  Charles de Gaulle Airport is located within portions of several communes 25 km to the northeast of Paris.  Charles de Gaulle Airport serves as the principal hub for Air France as well as a European hub for fellow SkyTeam alliance partner Delta Air Lines.  Additionally, the airport serves as a focus city for low-cost carriers Vueling and Norwegian Air Shuttle.

Air France–KLM: Air France–KLM is a Franco-Dutch airline holding company incorporated under French law with its headquarters at Charles de Gaulle Airport in Tremblay-en-France, near Paris.  The group has offices in Montreuil, Seine-Saint-Denis, Paris, and in Amstelveen, Netherlands.  Air France–KLM is the result of the merger in 2004 between Air France and KLM.  Both Air France and KLM are members of the SkyTeam airline alliance.  The company's namesake airlines rely on two major hubs, Amsterdam Airport Schiphol and Paris–Charles de Gaulle Airport.  Air France–KLM Airlines transported 87.3 million passengers in 2014.

Air France: Air France (] ; formally "Société Air France, S.A."), stylized as AIRFRANCE, is the French flag carrier headquartered in Tremblay-en-France.  It is a subsidiary of the Air France–KLM Group and a founding member of the SkyTeam global airline alliance.  As of 2013 Air France serves 36 destinations in France and operates worldwide scheduled passenger and cargo services to 168 destinations in 93 countries (including overseas departments and territories of France) and also carried 46,803,000 passengers in 2015.  The airline's global hub is at Charles de Gaulle Airport with Orly Airport.  Air France's corporate headquarters, previously in Montparnasse, Paris, are located on the grounds of Charles de Gaulle Airport, north of Paris.

Question: Mehran Karimi Nasseri, also known as Sir, Alfred Mehran, is an Iranian refugee who lived in the departure lounge of Terminal One in Charles de Gaulle Airport, also known as Roissy Airport (name of the local district), is the largest international airport in which country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airport_name": {
      "type": "string",
      "description": "The primary name of the airport."
    },
    "airport_country": {
      "type": "string",
      "description": "The country where the airport is located."
    },
    "airport_attributes": {
      "type": "object",
      "properties": {
        "alternative_names": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other names by which the airport is known."
        },
        "is_largest_international_airport_in_country": {
          "type": "boolean",
          "description": "Indicates if it is the largest international airport in its country."
        }
      },
      "required": [
        "alternative_names",
        "is_largest_international_airport_in_country"
      ],
      "additionalProperties": false
    },
    "refugee_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the refugee."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the refugee."
        },
        "terminal_of_residence": {
          "type": "string",
          "description": "The specific terminal where the refugee lived."
        },
        "years_lived_at_airport": {
          "type": "integer",
          "description": "The number of years the refugee lived at the airport."
        }
      },
      "required": [
        "name",
        "nationality",
        "terminal_of_residence",
        "years_lived_at_airport"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "airport_name",
    "airport_country",
    "airport_attributes",
    "refugee_details"
  ],
  "additionalProperties": false
}
