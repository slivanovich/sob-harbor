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
Domain Interchange: Domain Interchange is a major interchange on the Melbourne tram system.  Featuring two island platforms with four tracks, it has dedicated turning tracks and through tracks.  It is located on St Kilda Road between Domain Road and Park Street, adjacent to Kings Domain, and is one of the busiest interchanges on the system, being used by nine tram routes.  The current structure was opened in April 2013, replacing an earlier structure built in 1986.

Government House, Melbourne: Government House is the official residence of the Governor of Victoria, currently Linda Dessau.  It is located in Kings Domain, Melbourne, next to the Royal Botanic Gardens.

Pioneer Women's Memorial Garden (Melbourne): The Pioneer Women's Memorial Garden is located in Kings Domain, Melbourne, Australia and honours the contribution of white women settlers to the development of the state of Victoria.

Shrine of Remembrance: The Shrine of Remembrance, located in Kings Domain on St Kilda Road, Melbourne, Australia was built as a memorial to the men and women of Victoria who served in World War I and is now a memorial to all Australians who have served in war.  It is a site of annual observances of ANZAC Day (25 April) and Remembrance Day (11 November) and is one of the largest war memorials in Australia.

Treasury Gardens: The Treasury Gardens consist of 5.8 hectares (14.4 acres) on the south-eastern side of the Melbourne Central Business District, East Melbourne, Victoria, Australia.  The gardens are bounded by Wellington Parade, Spring Street, Treasury Place, and by the Fitzroy Gardens across Lansdowne street to the west.  They form part of a network of city gardens including Fitzroy Gardens, Carlton Gardens, Flagstaff Gardens and Kings Domain.  The gardens are listed on the Victorian Heritage Register for their historical, archaeological, social, "aesthetic and scientific (horticultural) importance for its outstanding nineteenth century design, path layout and planting."

Kings Domain: Kings Domain is an area of parklands in Melbourne, Victoria, Australia.  It surrounds Government House Reserve, the home of the Governors of Victoria, the Sidney Myer Music Bowl, and the Shrine Reserve incorporating the Shrine of Remembrance.

Governor of Victoria: The Governor of Victoria is the representative in the Australian state of Victoria of its monarch, Elizabeth II, Queen of Australia and is one of the Governors of the Australian states.  The governor performs the same constitutional and ceremonial functions at the state level as does the Governor-General of Australia at the federal level.  The governor's office and official residence is Government House next to the Royal Botanic Gardens and surrounded by Kings Domain in Melbourne.

Domain Tunnel: The Domain Tunnel is a road tunnel located in Melbourne, Australia, which carries traffic westbound from the Monash Freeway to the West Gate Freeway, running under the Yarra River and Kings Domain.  The tunnel is part of the CityLink Tollway operated by Transurban and provides a bypass of the central business district.

Sidney Myer Music Bowl: The Sidney Myer Music Bowl is an outdoor performance venue in Melbourne, Victoria, Australia.  It is located in the lawns and gardens of Kings Domain, Linlithgow Ave, Melbourne, close to the Arts Centre and the Southbank entertainment precinct.  It was officially opened by Prime Minister Robert Menzies on 12 February 1959, with an audience of 30,000 people, and is listed on the Victorian Heritage Register.

Alexandra Gardens, Melbourne: The Alexandra Gardens are located on the south bank of the Yarra River, opposite Federation Square and the Melbourne Central Business District, in Victoria, Australia.  The Gardens are bounded by the Yarra River to the north, Princes and Swan street bridges, with Queen Victoria Gardens and Kings Domain across Alexandra Avenue to the south.  The gardens are part of the Domain parklands which stretch to the Royal Botanic Gardens and were first laid out in 1901, under the direction of Carlo Catani, Chief Engineer of the Public Works Department.  They are listed on the Victorian Heritage Register due to their historical and archaeological significance.

Question: Kings Domain is an area of parklands in Melbourne, Victoria, Australia, it surrounds Govern House Reserve, the home of the Governors of Victoria, and which outdoor performance venue in Melbourne, Victoria, Australia, located in the lawns and gardens of Kings Domain?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "venue_name": {
      "type": "string",
      "description": "The name of the outdoor performance venue."
    },
    "venue_type": {
      "type": "string",
      "description": "The type of venue, e.g., outdoor performance venue."
    },
    "location_parkland": {
      "type": "string",
      "description": "The name of the parkland where the venue is located."
    },
    "is_surrounded_by_location": {
      "type": "boolean",
      "description": "Indicates if the venue is surrounded by the specified parkland."
    },
    "opening_year": {
      "type": "integer",
      "description": "The year the venue was officially opened."
    },
    "opening_audience_count": {
      "type": "integer",
      "description": "The number of people in the audience at the official opening."
    }
  },
  "required": [
    "venue_name",
    "venue_type",
    "location_parkland",
    "is_surrounded_by_location",
    "opening_year",
    "opening_audience_count"
  ],
  "additionalProperties": false
}
