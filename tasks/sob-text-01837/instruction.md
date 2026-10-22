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
Żubr (beer): Żubr beer (Polish: "European Bison") is a Polish lager brewed by the Kompania Piwowarska SA.

Landsmannschaft Schlesien: The Landsmannschaft Schlesien - Nieder- und Oberschlesien e.V. ("Territorial Association of Silesia - Lower and Upper Silesia", "Homeland Association of Silesia - Lower and Upper Silesia") is an organization of Germans born in the former Prussian provinces of Lower and Upper Silesia, and their descendants, who currently live in Germany.  The Landsmannschaft Schlesien was established in March 1950 and is a member of the Federation of Expellees, and has its headquarters in Königswinter, North Rhine-Westphalia.

Lech Browary Wielkopolski: Lech Browary Wielkopolski (] ; English: Lech Breweries of Greater Poland) is a big industrial brewery in Poznań, with a production capacity of 7.5 million hl.  The plant is owned by Kompania Piwowarska SA.

Kompania Piwowarska: Kompania Piwowarska is a Polish brewing group based in Poznań, established in 1999.  Since 2009 it was 100% owned by SABMiller.  Kompania Piwowarska currently has three breweries: Lech Browary Wielkopolski in Poznań, Tyskie Browary Książęce in Tychy and Browar Dojlidy in Białystok.  Tyskie Browary Książęce (Princely Brewery Tychy), one of the oldest breweries in Europe, was founded in 1629.

Dojlidy Brewery: Dojlidy Brewery (Polish: "Browar Dojlidy" ] ) is a brewery located in Białystok, Poland, and owned by Kompania Piwowarska SA, the Polish subsidiary of SABMiller.  The brewery was modernized between 1997 and 1999, then in 2003 it was purchased by Kompania Piwowarska SA.

East Upper Silesia: East Upper Silesia (German: "Ostoberschlesien" ) is a term denoting the easternmost extremity of Silesia, the eastern part of the Upper Silesian region around the city of Katowice (German: "Kattowitz" ).  The term is used primarily to denote those areas that became part of the Second Polish Republic on 20 June 1922, as a consequence of the post-World War I Treaty of Versailles.  Prior to World War II, the Second Polish Republic administered the area as Autonomous Silesian Voivodeship.  East Upper Silesia was also known as Polish (Upper) Silesia, and the German (Upper) Silesia was known as West Upper Silesia.

Tyskie Brewing Museum: The Tyskie Brewing Museum or "Tyskie Browarium" is a museum in Tychy in Silesia, Poland.  It was established in 2004.  The museum is an Anchor point on the European Route of Industrial Heritage.

Tyskie: Tyskie (] ) is a Polish brand of beer, its name comes from the brewery located in the Upper Silesia town of Tychy.  The brand is brewed by the Princely Brewery Tychy (Polish "Tyskie Browary Książęce"), part of the Kompania Piwowarska brewery group, itself a subsidiary of SABMiller since 1999 as a result of the merger of two SABMiller owned Polish breweries, the Lech Browary Wielkopolski (Lech Brewery Greater Poland) in Poznań, and the Tyskie Browary Książęce in Tychy.

TTC Tychy: Teacher Training College of Foreign Languages in Tychy (TTC Tychy, Polish: "" ) is a Polish state college established in 1990.  It trains teachers of English and German under the pedagogical guidance of the University of Silesia in Katowice.

Tychy Brewery: Princely Brewery Tychy (Polish "Tyskie Browary Książęce") or Tychy Brewery in the town of Tychy is one of the largest breweries in Poland.  It is operated by the Kompania Piwowarska company.  It traces its history to the 17th century.

Question: Kompania Piwowarska is a Polish brewing group based in Poznań, established in 1999, it currently has three breweries total, Tyskie Browary Książęce in Tychy, which Polish brand of beer, its name comes from the brewery located in the Upper Silesia town of Tychy?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "brewing_group": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the brewing group."
        },
        "established_year": {
          "type": "integer",
          "description": "The year the brewing group was established."
        },
        "total_breweries": {
          "type": "integer",
          "description": "The total number of breweries owned by the group."
        }
      },
      "required": [
        "name",
        "established_year",
        "total_breweries"
      ],
      "additionalProperties": false
    },
    "target_brewery_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the specific brewery in question."
        },
        "location_city": {
          "type": "string",
          "description": "The city where the brewery is located."
        },
        "location_region": {
          "type": "string",
          "description": "The region where the brewery is located."
        },
        "associated_beer_brand": {
          "type": "string",
          "description": "The beer brand associated with this brewery and location."
        }
      },
      "required": [
        "name",
        "location_city",
        "location_region",
        "associated_beer_brand"
      ],
      "additionalProperties": false
    },
    "answer": {
      "type": "string",
      "description": "The name of the Polish beer brand that comes from the brewery in Tychy."
    }
  },
  "required": [
    "brewing_group",
    "target_brewery_details",
    "answer"
  ],
  "additionalProperties": false
}
