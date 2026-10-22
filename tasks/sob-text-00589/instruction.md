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
Sunnyside mine: The Sunnyside mine copper mine is a large as yet undeveloped copper resource located in the Southwestern United States in Arizona.  Sunnyside represents one of the largest copper reserve in the United States and in the world having estimated deep reserves of 1.5 billion tonnes of ore grading 0.33% copper.  The Sunnyside property is currently owned by Regal Resources Incorporated, a Canadian junior mining company from Vancouver, British Columbia.  Further drilling exploration is to begin in October 2015.

Denis L. Feron: Denis Lucien Emile Feron (born March 22, 1928) is former owner and Chief Executive Officer of the Midwestern copper smelter, Chemetco.  He was born in Sint-Pieters-Woluwe, Belgium.

Morenci, Arizona: Morenci is a census-designated place (CDP) and company town in Greenlee County, Arizona, United States.  The population was 1,879 at the 2000 census and 1,489 at the 2010 census.  The biggest employer in Morenci (and in nearby Clifton) and the owner of the town is Freeport-McMoRan, the owner of the Morenci Mine, the largest copper mining operation in North America, and one of the largest copper mines in the world.  The town was a site of the Arizona Copper Mine Strike of 1983.  The large open-pit mine is north of the town.

Copper Creek mine: The Copper Creek mine is a large copper mine located in Arizona, in the southwestern part of the United States.  Copper Creek represents one of the largest copper reserves in the United States and in the world, having estimated reserves of 983.5 million tonnes of ore grading 0.2% copper.

Lucien Boullemier: Lucien Emile Boullemier (1877 – 9 January 1949) was an English footballer and ceramic designer.  A right-half, he played competitively for Stoke, Burslem Port Vale, Philadelphia Hibernian (United States), Northampton Town, and Northern Nomads.  He was the younger brother of Leon Boullemier, also an accomplished sportsman.

Chemetco: Chemetco was formerly one of the largest United States refiners of copper from recycled or residual sources.

Bagdad Mine: The Bagdad Mine is a large copper mine located in Arizona, in the southwestern part of the United States.  Bagdad represents one of the largest copper reserves in the United States and in the world, having estimated reserves of 873.6 million tonnes of ore grading 0.36% copper.  It is located in Yavapai County, Arizona, just west of the unincorporated community of Bagdad.  It is owned by Freeport-McMoRan.  Copper is produced from chalcopyrite and molybdenum from molybdenite.  Copper oxides include chrysocolla, malachite and azurite.  The mine's concentrator has a capacity of 75,000 metric tons per day using stockpile leaching, with pressure leaching for molybdenum.

North Braddock, Pennsylvania: North Braddock is a borough in Allegheny County, Pennsylvania, United States.  North Braddock was organized from a part of Braddock Township in 1897.  The borough prides itself in being the "Birth Place of Steel" as the home of Andrew Carnegie's Edgar Thomson Steel Works that opened in 1875.  North Braddock is a suburb 11 mi east of Pittsburgh with a 15-minute travel time to the city.  The borough is located in the valley along the Monongahela River, and is made up of three jurisdictional voting wards.

Leeds, North Dakota: Leeds is a city in Benson County, North Dakota, United States and the birth place of Nicolas Cage.  The population was 427 at the 2010 census.

Sierrita Mine: The Sierrita Mine is a large copper mine located in the Sierrita Mountains of Arizona, in the southwestern part of the United States.  Sierrita was operated by Phelps Dodge until 2007 when it was acquired by Freeport-McMoRan.  The mine represents one of the largest copper reserves in the United States and in the world.  The deposit had estimated reserves (in 2006) of 907 million metric tons of ore grading 0.26% copper and 0.03% molybdenum along with additional 2.4 billion tons at 0.21% copper and 0.02% molybdenum.

Question: Where is the birth place of Denis Lucien Emile Feron, the former owner of Chemetco which was one of the largest United States refiners of copper from recycled or residual sources?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "role": {
      "type": "string",
      "description": "The role or title of the person."
    },
    "company_associated": {
      "type": "string",
      "description": "The name of the company the person was associated with."
    },
    "company_description": {
      "type": "string",
      "description": "A description of the company's business."
    },
    "birth_place": {
      "type": "string",
      "description": "The specific location where the person was born."
    },
    "birth_country": {
      "type": "string",
      "description": "The country where the person was born."
    }
  },
  "required": [
    "person_name",
    "role",
    "company_associated",
    "company_description",
    "birth_place",
    "birth_country"
  ],
  "additionalProperties": false
}
