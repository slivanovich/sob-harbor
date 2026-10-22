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
São Paulo WCT: The Sao Paulo WCT was a men's tennis tournament played in Sao Paulo, Brazil from 1974–1976.  The event was part of the WCT Tour and was held on indoor carpet courts.

Seaborn Networks: Seaborn Networks is a developer owner and operator of submarine communications cables.  Seaborn is the owner and operator of the Seabras-1 “submarine communications cable” between Brazil and the United States.  Seabras-1 will provide the first direct route between Sao Paulo, Brazil and the United States.  The system will also have branching units installed on certain of its fiber pairs that point towards Ashburn (US), Miami (US), St. Croix (US), Fortaleza (Brazil), Cape Town (South Africa), Rio de Janeiro (Brazil), and Las Toninas (Argentina).  Partners Group (symbol: PGHN) is providing full project equity capital for Seabras-1 and development capital was provided by Seaborn.  Seabras-1 is owned jointly by Seaborn Networks and Partners Group.  The US$520 million project funding for Seabras-1 has been completed.  The project funding also includes a total project debt commitment of up to US$267 million provided by Natixis, Banco Santander, Commerzbank and Intesa Sanpaolo, which debt is backed by COFACE, the French Export Credit Agency.  Seabras-1 is the first direct point-to-point submarine cable system between the financial centers of the US and Brazil with an RFS of June 2017.  Seabras-1 is a 72Tbit/s system and will also be the world’s longest system built to date using 100 Gbit/s coherent technology.  The system offers carrier-class roundtrip latency POP to POP.  Seabras-1's ultra-low latency SeaSpeed™ solution between Carteret & Sao Paulo and Bandwidth-on-Demand is also available exclusively from Seaborn.  Seaborn was founded by successful submarine cable and wholesale carrier executives with experience in designing, building and operating many of the world's largest submarine and terrestrial networks.

Alliance Jiu Jitsu: Alliance (pronounced "ah-lee-AHN-say" from the Brazilian origin, but "uh-LAHY-uhns" in the American/English form) is one of the most prominent Brazilian Jiu-Jitsu associations and the current defending World team champion, having won the titles at the World Championships from 2008-2016.  They also won the World Championships back to back in 1998 and 1999.  Alliance was founded by Romero "Jacare" Cavalcanti and his students: Fabio Gurgel, Alexandre Paiva, and Fernando Gurgel.  Alliance Global headquarters is in Atlanta, Georgia at the Alliance Martial Arts Academy, where "Jacare" is the head instructor.  Fabio Gurgel, also known as the "General", is the co-leader of Alliance and the head instructor at Alliance Sao Paulo (Sao Paulo, Brazil).  Alexandre "Gigi" Paiva heads the third main Alliance academy in Rio de Janeiro, Brazil.

Jilmar Tatto: Jilmar Augustine Tatto (born in Corbélia, June 25, 1965) is a Brazilian politician affiliated to "PT" since 1981.  He is the brother of the São Paulo state deputy Enio Tatto and São Paulo councilors Arselino and Jair Tatto.  He is graduated in History from the Faculty of Philosophy Sciences and Languages of Moema and was militant at Basic Ecclesial Communities in Socorro.  He was elected president of the Sao Paulo directory in 1995, elected São Paulo state deputy in 1998, and he held positions at the secretariat of the city of Sao Paulo in Marta Suplicy's administration.

2014 6 Hours of São Paulo: The 2014 6 Hours of Sao Paulo was an endurance sports car racing event held at the Autódromo José Carlos Pace, Sao Paulo, Brazil on 28–30 November 2014, and served as the eighth and last race of the 2014 FIA World Endurance Championship season.

Reaching Horizons: Reaching Horizons is a demo-tape by the Brazilian power metal band Angra released in 1993 through Limb Music.  The original cassette contained six songs, with some re-recorded for their debut album Angels Cry.  In 1997, the record-company re-released the album, adding three bonus tracks.  The songs were recorded in July 1992 at the Guidon Studios, Sao Paulo, by sound engineer Ezequias Aureliano, except for the last two which were recorded in January 1993 at the Anonimatos Studios in Sao Paulo.  It is the only release by the band that features Antunes on drums before he was replaced during the sessions for their debut album.

João Sayad: João Sayad (born December 1, 1945) is a Brazilian economist, professor of the Department of Economics, Management and Accounting of the University of Sao Paulo and former Secretary of Finance for the state of Sao Paulo.  He was awarded a PhD in Economics by Yale University in New Haven, Connecticut.  Sayad has also been a former president and chairman of the board of directors of the Inter-American Express Bank in São Paulo and director of the Economic Research Institute Foundation at the University of São Paulo.

Confederados: The Confederados (] ) were some 10,000 to 20,000 Confederate American refugees who fled to Brazil, chiefly to the state of São Paulo, from the Southern United States after the American Civil War.  Although many eventually returned to the United States after Reconstruction, some remained and descendants of Confederados can be found in many cities throughout Brazil.

William Hutchinson Norris: William Hutchinson Norris (September 25, 1800 in Oglethorpe County, Georgia – July 13, 1893 in Santa Bárbara d'Oeste, São Paulo) is known for being a founder of the town of Americana and a settlement in Santa Bárbara d'Oeste, and a significant figure in the history of the "Confederados".

Vila Olímpia: The Vila Olímpia "(in English Olympia Village)" is an upper-class neighborhood in the city of Sao Paulo, capital of the state of Sao Paulo, in the district of Itaim Bibi.

Question: What group of people, mostly settled in Sao Paulo, is William Hutchinson Norris a significant figure of?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual in question."
    },
    "group_name": {
      "type": "string",
      "description": "The name of the group the person is associated with."
    },
    "group_description": {
      "type": "string",
      "description": "A brief description of the group."
    },
    "primary_settlement_location": {
      "type": "string",
      "description": "The primary location where the group settled."
    },
    "person_role_in_group": {
      "type": "string",
      "description": "The role of the person within the group."
    }
  },
  "required": [
    "person_name",
    "group_name",
    "group_description",
    "primary_settlement_location",
    "person_role_in_group"
  ],
  "additionalProperties": false
}
