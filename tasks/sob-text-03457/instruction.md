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
Nakhon Lampang Railway Station: Nakhon Lampang Railway Station is a railway station located in Lampang.  It is the main railway station for the province and is operated by the State Railway of Thailand.  Nakhon Lampang Railway Station is on the Northern Line and is 642.292 km from Bangkok Railway Station.  The station was built around 1915 and was open for use after the first Royal Train arrived at Lampang Station on 1 April 1916.

Deputy Lieutenant: In the United Kingdom, a Deputy Lieutenant is a Crown appointment and one of several deputies to the Lord Lieutenant of a lieutenancy area: an English ceremonial county, Welsh preserved county, Scottish lieutenancy area, or Northern Irish county borough or county.

Croydon Road Railway Station: Croydon Road Railway Station was a train station in Auckland, New Zealand.  It was on the Western Line and was between Fruitvale Road Railway Station and Glen Eden Railway Station.  The station closed at the same time as the St George's Street and Westbrook stations, also on the Western Line, on a six-month trial basis on 18 August 1980, with the closure being made permanent later.

Carrickfergus: Carrickfergus (from Irish: "Carraig Fhearghais" , meaning "Fergus's rock" ), colloquially known as "Carrick", is a large town in County Antrim, Northern Ireland.  It sits on the north shore of Belfast Lough, 11 mi from Belfast.  The town had a population of 27,903 at the 2011 Census.  It is County Antrim's oldest town and one of the oldest towns in Ireland as a whole.  Carrickfergus was the administrative centre for Carrickfergus Borough Council, before this was amalgamated into the Mid and East Antrim District Council in 2015, and forms part of the Belfast Metropolitan Area.  It is also a townland of 65 acres, a civil parish and a barony.

Westbrook railway station (New Zealand): Westbrook railway station was a station on the Western Line in Auckland, New Zealand between Waikomiti Train Station and Glen Eden Railway Station.  It closed at the same time as the Croydon Road and St George's Street stations, also on the Western Line, on a six-month trial basis on 18 August 1980, with the closure being made permanent later.

Mount Eden Railway Station: Mt Eden Railway Station is a Western Line station of the Auckland railway network in the Auckland suburb of Mount Eden in New Zealand.  It has an island platform, and is reached via a footbridge from Mount Eden Rd or from the level crossing between Ngahura Street and Fenton Street.

Glen Eden Railway Station: Glen Eden Railway Station is located on the Western Line of the Auckland Railway Network, New Zealand.  The station house is a local historical landmark that was restored in 2001.  A cafe is located in the old station building.

Changsari railway station: Changsari Railway Station is located in the northern part of Guwahati town.  It belongs to the Rangiya division of Northeast Frontier Railway.  Nearby neighbourhood stations are Baihata railway station, Agthori railway station, Kamakhya railway station and Guwahati railway station.

City Rail Link: The City Rail Link (CRL) is a rail project currently under construction in Auckland, New Zealand.  The project consists of the construction of a 3.5 km long double-track rail tunnel underneath Auckland's city centre, between Britomart Transport Centre and Mount Eden Railway Station.  Two new underground stations will be constructed to serve the city centre; Aotea Station near Aotea Square and Karangahape Station near Karangahape Road.  Britomart will be converted from a terminus station into a through station and Mount Eden Station will be completely rebuilt with four platforms to serve as an interchange between the new CRL line and the existing Western Line.

Eden railway station: Eden (also known as Eden Halt) was a station located in the townland of Eden, in and around the town of Carrickfergus in Northern Ireland.  At one time it formed part of a tight cluster of stations, each located almost one minute from the other, from Mount through to Kilroot.

Question: Eden railway station goes around the town in what Northern Irish county?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "station_name": {
      "type": "string",
      "description": "The name of the railway station."
    },
    "located_in_town": {
      "type": "string",
      "description": "The town where the railway station is located."
    },
    "located_in_county": {
      "type": "string",
      "description": "The Northern Irish county where the railway station is located."
    },
    "country_region": {
      "type": "string",
      "description": "The country or region where the station is located."
    }
  },
  "required": [
    "station_name",
    "located_in_town",
    "located_in_county",
    "country_region"
  ],
  "additionalProperties": false
}
